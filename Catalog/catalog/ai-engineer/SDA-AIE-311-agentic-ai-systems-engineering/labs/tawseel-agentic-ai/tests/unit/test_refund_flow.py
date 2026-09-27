"""Module 7 — pytest-style tests for `src/rafeeq/flows/refund_flow.py`.

The package's table tests (`amount_gate`, `eligibility_gate`), extended
for the SPEC §5 autonomous-under-50-SAR band, plus integration tests
against real seed data proving `load_order` -> gate -> `do_refund` /
`request_human_approval` actually dispatches to the governed billing
tool. See `tests/unit/run_without_pytest.py` for the stdlib mirror.
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
from rafeeq.core.config import AUTO_REFUND_LIMIT_SAR, REFUND_LIMIT_SAR
from rafeeq.flows.refund_flow import (
    amount_gate,
    do_refund,
    eligibility_gate,
    load_order,
    request_human_approval,
)

AUTO_APPROVE_ORDER_ID = "TW-2026-10206"    # 35.0 SAR, sla_breached, not refunded
APPROVE_ORDER_ID = "TW-2026-10233"         # 348.8 SAR, sla_breached, not refunded
NEEDS_HUMAN_ORDER_ID = "TW-2026-39725"     # 748.68 SAR, sla_breached, not refunded
NOT_ELIGIBLE_ORDER_ID = "TW-2026-10002"    # 35.0 SAR, NOT sla_breached


@pytest.fixture(autouse=True)
def _reset_store():
    store.reset()
    yield
    store.reset()


class TestAmountGateIsDeterministic:
    @pytest.mark.parametrize("amount, expected", [
        (0.01, "auto_approve"),
        (AUTO_REFUND_LIMIT_SAR, "auto_approve"),            # boundary: exactly 50 -> autonomous
        (AUTO_REFUND_LIMIT_SAR + 0.01, "approve"),           # just above 50 -> policy-controlled
        (REFUND_LIMIT_SAR, "approve"),                       # boundary: exactly 500 -> still autonomous
        (REFUND_LIMIT_SAR + 0.01, "needs_human"),            # just above 500 -> human required
        (5000.0, "needs_human"),
    ])
    def test_amount_gate(self, amount, expected):
        assert amount_gate({"amount": amount}) == expected   # same input, same route, always


class TestEligibilityGate:
    @pytest.mark.parametrize("refunded, sla, expected", [
        (True, True, "reject"),       # never twice
        (False, False, "reject"),     # not eligible
        (False, True, "decide"),      # eligible -> decide amount
        (True, False, "reject"),      # already refunded wins regardless of SLA
    ])
    def test_eligibility_gate(self, refunded, sla, expected):
        assert eligibility_gate({"already_refunded": refunded, "sla_breached": sla}) == expected


class TestLoadOrder:
    def test_load_order_populates_gate_inputs(self):
        state = load_order({"order_id": AUTO_APPROVE_ORDER_ID})
        assert state["sla_breached"] is True
        assert state["already_refunded"] is False
        assert state["amount"] == pytest.approx(35.0)

    def test_load_order_unknown_order_fails_closed(self):
        state = load_order({"order_id": "TW-2026-00000"})
        assert state["amount"] is None
        assert state["sla_breached"] is False
        assert state["order_error"] == "order_not_found"


class TestRefundFlowIntegration:
    """load_order -> eligibility_gate -> amount_gate -> do_refund /
    request_human_approval, end to end against real seed data."""

    def test_auto_approve_band_issues_refund(self):
        state = {"order_id": AUTO_APPROVE_ORDER_ID, "customer_id": "CUST-7845", "ticket_id": "t1"}
        state.update(load_order(state))
        assert eligibility_gate(state) == "decide"
        assert amount_gate(state) == "auto_approve"
        result = do_refund(state)
        assert result["decision"] == "auto_approve"
        assert result["refund_result"]["amount_sar"] == pytest.approx(35.0)
        assert result["refund_result"]["requires_human_approval"] is False

    def test_policy_controlled_band_issues_refund(self):
        state = {"order_id": APPROVE_ORDER_ID, "customer_id": "CUST-7047", "ticket_id": "t2"}
        state.update(load_order(state))
        assert amount_gate(state) == "approve"
        result = do_refund(state)
        assert result["decision"] == "approve"
        assert result["refund_result"]["amount_sar"] == pytest.approx(348.8)

    def test_over_limit_band_never_calls_issue_refund_and_records_request(self):
        state = {"order_id": NEEDS_HUMAN_ORDER_ID, "customer_id": "CUST-8180", "ticket_id": "t3"}
        state.update(load_order(state))
        assert amount_gate(state) == "needs_human"
        result = request_human_approval(state)
        assert result["decision"] == "needs_human"
        req = result["approval_request"]
        assert req["order_id"] == NEEDS_HUMAN_ORDER_ID
        assert req["amount_sar"] == pytest.approx(748.68)
        assert req["threshold_sar"] == REFUND_LIMIT_SAR
        assert req["status"] == "pending_human_approval"
        # The order must NOT be refunded by taking the needs_human path.
        assert store.get_order(NEEDS_HUMAN_ORDER_ID)["refunded"] is False

    def test_not_sla_breached_rejects_before_any_refund_call(self):
        state = {"order_id": NOT_ELIGIBLE_ORDER_ID, "customer_id": "CUST-4144"}
        state.update(load_order(state))
        assert eligibility_gate(state) == "reject"
        assert store.get_order(NOT_ELIGIBLE_ORDER_ID)["refunded"] is False

    def test_double_refund_is_rejected_by_eligibility_gate(self):
        """The M1 double-refund ghost, at the flow level: once refunded,
        eligibility_gate must reject a second pass before amount_gate is
        even consulted."""
        state = {"order_id": AUTO_APPROVE_ORDER_ID, "customer_id": "CUST-7845", "ticket_id": "t4"}
        state.update(load_order(state))
        do_refund(state)                                  # first refund succeeds
        state2 = {"order_id": AUTO_APPROVE_ORDER_ID}
        state2.update(load_order(state2))
        assert state2["already_refunded"] is True
        assert eligibility_gate(state2) == "reject"
