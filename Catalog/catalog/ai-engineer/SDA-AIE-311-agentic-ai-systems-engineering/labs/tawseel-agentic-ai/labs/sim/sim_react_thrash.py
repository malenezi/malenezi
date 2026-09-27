#!/usr/bin/env python3
"""sim_react_thrash — Module 2, `labs/lab02`.

Symptom:    The ReAct agent calls `track_shipment` five times with the
            SAME order id in one run.
Root cause: The tool's observation is never written back into the
            message history the model sees next — so the model, asked
            the identical question again, deterministically proposes the
            identical tool call again. Nothing ever tells it "you already
            know the answer".
Fix:        `rafeeq.reasoning.react.react_loop_explicit` appends BOTH the
            action and its observation to `messages` before looping again
            — the fix is one write-back, not a smarter model.

Run: `PYTHONPATH=src python3 labs/sim/sim_react_thrash.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.llm import get_model
from rafeeq.reasoning.react import ReactTrace, ReactTraceStep, count_redundant_tool_calls, react_loop_explicit
from rafeeq.tools.logistics import track_shipment_impl

OBJECTIVE = "Where is my order TW-2026-16382?"
TOOL_IMPLS = {"track_shipment": lambda args: track_shipment_impl(args.get("order_id", ""))}
TOOL_SPECS = [{"name": name} for name in TOOL_IMPLS]
MAX_STEPS = 5


def broken_react_loop(objective: str, max_steps: int = MAX_STEPS) -> ReactTrace:
    """THE ANTI-PATTERN: identical shape to `react_loop_explicit`, minus
    the two `messages.append(...)` lines that write the action and its
    observation back into history. The model is asked the exact same
    question, with the exact same context, every single step."""
    messages: list = [("human", objective)]  # NEVER appended to below
    trace = ReactTrace(objective=objective)

    for step_no in range(1, max_steps + 1):
        model = get_model().bind_tools(TOOL_SPECS)
        reply = model.invoke([("system", "You are Rafeeq."), *messages])
        if not reply.tool_calls:
            trace.final_answer = reply.content
            trace.step_count = step_no - 1
            return trace

        call = reply.tool_calls[0]
        name, args = call["name"], call.get("args", {})
        observation = TOOL_IMPLS.get(name, lambda a: {"error": "unknown_tool"})(args)
        trace.steps.append(ReactTraceStep(step=step_no, thought=f"need {name}", action=name,
                                           action_input=dict(args), observation=observation))
        # THE BUG: no messages.append(...) here — `messages` never changes,
        # so next loop the model sees the IDENTICAL input again.

    trace.step_count = max_steps
    trace.terminated_reason = "step_budget_exhausted"
    trace.redundant_tool_calls = count_redundant_tool_calls(trace)
    return trace


def main() -> int:
    print(f"-- broken: observation never written back to state --  objective={OBJECTIVE!r}")
    broken = broken_react_loop(OBJECTIVE)
    print(f"  steps taken: {len(broken.steps)}, redundant tool calls: {broken.redundant_tool_calls}")
    thrashed = broken.redundant_tool_calls >= 1 and len(broken.steps) == MAX_STEPS
    print(f"  the SAME tool call repeated (never learned the answer, exhausted the budget): {thrashed}\n")

    print("-- fixed: the real react_loop_explicit (writes the observation back) --")
    fixed = react_loop_explicit(OBJECTIVE, tool_impls=TOOL_IMPLS, verbose=False)
    print(f"  steps taken: {len(fixed.steps)}, redundant tool calls: {fixed.redundant_tool_calls}")
    no_thrash = fixed.redundant_tool_calls == 0 and len(fixed.steps) == 1
    print(f"  ONE call answers the objective, zero redundant calls: {no_thrash}\n")

    ok = thrashed and no_thrash
    print("FAILURE DEMONSTRATED (thrashing) AND FIX PROVEN (write-back stops it)" if ok
          else "DEMO DID NOT REPRODUCE THE EXPECTED CONTRAST (unexpected)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
