"""Module 3 — Logistics tools (LaDe-inspired operational backend, SPEC §6).

Six narrow tools over `rafeeq.adapters.logistics.LogisticsClient`, shaped
after the LaDe last-mile delivery dataset's tool surface (`get_delivery_status`,
`get_driver_status`, `estimate_eta`, `get_delivery_events`,
`find_delivery_exception`) plus `reschedule_delivery`, the one WRITE tool in
this file. Five tools are read-only (retry-safe); `reschedule_delivery` is
not — it mutates `promised_at`/`eta_iso` and must not be blindly retried
(SPEC §7 mistake #5). Per the action-risk matrix (SPEC §5) rescheduling is
"autonomous within policy": no human approval required, but every call is
auditable (see `mcp_servers/logistics_server.py`, which logs it).

Errors are RETURN VALUES, never raises.
"""
from __future__ import annotations

import re

from rafeeq.adapters.logistics import LogisticsClient
from rafeeq.core.config import DRIVER_ID_RE, ORDER_ID_RE
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
_DRIVER_ID_FULL_RE = re.compile(rf"^{DRIVER_ID_RE}$")

_client = LogisticsClient()


def track_shipment_impl(order_id: str) -> dict:
    """Get the current delivery status of ONE order by its id.

    Use for "where is my order" questions. Do NOT use for refunds or for
    changing the delivery time — see `rafeeq.tools.billing.issue_refund`
    and `reschedule_delivery` respectively.

    order_id format: TW-YYYY-NNNNN.

    Returns {"order_id", "status", "eta_iso", "sla_breached", "courier_id"}
    on success, or {"error": "invalid_order_id_format"} /
    {"error": "order_not_found"}. Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        return _client.status(order_id)
    except ToolError:
        return {"error": "order_not_found"}


def estimate_eta_impl(order_id: str) -> dict:
    """Get the current estimated (or actual, if delivered) arrival time
    for ONE order.

    Use when a customer asks "when will it arrive" specifically — prefer
    `track_shipment` for a general status question, since it returns the
    ETA too alongside the status. Do NOT use to promise a NEW delivery
    time — see `reschedule_delivery`, which actually changes it.

    order_id format: TW-YYYY-NNNNN.

    Returns {"order_id", "eta_iso", "delivered"} on success, or
    {"error": "invalid_order_id_format"} / {"error": "order_not_found"}.
    Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        return _client.estimate_eta(order_id)
    except ToolError:
        return {"error": "order_not_found"}


def get_delivery_events_impl(order_id: str) -> dict:
    """Get the full delivery-event timeline for ONE order (accepted,
    picked_up, at_hub, out_for_delivery, delivery_attempt, delivered,
    failed, returned — LaDe-shaped).

    Use when a customer disputes a status or asks "what happened" in
    detail, or to investigate a complaint. Do NOT use for a quick status
    check — that is `track_shipment`; this is heavier (a full event list).

    order_id format: TW-YYYY-NNNNN.

    Returns {"order_id", "events": [...]} (each event: seq, event, ts,
    courier_id, city, note, exception_code) on success, or
    {"error": "invalid_order_id_format"} / {"error": "order_not_found"}.
    Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        events = _client.events(order_id)
    except ToolError:
        return {"error": "order_not_found"}
    return {
        "order_id": order_id,
        "events": [
            {
                "seq": e.seq, "event": e.event, "ts": e.ts,
                "courier_id": e.courier_id, "city": e.city,
                "note": e.note, "exception_code": e.exception_code,
            }
            for e in events
        ],
    }


def get_driver_status_impl(courier_id: str) -> dict:
    """Get a courier/driver's most recent known activity (last event,
    last-seen time, location) across all their deliveries.

    Use for internal ops questions ("where is driver DRV-118 right now")
    — NOT for answering a customer's "where is my order" question, that
    is `track_shipment` keyed on the ORDER, not the driver.

    courier_id format: DRV-NNN (e.g. DRV-118).

    Returns {"courier_id", "last_event", "last_seen", "city", "lat",
    "lng"} on success, or {"error": "invalid_driver_id_format"} /
    {"error": "driver_not_found"}. Never raises.
    """
    if not _DRIVER_ID_FULL_RE.match(courier_id):
        return {"error": "invalid_driver_id_format"}
    try:
        return _client.driver_status(courier_id)
    except ToolError:
        return {"error": "driver_not_found"}


def find_delivery_exception_impl(order_id: str) -> dict:
    """Find the most recent delivery EXCEPTION for ONE order, if any
    (customer_unreachable, address_incorrect, damaged, refused, weather,
    vehicle_breakdown).

    Use when a customer reports a delivery problem or an order's status
    is "exception", to find out WHY before deciding next steps (reschedule?
    refund? escalate?). Do NOT use for a routine "where is my order" check
    — most orders have no exception; use `track_shipment` first.

    order_id format: TW-YYYY-NNNNN.

    Returns {"order_id", "exception_code", "ts", "note"} if one exists,
    {"order_id", "exception_code": null} if the order has none, or
    {"error": "invalid_order_id_format"} / {"error": "order_not_found"}.
    Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    from rafeeq.adapters.store import store  # local: only needed for the not-found check

    if store.get_order(order_id) is None:
        return {"error": "order_not_found"}
    found = _client.find_exception(order_id)
    if found is None:
        return {"order_id": order_id, "exception_code": None, "ts": None, "note": None}
    return found


def reschedule_delivery_impl(order_id: str, new_promised_at_iso: str) -> dict:
    """Reschedule ONE order's promised delivery time. WRITE — NOT
    idempotent-safe to blindly retry: two calls with different times
    genuinely change state twice; do not call this a second time to
    "make sure it went through" — check with `track_shipment` instead.

    Use only after confirming a new promised time with the customer AND
    checking with `find_delivery_exception`/`track_shipment` that the
    order is not already delivered or in an unrecoverable exception state
    (those cannot be rescheduled and this tool returns an error for them).
    Autonomous within policy (SPEC §5): no human approval required, but
    every call is logged with a before/after promised time.

    order_id format: TW-YYYY-NNNNN. new_promised_at_iso: ISO-8601
    datetime with timezone offset, e.g. "2026-03-05T18:00:00+03:00".

    Returns {"order_id", "rescheduled": true, "promised_at_before",
    "promised_at_after", "eta_iso"} on success, or
    {"error": "invalid_order_id_format"} / {"error": "order_not_found"} /
    {"error": "not_reschedulable", "status": ...} (order already delivered
    or in exception). Never raises.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}
    try:
        return _client.reschedule(order_id, new_promised_at_iso)
    except ToolError as exc:
        if "not found" in exc.message:
            return {"error": "order_not_found"}
        return {"error": "not_reschedulable", "detail": exc.detail}


@tool
def track_shipment(order_id: str) -> dict:
    """Get the current delivery status of ONE order by its id. Use for
    'where is my order' questions. Do NOT use for refunds or delivery-time
    changes. order_id format: TW-YYYY-NNNNN."""
    return track_shipment_impl(order_id)


@tool
def estimate_eta(order_id: str) -> dict:
    """Get the current estimated/actual arrival time for ONE order. Do NOT
    use to promise a NEW delivery time — see reschedule_delivery.
    order_id format: TW-YYYY-NNNNN."""
    return estimate_eta_impl(order_id)


@tool
def get_delivery_events(order_id: str) -> dict:
    """Get the full delivery-event timeline for ONE order. Use to
    investigate a dispute or complaint, not for a quick status check.
    order_id format: TW-YYYY-NNNNN."""
    return get_delivery_events_impl(order_id)


@tool
def get_driver_status(courier_id: str) -> dict:
    """Get a courier's most recent activity across deliveries. Internal
    ops use only — NOT for a customer's 'where is my order' question.
    courier_id format: DRV-NNN."""
    return get_driver_status_impl(courier_id)


@tool
def find_delivery_exception(order_id: str) -> dict:
    """Find the most recent delivery exception for ONE order, if any. Use
    when investigating a delivery problem before deciding next steps.
    order_id format: TW-YYYY-NNNNN."""
    return find_delivery_exception_impl(order_id)


@tool
def reschedule_delivery(order_id: str, new_promised_at_iso: str) -> dict:
    """Reschedule ONE order's promised delivery time. WRITE, not
    idempotent-safe to retry blindly. Confirm the new time with the
    customer first. order_id format: TW-YYYY-NNNNN; new_promised_at_iso:
    ISO-8601 datetime with timezone offset."""
    return reschedule_delivery_impl(order_id, new_promised_at_iso)


TOOLS = [
    track_shipment, estimate_eta, get_delivery_events,
    get_driver_status, find_delivery_exception, reschedule_delivery,
]
