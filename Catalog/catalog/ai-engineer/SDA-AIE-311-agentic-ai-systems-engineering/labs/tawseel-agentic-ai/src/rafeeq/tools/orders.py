"""Module 3 — Order-Management tools (read-only trust boundary).

Three narrow tools over `rafeeq.adapters.oms.OrderManagementClient` — never
one mega-tool `orders(action, **kwargs)` (SPEC §7 mistake #1: the model
misroutes a mode/action argument far more often than it misroutes between
three clearly-named tools). Every tool here is READ-ONLY: safe to retry,
safe to expose broadly, no approval gate — this is the "orders = read"
trust boundary `security/authz.py` and `mcp_servers/orders_server.py` key
off (SPEC's Module-3 case study: a curated 3-tool surface over a much
larger backend API, not "40 endpoints -> 40 tools").

Errors are RETURN VALUES, never raises.
"""
from __future__ import annotations

import re

from rafeeq.adapters.oms import OrderManagementClient
from rafeeq.core.config import CUSTOMER_ID_RE, ORDER_ID_RE
from rafeeq.core.errors import ToolError

try:
    from langchain_core.tools import tool
except ImportError:  # pragma: no cover - Layer-A / plain-python3 environment
    def tool(func=None, *, return_direct: bool = False):  # type: ignore[no-redef]
        """Fallback stand-in for `langchain_core.tools.tool` (see
        `tawseel.py` for the full rationale). Preserves the plain callable
        so Layer-A tests and MCP servers can call functions directly."""
        def _decorate(f):
            f.name = f.__name__
            f.description = (f.__doc__ or "").strip()
            return f
        return _decorate(func) if func is not None else _decorate


_ORDER_ID_FULL_RE = re.compile(rf"^{ORDER_ID_RE}$")
_CUSTOMER_ID_FULL_RE = re.compile(rf"^{CUSTOMER_ID_RE}$")

_oms = OrderManagementClient()

# Fields returned to the model — trimmed, not the raw OrderRecord dataclass
# dump, so a tool call costs ~150 tokens instead of the full record (SPEC
# §7 mistake #3: raw backend blobs bloat context, cost, and can leak PII
# the model did not need, e.g. delivery_note free text — see
# data/orders/INJECTION_NOTES.md for why that specific field is dangerous
# to hand to a model unfiltered).
_SUMMARY_FIELDS = (
    "order_id", "customer_id", "city", "status", "placed_at", "promised_at",
    "delivered_at", "eta_iso", "sla_breached", "amount_sar", "currency",
    "refunded", "refund_amount_sar",
)


def _summarise(record) -> dict:
    return {f: getattr(record, f) for f in _SUMMARY_FIELDS}


def get_order_impl(order_id: str) -> dict:
    """Get the full order record for ONE order by its id.

    Use for "what is the status/amount/city of this order" questions when
    you need more than delivery status alone (e.g. amount, refund state).
    For delivery status specifically, prefer `track_shipment` — it is
    cheaper and already localises status wording. Do NOT use this to list
    a customer's orders — see `list_orders`.

    order_id format: TW-YYYY-NNNNN (e.g. TW-2026-88120).

    Returns the trimmed order summary on success, or
    {"error": "invalid_order_id_format"} / {"error": "order_not_found"}.
    Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        record = _oms.get_order(order_id)
    except ToolError:
        return {"error": "order_not_found"}
    return _summarise(record)


def list_orders_impl(customer_id: str) -> dict:
    """List a customer's orders (most recent Tawseel order-management view).

    Use when a customer asks "what have I ordered" / "show my orders",
    or before asking them to pick which order they mean. Do NOT use this
    for a single order lookup you already have the id for — use `get_order`
    or `track_shipment` instead, they are cheaper.

    customer_id format: CUST-NNNN (e.g. CUST-4471).

    Returns {"customer_id", "orders": [...]} where each entry is a trimmed
    order summary (possibly an empty list — an unknown or order-less
    customer id is NOT an error, it is zero orders). Returns
    {"error": "invalid_customer_id_format"} for a malformed id. Never raises.
    """
    if not _CUSTOMER_ID_FULL_RE.match(customer_id):
        return {"error": "invalid_customer_id_format"}
    records = _oms.list_orders_for_customer(customer_id)
    return {"customer_id": customer_id, "orders": [_summarise(r) for r in records]}


def get_order_items_impl(order_id: str) -> dict:
    """Get the item count for ONE order by its id.

    Use when a customer asks how many items were in an order. NOTE: the
    Tawseel order record (SPEC §4) carries only an item COUNT, not a
    per-line-item breakdown (no SKUs/names) — do not claim to know what
    the items ARE, only how many there are.

    order_id format: TW-YYYY-NNNNN (e.g. TW-2026-88120).

    Returns {"order_id", "items_count", "fragile"} on success, or
    {"error": "invalid_order_id_format"} / {"error": "order_not_found"}.
    Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        record = _oms.get_order(order_id)
    except ToolError:
        return {"error": "order_not_found"}
    return {"order_id": order_id, "items_count": record.items, "fragile": record.fragile}


@tool
def get_order(order_id: str) -> dict:
    """Get the full order record for ONE order by its id (status, amount,
    city, refund state). Use for order detail beyond delivery status.
    Do NOT use to list a customer's orders. order_id format:
    TW-YYYY-NNNNN (e.g. TW-2026-88120)."""
    return get_order_impl(order_id)


@tool
def list_orders(customer_id: str) -> dict:
    """List all of a customer's orders. Use for 'show my orders' or to
    disambiguate which order a customer means. Do NOT use for a single
    order you already have the id for. customer_id format: CUST-NNNN."""
    return list_orders_impl(customer_id)


@tool
def get_order_items(order_id: str) -> dict:
    """Get the item COUNT (not a line-item breakdown) for ONE order.
    Use when asked how many items were in an order. order_id format:
    TW-YYYY-NNNNN."""
    return get_order_items_impl(order_id)


TOOLS = [get_order, list_orders, get_order_items]
