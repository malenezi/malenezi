#!/usr/bin/env python3
"""Lab 1 solution — verification script.

Stdlib-runnable (no langgraph required): it drives `reason()`/`route()`
BY HAND, exactly the way a compiled `StateGraph` would, against the
default `StubChatModel` (SPEC §2) — so every check below runs with zero
keys, zero network, and zero third-party dependencies, and still proves
the graph layer's own termination CONTRACT (`route()`'s two branches),
which is what `build_graph()` wires into an actual LangGraph graph once
`langgraph` is installed.

Run: `PYTHONPATH=src python3 labs/lab01/solution/verify.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.state import new_state
from rafeeq.core.graph import reason, route

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def _drive_loop(text: str, *, max_iterations: int) -> tuple[dict, str]:
    """The by-hand equivalent of `build_graph().invoke(...)`: call
    `reason`, then `route`, repeat, until `route` says something other
    than "reason". Returns (final_state, terminated_reason)."""
    state = new_state(customer_id="CUST-4471", locale="ar", messages=[("human", text)])
    for _ in range(max_iterations):
        update = reason(state)
        state["messages"] = list(state["messages"]) + list(update["messages"])
        state["step_count"] = update["step_count"]
        decision = route(state)
        if decision != "reason":
            reason_str = "step_budget_exhausted" if state["step_count"] >= MAX_STEPS else "final_answer"
            return state, reason_str
    return state, "OVERRAN max_iterations without route() ever halting"  # should never happen if route() is correct


def main() -> int:
    # -- 1. adversarial input: a track/refund-shaped message that always --
    #    gets a tool-call reply from StubChatModel, so it can ONLY halt on
    #    the step budget, never on "the model decided it was done".
    adversarial_text = "أين طلبي رقم TW-2026-88120؟"
    state, terminated_reason = _drive_loop(adversarial_text, max_iterations=MAX_STEPS + 5)
    check(
        "Loop termination (adversarial input) halts <= MAX_STEPS",
        state["step_count"] <= MAX_STEPS,
        f"halted at step_count={state['step_count']} (MAX_STEPS={MAX_STEPS}), reason={terminated_reason}",
    )
    check(
        "Adversarial input halts BECAUSE OF the budget, not a lucky final answer",
        terminated_reason == "step_budget_exhausted",
        terminated_reason,
    )
    check("Runaway runs (> MAX_STEPS) — none on this run", state["step_count"] <= MAX_STEPS)

    # -- 2. simple task: a message with no recognisable intent gets an --
    #    immediate final answer (no tool call) — the OTHER route() branch.
    simple_text = "شكراً على المساعدة"  # "thank you for your help" — no intent, no order id
    state2, terminated_reason2 = _drive_loop(simple_text, max_iterations=MAX_STEPS + 5)
    check(
        "Steps per simple task <= 3",
        state2["step_count"] <= 3,
        f"step_count={state2['step_count']}",
    )
    check("Simple task terminates on a genuine final answer, not the budget",
          terminated_reason2 == "final_answer", terminated_reason2)
    check("resolution field present in state (auditability)", "resolution" in state2)
    check("state inspectable: step_count is an int derivable from state alone", isinstance(state2["step_count"], int))

    # -- 3. broken_agent.py contrast — importable, runs unbounded (we only --
    #    prove it EXISTS and its three SMELLs are documented; running it
    #    forever is Task 1's job, not this checklist's).
    broken = Path(__file__).resolve().parent.parent / "start" / "broken_agent.py"
    broken_text = broken.read_text(encoding="utf-8") if broken.exists() else ""
    check("start/broken_agent.py exists", broken.exists())
    smell_markers = broken_text.count("# SMELL:")
    check("start/broken_agent.py has 3 # SMELL markers", smell_markers == 3, f"found {smell_markers}")
    check("start/broken_agent.py has no step/cost/wall-clock bound (no MAX_STEPS/RunBudget assignment)",
          "MAX_STEPS =" not in broken_text and "RunBudget(" not in broken_text)

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("\nLab 1 verification — bounded core loop")
    print("=" * (name_w + 24))
    n_pass = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        line = f"[{status}] {name:<{name_w}}"
        if detail:
            line += f"  ({detail})"
        print(line)
    print("=" * (name_w + 24))
    print(f"{n_pass}/{len(RESULTS)} checks passed")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
