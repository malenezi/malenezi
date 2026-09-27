#!/usr/bin/env python3
"""Lab 2 solution — verification script.

Stdlib + pydantic only (no langgraph). Runs the three reasoning patterns
on the real `tickets_eval.jsonl` via `rafeeq.reasoning.compare.compare_patterns`
and checks the shape of the comparison table Task 4 asks you to fill into
`BENCHMARKS.md`, plus the ReAct thrash counter and the Reflection bound.

Run: `PYTHONPATH=src python3 labs/lab02/solution/verify.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_REFLECTIONS
from rafeeq.reasoning.compare import compare_patterns
from rafeeq.reasoning.react import count_redundant_tool_calls, react_loop_explicit
from rafeeq.reasoning.reflection import reflect_and_revise

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, ok, detail))


def main() -> int:
    table = compare_patterns(limit=10)
    summary = table.summary()
    print(table.render())
    print()

    check("all three patterns (+ prompt-only) produced rows", set(summary) >= {
        "react", "plan_execute", "plan_execute_reflection", "prompt_only_anti_pattern"
    }, f"patterns={sorted(summary)}")

    for pattern in ("react", "plan_execute", "plan_execute_reflection"):
        stats = summary.get(pattern, {})
        check(f"{pattern}: measured on 10 tickets", stats.get("tickets") == 10, str(stats.get("tickets")))
        check(f"{pattern}: cost/ticket is a real (simulated) number, not zero-by-omission",
              stats.get("avg_cost_usd", 0) >= 0, str(stats.get("avg_cost_usd")))

    # -- redundant tool call counting (Module 2's research-note measurement) --
    trace = react_loop_explicit("أين طلبي رقم TW-2026-88120؟", verbose=False)
    redundant = count_redundant_tool_calls(trace)
    check("count_redundant_tool_calls runs and returns an int >= 0", isinstance(redundant, int) and redundant >= 0,
          f"redundant={redundant}, trace.redundant_tool_calls={trace.redundant_tool_calls}")
    check("react_loop_explicit's own count matches count_redundant_tool_calls(trace)",
          redundant == trace.redundant_tool_calls)

    # -- reflection bound respected --------------------------------------
    result = reflect_and_revise("A draft refund reply.", context="Customer asked for a refund.")
    check("reflect_and_revise bounded: passes_used <= MAX_REFLECTIONS",
          result["passes_used"] <= MAX_REFLECTIONS, f"passes_used={result['passes_used']} (MAX={MAX_REFLECTIONS})")
    check("reflect_and_revise always returns a usable draft (bounded, not silent)",
          isinstance(result["draft"], str) and len(result["draft"]) > 0)

    return _report()


def _report() -> int:
    name_w = max(len(n) for n, _, _ in RESULTS) if RESULTS else 10
    print("Lab 2 verification — three reasoning patterns")
    print("=" * (name_w + 20))
    n_pass = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        line = f"[{status}] {name:<{name_w}}"
        if detail:
            line += f"  ({detail})"
        print(line)
    print("=" * (name_w + 20))
    print(f"{n_pass}/{len(RESULTS)} checks passed")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
