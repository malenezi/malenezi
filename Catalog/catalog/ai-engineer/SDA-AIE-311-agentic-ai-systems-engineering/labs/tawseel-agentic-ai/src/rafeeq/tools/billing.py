"""Module 3/7/8 — Billing tools (elevated trust boundary).

Four narrow tools over `rafeeq.adapters.billing.BillingClient`. `billing`
is an ELEVATED domain (SPEC's Module-3 case study on trust boundaries):
`get_invoice`/`get_payment` are read-only, but `issue_refund` moves real
money and `mark_refunded` mutates an order's refund state directly — both
are WRITE tools and neither is safe to retry blindly.

TEACHING POINT (SPEC §7 mistake #6): authorisation for refunds does NOT
live in this file or in a prompt instruction — "only refund if allowed"
in a system prompt is not an access-control mechanism, because a crafted
input can talk the model past it (see `data/orders/INJECTION_NOTES.md`
for the exact 5,000 SAR injection this repo uses to teach that). This
tool enforces backend invariants only (idempotency, "cannot refund more
than was paid" — `BillingClient.issue_refund`); the 500 SAR
human-approval gate from the action-risk matrix (SPEC §5) is enforced by
the CALLER — `flows/refund_flow.py` and, as defence in depth,
`mcp_servers/billing_server.py` at the server boundary. `issue_refund`
here still reports `requires_human_approval` in its result so any caller
can see the gate was crossed.

Errors are RETURN VALUES, never raises.
"""
from __future__ import annotations

import re

from rafeeq.adapters.billing import BillingClient
from rafeeq.adapters.oms import OrderManagementClient
from rafeeq.core.config import ORDER_ID_RE, PAYMENT_ID_RE
from rafeeq.core.errors import ToolError

try:
    from langchain_core.tools import tool
except ImportError:  # pragma: no cover - Layer-A / plain-python3 environment
    def tool(func=None, *, return_direct: bool = False):  # type: ignore[no-redef]
        """Fallback stand-in for `langchain_core.tools.tool` (see
        `tawseel.py` for the full rationale)."""
        def _decorate(f):
            f.name = f.__name__
            f.description = (f.__doc__ or "").strip()
            return f
        return _decorate(func) if func is not None else _decorate


_ORDER_ID_FULL_RE = re.compile(rf"^{ORDER_ID_RE}$")
_PAYMENT_ID_FULL_RE = re.compile(rf"^{PAYMENT_ID_RE}$")

_billing = BillingClient()
_oms = OrderManagementClient()


def get_invoice_impl(order_id: str) -> dict:
    """Get invoice/billing summary for ONE order by its id.

    Use when a customer asks for a receipt/invoice/billing statement. Do
    NOT use this for refund status detail — see `get_payment` for the
    full refund history of the underlying payment.

    order_id format: TW-YYYY-NNNNN.

    Returns {"invoice_id", "order_id", "customer_id", "issued_at",
    "amount_sar", "currency", "items", "payment_status", "method"} on
    success, or {"error": "invalid_order_id_format"} /
    {"error": "order_not_found"}. Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        inv = _billing.get_invoice(order_id)
    except ToolError:
        return {"error": "order_not_found"}
    return {
        "invoice_id": inv.invoice_id, "order_id": inv.order_id,
        "customer_id": inv.customer_id, "issued_at": inv.issued_at,
        "amount_sar": inv.amount_sar, "currency": inv.currency,
        "items": inv.items, "payment_status": inv.payment_status,
        "method": inv.method,
    }


def get_payment_impl(payment_id: str) -> dict:
    """Get ONE payment record by its id, including its refund history.

    Use to check whether/how much of a payment has already been refunded
    before deciding whether a new refund is appropriate. Do NOT use this
    to look up a payment by order id — you need the payment id (from
    `get_invoice` or `get_order`).

    payment_id format: PAY-NNNNNN.

    Returns {"payment_id", "order_id", "customer_id", "amount_sar",
    "method", "status", "captured_at", "refunds"} on success, or
    {"error": "invalid_payment_id_format"} / {"error": "payment_not_found"}.
    Never raises.
    """
    if not _PAYMENT_ID_FULL_RE.match(payment_id):
        return {"error": "invalid_payment_id_format"}
    try:
        pay = _billing.get_payment(payment_id)
    except ToolError:
        return {"error": "payment_not_found"}
    return {
        "payment_id": pay.payment_id, "order_id": pay.order_id,
        "customer_id": pay.customer_id, "amount_sar": pay.amount_sar,
        "method": pay.method, "status": pay.status,
        "captured_at": pay.captured_at, "refunds": pay.refunds,
    }


def issue_refund_impl(
    order_id: str, amount_sar: float, reason: str, idempotency_key: str,
) -> dict:
    """Issue a refund of `amount_sar` SAR against ONE order's payment.

    WRITE, NOT idempotent-safe to call blindly twice — but calling it
    TWICE with the exact SAME `idempotency_key` is safe and returns the
    original result unchanged (`idempotent_replay: true`), never a second
    payment. Always pass a NEW, stable idempotency_key per distinct refund
    DECISION (e.g. derived from the ticket id), never a fresh random key
    on every retry — a fresh key on retry defeats the whole protection
    (Module 1's double-refund incident, reborn at the tool layer if you
    get this wrong).

    Use only after confirming the refund amount and reason with the
    customer/policy. This tool does NOT itself enforce the 500 SAR
    human-approval gate (SPEC §5) — the caller must have already checked
    `security/action_risk.py` and, for amounts requiring approval, obtained
    it before calling this. The result's `requires_human_approval` field
    tells you whether this amount crossed that threshold.

    order_id format: TW-YYYY-NNNNN. amount_sar must be positive and must
    not exceed the payment's remaining refundable balance.

    Returns {"order_id", "payment_id", "amount_sar", "reason",
    "idempotency_key", "issued_at", "total_refunded_sar",
    "payment_status", "requires_human_approval", "idempotent_replay"} on
    success, or {"error": "invalid_order_id_format"} /
    {"error": "missing_idempotency_key"} / {"error": "invalid_amount"} /
    {"error": "order_not_found"} / {"error": "payment_not_found"} /
    {"error": "amount_exceeds_refundable_balance", "remaining_sar": ...}.
    Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    if not idempotency_key or not idempotency_key.strip():
        return {"error": "missing_idempotency_key"}
    if amount_sar <= 0:
        return {"error": "invalid_amount"}
    try:
        result = _billing.issue_refund(order_id, amount_sar, reason, idempotency_key)
    except ToolError as exc:
        if "not found" in exc.message and "Order" in exc.message:
            return {"error": "order_not_found"}
        if "No payment found" in exc.message:
            return {"error": "payment_not_found"}
        if "exceeds remaining refundable balance" in exc.message:
            return {
                "error": "amount_exceeds_refundable_balance",
                "remaining_sar": exc.detail.get("remaining_sar"),
            }
        return {"error": "refund_rejected", "detail": exc.detail}
    return {**result, "requires_human_approval": result["amount_sar"] > 500.0}


def mark_refunded_impl(order_id: str, refund_amount_sar: float) -> dict:
    """RECONCILIATION ONLY: manually mark ORDER `order_id` as refunded for
    `refund_amount_sar` SAR on the order record.

    Use ONLY when a refund was already issued through an external/manual
    channel (e.g. a finance team adjustment made directly in the payment
    gateway, outside Tawseel) and the order record needs to be corrected
    to match. Do NOT call this after `issue_refund` in the normal flow —
    `issue_refund` already updates the order's refund fields itself;
    calling both double-counts the refund amount on the order.

    WRITE, NOT idempotent — calling it twice adds the amount twice. There
    is no idempotency key here because this is a manual correction tool,
    not a payment action; the caller is responsible for calling it exactly
    once per external adjustment.

    order_id format: TW-YYYY-NNNNN. refund_amount_sar must be positive.

    Returns {"order_id", "refunded": true, "refund_amount_sar"} on
    success, or {"error": "invalid_order_id_format"} /
    {"error": "invalid_amount"} / {"error": "order_not_found"}. Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    if refund_amount_sar <= 0:
        return {"error": "invalid_amount"}
    try:
        record = _oms.mark_refunded(order_id, refund_amount_sar)
    except ToolError:
        return {"error": "order_not_found"}
    return {
        "order_id": order_id, "refunded": record.refunded,
        "refund_amount_sar": record.refund_amount_sar,
    }


@tool
def get_invoice(order_id: str) -> dict:
    """Get the invoice/billing summary for ONE order. Use for
    receipt/invoice requests. order_id format: TW-YYYY-NNNNN."""
    return get_invoice_impl(order_id)


@tool
def get_payment(payment_id: str) -> dict:
    """Get ONE payment record by its id, including refund history. Needs
    a payment id, not an order id. payment_id format: PAY-NNNNNN."""
    return get_payment_impl(payment_id)


@tool
def issue_refund(order_id: str, amount_sar: float, reason: str, idempotency_key: str) -> dict:
    """Issue a refund against ONE order's payment. WRITE — pass a stable
    idempotency_key (never a fresh random one on retry); a repeated call
    with the same key safely replays the original result. Does NOT itself
    enforce the 500 SAR human-approval gate; check that before calling.
    order_id format: TW-YYYY-NNNNN."""
    return issue_refund_impl(order_id, amount_sar, reason, idempotency_key)


@tool
def mark_refunded(order_id: str, refund_amount_sar: float) -> dict:
    """RECONCILIATION ONLY: manually mark an order refunded to match an
    external adjustment. Do NOT call after issue_refund — it already
    updates the order; calling both double-counts. order_id format:
    TW-YYYY-NNNNN."""
    return mark_refunded_impl(order_id, refund_amount_sar)


TOOLS = [get_invoice, get_payment, issue_refund, mark_refunded]
