"""Module 6/7 — deterministic intent classification for routing.

`classify_intent(text) -> (intent, confidence)` is a bilingual
keyword+regex classifier over `rafeeq.core.config.TICKET_INTENTS`. Zero
model calls, zero third-party dependencies — pure stdlib `re` — so it is
importable and unit-testable without langgraph, and it is FREE (Module
7's cost argument: a decision a rule can make should never be re-billed
to a model on every request).

Used by `orchestration.fastpath` (bypass the supervisor for the confident
majority) and by the eval harness (`routing_eval.jsonl` labels the
correct first-hop specialist; this module is what a deterministic router
is graded against). Deliberately simpler than `core.llm`'s
`StubChatModel._classify_intent` — that one exists to make a FAKE model
plausible; this one exists to BE the real, production routing signal for
the confident majority of tickets, so its false-positive behaviour (never
claim high confidence on a genuinely ambiguous ticket) matters more than
its recall.
"""
from __future__ import annotations

import re

from rafeeq.core.config import ORDER_ID_RE, TICKET_INTENTS

_ORDER_ID_RE = re.compile(ORDER_ID_RE)

# intent -> (english keywords, arabic keywords). Longer/more specific
# phrases are listed first within each language so a specific match (e.g.
# "reschedule") is not shadowed by a broader one checked later.
_INTENT_KEYWORDS: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "refund": (
        ("refund", "money back", "reimburse", "charged twice", "over-charged", "overcharged"),
        ("استرداد", "استرجاع", "ارجاع فلوس", "رجع فلوسي", "استرد المبلغ", "استرجاع المبلغ", "خصم مكرر"),
    ),
    "reschedule": (
        ("reschedule", "change delivery time", "delay delivery", "postpone delivery", "different day"),
        ("تأجيل", "غير موعد التوصيل", "تغيير موعد التوصيل", "أجل التوصيل", "يوم ثاني"),
    ),
    "invoice": (
        ("invoice", "receipt", "bill me", "billing statement"),
        ("فاتورة", "ايصال", "إيصال"),
    ),
    "lost_parcel": (
        ("lost my parcel", "parcel is lost", "package is lost", "never arrived", "missing package",
         "parcel", "my package", "is lost"),
        ("الطرد ضاع", "الطرد مفقود", "لم يصل", "ماوصل الطرد", "طردي", "مفقود"),
    ),
    "damaged": (
        ("arrived damaged", "damaged item", "broken item", "defective"),
        ("وصل تالف", "منتج تالف", "مكسور", "معطوب"),
    ),
    "address_change": (
        ("change my address", "update the address", "wrong address", "different address",
         "change the delivery address", "change my delivery address", "delivery address"),
        ("تغيير العنوان", "تحديث العنوان", "العنوان غلط", "عنوان التوصيل"),
    ),
    "fraud_check": (
        ("did not make this order", "i did not order", "fraudulent charge", "unauthorised charge",
         "unauthorized charge", "without my knowledge", "without my consent", "wasn't me",
         "didn't place this order", "i never ordered"),
        ("ما طلبت", "عملية احتيال", "شحنة احتيال", "لم أطلب", "دون علمي", "بدون علمي", "دون موافقتي"),
    ),
    "complaint": (
        ("complaint", "unacceptable", "very unhappy", "terrible service", "disappointed"),
        ("شكوى", "خدمة سيئة", "مستاء", "غير مقبول"),
    ),
    "track": (
        ("track", "where is my order", "where's my order", "status of my order"),
        ("تتبع", "وين طلبي", "أين طلبي", "فين طلبي"),
    ),
    "order_status": (
        ("order status", "what's the status", "status of my"),
        ("حالة الطلب", "حالة طلبي"),
    ),
}

# Only these intents route to a known, single specialist (SPEC's Module-6
# routing table restricted to orders/logistics/billing) — the others
# genuinely need the supervisor's broader judgement or human escalation,
# so `fastpath.py` never bypasses on them regardless of confidence.
INTENT_SPECIALIST: dict[str, str | None] = {
    "order_status": "logistics",
    "track": "logistics",
    "reschedule": "logistics",
    "lost_parcel": "logistics",
    "damaged": "logistics",
    "refund": "billing",
    "invoice": "billing",
    "address_change": None,     # no orders/logistics/billing specialist owns this
    "complaint": None,          # needs judgement, not a rule
    "fraud_check": None,        # SPEC §5: fraud_flag -> human, never autonomous
    "multi_domain": None,       # by definition spans specialists
    "out_of_scope": None,
}

assert set(INTENT_SPECIALIST) == set(TICKET_INTENTS), (
    "INTENT_SPECIALIST must cover exactly TICKET_INTENTS (core.config) — "
    "a new intent added to the domain model needs a routing decision here too."
)


def classify_intent(text: str) -> tuple[str, float]:
    """Classify `text` into one of `TICKET_INTENTS` with a confidence in
    `[0.0, 1.0]`. Deterministic: the same input always returns the same
    (intent, confidence) pair.

    Confidence model (deliberately simple and explainable, not tuned to
    an eval set — a real deployment would calibrate this against
    `routing_eval.jsonl`, which is exactly what the Lab asks for):
      - a keyword match plus a well-formed order id present -> 0.92
      - a keyword match alone -> 0.78
      - no keyword match at all -> ("out_of_scope", 0.3)
    """
    if not text or not text.strip():
        return "out_of_scope", 0.0

    has_order_id = bool(_ORDER_ID_RE.search(text))
    lowered = text.lower()

    for intent, (en_kw, ar_kw) in _INTENT_KEYWORDS.items():
        matched = any(kw in lowered for kw in en_kw) or any(kw in text for kw in ar_kw)
        if matched:
            return intent, (0.92 if has_order_id else 0.78)

    if has_order_id:
        # An order id with no other signal: most likely a status/track
        # question (the least destructive, most common bare-id intent).
        return "order_status", 0.6

    return "out_of_scope", 0.3


def specialist_for_intent(intent: str) -> str | None:
    """The single specialist that owns `intent`, or `None` if no one
    specialist (orders/logistics/billing) can resolve it alone — those
    tickets need the supervisor's routing judgement or escalation."""
    return INTENT_SPECIALIST.get(intent)


def classify_intents_multi(text: str) -> list[str]:
    """Return EVERY `TICKET_INTENTS` entry whose keyword set matches
    `text`, in `_INTENT_KEYWORDS`'s priority order — unlike
    `classify_intent`, which stops at the first match to pick ONE
    first-hop specialist, this is for a caller that needs to notice a
    ticket is asking for more than one thing at once (a `multi_domain`
    ticket bundles two requests into one message, e.g. "track this AND
    refund me") and must chain the tools for every request actually
    present, not just the highest-priority one. Same deterministic,
    dependency-free keyword table — no separate model of intent, so the
    two functions can never disagree about what a phrase means."""
    if not text or not text.strip():
        return []
    lowered = text.lower()
    return [
        intent for intent, (en_kw, ar_kw) in _INTENT_KEYWORDS.items()
        if any(kw in lowered for kw in en_kw) or any(kw in text for kw in ar_kw)
    ]
