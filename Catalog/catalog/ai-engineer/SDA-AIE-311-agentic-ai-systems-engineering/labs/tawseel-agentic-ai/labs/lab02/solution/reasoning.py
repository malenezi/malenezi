"""Lab 2 solution — thin re-export, not a fork.

The real implementations live in `src/rafeeq/reasoning/{react,plan_execute,
reflection}.py`. Read those for the actual logic; this module just
re-exposes them under the lab's own import path, plus
`rafeeq.reasoning.compare.compare_patterns` — the same comparison the
Module 2 package's Code Examples section builds toward — so
`labs/lab02/solution/` is a complete, runnable answer key on its own.
"""
from __future__ import annotations

from rafeeq.reasoning.react import (
    ReactTrace,
    ReactTraceStep,
    count_redundant_tool_calls,
    react_loop_explicit,
)
from rafeeq.reasoning.plan_execute import Plan, make_plan, plan_approval_gate, run_plan_execute
from rafeeq.reasoning.reflection import Critique, reflect, reflect_and_revise
from rafeeq.reasoning.compare import ComparisonTable, PatternResult, compare_patterns, load_tickets

__all__ = [
    "ReactTrace", "ReactTraceStep", "count_redundant_tool_calls", "react_loop_explicit",
    "Plan", "make_plan", "plan_approval_gate", "run_plan_execute",
    "Critique", "reflect", "reflect_and_revise",
    "ComparisonTable", "PatternResult", "compare_patterns", "load_tickets",
]
