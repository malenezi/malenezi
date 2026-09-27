"""Lab 9 solution — thin re-export, not a fork.

The real tracing/cost/optimise/retry stack lives in
`src/rafeeq/observability/*` (Layer A throughout — no langgraph anywhere
in this lab). `tracing_glue.py` is this lab's own glue (not a repo
module): it wires the existing deterministic routing/tool layer through
tracing spans, which is exactly Lab 9's job — nothing upstream already
does this wiring for you.
"""
from __future__ import annotations

from rafeeq.observability.cost import CostBreakdown, blended_cost_per_contact, cost_of_run, cost_report
from rafeeq.observability.optimise import CacheStats, cached_policy, route_model_name
from rafeeq.observability.retry import Attempt, RetryLedger, call_with_retry
from rafeeq.observability.tracing import Run, Span, render_tree, start_run, start_span

__all__ = [
    "CostBreakdown", "blended_cost_per_contact", "cost_of_run", "cost_report",
    "CacheStats", "cached_policy", "route_model_name",
    "Attempt", "RetryLedger", "call_with_retry",
    "Run", "Span", "render_tree", "start_run", "start_span",
]
