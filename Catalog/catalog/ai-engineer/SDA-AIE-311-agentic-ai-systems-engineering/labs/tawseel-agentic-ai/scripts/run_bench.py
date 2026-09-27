#!/usr/bin/env python3
"""Module 9 (evaluation layer) — the top-level "run everything" CLI.

Runs TawseelBench and/or the cross-module harness over one target and
prints/writes the results — the single command a student or CI job
reaches for instead of remembering `python -m evaluations.<...>` paths.

Usage (from anywhere; paths are resolved relative to the repo root):
    python3 scripts/run_bench.py --target stub
    python3 scripts/run_bench.py --target stub --suite tawseelbench --family security
    python3 scripts/run_bench.py --target stub --suite harness --tag multi_domain
    python3 scripts/run_bench.py --target stub --suite both --out-dir reports/
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
    parser = argparse.ArgumentParser(description="Run TawseelBench and/or the cross-module harness.")
    parser.add_argument("--target", default="stub", help="stub | monolith | supervisor | agents_as_tools | recorded:<path>")
    parser.add_argument("--suite", choices=["tawseelbench", "harness", "both"], default="both")
    parser.add_argument("--family", default=None, help="tawseelbench only: orders|logistics|billing|multi_domain|security|policy_edge")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default=None)
    parser.add_argument("--tag", default=None)
    parser.add_argument("--locale", choices=["ar", "en"], default=None)
    parser.add_argument("--out-dir", default=None, help="write full JSON+markdown reports under this directory")
    args = parser.parse_args(argv)

    from evaluations.targets import TargetUnavailable, get_target

    try:
        target = get_target(args.target)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not construct target {args.target!r}: {exc}")
        return 1

    exit_code = 0

    if args.suite in ("tawseelbench", "both"):
        from evaluations.tawseelbench import runner as tb_runner

        print("=" * 78)
        print(f"TawseelBench — target={args.target!r}")
        print("=" * 78)
        scenarios = tb_runner.load_scenarios(args.family)
        scenarios = tb_runner.filter_scenarios(scenarios, difficulty=args.difficulty, tag=args.tag, locale=args.locale)
        if not scenarios:
            print("No TawseelBench scenarios matched the given filters.")
            exit_code = 1
        else:
            try:
                results = tb_runner.run_bench(scenarios, target)
            except TargetUnavailable as exc:
                print(f"Target unavailable: {exc}")
                return 1
            tb_runner._print_summary(results)
            if not all(r["passed"] for r in results):
                exit_code = 1
            if args.out_dir:
                import json
                out_path = Path(args.out_dir) / f"tawseelbench_{args.target.replace(':', '_')}.json"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
                print(f"\nwrote {out_path}")
        print()

    if args.suite in ("harness", "both"):
        from evaluations import harness

        print("=" * 78)
        print(f"Harness (tickets_eval.jsonl) — target={args.target!r}")
        print("=" * 78)
        tickets = harness.load_tickets()
        tickets = harness.filter_tickets(tickets, difficulty=args.difficulty, tag=args.tag, locale=args.locale)
        if not tickets:
            print("No tickets matched the given filters.")
            exit_code = 1
        else:
            try:
                results = harness.run_harness(tickets, target)
            except TargetUnavailable as exc:
                print(f"Target unavailable: {exc}")
                return 1
            harness._print_summary(results, args.target)
            out_dir = Path(args.out_dir) if args.out_dir else harness.REPORTS_DIR
            from datetime import datetime, timezone
            ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            out_path = out_dir / f"eval_{args.target.replace(':', '_')}_{ts}.json"
            harness._write_report(results, args.target, out_path)
            print(f"\nwrote {out_path}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
