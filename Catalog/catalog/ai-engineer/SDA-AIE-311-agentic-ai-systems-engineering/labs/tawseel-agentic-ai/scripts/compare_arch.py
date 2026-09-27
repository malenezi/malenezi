#!/usr/bin/env python3
"""Module 6 — Architecture A vs B comparison CLI.

SPEC §6: "implement BOTH [supervisor and agents-as-tools] and compare on
task success / tool calls / tokens / latency / handoff failures /
unauthorised-action risk." This script runs both over `tickets_eval.jsonl`
(and, with `--tawseelbench`, TawseelBench too) and prints/writes the
side-by-side `evaluations.metrics.render_comparison` table.

Both architectures require `langgraph` — not installable in this build
sandbox (SPEC §1) — so this script's own worked example is a `--dry-run`
that compares two OFFLINE targets instead (`stub` against itself, or
`stub` against a `recorded:<path>` replay) purely to exercise the
plumbing; the real comparison this script exists for runs once
`langgraph` is installed.

Usage:
    python3 scripts/compare_arch.py                       # supervisor vs agents_as_tools
    python3 scripts/compare_arch.py --a monolith --b supervisor
    python3 scripts/compare_arch.py --dry-run              # stub vs stub, offline smoke test
    python3 scripts/compare_arch.py --tawseelbench
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
for _p in (REPO_ROOT / "src", REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare two targets (Architecture A vs B by default).")
    parser.add_argument("--a", default="supervisor", help="Architecture A target name (default: supervisor)")
    parser.add_argument("--b", default="agents_as_tools", help="Architecture B target name (default: agents_as_tools)")
    parser.add_argument("--dry-run", action="store_true", help="use --a stub --b stub instead — an offline smoke test of this script's plumbing, not a real architecture comparison")
    parser.add_argument("--tawseelbench", action="store_true", help="also compare over the full TawseelBench suite, not just tickets_eval.jsonl")
    parser.add_argument("--out", default=None, help="write the comparison markdown here")
    args = parser.parse_args(argv)

    target_a_name = "stub" if args.dry_run else args.a
    target_b_name = "stub" if args.dry_run else args.b

    from evaluations import harness
    from evaluations.metrics import Metrics, render_comparison
    from evaluations.targets import TargetUnavailable, get_target

    try:
        target_a = get_target(target_a_name)
        target_b = get_target(target_b_name)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not construct a target: {exc}")
        return 1

    sections: list[str] = []
    exit_code = 0

    try:
        tickets = harness.load_tickets()
        results_a = harness.run_harness(tickets, target_a)
        results_b = harness.run_harness(tickets, target_b)
    except TargetUnavailable as exc:
        print(f"Target unavailable: {exc}")
        print()
        print("This is expected in the build sandbox (SPEC §1: `langgraph` is not "
              "installable here). Use `--dry-run` to exercise this script's comparison "
              "plumbing offline (stub vs stub), or run this again in a classroom "
              "environment with `langgraph` installed for the real Architecture A vs B "
              "numbers.")
        return 1

    m_a, m_b = Metrics.from_results(results_a), Metrics.from_results(results_b)
    sections.append(f"## tickets_eval.jsonl (n={len(tickets)})\n\n" + render_comparison(m_a, m_b, labels=(target_a_name, target_b_name)))

    if args.tawseelbench:
        from evaluations.tawseelbench import runner as tb_runner

        scenarios = tb_runner.load_scenarios()
        tb_results_a = tb_runner.run_bench(scenarios, target_a)
        tb_results_b = tb_runner.run_bench(scenarios, target_b)
        tb_m_a, tb_m_b = Metrics.from_results(tb_results_a), Metrics.from_results(tb_results_b)
        sections.append(f"## TawseelBench (n={len(scenarios)})\n\n" + render_comparison(tb_m_a, tb_m_b, labels=(target_a_name, target_b_name)))

    header = f"# Architecture comparison: {target_a_name} vs {target_b_name}"
    if args.dry_run:
        header += "\n\n(--dry-run: both targets are `stub` — this exercises the comparison plumbing only, it is not a real architecture result.)"
    markdown = header + "\n\n" + "\n\n".join(sections)
    print(markdown)

    if args.out:
        Path(args.out).write_text(markdown, encoding="utf-8")
        print(f"\nwrote {args.out}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
