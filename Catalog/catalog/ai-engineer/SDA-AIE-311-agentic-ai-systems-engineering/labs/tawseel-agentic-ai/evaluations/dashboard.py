"""Module 9 (evaluation layer) — the evaluation dashboard.

Renders `reports/DASHBOARD.md`: the 12-dimension metrics table (over the
full `tickets_eval.jsonl` harness), TawseelBench's per-family results,
an Architecture A (supervisor) vs B (agents-as-tools) comparison when
both are runnable, and a plain-text trend sparkline built from every
prior report already sitting in `reports/`. No plotting library — this
is markdown, meant to render in a PR review or a classroom terminal
alike.

CLI:
    python -m evaluations.dashboard --target stub
    python -m evaluations.dashboard --target stub --compare-arch
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"

for _p in (REPO_ROOT / "src", REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
del _p

# Eight levels, low to high — a dependency-free stand-in for a real
# sparkline chart (SPEC §1: no plotting libraries in this sandbox).
_SPARK_LEVELS = " ▁▂▃▄▅▆▇█"


def _sparkline(values: list[float]) -> str:
    if not values:
        return "(no history yet)"
    lo, hi = min(values), max(values)
    if hi - lo < 1e-9:
        return _SPARK_LEVELS[4] * len(values)
    chars = []
    for v in values:
        idx = round((v - lo) / (hi - lo) * (len(_SPARK_LEVELS) - 1))
        chars.append(_SPARK_LEVELS[idx])
    return "".join(chars)


def _load_history(target_name: str) -> list[tuple[str, float]]:
    """Every prior `reports/eval_<target>_*.json` report's
    (generated_at, task_success_rate), oldest first — the trend line."""
    if not REPORTS_DIR.is_dir():
        return []
    history: list[tuple[str, float]] = []
    for path in sorted(REPORTS_DIR.glob(f"eval_{target_name}_*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        rate = data.get("metrics", {}).get("task_success_rate")
        ts = data.get("generated_at", path.stem)
        if rate is not None:
            history.append((ts, rate))
    return history


def _render_architecture_comparison(target_a: str, target_b: str) -> str:
    from evaluations import harness
    from evaluations.metrics import Metrics, render_comparison
    from evaluations.targets import TargetUnavailable, get_target

    try:
        ta, tb = get_target(target_a), get_target(target_b)
        tickets = harness.load_tickets()
        results_a = harness.run_harness(tickets, ta)
        m_a = Metrics.from_results(results_a)
        results_b = harness.run_harness(tickets, tb)
        m_b = Metrics.from_results(results_b)
    except TargetUnavailable as exc:
        return (
            f"Architecture comparison unavailable in this environment: {exc}\n\n"
            "This is expected in the build sandbox (SPEC §1: `langgraph` is not "
            "installable here). Run `python -m evaluations.dashboard --compare-arch` "
            "again once `langgraph` is installed to populate this section — the "
            "comparison logic itself does not change."
        )
    except Exception as exc:  # noqa: BLE001
        return f"### Architecture comparison: {target_a} vs {target_b}\n\nCould not construct one of the targets: {exc}"

    return render_comparison(m_a, m_b, labels=(target_a, target_b))


def render_dashboard(target_name: str, compare_arch: bool, arch_a: str, arch_b: str) -> str:
    from evaluations import harness
    from evaluations.metrics import Metrics, render_family_table, render_table
    from evaluations.tawseelbench import runner as tb_runner
    from evaluations.targets import get_target

    now = datetime.now(timezone.utc).isoformat()
    target = get_target(target_name)

    # -- 1. 12-dimension dashboard, over the full ticket harness --------
    tickets = harness.load_tickets()
    ticket_results = harness.run_harness(tickets, target)
    ticket_metrics = Metrics.from_results(ticket_results)

    # -- 2. TawseelBench, all 60 scenarios, per family -------------------
    scenarios = tb_runner.load_scenarios()
    tb_results = tb_runner.run_bench(scenarios, target)
    tb_overall = Metrics.from_results(tb_results)
    by_family: dict[str, list[dict[str, Any]]] = {}
    for r in tb_results:
        by_family.setdefault(r["family"], []).append(r)
    family_metrics = {fam: Metrics.from_results(rs) for fam, rs in by_family.items()}

    # -- 3. history / trend ---------------------------------------------
    history = _load_history(target_name)
    current_rate = ticket_metrics.task_success_rate
    trend_values = [rate for _, rate in history] + [current_rate]

    lines: list[str] = []
    lines.append("# TawseelBench / harness evaluation dashboard")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append(f"Target under test: `{target_name}`")
    lines.append("")
    lines.append("## 1. Twelve-dimension dashboard (tickets_eval.jsonl, n=%d)" % len(ticket_results))
    lines.append("")
    lines.append(render_table(ticket_metrics, title=f"harness — {target_name}"))
    lines.append("")
    lines.append("## 2. TawseelBench (n=%d)" % len(tb_results))
    lines.append("")
    lines.append(render_table(tb_overall, title=f"TawseelBench — {target_name}"))
    lines.append("")
    lines.append("### Per-family results")
    lines.append("")
    lines.append(render_family_table(family_metrics))
    lines.append("")
    lines.append("## 3. Architecture A vs B")
    lines.append("")
    if compare_arch:
        lines.append(_render_architecture_comparison(arch_a, arch_b))
    else:
        lines.append(f"Skipped (pass `--compare-arch` to run `{arch_a}` vs `{arch_b}` — "
                      f"both require `langgraph`, not installable in this build sandbox; "
                      f"see SPEC §1).")
    lines.append("")
    lines.append("## 4. Task-success trend (harness, `--target %s`)" % target_name)
    lines.append("")
    lines.append("```")
    lines.append(_sparkline(trend_values))
    lines.append("```")
    if history:
        lines.append("")
        lines.append(f"{len(history)} prior report(s) under `reports/eval_{target_name}_*.json`, "
                      f"oldest {history[0][0]} -> latest (this run) {current_rate:.1%}.")
    else:
        lines.append("")
        lines.append("No prior `reports/eval_%s_*.json` reports found — this is the first point "
                      "on the trend. Run `python -m evaluations.harness --target %s` again later "
                      "to add more." % (target_name, target_name))
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render reports/DASHBOARD.md.")
    parser.add_argument("--target", default="stub")
    parser.add_argument("--compare-arch", action="store_true", help="also run the Architecture A vs B comparison")
    parser.add_argument("--arch-a", default="supervisor")
    parser.add_argument("--arch-b", default="agents_as_tools")
    parser.add_argument("--out", default=str(REPORTS_DIR / "DASHBOARD.md"))
    args = parser.parse_args(argv)

    markdown = render_dashboard(args.target, args.compare_arch, args.arch_a, args.arch_b)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    print(f"wrote {out_path}")
    print()
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
