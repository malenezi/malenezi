"""Module 3/8 — pytest-style tests for `src/rafeeq/security/authz.py`.

Covers allow, deny (unknown agent, unknown tool, domain not granted,
tool explicitly denied, prohibited action) and cross-customer deny — the
module's central lesson made testable: authorisation is enforced in code,
not by trusting a prompt. See `tests/unit/run_without_pytest.py` for the
stdlib-`unittest` mirror of these same assertions.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.security.authz import PROHIBITED_TOOLS, agent_may_access, explain


class TestAllow:
    def test_customer_agent_may_read_own_customer_orders(self):
        assert agent_may_access(
            "customer_agent", "track_shipment", "CUST-4144",
            session_customer_id="CUST-4144",
        ) is True

    def test_customer_agent_may_refund_own_customer(self):
        assert agent_may_access(
            "customer_agent", "issue_refund", "CUST-4144",
            session_customer_id="CUST-4144",
        ) is True

    def test_ops_agent_may_read_any_customer(self):
        """ops_agent is explicitly cross-customer for read domains — no
        session_customer_id needed because same_customer_only=False."""
        assert agent_may_access("ops_agent", "get_order", "CUST-8183") is True

    def test_billing_admin_may_mark_refunded(self):
        assert agent_may_access("billing_admin_agent", "mark_refunded", "CUST-8183") is True


class TestDeny:
    def test_unknown_agent_denied(self):
        decision = explain("nobody", "track_shipment", "CUST-4144")
        assert decision.allowed is False
        assert decision.reason == "unknown_agent"

    def test_unknown_tool_denied(self):
        decision = explain("customer_agent", "delete_everything", "CUST-4144",
                            session_customer_id="CUST-4144")
        assert decision.allowed is False
        assert decision.reason == "unknown_tool"

    def test_domain_not_granted_denied(self):
        """partner_agent has NO billing domain grant at all."""
        decision = explain("partner_agent", "issue_refund", "CUST-4144",
                            session_customer_id="CUST-4144")
        assert decision.allowed is False
        assert decision.reason == "domain_not_granted"

    def test_ops_agent_cannot_touch_billing(self):
        assert agent_may_access("ops_agent", "issue_refund", "CUST-8183") is False

    def test_explicitly_denied_tool(self):
        """customer_agent has the billing DOMAIN, but mark_refunded is an
        explicit exception within it (reconciliation-only tool)."""
        decision = explain("customer_agent", "mark_refunded", "CUST-4144",
                            session_customer_id="CUST-4144")
        assert decision.allowed is False
        assert decision.reason == "tool_explicitly_denied"

    def test_prohibited_action_always_denied(self):
        for tool_name in PROHIBITED_TOOLS:
            decision = explain("customer_agent", tool_name, "CUST-4144",
                                session_customer_id="CUST-4144")
            assert decision.allowed is False
            assert decision.reason == "prohibited_action"

    def test_missing_session_customer_id_fails_closed(self):
        """A same-customer-only identity with NO session scope declared
        must be denied, not defaulted to allow."""
        decision = explain("customer_agent", "get_customer", "CUST-4144")
        assert decision.allowed is False
        assert decision.reason == "missing_session_customer_id"


class TestCrossCustomerDeny:
    def test_customer_agent_cannot_read_a_different_customer(self):
        decision = explain(
            "customer_agent", "get_customer", "CUST-8183",
            session_customer_id="CUST-4144",
        )
        assert decision.allowed is False
        assert decision.reason == "cross_customer_denied"

    def test_partner_agent_cannot_read_a_different_customer(self):
        decision = explain(
            "partner_agent", "track_shipment", "CUST-8183",
            session_customer_id="CUST-4144",
        )
        assert decision.allowed is False
        assert decision.reason == "cross_customer_denied"

    def test_customer_agent_cannot_refund_a_different_customer(self):
        """The exact injection this guards against (SPEC §6, AgentDojo-
        style): even if a jailbroken prompt insists on a DIFFERENT
        customer's order, the server-side check still refuses it."""
        decision = explain(
            "customer_agent", "issue_refund", "CUST-8183",
            session_customer_id="CUST-4144",
        )
        assert decision.allowed is False
        assert decision.reason == "cross_customer_denied"
