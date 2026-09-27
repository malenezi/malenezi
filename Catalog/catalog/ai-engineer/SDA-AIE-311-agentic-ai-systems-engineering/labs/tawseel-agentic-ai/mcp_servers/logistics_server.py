"""Module 3 — the Tawseel Logistics/Tracking MCP server.

TRUST BOUNDARY: read-heavy (five of six tools are read-only) plus ONE
autonomous-within-policy write, `reschedule_delivery` — no refund or
customer-identity capability lives here at all, so this server's blast
radius stops at delivery state, never payments or PII. OWASP risk
addressed: Indirect Prompt Injection via tool output — delivery notes are
free text a courier or customer can influence (see
`data/orders/INJECTION_NOTES.md` for planted examples shaped exactly like
this), so this server's tools return only the STRUCTURED delivery fields
the model needs (status/eta/exception code), never raw note text folded
into an instruction-shaped response, and no tool here can act on
instructions found inside one.

`track_shipment` below mirrors the instructor package's Module 3 worked
example (`mcp.tool()` wrapping a function that checks `agent_may_access`
before touching the backend) — refactored through `mcp_servers/common.py`'s
shared `guarded_tool` so all six tools in this server get the identical
enforcement instead of five of them re-deriving it by hand, and extended
with the rest of the LaDe-inspired suite (`estimate_eta`,
`get_delivery_events`, `get_driver_status`, `find_delivery_exception`,
`reschedule_delivery`).

Run standalone: `python3 mcp_servers/logistics_server.py` (stdio transport).
"""
from __future__ import annotations

import sys
from pathlib import Path

# So `python3 mcp_servers/logistics_server.py` works standalone regardless
# of cwd/PYTHONPATH — see orders_server.py for the full rationale.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from mcp_servers.common import guarded_tool, make_server, serve  # noqa: E402

from rafeeq.tools.logistics import (  # noqa: E402
    estimate_eta_impl,
    find_delivery_exception_impl,
    get_delivery_events_impl,
    get_driver_status_impl,
    reschedule_delivery_impl,
    track_shipment_impl,
)

mcp = make_server("tawseel-logistics")


@guarded_tool(mcp, domain="logistics")
def track_shipment(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Return delivery status for ONE order. Authorisation is enforced
    HERE, not in the calling agent's prompt. order_id format:
    TW-YYYY-NNNNN."""
    return track_shipment_impl(order_id)


@guarded_tool(mcp, domain="logistics")
def estimate_eta(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Return the current estimated/actual arrival time for ONE order.
    Authorisation is enforced HERE. order_id format: TW-YYYY-NNNNN."""
    return estimate_eta_impl(order_id)


@guarded_tool(mcp, domain="logistics")
def get_delivery_events(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Return the full delivery-event timeline for ONE order.
    Authorisation is enforced HERE. order_id format: TW-YYYY-NNNNN."""
    return get_delivery_events_impl(order_id)


@guarded_tool(mcp, domain="logistics")
def get_driver_status(courier_id: str, agent_id: str, customer_id: str) -> dict:
    """Return a courier's most recent known activity. Internal ops use
    only. Authorisation is enforced HERE. courier_id format: DRV-NNN."""
    return get_driver_status_impl(courier_id)


@guarded_tool(mcp, domain="logistics")
def find_delivery_exception(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Return the most recent delivery exception for ONE order, if any.
    Authorisation is enforced HERE. order_id format: TW-YYYY-NNNNN."""
    return find_delivery_exception_impl(order_id)


@guarded_tool(mcp, domain="logistics")
def reschedule_delivery(order_id: str, new_promised_at_iso: str, agent_id: str, customer_id: str) -> dict:
    """Reschedule ONE order's promised delivery time. WRITE, not
    idempotent-safe to retry blindly. Authorisation is enforced HERE.
    order_id format: TW-YYYY-NNNNN."""
    return reschedule_delivery_impl(order_id, new_promised_at_iso)


if __name__ == "__main__":
    serve(mcp)
