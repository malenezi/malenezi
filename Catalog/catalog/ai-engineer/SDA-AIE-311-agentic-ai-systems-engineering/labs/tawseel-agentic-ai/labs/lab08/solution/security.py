"""Lab 8 solution — thin re-export, not a fork.

The real guard/red-team stack lives in `src/rafeeq/security/*` (Layer A
throughout — no langgraph anywhere in this lab); `solution/verify.py`
drives it directly. This module exists only so the lab's own code can be
imported as one name, matching every other lab's `solution/` pattern.
"""
from __future__ import annotations

from rafeeq.security.action_risk import Decision, classify
from rafeeq.security.authz import PROHIBITED_TOOLS, agent_may_access, explain
from rafeeq.security.input_guard import PII_PATTERNS, screen_input
from rafeeq.security.output_guard import guard_response, guard_tool_call
from rafeeq.security.red_team import (
    Finding,
    StubTarget,
    demo_layered_defence,
    load_corpus,
    retest_finding,
    run_suite,
    write_report,
)

__all__ = [
    "Decision", "classify",
    "PROHIBITED_TOOLS", "agent_may_access", "explain",
    "PII_PATTERNS", "screen_input",
    "guard_response", "guard_tool_call",
    "Finding", "StubTarget", "demo_layered_defence", "load_corpus",
    "retest_finding", "run_suite", "write_report",
]
