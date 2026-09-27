"""Module 3/7/8 — the Tawseel Billing MCP server. ELEVATED trust boundary.

TRUST BOUNDARY: elevated — this is the only server with a write capability
that moves real money (`issue_refund`), so it is the narrowest-granted
domain in `security/authz.py`'s policy table (only `customer_agent` is
even eligible; `ops_agent` and `partner_agent` are refused at the domain
check before `issue_refund`'s own body runs). OWASP risk addressed:
Excessive Agency — specifically an agent being talked (via a crafted
customer message, or an injected instruction in unrelated tool output,
per `data/orders/INJECTION_NOTES.md`) into authorising a refund beyond
what policy allows. SPEC §5's action-risk matrix makes anything above
`REFUND_LIMIT_SAR` human-approval-required, not autonomous; a prompt
instruction saying "never refund over 500" is NOT an enforcement
mechanism (a crafted input can talk a model past it) — so this server
enforces the limit itself, in code, as DEFENCE IN DEPTH alongside
`flows/refund_flow.py`'s own gate: two independent places would have to
both be wrong for an over-limit refund to go through un-approved.

Run standalone: `python3 mcp_servers/billing_server.py` (stdio transport).
"""
from __future__ import annotations

import sys
from pathlib import Path

# So `python3 mcp_servers/billing_server.py` works standalone regardless
# of cwd/PYTHONPATH — see orders_server.py for the full rationale.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from mcp_servers.common import guarded_tool, make_server, serve  # noqa: E402

from rafeeq.core.config import REFUND_LIMIT_SAR  # noqa: E402
from rafeeq.tools.billing import (  # noqa: E402
    get_invoice_impl,
    get_payment_impl,
    issue_refund_impl,
    mark_refunded_impl,
)

mcp = make_server("tawseel-billing")


@guarded_tool(mcp, domain="billing")
def get_invoice(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Get the invoice/billing summary for ONE order. Authorisation is
    enforced HERE. order_id format: TW-YYYY-NNNNN."""
    return get_invoice_impl(order_id)


@guarded_tool(mcp, domain="billing")
def get_payment(payment_id: str, agent_id: str, customer_id: str) -> dict:
    """Get ONE payment record, including refund history. Authorisation is
    enforced HERE. payment_id format: PAY-NNNNNN."""
    return get_payment_impl(payment_id)


@guarded_tool(mcp, domain="billing")
def issue_refund(
    order_id: str,
    amount_sar: float,
    reason: str,
    idempotency_key: str,
    agent_id: str,
    customer_id: str,
    approved: bool = False,
) -> dict:
    """Issue a refund against ONE order's payment. Authorisation is
    enforced HERE, and — DEFENCE IN DEPTH (SPEC §5/§7) — this server ALSO
    hard-blocks any amount above `REFUND_LIMIT_SAR` (500 SAR) unless the
    caller explicitly sets `approved=True`, simulating an upstream
    human-approval step having already happened; no prompt instruction
    can set that flag for itself. WRITE, requires a stable
    `idempotency_key` (see `rafeeq.tools.billing.issue_refund_impl`).
    order_id format: TW-YYYY-NNNNN.
    """
    if amount_sar > REFUND_LIMIT_SAR and not approved:
        return {
            "error": "human_approval_required",
            "limit_sar": REFUND_LIMIT_SAR,
            "amount_sar": amount_sar,
        }
    return issue_refund_impl(order_id, amount_sar, reason, idempotency_key)


@guarded_tool(mcp, domain="billing")
def mark_refunded(order_id: str, refund_amount_sar: float, agent_id: str, customer_id: str) -> dict:
    """RECONCILIATION ONLY: manually mark an order refunded to match an
    external adjustment. Authorisation is enforced HERE — and, per
    `security/authz.py`'s policy table, the conversational `customer_agent`
    identity is explicitly denied this tool; only `billing_admin_agent`
    (internal finance/reconciliation) may call it. order_id format:
    TW-YYYY-NNNNN."""
    return mark_refunded_impl(order_id, refund_amount_sar)


if __name__ == "__main__":
    serve(mcp)
