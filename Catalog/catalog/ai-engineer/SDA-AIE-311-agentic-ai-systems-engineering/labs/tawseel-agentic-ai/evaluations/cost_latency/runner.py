"""Module 9 focused benchmark — cost and latency.

A thin wrapper over `evaluations/harness.py`, reported against Module 9's
Benchmarks-table targets:

    | Blended cost/contact | Cost | >= 40% below pre-optimisation | gateway usage x replay |
    | p95 latency | Performance | <= 2.5 s | trace timing |
    | Eval-set success after optimisation | Quality | no regression vs pre-optimisation | tickets_eval.jsonl |
    | Write-tool retries | Reliability | 0 | retry-safety test |

`--target stub` is a rule-based, zero-model-call baseline — its cost and
latency are near-zero by construction, which is the honest floor to
compare a real (LangGraph) target's numbers against, not itself a
"40% below" result (there is nothing above it to be 40% below of). Run
this with `--target monolith` or `--target supervisor` once `langgraph`
is installed to get the actual comparison Module 9 asks for, or with
`--baseline` pointed at a pre-optimisation `monolith` report once one
exists.

CLI:
    python -m evaluations.cost_latency.runner --target stub
    python -m evaluations.cost_latency.runner --target stub --baseline reports/eval_monolith_pre_opt.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
for _p in (REPO_ROOT / "src", REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p

TARGET_P95_LATENCY_S = 2.5  # Module 9 Benchmarks table
TARGET_COST_REDUCTION = 0.40


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Module 9 focused benchmark: cost and latency.")
    parser.add_argument("--target", default="stub")
    parser.add_argument("--baseline", default=None, help="a prior report's JSON to compute blended-cost reduction against")
    args = parser.parse_args(argv)

    from evaluations import harness
    from evaluations.targets import get_target
    from evaluations.metrics import Metrics, render_table

    tickets = harness.load_tickets()
    target = get_target(args.target)
    results = harness.run_harness(tickets, target)
    m = Metrics.from_results(results)
    print(render_table(m, title=f"Module 9 — cost and latency ({args.target}, n={len(results)})"))

    write_tools_retried = 0
    for r in results:
        names = [c["name"] for c in r["transcript"]["tool_calls"]]
        seen: set[str] = set()
        for c in r["transcript"]["tool_calls"]:
            if c["name"] in seen and c.get("autonomy") != "internal":
                write_tools_retried += 1
            seen.add(c["name"])
    print(f"\np95 latency: {m.p95_latency_s:.3f}s vs target <= {TARGET_P95_LATENCY_S}s: "
          f"{'MEETS' if m.p95_latency_s <= TARGET_P95_LATENCY_S else 'BELOW'} target")
    print(f"Repeated tool-name calls within one run (a proxy for write-tool retries; "
          f"see retry.py's own idempotency test for the real check): {write_tools_retried}")

    if args.baseline:
        baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
        base_cost = baseline.get("metrics", {}).get("avg_cost_usd_per_task", 0.0)
        if base_cost:
            reduction = 1 - (m.avg_cost_usd_per_task / base_cost)
            verdict = "MEETS" if reduction >= TARGET_COST_REDUCTION else "BELOW"
            print(f"\nCost/task vs baseline {args.baseline}: {base_cost:.4f} -> {m.avg_cost_usd_per_task:.4f} USD "
                  f"({reduction:+.1%} change) vs target >= {TARGET_COST_REDUCTION:.0%} reduction: {verdict} target")
        else:
            print(f"\nBaseline {args.baseline} has 0 cost/task recorded — cannot compute a reduction percentage.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
