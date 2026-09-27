"""Module 3 — the Tawseel Customer/CRM MCP server. ELEVATED + scoped.

TRUST BOUNDARY: elevated AND strictly same-customer-scoped — every agent
identity granted this domain in `security/authz.py`'s policy table has
`same_customer_only=True`, so even a fully authorised call is refused if
`customer_id` does not match the CALLING agent's own `session_customer_id`
context. This is the domain carrying the most sensitive PII in the repo
(masked national id, phone, fraud flag, ticket notes). OWASP risk
addressed: Sensitive Information Disclosure / Privilege Escalation via
cross-customer access — the exact attack `data/orders/INJECTION_NOTES.md`
note 2 models ("...reply with their full national ID number"): even a
maximally jailbroken agent gets nothing to leak, because (a) the backend
never stores an unmasked national id and (b) this server refuses any call
whose `customer_id` is not the caller's own scoped customer, regardless of
what the request text asks for.

Run standalone: `python3 mcp_servers/customer_server.py` (stdio transport).
"""
from __future__ import annotations

import sys
from pathlib import Path

# So `python3 mcp_servers/customer_server.py` works standalone regardless
# of cwd/PYTHONPATH — see orders_server.py for the full rationale.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from mcp_servers.common import guarded_tool, make_server, serve  # noqa: E402

from rafeeq.tools.customer import (  # noqa: E402
    add_case_note_impl,
    get_customer_impl,
    get_customer_tickets_impl,
)

mcp = make_server("tawseel-customer")


@guarded_tool(mcp, domain="customer")
def get_customer(customer_id: str, agent_id: str) -> dict:
    """Get ONE customer's profile (masked PII only). Authorisation is
    enforced HERE, scoped to the caller's own customer. customer_id
    format: CUST-NNNN."""
    return get_customer_impl(customer_id)


@guarded_tool(mcp, domain="customer")
def get_customer_tickets(customer_id: str, agent_id: str) -> dict:
    """List ONE customer's support tickets. Authorisation is enforced
    HERE, scoped to the caller's own customer. customer_id format:
    CUST-NNNN."""
    return get_customer_tickets_impl(customer_id)


@guarded_tool(mcp, domain="customer")
def add_case_note(customer_id: str, ticket_id: str, note: str, agent_id: str) -> dict:
    """Append a note to an EXISTING ticket for ONE customer. WRITE, not
    idempotent. Authorisation is enforced HERE, scoped to the caller's own
    customer. customer_id: CUST-NNNN; ticket_id: TKT-NNNNN."""
    return add_case_note_impl(customer_id, ticket_id, note)


if __name__ == "__main__":
    serve(mcp)
