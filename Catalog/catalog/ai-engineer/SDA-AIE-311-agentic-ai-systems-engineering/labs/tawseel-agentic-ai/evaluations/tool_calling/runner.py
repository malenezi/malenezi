"""Module 3 focused benchmark — tool selection accuracy.

A thin wrapper over `evaluations/harness.py`, reported against Module 3's
Benchmarks-table target:

    | Tool-selection accuracy | Reliability | >= 95% correct tool on eval set | labelled tickets |

`Metrics.correct_tool_call_rate` (from `tool_selection_correct`) is not
the right number to read here for a ticket-fixture run: that oracle only
grades ORDER (first call matches an expected FIRST tool) and reports
"not applicable" whenever no ordered `tool_sequence` is declared — which
`harness.ticket_to_pseudo_scenario` deliberately never does for tickets
(see its docstring). What `tickets_eval.jsonl`'s `expected.tools` field
actually encodes is an unordered COVERAGE requirement, so this runner
reports `required_tools_called` pass rate instead — "did every tool the
ticket says must run, actually run" — which is what Module 3's target is
really asking after correct routing.

CLI:
    python -m evaluations.tool_calling.runner --target stub
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (REPO_ROOT / "src", REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p

TARGET_ACCURACY = 0.95  # Module 3 Benchmarks table


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Module 3 focused benchmark: tool-selection accuracy.")
    parser.add_argument("--target", default="stub")
    args = parser.parse_args(argv)

    from evaluations import harness
    from evaluations.targets import get_target

    tickets = harness.load_tickets()
    target = get_target(args.target)
    results = harness.run_harness(tickets, target)

    n = len(results)
    correct = sum(1 for r in results if r["oracle_results"].get("required_tools_called", {}).get("passed", True))
    forbidden_hit = sum(1 for r in results if not r["oracle_results"].get("forbidden_tools_not_called", {}).get("passed", True))
    crashed = sum(1 for r in results if r["transcript"].get("error"))

    accuracy = correct / n if n else 0.0
    print(f"### Module 3 — tool-selection accuracy ({args.target})\n")
    print(f"n = {n} ticket(s)")
    print(f"required_tools_called pass rate (accuracy): {accuracy:.1%}")
    print(f"forbidden tool called: {forbidden_hit}/{n}")
    print(f"target crashed on tool error: {crashed}/{n}")
    verdict = "MEETS" if accuracy >= TARGET_ACCURACY else "BELOW"
    print(f"\naccuracy={accuracy:.1%} vs target >= {TARGET_ACCURACY:.0%}: {verdict} target")
    if accuracy < TARGET_ACCURACY:
        print("\nfailing tickets:")
        for r in results:
            if not r["oracle_results"].get("required_tools_called", {}).get("passed", True):
                print(f"  - {r['scenario_id']}: {r['oracle_results']['required_tools_called']['detail']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
