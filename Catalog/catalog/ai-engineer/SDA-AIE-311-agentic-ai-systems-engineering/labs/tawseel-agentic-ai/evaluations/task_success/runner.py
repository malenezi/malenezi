"""Module 2 focused benchmark — task success.

A thin wrapper over `evaluations/harness.py`: no filters, the full
120-ticket `tickets_eval.jsonl` set, reported against the ONE metric
Module 2's Benchmarks table names explicitly:

    | Eval-set task success | Quality | >= 85% correct resolution | `tickets_eval.jsonl` |

CLI:
    python -m evaluations.task_success.runner --target stub
    python -m evaluations.task_success.runner --target stub --out reports/task_success_stub.json
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

TARGET_TASK_SUCCESS_RATE = 0.85  # Module 2 Benchmarks table


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Module 2 focused benchmark: task success over tickets_eval.jsonl.")
    parser.add_argument("--target", default="stub")
    parser.add_argument("--out", default=None)
    args = parser.parse_args(argv)

    from evaluations import harness
    from evaluations.targets import get_target

    tickets = harness.load_tickets()
    target = get_target(args.target)
    results = harness.run_harness(tickets, target)
    from evaluations.metrics import Metrics, render_table
    m = Metrics.from_results(results)
    print(render_table(m, title=f"Module 2 — task success ({args.target})"))
    verdict = "MEETS" if m.task_success_rate >= TARGET_TASK_SUCCESS_RATE else "BELOW"
    print(f"\ntask_success_rate={m.task_success_rate:.1%} vs target >= {TARGET_TASK_SUCCESS_RATE:.0%}: {verdict} target")

    if args.out:
        report = harness._write_report(results, args.target, Path(args.out))
        print(f"\nwrote {args.out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
