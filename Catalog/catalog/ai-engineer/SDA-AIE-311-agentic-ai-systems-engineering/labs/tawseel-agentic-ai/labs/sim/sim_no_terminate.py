#!/usr/bin/env python3
"""sim_no_terminate — Module 1, `labs/lab01`.

Symptom:    Rafeeq never stops replying to an order-status ticket. In a
            real LangGraph build this is `GraphRecursionError` after 25
            steps; offline, it is a loop that never reaches `END`.
Root cause: `route()` checks only "does the last message carry a tool
            call" (the model's own "am I done" signal) and NEVER checks
            a step budget. A model that keeps proposing the same tool
            call (because nothing ever executes it and reports back) has
            no other reason to stop — the SAME anti-pattern as
            `labs/lab01/start/broken_agent.py`'s `# SMELL`.
Fix:        `rafeeq.core.graph.route()` checks BOTH conditions — the
            model's signal AND `state["step_count"] >= MAX_STEPS` — so
            the loop is bounded BY CONSTRUCTION, never by hope.

Run: `PYTHONPATH=src python3 labs/sim/sim_no_terminate.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.graph import reason, route
from rafeeq.core.state import new_state

# A safety cap for THIS DEMO SCRIPT only — not part of the anti-pattern,
# not part of the fix. Without it, `route_no_budget` below truly never
# returns, which would hang the grader; this cap exists only so the sim
# can print "it would have kept going" and exit cleanly.
DEMO_SAFETY_CAP = 40


def route_no_budget(state: dict) -> str:
    """THE ANTI-PATTERN: identical to `rafeeq.core.graph.route`, minus
    the step-budget branch. Reproduced here, not imported, because the
    real module correctly does not expose a broken version of itself."""
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "reason"
    return "__end__"


def drive(route_fn, cap: int) -> int:
    """Hand-drive `reason` -> `route_fn` -> ... exactly like a compiled
    LangGraph would, without needing `langgraph` installed (Layer A)."""
    state = new_state(
        customer_id="CUST-0001", locale="en",
        messages=[("human", "Where is my order TW-2026-10002?")],
    )
    for _ in range(cap):
        update = reason(state)
        state["messages"] = list(state["messages"]) + list(update["messages"])
        state["step_count"] = update["step_count"]
        decision = route_fn(state)
        if decision == "__end__":
            return state["step_count"]
    return state["step_count"]  # hit the cap without ever choosing __end__


def main() -> int:
    print(f"MAX_STEPS = {MAX_STEPS}\n")

    print("-- broken: route_no_budget (no step-budget branch) --")
    broken_steps = drive(route_no_budget, DEMO_SAFETY_CAP)
    broken_would_loop_forever = broken_steps >= DEMO_SAFETY_CAP
    print(f"stopped after {broken_steps} steps only because this demo capped it at "
          f"{DEMO_SAFETY_CAP} — a real run would never call __end__ and would hang "
          f"(or hit GraphRecursionError in a real LangGraph build).\n")

    print("-- fixed: the real rafeeq.core.graph.route() --")
    fixed_steps = drive(route, DEMO_SAFETY_CAP)
    fixed_terminated_on_budget = fixed_steps == MAX_STEPS
    print(f"terminated after exactly {fixed_steps} steps (== MAX_STEPS), by construction.\n")

    ok = broken_would_loop_forever and fixed_terminated_on_budget
    print("FAILURE DEMONSTRATED" if ok else "DEMO DID NOT REPRODUCE THE BUG (unexpected)")
    print(f"  broken route ran to the demo's safety cap ({DEMO_SAFETY_CAP}) without ever "
          f"terminating: {broken_would_loop_forever}")
    print(f"  fixed route terminated at MAX_STEPS ({MAX_STEPS}): {fixed_terminated_on_budget}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
