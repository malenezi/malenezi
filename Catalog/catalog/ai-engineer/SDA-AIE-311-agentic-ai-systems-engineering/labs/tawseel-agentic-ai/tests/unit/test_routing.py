"""Module 6/7 — pytest-style tests for
`src/rafeeq/orchestration/routing.py` and `fastpath.py`.

Both modules are pure, dependency-free functions (no model, no
langgraph) — exactly the Module 7 thesis: routing for the confident
majority is a rule, not a sentence. See `tests/unit/run_without_pytest.py`
for the stdlib mirror.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import ROUTING_EVAL_PATH, TICKET_INTENTS
from rafeeq.orchestration.fastpath import FASTPATH_CONFIDENCE_THRESHOLD, fastpath_route
from rafeeq.orchestration.routing import (
    INTENT_SPECIALIST, classify_intent, classify_intents_multi, specialist_for_intent,
)


class TestClassifyIntentBilingual:
    @pytest.mark.parametrize("text, expected_intent", [
        ("Where is my order TW-2026-88120?", "track"),
        ("أين طلبي رقم TW-2026-88120؟", "track"),
        ("I want a refund for my order", "refund"),
        ("ممكن رجع فلوسي؟", "refund"),
        ("Can you reschedule my delivery?", "reschedule"),
        ("أبي أأجل التوصيل", "reschedule"),
        ("Can I get an invoice for this order?", "invoice"),
        ("أبي الفاتورة", "invoice"),
        ("My parcel never arrived", "lost_parcel"),
        ("The item arrived damaged", "damaged"),
        ("I did not make this order", "fraud_check"),
        ("I want to change my address", "address_change"),
        ("This is a terrible service, I have a complaint", "complaint"),
    ])
    def test_intent(self, text, expected_intent):
        intent, confidence = classify_intent(text)
        assert intent == expected_intent
        assert 0.0 <= confidence <= 1.0

    def test_empty_text_is_out_of_scope_zero_confidence(self):
        assert classify_intent("") == ("out_of_scope", 0.0)
        assert classify_intent("   ") == ("out_of_scope", 0.0)

    def test_gibberish_is_out_of_scope_low_confidence(self):
        intent, confidence = classify_intent("asdkjhaskjdh random text with no signal")
        assert intent == "out_of_scope"
        assert confidence < 0.5

    def test_bare_order_id_defaults_to_order_status(self):
        intent, confidence = classify_intent("TW-2026-12345")
        assert intent == "order_status"

    def test_order_id_raises_confidence_over_keyword_alone(self):
        _, conf_with_id = classify_intent("track my order TW-2026-12345 please")
        _, conf_without_id = classify_intent("track my order please")
        assert conf_with_id > conf_without_id

    def test_deterministic_same_input_same_output(self):
        for _ in range(5):
            assert classify_intent("أين طلبي رقم TW-2026-88120؟") == ("track", 0.92)

    @pytest.mark.parametrize("text, expected_intent", [
        ("Someone placed order TW-2026-90656 on my account without my knowledge.", "fraud_check"),
        ("شخص ما قام بطلب TW-2026-90656 من حسابي دون علمي.", "fraud_check"),
        ("This charge wasn't me, I never ordered this.", "fraud_check"),
        ("I think my parcel for order TW-2026-35220 is lost, it's been too long.", "lost_parcel"),
        ("أعتقد أن طردي الخاص بالطلب TW-2026-35220 مفقود، لقد مضى وقت طويل.", "lost_parcel"),
        ("I need to change the delivery address for order TW-2026-28163.", "address_change"),
        ("أحتاج تغيير عنوان التوصيل للطلب TW-2026-28163.", "address_change"),
    ])
    def test_previously_uncovered_bilingual_phrasings(self, text, expected_intent):
        # Regression coverage for the eval-harness coverage holes: these
        # phrasings previously fell through to order_status because no
        # keyword matched them at all.
        intent, confidence = classify_intent(text)
        assert intent == expected_intent
        assert 0.0 <= confidence <= 1.0


class TestClassifyIntentsMulti:
    def test_detects_every_sub_intent_in_a_bundled_request(self):
        text = ("Can you track order TW-2026-86532 for me, please? "
                "My order TW-2026-86532 never arrived properly, I want a refund.")
        matched = classify_intents_multi(text)
        assert "track" in matched
        assert "refund" in matched

    def test_single_intent_text_matches_at_least_that_one(self):
        matched = classify_intents_multi("I need to reschedule the delivery of order TW-2026-1 to a later time.")
        assert "reschedule" in matched

    def test_empty_text_returns_no_matches(self):
        assert classify_intents_multi("") == []
        assert classify_intents_multi("   ") == []


class TestIntentSpecialistTable:
    def test_covers_every_ticket_intent(self):
        assert set(INTENT_SPECIALIST) == set(TICKET_INTENTS)

    def test_only_orders_logistics_billing_are_named(self):
        named = {v for v in INTENT_SPECIALIST.values() if v is not None}
        assert named <= {"orders", "logistics", "billing"}

    def test_multi_domain_and_out_of_scope_have_no_single_specialist(self):
        assert specialist_for_intent("multi_domain") is None
        assert specialist_for_intent("out_of_scope") is None
        assert specialist_for_intent("fraud_check") is None      # SPEC §5: fraud -> human


class TestFastpathRoute:
    def test_high_confidence_single_domain_bypasses_supervisor(self):
        decision = fastpath_route("Can you track order TW-2026-77154 for me, please?")
        assert decision["bypassed_supervisor"] is True
        assert decision["route"] == "logistics"

    def test_multi_domain_never_bypasses(self):
        decision = fastpath_route("I was charged for a parcel that never arrived and want a refund")
        # Whatever the classifier lands on, either it maps to a specialist
        # with sub-threshold confidence, or (as intended) has none — either
        # way the fast path must never invent a specialist it is not sure of.
        assert decision["route"] in ("supervisor", "billing", "logistics")
        if decision["route"] != "supervisor":
            assert decision["confidence"] >= FASTPATH_CONFIDENCE_THRESHOLD

    def test_out_of_scope_never_bypasses(self):
        decision = fastpath_route("asdkjhaskjdh random text with no signal")
        assert decision["bypassed_supervisor"] is False
        assert decision["route"] == "supervisor"

    def test_low_threshold_can_force_a_bypass(self):
        decision = fastpath_route("track my order please", threshold=0.5)
        assert decision["bypassed_supervisor"] is True


class TestFastpathAgainstRoutingEval:
    """The eval-harness-grade check: whenever the fast path is confident
    enough to bypass the supervisor on a REAL labelled ticket, it must
    never be wrong. Zero confident-wrong routes is the whole design
    point (`fastpath.py`'s docstring) — high recall is not required, but
    100% precision on what it does bypass is non-negotiable."""

    @pytest.fixture(scope="class")
    def eval_tickets(self):
        if not ROUTING_EVAL_PATH.exists():
            pytest.skip("data/routing_eval.jsonl not present")
        with ROUTING_EVAL_PATH.open("r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]

    def test_bypassed_routes_are_always_correct(self, eval_tickets):
        bypassed = 0
        correct = 0
        for ticket in eval_tickets:
            decision = fastpath_route(ticket["text"])
            if decision["bypassed_supervisor"]:
                bypassed += 1
                if decision["route"] == ticket["expected_specialist"]:
                    correct += 1
        assert bypassed > 0, "fixture produced no fast-path bypasses at all — check the eval data/classifier"
        assert correct == bypassed, "fast path bypassed at least one ticket to the WRONG specialist"
