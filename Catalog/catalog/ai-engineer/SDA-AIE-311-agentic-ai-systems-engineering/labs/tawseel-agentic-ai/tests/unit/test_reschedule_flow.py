"""Module 7 — pytest-style tests for `src/rafeeq/flows/reschedule_flow.py`.

Same discipline as `test_refund_flow.py`, applied to the four named
rules SPEC asks this flow to encode as branches: window validity, city
cut-off, max 2 reschedules, courier availability. See
`tests/unit/run_without_pytest.py` for the stdlib mirror.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.adapters.store import store
from rafeeq.flows.reschedule_flow import (
    MAX_RESCHEDULES_PER_ORDER,
    city_cutoff_gate,
    courier_availability_gate,
    do_reschedule,
    load_order_context,
    max_reschedules_gate,
    reschedulable_gate,
    request_human_approval,
    window_gate,
)

RESCHEDULABLE_ORDER_ID = "TW-2026-10030"     # in_transit (see tests/unit/run_without_pytest.py)
DELIVERED_ORDER_ID = "TW-2026-10002"


@pytest.fixture(autouse=True)
def _reset_store():
    store.reset()
    yield
    store.reset()


class TestReschedulableGate:
    @pytest.mark.parametrize("status, expected", [
        ("processing", "proceed"),
        ("in_transit", "proceed"),
        ("out_for_delivery", "proceed"),
        ("delivered", "not_reschedulable"),
        ("exception", "not_reschedulable"),
    ])
    def test_status(self, status, expected):
        assert reschedulable_gate({"status": status}) == expected


class TestMaxReschedulesGate:
    @pytest.mark.parametrize("count, expected", [
        (0, "proceed"),
        (1, "proceed"),
        (MAX_RESCHEDULES_PER_ORDER, "needs_human"),         # the THIRD request escalates
        (MAX_RESCHEDULES_PER_ORDER + 1, "needs_human"),
    ])
    def test_count(self, count, expected):
        assert max_reschedules_gate({"reschedule_count": count}) == expected

    def test_missing_count_defaults_to_zero_and_proceeds(self):
        assert max_reschedules_gate({}) == "proceed"


class TestWindowGate:
    @pytest.mark.parametrize("requested_at, new_at, expected", [
        ("2026-03-04T08:00:00+03:00", "2026-03-04T12:00:00+03:00", "proceed"),      # exactly 4h
        ("2026-03-04T08:00:00+03:00", "2026-03-11T08:00:00+03:00", "proceed"),      # exactly 7 days
        ("2026-03-04T08:00:00+03:00", "2026-03-04T09:00:00+03:00", "invalid_window"),  # too soon
        ("2026-03-04T08:00:00+03:00", "2026-03-12T08:00:01+03:00", "invalid_window"),  # too far out
        ("2026-03-04T08:00:00+03:00", "2026-03-03T08:00:00+03:00", "invalid_window"),  # in the past
    ])
    def test_window(self, requested_at, new_at, expected):
        state = {"requested_at_iso": requested_at, "new_promised_at_iso": new_at}
        assert window_gate(state) == expected

    def test_missing_fields_fail_closed(self):
        assert window_gate({}) == "invalid_window"


class TestCityCutoffGate:
    def test_friday_is_unavailable(self):
        # 2026-03-06 is a Friday.
        assert city_cutoff_gate({"new_promised_at_iso": "2026-03-06T13:00:00+03:00"}) == "friday_unavailable"

    def test_non_friday_proceeds(self):
        # 2026-03-05 is a Thursday.
        assert city_cutoff_gate({"new_promised_at_iso": "2026-03-05T13:00:00+03:00"}) == "proceed"

    def test_unparsable_time_fails_closed(self):
        assert city_cutoff_gate({"new_promised_at_iso": "not-a-date"}) == "friday_unavailable"


class TestCourierAvailabilityGate:
    def test_explicit_unavailable_blocks(self):
        assert courier_availability_gate({"courier_available": False}) == "courier_unavailable"

    def test_explicit_available_proceeds(self):
        assert courier_availability_gate({"courier_available": True}) == "proceed"

    def test_unknown_availability_proceeds(self):
        """Absence of information must not be treated as unavailability —
        only an explicit False blocks."""
        assert courier_availability_gate({}) == "proceed"


class TestRescheduleFlowIntegration:
    def test_load_order_context_populates_status_and_city(self):
        state = load_order_context({"order_id": RESCHEDULABLE_ORDER_ID})
        assert state["status"] == "in_transit"
        assert state["city"]

    def test_full_chain_happy_path_reschedules(self):
        state = {"order_id": RESCHEDULABLE_ORDER_ID}
        state.update(load_order_context(state))
        assert reschedulable_gate(state) == "proceed"
        state["reschedule_count"] = 0
        assert max_reschedules_gate(state) == "proceed"
        state["requested_at_iso"] = "2026-03-04T08:00:00+03:00"
        state["new_promised_at_iso"] = "2026-03-05T18:00:00+03:00"    # Thursday, +34h
        assert window_gate(state) == "proceed"
        assert city_cutoff_gate(state) == "proceed"
        assert courier_availability_gate(state) == "proceed"
        result = do_reschedule(state)
        assert result["decision"] == "approve"
        assert result["reschedule_result"]["rescheduled"] is True

    def test_delivered_order_is_not_reschedulable(self):
        state = {"order_id": DELIVERED_ORDER_ID}
        state.update(load_order_context(state))
        assert reschedulable_gate(state) == "not_reschedulable"

    def test_third_request_escalates_and_records_approval_request(self):
        state = {"order_id": RESCHEDULABLE_ORDER_ID, "customer_id": "CUST-6425",
                  "reschedule_count": MAX_RESCHEDULES_PER_ORDER,
                  "new_promised_at_iso": "2026-03-05T18:00:00+03:00"}
        assert max_reschedules_gate(state) == "needs_human"
        result = request_human_approval(state)
        assert result["decision"] == "needs_human"
        assert result["approval_request"]["order_id"] == RESCHEDULABLE_ORDER_ID
        assert result["approval_request"]["threshold"] == MAX_RESCHEDULES_PER_ORDER
