"""Module 5 — pytest-style tests for `src/rafeeq/agents/scoping.py`.

Context isolation is a STRUCTURAL PDPL control (Module 5's central
lesson), not a prompt instruction — these tests are the "billing input
carries no address/geo field" proof the module's benchmark table asks
for, plus the "a forbidden field raises rather than silently passing"
behaviour the build task calls out explicitly. See
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

from rafeeq.agents.scoping import FORBIDDEN_FIELDS, SCOPE, assert_no_forbidden_leak, scoped_input


FULL_STATE = {
    "customer_id": "CUST-4471",
    "locale": "ar",
    "order_id": "TW-2026-88120",
    "messages": [("human", "أين طلبي؟")],
    "step_count": 3,
    "handoff_count": 1,
    "address": "12 King Fahd Road, Riyadh",
    "shipment_address": "12 King Fahd Road, Riyadh",
    "geo": {"lat": 24.7, "lng": 46.6},
    "national_id_masked": "1XXXXXXXXX",
}


class TestScopedInputProjection:
    def test_billing_input_carries_no_address_or_geo_field(self):
        payload = scoped_input(FULL_STATE, "billing")
        for forbidden_key in ("address", "shipment_address", "delivery_address", "geo",
                               "lat", "lng", "delivery_note", "delivery_note_ar",
                               "national_id_masked"):
            assert forbidden_key not in payload

    def test_billing_input_only_carries_allowed_fields(self):
        payload = scoped_input(FULL_STATE, "billing")
        assert set(payload.keys()) == SCOPE["billing"]
        assert payload["customer_id"] == "CUST-4471"
        assert payload["order_id"] == "TW-2026-88120"

    @pytest.mark.parametrize("specialist", ["orders", "logistics", "billing"])
    def test_extraneous_fields_never_leak_for_any_specialist(self, specialist):
        payload = scoped_input(FULL_STATE, specialist)
        assert "step_count" not in payload
        assert "handoff_count" not in payload
        assert "address" not in payload


class TestScopedInputFailsLoud:
    def test_unknown_specialist_raises_key_error(self):
        with pytest.raises(KeyError):
            scoped_input(FULL_STATE, "accounts")   # no SCOPE entry for a 4th specialist

    def test_forbidden_field_raises_rather_than_silently_passing(self):
        """The task's explicit requirement: construct a payload that
        WOULD leak a forbidden field and confirm the guard raises, not
        silently strips or ignores it."""
        leaking_payload = {"customer_id": "CUST-4471", "address": "12 King Fahd Road"}
        with pytest.raises(ValueError, match="forbidden"):
            assert_no_forbidden_leak(leaking_payload, "billing")

    def test_forbidden_field_absent_does_not_raise(self):
        clean_payload = {"customer_id": "CUST-4471", "order_id": "TW-2026-88120"}
        assert_no_forbidden_leak(clean_payload, "billing") is None

    def test_specialist_with_no_forbidden_list_never_raises(self):
        # orders/logistics have no FORBIDDEN_FIELDS entry at all -> the
        # empty-set default must never raise regardless of payload.
        assert "orders" not in FORBIDDEN_FIELDS
        assert_no_forbidden_leak({"anything": "goes"}, "orders") is None
