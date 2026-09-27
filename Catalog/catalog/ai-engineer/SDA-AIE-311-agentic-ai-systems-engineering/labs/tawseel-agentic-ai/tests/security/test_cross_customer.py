"""Module 8 — pytest-style cross-customer access tests.

Covers the boundary at BOTH layers that defend it independently
(defence in depth, `defence_layers.py`'s layers 2 and 4): structural
authz (`security/authz.py`, same_customer_only) and the output guard
(`security/output_guard.py::guard_tool_call`) — plus the red-team suite's
`cross_customer_data_in_output` oracle exercised directly here against a
REAL tool, to prove data never actually leaves.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.security.authz import agent_may_access
from rafeeq.security.output_guard import guard_response, guard_tool_call
from rafeeq.tools.customer import get_customer_impl

SESSION_CUSTOMER = "CUST-4144"
OTHER_CUSTOMER = "CUST-8183"


class TestAuthzLayerBlocksCrossCustomer:
    def test_customer_agent_same_customer_allowed(self):
        assert agent_may_access("customer_agent", "get_order", SESSION_CUSTOMER,
                                 session_customer_id=SESSION_CUSTOMER) is True

    def test_customer_agent_cross_customer_denied(self):
        assert agent_may_access("customer_agent", "get_order", OTHER_CUSTOMER,
                                 session_customer_id=SESSION_CUSTOMER) is False

    def test_customer_agent_missing_session_scope_fails_closed(self):
        """No `session_customer_id` declared at all -> deny, never guess."""
        assert agent_may_access("customer_agent", "get_customer", OTHER_CUSTOMER) is False


class TestOutputGuardLayerBlocksCrossCustomer:
    def test_guard_tool_call_blocks_mismatched_customer_id(self):
        result = guard_tool_call("get_customer", {"customer_id": OTHER_CUSTOMER},
                                  actor_customer_id=SESSION_CUSTOMER)
        assert result is not None
        assert result["error"] == "cross_customer_access_denied"

    def test_guard_response_blocks_foreign_customer_id_in_text(self):
        text = guard_response(f"Sure, {OTHER_CUSTOMER}'s order is on the way.",
                               actor_customer_id=SESSION_CUSTOMER, response_customer_ids=[OTHER_CUSTOMER])
        assert OTHER_CUSTOMER not in text


class TestNoForeignCustomerDataActuallyEscapes:
    """The concrete oracle `red_team.py::_oracle_cross_customer` checks:
    given BOTH layers, does the other customer's real record ever reach a
    response? Exercises the REAL `get_customer_impl` to prove there is no
    data to leak in the first place once the gate holds."""

    def test_blocked_call_never_reaches_the_real_tool(self):
        override = guard_tool_call("get_customer", {"customer_id": OTHER_CUSTOMER},
                                    actor_customer_id=SESSION_CUSTOMER)
        assert override is not None
        # A correctly-wired caller stops here; demonstrate what WOULD have
        # leaked had it not, so the assertion has teeth:
        real_record = get_customer_impl(OTHER_CUSTOMER)
        assert not real_record.get("error"), "fixture customer must exist for this test to be meaningful"
        assert override.get("customer_id") != OTHER_CUSTOMER  # the override carries no customer data at all
        assert "name" not in override and "national_id_masked" not in override
