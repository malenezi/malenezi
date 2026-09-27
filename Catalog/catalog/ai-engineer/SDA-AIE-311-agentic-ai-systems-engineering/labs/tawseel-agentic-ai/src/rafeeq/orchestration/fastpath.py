"""Module 6/7/9 — deterministic fast-path routing.

The capstone extension Module 6's instructor notes flag ("add a
deterministic fast-path router for high-confidence intents and measure
the cost saving") and Module 9's cost lever, pulled forward: for the
confident majority of single-domain tickets, `fastpath_route` decides the
first hop with NO model call at all — a pure function of
`routing.classify_intent`'s output. Module 7's thesis lives here in its
most literal form: "anything that can be decided by a rule should be a
branch, not a sentence," and a routing decision that never needed
judgement should never cost a token.

Pure, dependency-free, unit-testable without a model, a graph, or a
network call. `orchestration.supervisor`'s LLM router remains the
fallback for anything this function declines to answer.
"""
from __future__ import annotations

from typing import Literal, TypedDict

from rafeeq.orchestration.routing import classify_intent, specialist_for_intent

FASTPATH_CONFIDENCE_THRESHOLD = 0.85


class FastpathDecision(TypedDict):
    route: Literal["orders", "logistics", "billing", "supervisor"]
    intent: str
    confidence: float
    bypassed_supervisor: bool
    reason: str


def fastpath_route(text: str, *, threshold: float = FASTPATH_CONFIDENCE_THRESHOLD) -> FastpathDecision:
    """Decide, without any model call, whether `text` can be routed
    directly to a specialist. Returns `route="supervisor"` (never guesses
    a specialist it is not confident about) whenever:

      - the classified intent has no single owning specialist
        (`multi_domain`, `out_of_scope`, `complaint`, `fraud_check`,
        `address_change` — SPEC's routing table, `routing.py`), or
      - confidence is below `threshold`.

    A wrong fast-path route is strictly worse than a slightly slower
    supervisor round-trip (a misroute wastes a specialist call AND delays
    resolution — Module 6 §2), so this function is deliberately
    conservative: high recall is not the goal, zero confident-wrong
    routes is.
    """
    intent, confidence = classify_intent(text)
    specialist = specialist_for_intent(intent)

    if specialist is None:
        return FastpathDecision(
            route="supervisor", intent=intent, confidence=confidence,
            bypassed_supervisor=False,
            reason=f"intent {intent!r} has no single owning specialist",
        )
    if confidence < threshold:
        return FastpathDecision(
            route="supervisor", intent=intent, confidence=confidence,
            bypassed_supervisor=False,
            reason=f"confidence {confidence:.2f} below threshold {threshold:.2f}",
        )
    return FastpathDecision(
        route=specialist, intent=intent, confidence=confidence,
        bypassed_supervisor=True,
        reason=f"high-confidence single-domain intent {intent!r} -> {specialist}",
    )
