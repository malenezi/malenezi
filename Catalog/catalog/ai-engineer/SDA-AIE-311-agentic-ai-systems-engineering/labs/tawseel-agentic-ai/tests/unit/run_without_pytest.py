#!/usr/bin/env python3
"""Module 3 — stdlib-only test runner (no pytest).

SPEC §1: pytest cannot be installed in the build/CI sandbox this repo was
authored in, so the assertions in `test_tools.py` and `test_authz.py`
(pytest-style, for the classroom container where pytest DOES exist) are
mirrored here using nothing but `unittest`, so they can be verified in
THIS environment too. Keep the two files in sync: every case added to
`test_tools.py`/`test_authz.py` should have a stdlib equivalent here, and
vice versa.

Usage: `python3 tests/unit/run_without_pytest.py` (from anywhere; the repo
root and `src/` are resolved relative to this file, exactly like
`scripts/selfcheck.py`).
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_REPO_ROOT) not in sys.path:  # for `import mcp_servers.*`
    sys.path.insert(0, str(_REPO_ROOT))

from rafeeq.adapters.store import store  # noqa: E402
from rafeeq.security.authz import PROHIBITED_TOOLS, agent_may_access, explain  # noqa: E402
from rafeeq.tools.billing import (  # noqa: E402
    get_invoice_impl,
    get_payment_impl,
    issue_refund_impl,
    mark_refunded_impl,
)
from rafeeq.tools.customer import (  # noqa: E402
    add_case_note_impl,
    get_customer_impl,
    get_customer_tickets_impl,
)
from rafeeq.tools.logistics import (  # noqa: E402
    estimate_eta_impl,
    find_delivery_exception_impl,
    get_delivery_events_impl,
    get_driver_status_impl,
    reschedule_delivery_impl,
)
from rafeeq.tools.logistics import track_shipment_impl as logistics_track_shipment_impl  # noqa: E402
from rafeeq.tools.orders import get_order_impl, get_order_items_impl, list_orders_impl  # noqa: E402
from rafeeq.tools.tawseel import track_shipment_impl  # noqa: E402

# --- Module 2/5/6/7 additions (agent/graph layer) -------------------------
from rafeeq.agents.scoping import FORBIDDEN_FIELDS, SCOPE, assert_no_forbidden_leak, scoped_input  # noqa: E402
from rafeeq.core.config import (  # noqa: E402
    AUTO_REFUND_LIMIT_SAR,
    MAX_STEPS,
    REFUND_LIMIT_SAR,
    ROUTING_EVAL_PATH,
    TICKET_INTENTS,
)
from rafeeq.core.graph import route as core_route  # noqa: E402
from rafeeq.core.graph import route_with_tools as core_route_with_tools  # noqa: E402
from rafeeq.flows.refund_flow import (  # noqa: E402
    amount_gate as refund_amount_gate,
)
from rafeeq.flows.refund_flow import do_refund as refund_do_refund  # noqa: E402
from rafeeq.flows.refund_flow import eligibility_gate as refund_eligibility_gate  # noqa: E402
from rafeeq.flows.refund_flow import load_order as refund_load_order  # noqa: E402
from rafeeq.flows.refund_flow import request_human_approval as refund_request_human_approval  # noqa: E402
from rafeeq.flows.reschedule_flow import MAX_RESCHEDULES_PER_ORDER  # noqa: E402
from rafeeq.flows.reschedule_flow import city_cutoff_gate  # noqa: E402
from rafeeq.flows.reschedule_flow import courier_availability_gate  # noqa: E402
from rafeeq.flows.reschedule_flow import do_reschedule  # noqa: E402
from rafeeq.flows.reschedule_flow import load_order_context  # noqa: E402
from rafeeq.flows.reschedule_flow import max_reschedules_gate  # noqa: E402
from rafeeq.flows.reschedule_flow import reschedulable_gate  # noqa: E402
from rafeeq.flows.reschedule_flow import request_human_approval as reschedule_request_human_approval  # noqa: E402
from rafeeq.flows.reschedule_flow import window_gate  # noqa: E402
from rafeeq.orchestration.fastpath import FASTPATH_CONFIDENCE_THRESHOLD, fastpath_route  # noqa: E402
from rafeeq.orchestration.routing import (  # noqa: E402
    INTENT_SPECIALIST, classify_intent, classify_intents_multi, specialist_for_intent,
)

ORDER_ID = "TW-2026-10002"
ORDER_CUSTOMER_ID = "CUST-4144"
PAYMENT_ID = "PAY-110002"
EXCEPTION_ORDER_ID = "TW-2026-10206"
DRIVER_ID = "DRV-254"
RESCHEDULABLE_ORDER_ID = "TW-2026-10030"
TICKETED_CUSTOMER_ID = "CUST-1045"
HIGH_VALUE_ORDER_ID = "TW-2026-23560"
HIGH_VALUE_CUSTOMER_ID = "CUST-1897"


class ToolsBase(unittest.TestCase):
    def setUp(self) -> None:
        store.reset()

    def tearDown(self) -> None:
        store.reset()


class TestTawseelTrackShipment(ToolsBase):
    def test_bad_id_format(self):
        self.assertEqual(track_shipment_impl("not-an-order-id"), {"error": "invalid_order_id_format"})

    def test_not_found(self):
        self.assertEqual(track_shipment_impl("TW-2026-00000"), {"error": "order_not_found"})

    def test_happy_path(self):
        result = track_shipment_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)
        self.assertEqual(result["status"], "delivered")
        self.assertNotIn("error", result)


class TestOrdersTools(ToolsBase):
    def test_get_order_bad_format(self):
        self.assertEqual(get_order_impl("garbage"), {"error": "invalid_order_id_format"})

    def test_get_order_not_found(self):
        self.assertEqual(get_order_impl("TW-2026-00000"), {"error": "order_not_found"})

    def test_get_order_happy_path(self):
        result = get_order_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)
        self.assertEqual(result["customer_id"], ORDER_CUSTOMER_ID)

    def test_list_orders_bad_format(self):
        self.assertEqual(list_orders_impl("nope"), {"error": "invalid_customer_id_format"})

    def test_list_orders_unknown_customer_is_empty_not_an_error(self):
        self.assertEqual(list_orders_impl("CUST-0000"), {"customer_id": "CUST-0000", "orders": []})

    def test_list_orders_happy_path(self):
        result = list_orders_impl(ORDER_CUSTOMER_ID)
        self.assertTrue(any(o["order_id"] == ORDER_ID for o in result["orders"]))

    def test_get_order_items_happy_path(self):
        result = get_order_items_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)
        self.assertIsInstance(result["items_count"], int)


class TestLogisticsTools(ToolsBase):
    def test_track_shipment_bad_format(self):
        self.assertEqual(logistics_track_shipment_impl("garbage"), {"error": "invalid_order_id_format"})

    def test_track_shipment_not_found(self):
        self.assertEqual(logistics_track_shipment_impl("TW-2026-00000"), {"error": "order_not_found"})

    def test_track_shipment_happy_path(self):
        result = logistics_track_shipment_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)
        self.assertIn("status", result)

    def test_estimate_eta_happy_path(self):
        result = estimate_eta_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)
        self.assertIn("eta_iso", result)

    def test_estimate_eta_not_found(self):
        self.assertEqual(estimate_eta_impl("TW-2026-00000"), {"error": "order_not_found"})

    def test_get_delivery_events_happy_path(self):
        result = get_delivery_events_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)
        self.assertGreater(len(result["events"]), 0)

    def test_get_driver_status_bad_format(self):
        self.assertEqual(get_driver_status_impl("nope"), {"error": "invalid_driver_id_format"})

    def test_get_driver_status_happy_path(self):
        result = get_driver_status_impl(DRIVER_ID)
        self.assertEqual(result["courier_id"], DRIVER_ID)

    def test_find_delivery_exception_found(self):
        result = find_delivery_exception_impl(EXCEPTION_ORDER_ID)
        self.assertEqual(result["order_id"], EXCEPTION_ORDER_ID)
        self.assertIsNotNone(result["exception_code"])

    def test_find_delivery_exception_none(self):
        result = find_delivery_exception_impl(ORDER_ID)
        self.assertIsNone(result["exception_code"])

    def test_reschedule_delivery_not_found(self):
        result = reschedule_delivery_impl("TW-2026-00000", "2026-05-01T18:00:00+03:00")
        self.assertEqual(result, {"error": "order_not_found"})

    def test_reschedule_delivery_not_reschedulable(self):
        result = reschedule_delivery_impl(ORDER_ID, "2026-05-01T18:00:00+03:00")
        self.assertEqual(result["error"], "not_reschedulable")

    def test_reschedule_delivery_happy_path(self):
        new_time = "2026-05-01T18:00:00+03:00"
        result = reschedule_delivery_impl(RESCHEDULABLE_ORDER_ID, new_time)
        self.assertTrue(result["rescheduled"])
        self.assertEqual(result["promised_at_after"], new_time)


class TestBillingTools(ToolsBase):
    def test_get_invoice_happy_path(self):
        result = get_invoice_impl(ORDER_ID)
        self.assertEqual(result["order_id"], ORDER_ID)

    def test_get_invoice_not_found(self):
        self.assertEqual(get_invoice_impl("TW-2026-00000"), {"error": "order_not_found"})

    def test_get_payment_bad_format(self):
        self.assertEqual(get_payment_impl("nope"), {"error": "invalid_payment_id_format"})

    def test_get_payment_happy_path(self):
        result = get_payment_impl(PAYMENT_ID)
        self.assertEqual(result["payment_id"], PAYMENT_ID)

    def test_issue_refund_missing_idempotency_key(self):
        self.assertEqual(issue_refund_impl(ORDER_ID, 10.0, "goodwill", ""), {"error": "missing_idempotency_key"})

    def test_issue_refund_invalid_amount(self):
        self.assertEqual(issue_refund_impl(ORDER_ID, 0.0, "goodwill", "key-1"), {"error": "invalid_amount"})

    def test_issue_refund_order_not_found(self):
        result = issue_refund_impl("TW-2026-00000", 10.0, "goodwill", "key-1")
        self.assertEqual(result, {"error": "order_not_found"})

    def test_issue_refund_is_idempotent_by_key(self):
        first = issue_refund_impl(ORDER_ID, 5.0, "goodwill", "same-key")
        second = issue_refund_impl(ORDER_ID, 5.0, "goodwill", "same-key")
        self.assertFalse(first["idempotent_replay"])
        self.assertTrue(second["idempotent_replay"])
        self.assertEqual(first["amount_sar"], second["amount_sar"])
        third = issue_refund_impl(ORDER_ID, 5.0, "goodwill", "different-key")
        self.assertFalse(third["idempotent_replay"])
        self.assertEqual(third["total_refunded_sar"], 10.0)

    def test_issue_refund_flags_human_approval_above_limit(self):
        result = issue_refund_impl(HIGH_VALUE_ORDER_ID, 970.36, "damaged", "big-refund-key")
        self.assertTrue(result["requires_human_approval"])

    def test_mark_refunded_bad_format(self):
        self.assertEqual(mark_refunded_impl("nope", 10.0), {"error": "invalid_order_id_format"})

    def test_mark_refunded_happy_path(self):
        result = mark_refunded_impl(ORDER_ID, 15.0)
        self.assertTrue(result["refunded"])
        self.assertEqual(result["refund_amount_sar"], 15.0)


class TestCustomerTools(ToolsBase):
    def test_get_customer_bad_format(self):
        self.assertEqual(get_customer_impl("nope"), {"error": "invalid_customer_id_format"})

    def test_get_customer_not_found(self):
        self.assertEqual(get_customer_impl("CUST-0000"), {"error": "customer_not_found"})

    def test_get_customer_happy_path(self):
        result = get_customer_impl(ORDER_CUSTOMER_ID)
        self.assertEqual(result["customer_id"], ORDER_CUSTOMER_ID)
        self.assertTrue(result["national_id_masked"].startswith("1X"))

    def test_get_customer_tickets_happy_path(self):
        result = get_customer_tickets_impl(TICKETED_CUSTOMER_ID)
        self.assertEqual(result["customer_id"], TICKETED_CUSTOMER_ID)
        self.assertGreaterEqual(len(result["tickets"]), 1)

    def test_add_case_note_ticket_not_found(self):
        result = add_case_note_impl(TICKETED_CUSTOMER_ID, "TKT-99999999", "note")
        self.assertEqual(result, {"error": "ticket_not_found"})

    def test_add_case_note_happy_path(self):
        ticket_id = get_customer_tickets_impl(TICKETED_CUSTOMER_ID)["tickets"][0]["ticket_id"]
        result = add_case_note_impl(TICKETED_CUSTOMER_ID, ticket_id, "resolved on first contact")
        self.assertIn("resolved on first contact", result["notes"])


class TestErrorsAreValuesNotRaises(ToolsBase):
    """Every tool called with a malformed id must return {"error": ...},
    never raise (SPEC §7 mistake #4)."""

    CASES = [
        (track_shipment_impl, ("bad",)),
        (get_order_impl, ("bad",)),
        (list_orders_impl, ("bad",)),
        (get_order_items_impl, ("bad",)),
        (logistics_track_shipment_impl, ("bad",)),
        (estimate_eta_impl, ("bad",)),
        (get_delivery_events_impl, ("bad",)),
        (get_driver_status_impl, ("bad",)),
        (find_delivery_exception_impl, ("bad",)),
        (reschedule_delivery_impl, ("bad", "2026-01-01T00:00:00+03:00")),
        (get_invoice_impl, ("bad",)),
        (get_payment_impl, ("bad",)),
        (issue_refund_impl, ("bad", 10.0, "x", "k")),
        (mark_refunded_impl, ("bad", 10.0)),
        (get_customer_impl, ("bad",)),
        (get_customer_tickets_impl, ("bad",)),
    ]

    def test_bad_input_never_raises(self):
        for fn, args in self.CASES:
            with self.subTest(fn=fn.__name__):
                result = fn(*args)
                self.assertIsInstance(result, dict)
                self.assertTrue(result.get("error"))


class TestAuthzAllow(unittest.TestCase):
    def test_customer_agent_may_read_own_customer_orders(self):
        self.assertTrue(agent_may_access(
            "customer_agent", "track_shipment", "CUST-4144", session_customer_id="CUST-4144"))

    def test_customer_agent_may_refund_own_customer(self):
        self.assertTrue(agent_may_access(
            "customer_agent", "issue_refund", "CUST-4144", session_customer_id="CUST-4144"))

    def test_ops_agent_may_read_any_customer(self):
        self.assertTrue(agent_may_access("ops_agent", "get_order", "CUST-8183"))

    def test_billing_admin_may_mark_refunded(self):
        self.assertTrue(agent_may_access("billing_admin_agent", "mark_refunded", "CUST-8183"))


class TestAuthzDeny(unittest.TestCase):
    def test_unknown_agent_denied(self):
        decision = explain("nobody", "track_shipment", "CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "unknown_agent")

    def test_unknown_tool_denied(self):
        decision = explain("customer_agent", "delete_everything", "CUST-4144", session_customer_id="CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "unknown_tool")

    def test_domain_not_granted_denied(self):
        decision = explain("partner_agent", "issue_refund", "CUST-4144", session_customer_id="CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "domain_not_granted")

    def test_ops_agent_cannot_touch_billing(self):
        self.assertFalse(agent_may_access("ops_agent", "issue_refund", "CUST-8183"))

    def test_explicitly_denied_tool(self):
        decision = explain("customer_agent", "mark_refunded", "CUST-4144", session_customer_id="CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "tool_explicitly_denied")

    def test_prohibited_action_always_denied(self):
        for tool_name in PROHIBITED_TOOLS:
            decision = explain("customer_agent", tool_name, "CUST-4144", session_customer_id="CUST-4144")
            self.assertFalse(decision.allowed)
            self.assertEqual(decision.reason, "prohibited_action")

    def test_missing_session_customer_id_fails_closed(self):
        decision = explain("customer_agent", "get_customer", "CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "missing_session_customer_id")


class TestAuthzCrossCustomerDeny(unittest.TestCase):
    def test_customer_agent_cannot_read_a_different_customer(self):
        decision = explain("customer_agent", "get_customer", "CUST-8183", session_customer_id="CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "cross_customer_denied")

    def test_partner_agent_cannot_read_a_different_customer(self):
        decision = explain("partner_agent", "track_shipment", "CUST-8183", session_customer_id="CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "cross_customer_denied")

    def test_customer_agent_cannot_refund_a_different_customer(self):
        decision = explain("customer_agent", "issue_refund", "CUST-8183", session_customer_id="CUST-4144")
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason, "cross_customer_denied")


class TestMcpServersGuardedTool(unittest.TestCase):
    """Smoke-tests `mcp_servers/*.py`'s `guarded_tool` end to end: missing
    context, denial, allow, and the billing server's own defence-in-depth
    500 SAR gate — on top of (not instead of) `security/authz.py`."""

    def setUp(self) -> None:
        store.reset()
        import mcp_servers.billing_server as billing_server
        import mcp_servers.customer_server as customer_server
        import mcp_servers.logistics_server as logistics_server
        import mcp_servers.orders_server as orders_server

        self.orders_server = orders_server
        self.logistics_server = logistics_server
        self.billing_server = billing_server
        self.customer_server = customer_server

    def tearDown(self) -> None:
        store.reset()

    def test_missing_authz_context_is_an_error_value(self):
        result = self.orders_server.get_order(order_id=ORDER_ID)
        self.assertEqual(result["error"], "missing_authz_context")

    def test_unauthorised_agent_rejected_at_server(self):
        result = self.orders_server.get_order(order_id=ORDER_ID, agent_id="rogue", customer_id=ORDER_CUSTOMER_ID)
        self.assertEqual(result, {"error": "not_authorised"})

    def test_authorised_call_succeeds(self):
        result = self.logistics_server.track_shipment(
            order_id=ORDER_ID, agent_id="customer_agent", customer_id=ORDER_CUSTOMER_ID,
            session_customer_id=ORDER_CUSTOMER_ID,
        )
        self.assertEqual(result["order_id"], ORDER_ID)

    def test_billing_server_blocks_over_limit_refund_without_approval(self):
        result = self.billing_server.issue_refund(
            order_id=HIGH_VALUE_ORDER_ID, amount_sar=970.36, reason="damaged",
            idempotency_key="server-test-key-1", agent_id="customer_agent",
            customer_id=HIGH_VALUE_CUSTOMER_ID, session_customer_id=HIGH_VALUE_CUSTOMER_ID,
        )
        self.assertEqual(result["error"], "human_approval_required")

    def test_billing_server_allows_over_limit_refund_when_approved(self):
        result = self.billing_server.issue_refund(
            order_id=HIGH_VALUE_ORDER_ID, amount_sar=970.36, reason="damaged",
            idempotency_key="server-test-key-2", agent_id="customer_agent",
            customer_id=HIGH_VALUE_CUSTOMER_ID, session_customer_id=HIGH_VALUE_CUSTOMER_ID,
            approved=True,
        )
        self.assertTrue(result["idempotent_replay"] is False)
        self.assertEqual(result["amount_sar"], 970.36)

    def test_customer_server_cross_customer_denied(self):
        result = self.customer_server.get_customer(
            customer_id="CUST-8183", agent_id="customer_agent", session_customer_id=ORDER_CUSTOMER_ID,
        )
        self.assertEqual(result, {"error": "not_authorised"})


AUTO_APPROVE_ORDER_ID = "TW-2026-10206"    # 35.0 SAR, sla_breached, not refunded
APPROVE_ORDER_ID = "TW-2026-10233"         # 348.8 SAR, sla_breached, not refunded
NEEDS_HUMAN_ORDER_ID = "TW-2026-39725"     # 748.68 SAR, sla_breached, not refunded
NOT_ELIGIBLE_ORDER_ID = "TW-2026-10002"    # 35.0 SAR, NOT sla_breached
RESCHEDULABLE_FLOW_ORDER_ID = "TW-2026-10030"
DELIVERED_FLOW_ORDER_ID = "TW-2026-10002"


class TestRefundFlowGates(unittest.TestCase):
    """Module 7 — mirrors tests/unit/test_refund_flow.py."""

    def test_amount_gate_bands(self):
        self.assertEqual(refund_amount_gate({"amount": 0.01}), "auto_approve")
        self.assertEqual(refund_amount_gate({"amount": AUTO_REFUND_LIMIT_SAR}), "auto_approve")
        self.assertEqual(refund_amount_gate({"amount": AUTO_REFUND_LIMIT_SAR + 0.01}), "approve")
        self.assertEqual(refund_amount_gate({"amount": REFUND_LIMIT_SAR}), "approve")
        self.assertEqual(refund_amount_gate({"amount": REFUND_LIMIT_SAR + 0.01}), "needs_human")
        self.assertEqual(refund_amount_gate({"amount": 5000.0}), "needs_human")

    def test_eligibility_gate(self):
        self.assertEqual(refund_eligibility_gate({"already_refunded": True, "sla_breached": True}), "reject")
        self.assertEqual(refund_eligibility_gate({"already_refunded": False, "sla_breached": False}), "reject")
        self.assertEqual(refund_eligibility_gate({"already_refunded": False, "sla_breached": True}), "decide")


class TestRefundFlowIntegration(ToolsBase):
    """Module 7 — load_order -> gate -> do_refund/request_human_approval
    against real seed data."""

    def test_auto_approve_band(self):
        state = {"order_id": AUTO_APPROVE_ORDER_ID, "customer_id": "CUST-7845", "ticket_id": "t1"}
        state.update(refund_load_order(state))
        self.assertEqual(refund_eligibility_gate(state), "decide")
        self.assertEqual(refund_amount_gate(state), "auto_approve")
        result = refund_do_refund(state)
        self.assertEqual(result["decision"], "auto_approve")
        self.assertAlmostEqual(result["refund_result"]["amount_sar"], 35.0)

    def test_needs_human_band_never_refunds(self):
        state = {"order_id": NEEDS_HUMAN_ORDER_ID, "customer_id": "CUST-8180", "ticket_id": "t3"}
        state.update(refund_load_order(state))
        self.assertEqual(refund_amount_gate(state), "needs_human")
        result = refund_request_human_approval(state)
        self.assertEqual(result["decision"], "needs_human")
        self.assertEqual(result["approval_request"]["threshold_sar"], REFUND_LIMIT_SAR)
        self.assertFalse(store.get_order(NEEDS_HUMAN_ORDER_ID)["refunded"])

    def test_not_sla_breached_rejects(self):
        state = {"order_id": NOT_ELIGIBLE_ORDER_ID}
        state.update(refund_load_order(state))
        self.assertEqual(refund_eligibility_gate(state), "reject")

    def test_double_refund_rejected_second_time(self):
        state = {"order_id": AUTO_APPROVE_ORDER_ID, "ticket_id": "t4"}
        state.update(refund_load_order(state))
        refund_do_refund(state)
        state2 = {"order_id": AUTO_APPROVE_ORDER_ID}
        state2.update(refund_load_order(state2))
        self.assertTrue(state2["already_refunded"])
        self.assertEqual(refund_eligibility_gate(state2), "reject")


class TestRescheduleFlowGates(unittest.TestCase):
    """Module 7 — mirrors tests/unit/test_reschedule_flow.py."""

    def test_reschedulable_gate(self):
        self.assertEqual(reschedulable_gate({"status": "in_transit"}), "proceed")
        self.assertEqual(reschedulable_gate({"status": "delivered"}), "not_reschedulable")
        self.assertEqual(reschedulable_gate({"status": "exception"}), "not_reschedulable")

    def test_max_reschedules_gate(self):
        self.assertEqual(max_reschedules_gate({"reschedule_count": 0}), "proceed")
        self.assertEqual(max_reschedules_gate({"reschedule_count": MAX_RESCHEDULES_PER_ORDER}), "needs_human")
        self.assertEqual(max_reschedules_gate({}), "proceed")

    def test_window_gate(self):
        self.assertEqual(window_gate({
            "requested_at_iso": "2026-03-04T08:00:00+03:00",
            "new_promised_at_iso": "2026-03-04T12:00:00+03:00",
        }), "proceed")
        self.assertEqual(window_gate({
            "requested_at_iso": "2026-03-04T08:00:00+03:00",
            "new_promised_at_iso": "2026-03-04T09:00:00+03:00",
        }), "invalid_window")
        self.assertEqual(window_gate({}), "invalid_window")

    def test_city_cutoff_gate(self):
        self.assertEqual(city_cutoff_gate({"new_promised_at_iso": "2026-03-06T13:00:00+03:00"}), "friday_unavailable")
        self.assertEqual(city_cutoff_gate({"new_promised_at_iso": "2026-03-05T13:00:00+03:00"}), "proceed")

    def test_courier_availability_gate(self):
        self.assertEqual(courier_availability_gate({"courier_available": False}), "courier_unavailable")
        self.assertEqual(courier_availability_gate({}), "proceed")


class TestRescheduleFlowIntegration(ToolsBase):
    def test_full_chain_happy_path(self):
        state = {"order_id": RESCHEDULABLE_FLOW_ORDER_ID}
        state.update(load_order_context(state))
        self.assertEqual(reschedulable_gate(state), "proceed")
        state["reschedule_count"] = 0
        self.assertEqual(max_reschedules_gate(state), "proceed")
        state["requested_at_iso"] = "2026-03-04T08:00:00+03:00"
        state["new_promised_at_iso"] = "2026-03-05T18:00:00+03:00"
        self.assertEqual(window_gate(state), "proceed")
        self.assertEqual(city_cutoff_gate(state), "proceed")
        self.assertEqual(courier_availability_gate(state), "proceed")
        result = do_reschedule(state)
        self.assertEqual(result["decision"], "approve")

    def test_delivered_order_not_reschedulable(self):
        state = {"order_id": DELIVERED_FLOW_ORDER_ID}
        state.update(load_order_context(state))
        self.assertEqual(reschedulable_gate(state), "not_reschedulable")

    def test_third_request_escalates(self):
        state = {"order_id": RESCHEDULABLE_FLOW_ORDER_ID, "customer_id": "CUST-6425",
                 "reschedule_count": MAX_RESCHEDULES_PER_ORDER}
        self.assertEqual(max_reschedules_gate(state), "needs_human")
        result = reschedule_request_human_approval(state)
        self.assertEqual(result["decision"], "needs_human")


class TestScopingContextIsolation(unittest.TestCase):
    """Module 5 — mirrors tests/unit/test_scoping.py."""

    FULL_STATE = {
        "customer_id": "CUST-4471", "locale": "ar", "order_id": "TW-2026-88120",
        "messages": [], "step_count": 3, "handoff_count": 1,
        "address": "12 King Fahd Road, Riyadh", "geo": {"lat": 24.7, "lng": 46.6},
        "national_id_masked": "1XXXXXXXXX",
    }

    def test_billing_input_carries_no_address_or_geo_field(self):
        payload = scoped_input(self.FULL_STATE, "billing")
        for key in ("address", "geo", "national_id_masked"):
            self.assertNotIn(key, payload)
        self.assertEqual(set(payload.keys()), SCOPE["billing"])

    def test_unknown_specialist_raises(self):
        with self.assertRaises(KeyError):
            scoped_input(self.FULL_STATE, "accounts")

    def test_forbidden_field_raises_rather_than_silently_passing(self):
        leaking_payload = {"customer_id": "CUST-4471", "address": "12 King Fahd Road"}
        with self.assertRaises(ValueError):
            assert_no_forbidden_leak(leaking_payload, "billing")

    def test_specialist_with_no_forbidden_list_never_raises(self):
        self.assertNotIn("orders", FORBIDDEN_FIELDS)
        assert_no_forbidden_leak({"anything": "goes"}, "orders")  # must not raise


class TestRoutingAndFastpath(unittest.TestCase):
    """Module 6/7 — mirrors tests/unit/test_routing.py."""

    def test_classify_intent_bilingual(self):
        self.assertEqual(classify_intent("Where is my order TW-2026-88120?")[0], "track")
        self.assertEqual(classify_intent("أين طلبي رقم TW-2026-88120؟")[0], "track")
        self.assertEqual(classify_intent("I want a refund for my order")[0], "refund")
        self.assertEqual(classify_intent("ممكن رجع فلوسي؟")[0], "refund")
        self.assertEqual(classify_intent("")[0], "out_of_scope")

    def test_classify_intent_fraud_check_without_my_knowledge_phrasing(self):
        # SPEC-flagged coverage hole: "someone placed this without my
        # knowledge" and its Arabic equivalent were previously falling
        # through to order_status because no keyword matched them at all.
        self.assertEqual(classify_intent(
            "Someone placed order TW-2026-90656 on my account without my knowledge.")[0], "fraud_check")
        self.assertEqual(classify_intent(
            "شخص ما قام بطلب TW-2026-90656 من حسابي دون علمي.")[0], "fraud_check")
        self.assertEqual(classify_intent("This charge wasn't me, I never ordered this.")[0], "fraud_check")

    def test_classify_intent_lost_parcel_natural_phrasing(self):
        # "my parcel for order X is lost" (word order differs from the
        # older "lost my parcel"/"parcel is lost" fixed phrases).
        self.assertEqual(classify_intent(
            "I think my parcel for order TW-2026-35220 is lost, it's been too long.")[0], "lost_parcel")
        self.assertEqual(classify_intent(
            "أعتقد أن طردي الخاص بالطلب TW-2026-35220 مفقود، لقد مضى وقت طويل.")[0], "lost_parcel")

    def test_classify_intent_address_change_natural_phrasing(self):
        self.assertEqual(classify_intent(
            "I need to change the delivery address for order TW-2026-28163.")[0], "address_change")
        self.assertEqual(classify_intent(
            "أحتاج تغيير عنوان التوصيل للطلب TW-2026-28163.")[0], "address_change")

    def test_classify_intents_multi_detects_every_sub_intent(self):
        matched = classify_intents_multi(
            "Can you track order TW-2026-86532 for me, please? "
            "My order TW-2026-86532 never arrived properly, I want a refund.")
        self.assertIn("track", matched)
        self.assertIn("refund", matched)
        self.assertEqual(classify_intents_multi(""), [])
        self.assertEqual(classify_intents_multi("   "), [])

    def test_intent_specialist_table_covers_all_intents(self):
        self.assertEqual(set(INTENT_SPECIALIST), set(TICKET_INTENTS))
        self.assertIsNone(specialist_for_intent("multi_domain"))
        self.assertIsNone(specialist_for_intent("fraud_check"))

    def test_fastpath_bypasses_high_confidence_single_domain(self):
        decision = fastpath_route("Can you track order TW-2026-77154 for me, please?")
        self.assertTrue(decision["bypassed_supervisor"])
        self.assertEqual(decision["route"], "logistics")

    def test_fastpath_never_bypasses_out_of_scope(self):
        decision = fastpath_route("asdkjhaskjdh random text with no signal")
        self.assertFalse(decision["bypassed_supervisor"])
        self.assertEqual(decision["route"], "supervisor")

    def test_fastpath_against_routing_eval_never_wrong_when_bypassed(self):
        if not ROUTING_EVAL_PATH.exists():
            self.skipTest("data/routing_eval.jsonl not present")
        import json as _json
        bypassed = correct = 0
        with ROUTING_EVAL_PATH.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                ticket = _json.loads(line)
                decision = fastpath_route(ticket["text"])
                if decision["bypassed_supervisor"]:
                    bypassed += 1
                    if decision["route"] == ticket["expected_specialist"]:
                        correct += 1
        self.assertGreater(bypassed, 0)
        self.assertEqual(correct, bypassed)


class _AlwaysWantsToActMessage:
    tool_calls = [{"name": "track_shipment", "args": {"order_id": "TW-2026-00000"}, "id": "call_1"}]


class _FinalAnswerMessage:
    tool_calls: list = []


class TestAdversarialTermination(unittest.TestCase):
    """Module 1 — Lab 1's adversarial termination test against the pure
    router, mirrors tests/unit/test_termination.py."""

    def test_never_satisfies_goal_still_halts_at_budget(self):
        halted_at = None
        for step_count in range(0, MAX_STEPS + 5):
            state = {"step_count": step_count, "messages": [_AlwaysWantsToActMessage()]}
            decision = core_route(state)
            if decision == "reason":
                self.assertLess(step_count, MAX_STEPS)
            else:
                halted_at = step_count
                break
        self.assertIsNotNone(halted_at)
        self.assertLessEqual(halted_at, MAX_STEPS)

    def test_halts_exactly_at_max_steps(self):
        state = {"step_count": MAX_STEPS, "messages": [_AlwaysWantsToActMessage()]}
        self.assertNotEqual(core_route(state), "reason")

    def test_route_with_tools_same_guarantee(self):
        state = {"step_count": MAX_STEPS, "messages": [_AlwaysWantsToActMessage()]}
        self.assertNotEqual(core_route_with_tools(state), "tools")

    def test_final_answer_ends_immediately(self):
        state = {"step_count": 1, "messages": [_FinalAnswerMessage()]}
        self.assertNotEqual(core_route(state), "reason")


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print(f"\n{result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun} checks passed")
    raise SystemExit(0 if result.wasSuccessful() else 1)
