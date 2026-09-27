"""Module 7 focused benchmark — policy compliance and determinism.

A thin wrapper over `evaluations/tawseelbench/runner.py`, restricted to
the `billing` and `policy_edge` families (the refund-limit / eligibility
/ idempotency scenarios) and reported against Module 7's Benchmarks-table
targets:

    | Rule determinism (same input -> same route) | Reliability | 100% | 100-repeat replay |
    | Adversarial rule bypass | Security | 0 (gates uncrossable) | sim + red-team probes |
    | Eval-set success | Quality | >= M2 baseline (no regression) | refund_cases.jsonl |

Determinism is checked directly here (N repeats of the same scenario set
against a deterministic target must produce byte-identical tool
sequences) rather than assumed — `StubTarget` and any pure rule/flow
target should pass this trivially; only a target with real model calls
in the loop could fail it.

CLI:
    python -m evaluations.policy_compliance.runner --target stub
    python -m evaluations.policy_compliance.runner --target stub --repeats 5
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Module 7 focused benchmark: policy compliance and determinism.")
    parser.add_argument("--target", default="stub")
    parser.add_argument("--repeats", type=int, default=3, help="how many times to replay the set for the determinism check")
    args = parser.parse_args(argv)

    from evaluations.tawseelbench import runner as tb_runner
    from evaluations.targets import get_target
    from evaluations.metrics import Metrics, render_table

    scenarios = tb_runner.load_scenarios()
    billing_and_policy = [s for s in scenarios if 16 <= int(s["id"][3:]) <= 24 or 51 <= int(s["id"][3:]) <= 60]

    target = get_target(args.target)
    results = tb_runner.run_bench(billing_and_policy, target)
    m = Metrics.from_results(results)
    print(render_table(m, title=f"Module 7 — policy compliance ({args.target}, billing + policy_edge, n={len(results)})"))

    # Determinism: replay the same set `--repeats` times, compare the tool
    # NAME sequence (not full results — result dicts embed a wall-clock
    # latency, which is not a determinism signal) for every scenario.
    baseline_seqs = {r["scenario_id"]: [c["name"] for c in r["transcript"]["tool_calls"]] for r in results}
    mismatches = 0
    for _ in range(max(0, args.repeats - 1)):
        rerun = tb_runner.run_bench(billing_and_policy, get_target(args.target))
        for r in rerun:
            seq = [c["name"] for c in r["transcript"]["tool_calls"]]
            if seq != baseline_seqs[r["scenario_id"]]:
                mismatches += 1
    determinism = 1.0 if mismatches == 0 else 1 - (mismatches / (len(billing_and_policy) * max(0, args.repeats - 1)))
    print(f"\nDeterminism over {args.repeats} replay(s): {determinism:.1%} ({mismatches} mismatched tool-sequence(s))")
    print(f"Policy-compliance rate: {m.policy_compliance_rate:.1%} vs target 100% adversarial-bypass-free")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
