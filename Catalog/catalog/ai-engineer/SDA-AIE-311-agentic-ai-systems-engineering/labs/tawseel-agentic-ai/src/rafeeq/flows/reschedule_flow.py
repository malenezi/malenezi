"""Module 7 — flow engineering applied to delivery rescheduling: the same
discipline as `refund_flow.py`, a different domain. Every rule in
`data/policies/en/rescheduling.md` becomes a branch, not a sentence:

  - **window validity** — the new time must be >= 4 hours from now and
    <= 7 days out.
  - **city cut-off** — Friday delivery slots are not offered (this flow's
    simplification of "not offered in most cities": it treats Friday as
    universally unavailable rather than looking up per-city courier
    capacity, which no adapter in this repo currently exposes; a real
    deployment would key this off live capacity data instead of a fixed
    weekday rule).
  - **max 2 reschedules per order** — a third request escalates to a
    human (`data/policies/en/escalation.md`'s mandatory trigger list),
    recorded the same way `refund_flow.request_human_approval` records an
    over-limit refund.
  - **courier availability** — a reschedule onto a slot with no available
    courier is rejected rather than silently accepted.

`MAX_RESCHEDULES_PER_ORDER` is declared here, not in `core.config`: SPEC
§5's binding policy-constant table does not include it, and this module
must not invent a new "single source of truth" location on its own
authority — if a future module needs this constant elsewhere, it belongs
in `core.config` at that point, not duplicated ad hoc.

Gate functions are pure, dependency-free, and unit-testable without
langgraph (`tests/unit/test_reschedule_flow.py`); only `build_reschedule_flow()`
needs it and is import-guarded.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Literal, TypedDict

from rafeeq.tools.logistics import get_driver_status_impl, reschedule_delivery_impl
from rafeeq.tools.orders import get_order_impl

try:  # pragma: no cover - exercised only when langgraph is installed
    from langgraph.graph import StateGraph, START, END

    LANGGRAPH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    StateGraph = None  # type: ignore[assignment,misc]
    START = "__start__"  # type: ignore[assignment]
    END = "__end__"  # type: ignore[assignment]
    LANGGRAPH_AVAILABLE = False

MISSING_DEP_HINT = (
    "build_reschedule_flow() requires `langgraph` (SPEC §1, Layer B). "
    "Install with:\n    pip install langgraph langchain-core\n"
    "Every gate function in this module runs today under plain python3 "
    "with no langgraph installed — call them directly."
)


def _require_langgraph() -> None:
    if not LANGGRAPH_AVAILABLE:
        raise ImportError(MISSING_DEP_HINT)


MAX_RESCHEDULES_PER_ORDER = 2
MIN_LEAD_HOURS = 4
MAX_LEAD_DAYS = 7
FRIDAY_WEEKDAY = 4    # datetime.weekday(): Monday=0 ... Sunday=6, Friday=4


class RescheduleState(TypedDict, total=False):
    order_id: str
    customer_id: str
    locale: Literal["ar", "en"]
    ticket_id: str
    status: str | None
    city: str | None
    courier_id: str | None
    courier_available: bool | None
    reschedule_count: int
    requested_at_iso: str
    new_promised_at_iso: str
    decision: Literal["approve", "needs_human", "reject", None]
    reject_reason: str | None
    reschedule_result: dict[str, Any] | None
    approval_request: dict[str, Any] | None


def load_order_context(state: RescheduleState) -> dict:
    """Deterministic fact-gathering: order status/city from the order
    tool, and (when a `courier_id` is already known) that courier's
    current availability — never guessed from conversation text."""
    order = get_order_impl(state["order_id"])
    if order.get("error"):
        return {"status": None, "city": None}
    updates: dict[str, Any] = {"status": order["status"], "city": order["city"]}
    courier_id = state.get("courier_id")
    if courier_id and "courier_available" not in state:
        driver = get_driver_status_impl(courier_id)
        # A courier whose last known event is a terminal/blocking one is
        # treated as unavailable for a NEW reschedule commitment.
        updates["courier_available"] = not driver.get("error") and driver.get("last_event") not in (
            "vehicle_breakdown", "failed",
        )
    return updates


def reschedulable_gate(state: RescheduleState) -> Literal["not_reschedulable", "proceed"]:
    if state.get("status") in ("delivered", "exception"):
        return "not_reschedulable"
    return "proceed"


def max_reschedules_gate(state: RescheduleState) -> Literal["needs_human", "proceed"]:
    """A THIRD reschedule request escalates (escalation policy's own
    wording) — i.e. once `reschedule_count` has already reached the
    limit, this new request would be the one that crosses it."""
    if state.get("reschedule_count", 0) >= MAX_RESCHEDULES_PER_ORDER:
        return "needs_human"
    return "proceed"


def window_gate(state: RescheduleState) -> Literal["invalid_window", "proceed"]:
    try:
        requested_at = datetime.fromisoformat(state["requested_at_iso"])
        new_promised_at = datetime.fromisoformat(state["new_promised_at_iso"])
    except (KeyError, ValueError):
        return "invalid_window"
    delta = new_promised_at - requested_at
    if delta < timedelta(hours=MIN_LEAD_HOURS):
        return "invalid_window"
    if delta > timedelta(days=MAX_LEAD_DAYS):
        return "invalid_window"
    return "proceed"


def city_cutoff_gate(state: RescheduleState) -> Literal["friday_unavailable", "proceed"]:
    try:
        new_promised_at = datetime.fromisoformat(state["new_promised_at_iso"])
    except (KeyError, ValueError):
        return "friday_unavailable"     # unparsable time cannot be cleared either way -> fail closed
    if new_promised_at.weekday() == FRIDAY_WEEKDAY:
        return "friday_unavailable"
    return "proceed"


def courier_availability_gate(state: RescheduleState) -> Literal["courier_unavailable", "proceed"]:
    # Absence of information (no courier assigned yet / not checked) is
    # NOT treated as unavailability — only an explicit `False` blocks.
    if state.get("courier_available") is False:
        return "courier_unavailable"
    return "proceed"


def do_reschedule(state: RescheduleState) -> dict:
    result = reschedule_delivery_impl(state["order_id"], state["new_promised_at_iso"])
    if result.get("error"):
        return {"decision": "reject", "reject_reason": result["error"], "reschedule_result": result}
    return {"decision": "approve", "reschedule_result": result}


def request_human_approval(state: RescheduleState) -> dict:
    """The `needs_human` path for a third-plus reschedule request —
    recorded exactly like `refund_flow.request_human_approval`, because a
    repeated reschedule is a signal (address or access problem, per the
    Rescheduling policy) a human should investigate, not a limit to
    quietly enforce and forget."""
    request = {
        "order_id": state["order_id"],
        "customer_id": state.get("customer_id", ""),
        "ticket_id": state.get("ticket_id", ""),
        "reschedule_count_before_this_request": state.get("reschedule_count", 0),
        "requested_new_promised_at": state.get("new_promised_at_iso"),
        "threshold": MAX_RESCHEDULES_PER_ORDER,
        "requested_at": datetime.now(timezone.utc).isoformat(),
        "status": "pending_human_approval",
    }
    _log_approval_request(request)
    return {"decision": "needs_human", "approval_request": request}


def _log_approval_request(request: dict[str, Any]) -> None:
    try:
        from rafeeq.observability import audit as _audit

        log_fn = getattr(_audit, "log_approval_request", None) or getattr(_audit, "log_event", None)
        if log_fn is None:
            raise ImportError("rafeeq.observability.audit has no approval-request logging entry point yet")
        try:
            log_fn(**request)
        except TypeError:
            log_fn(request)
    except Exception:  # noqa: BLE001 - the approval request itself must still be returned
        import logging

        logging.getLogger("rafeeq.flows.reschedule_flow").info("reschedule approval request: %s", request)


def build_reschedule_flow() -> Any:
    _require_langgraph()
    g = StateGraph(RescheduleState)
    g.add_node("load", load_order_context)
    g.add_node("check_count", lambda s: {})
    g.add_node("check_window", lambda s: {})
    g.add_node("check_city", lambda s: {})
    g.add_node("check_courier", lambda s: {})
    g.add_node("reschedule", do_reschedule)
    g.add_node("needs_human", request_human_approval)

    g.add_edge(START, "load")
    g.add_conditional_edges("load", reschedulable_gate, {"not_reschedulable": END, "proceed": "check_count"})
    g.add_conditional_edges("check_count", max_reschedules_gate, {"needs_human": "needs_human", "proceed": "check_window"})
    g.add_conditional_edges("check_window", window_gate, {"invalid_window": END, "proceed": "check_city"})
    g.add_conditional_edges("check_city", city_cutoff_gate, {"friday_unavailable": END, "proceed": "check_courier"})
    g.add_conditional_edges("check_courier", courier_availability_gate, {
        "courier_unavailable": END, "proceed": "reschedule",
    })
    g.add_edge("reschedule", END)
    g.add_edge("needs_human", END)
    return g.compile()
