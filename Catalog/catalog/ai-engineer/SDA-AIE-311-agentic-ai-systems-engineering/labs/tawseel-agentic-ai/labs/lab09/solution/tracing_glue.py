"""Lab 9 solution — lab glue: wires the existing deterministic routing/
tool layer through `rafeeq.observability.tracing` spans, and the two
cost levers (caching + model routing), for a batch of real
`data/tickets_eval.jsonl` tickets.

Not a fork of anything in `src/rafeeq/**` — this wiring is exactly
Lab 9's job (SPEC's Module 9: "Instrument Rafeeq with tracing"); no
module upstream already does it, the same way Lab 7's flow gates did not
pre-exist before that lab wired them into `refund_flow.py`.
"""
from __future__ import annotations

from typing import Any

from rafeeq.core.config import get_settings
from rafeeq.core.llm import estimate_tokens
from rafeeq.observability.optimise import CacheStats, cached_policy, route_model_name
from rafeeq.observability.tracing import Run, start_run, start_span
from rafeeq.orchestration.routing import classify_intent, specialist_for_intent
from rafeeq.tools.billing import get_invoice_impl
from rafeeq.tools.logistics import track_shipment_impl

_TOOL_FOR_SPECIALIST = {
    "logistics": ("track_shipment", track_shipment_impl),
    "billing": ("get_invoice", get_invoice_impl),
}

_ASSUMED_REPLY_TOKENS = 120

# A real Rafeeq run retrieves policy for the TOPIC a ticket is about, not
# the customer's exact wording — many different tickets share the same
# topic (e.g. every `refund` ticket asks about the same refund policy),
# which is exactly what makes `cached_policy`'s (question, locale,
# version) key hit repeatedly across a batch. Keying on raw ticket text
# instead would make every question unique and the cache pointless —
# see the lab README's troubleshooting row on this exact mistake.
_POLICY_TOPIC_FOR_INTENT: dict[str, str] = {
    "order_status": "order status policy", "track": "shipment tracking policy",
    "reschedule": "delivery reschedule policy", "refund": "refund policy",
    "invoice": "invoice and billing policy", "complaint": "complaint handling policy",
    "address_change": "address change policy", "lost_parcel": "lost parcel policy",
    "damaged": "damaged item policy", "fraud_check": "fraud check policy",
    "out_of_scope": "general help policy", "multi_domain": "multi domain policy",
}


def run_traced_ticket(
    ticket: dict[str, Any],
    *,
    use_cache: bool = False,
    route_by_confidence: bool = False,
    cache_stats: CacheStats | None = None,
) -> Run:
    """Instrument one ticket end to end. `use_cache=False,
    route_by_confidence=False` reproduces the PRE-optimisation
    configuration (always frontier, no cache — Task 1/2's baseline);
    both `True` reproduces the POST-optimisation configuration (Task 3)."""
    settings = get_settings()
    intent, confidence = classify_intent(ticket["text"])

    with start_run(
        f"ticket:{ticket['ticket_id']}", intent=intent,
        ticket_id=ticket["ticket_id"], locale=ticket["locale"],
    ) as run:
        with start_span(
            "classify_intent", run_type="llm", model=settings.cheap_model_name,
            tokens_in=estimate_tokens(ticket["text"]), tokens_out=estimate_tokens(intent or ""),
        ):
            pass  # classification IS the span; classify_intent already ran above

        specialist = specialist_for_intent(intent)
        tool_entry = _TOOL_FOR_SPECIALIST.get(specialist or "")
        if tool_entry and ticket.get("order_id"):
            tool_name, tool_fn = tool_entry
            with start_span(
                f"specialist:{specialist}", run_type="tool", tool_name=tool_name,
                args={"order_id": ticket["order_id"]},
            ):
                tool_fn(ticket["order_id"])  # a tool span costs 0 USD — only `model=` spans bill

        # Policy retrieval — cached (scoped, versioned key) post-optimisation,
        # a fresh uncached lookup pre-optimisation (Task 3's first lever).
        topic = _POLICY_TOPIC_FOR_INTENT.get(intent, "general help policy")
        with start_span("policy_retrieval", run_type="tool"):
            if use_cache:
                cached_policy(topic, ticket["locale"], stats=cache_stats)
            else:
                from rafeeq.memory.knowledge_base import policy_context

                policy_context(topic, ticket["locale"])

        # Reply composition — routed to the cheap model for the confident,
        # simple majority post-optimisation (Task 3's second lever); always
        # frontier pre-optimisation (Task 1/2's baseline, matching the case
        # study's "68% of spend in order-status on frontier model").
        reply_model = (
            route_model_name(intent, confidence) if route_by_confidence else settings.frontier_model_name
        )
        with start_span(
            "compose_reply", run_type="llm", model=reply_model,
            tokens_in=estimate_tokens(ticket["text"]), tokens_out=_ASSUMED_REPLY_TOKENS,
        ):
            pass

    return run


def run_batch(
    tickets: list[dict[str, Any]], *, use_cache: bool = False, route_by_confidence: bool = False,
) -> tuple[list[Run], CacheStats]:
    """Run every ticket in `tickets` through `run_traced_ticket` with ONE
    shared `CacheStats` for the batch (so hit_rate reflects the whole run,
    not a single ticket) and return `(runs, cache_stats)`."""
    stats = CacheStats()
    runs = [
        run_traced_ticket(t, use_cache=use_cache, route_by_confidence=route_by_confidence, cache_stats=stats)
        for t in tickets
    ]
    return runs, stats
