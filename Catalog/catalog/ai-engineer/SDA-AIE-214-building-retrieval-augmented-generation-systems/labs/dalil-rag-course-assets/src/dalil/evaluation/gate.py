"""The regression gate: evaluation that changes behaviour. Module 6, Lab 6.

An evaluation harness nobody is forced to look at is a report. A gate that
fails the build is an engineering control. The difference is the entire point
of Module 6.

Rules encoded here:
  * a metric may not drop more than `tolerance` (default 0.03) below baseline;
  * hard floors are absolute — faithfulness below 0.90 fails even if the
    baseline was lower, because the floor is a safety property, not a trend;
  * the baseline records the CONFIG it was measured under. Comparing a run at
    top_k=10 against a baseline at top_k=6 is comparing two systems, and the
    gate says so instead of silently passing;
  * regenerating the baseline is a separate, deliberate command
    (`--update-baseline`) and the capstone rubric flags any commit that changes
    quality and the baseline together.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path

from ..config import settings

# Absolute floors from the course benchmark targets (capstone requirement 5).
FLOORS = {
    "faithfulness": 0.90,
    "context_recall": 0.88,
    "answer_relevancy": 0.85,
    "context_precision": 0.80,
}

CONFIG_KEYS = ("embed_model", "reranker", "fetch_k", "top_k", "ef",
               "context_budget", "refusal_tau")


@dataclass
class GateResult:
    passed: bool
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    deltas: dict = field(default_factory=dict)

    def render(self) -> str:
        lines = ["REGRESSION GATE: " + ("PASS" if self.passed else "FAIL")]
        for k, d in sorted(self.deltas.items()):
            arrow = "+" if d >= 0 else ""
            lines.append(f"  {k:20s} {arrow}{d:+.4f}")
        for w in self.warnings:
            lines.append(f"  [warn] {w}")
        for f in self.failures:
            lines.append(f"  [FAIL] {f}")
        return "\n".join(lines)


def check_gate(current: dict, baseline: dict | None, *,
               tolerance: float | None = None,
               floors: dict | None = None) -> GateResult:
    tol = settings.gate_tolerance if tolerance is None else tolerance
    floors = FLOORS if floors is None else floors
    res = GateResult(passed=True)

    cur_m = current.get("metrics", {})
    if current.get("judge", "").startswith("offline"):
        res.warnings.append("current run used offline proxy metrics — gate is advisory only")

    for metric, floor in floors.items():
        if metric in cur_m and cur_m[metric] < floor:
            res.passed = False
            res.failures.append(f"{metric}={cur_m[metric]:.4f} below absolute floor {floor}")

    if baseline is None:
        res.warnings.append("no baseline found — recording the first one is not a pass")
        return res

    base_cfg = baseline.get("config", {})
    cur_cfg = current.get("config", {})
    drift = [k for k in CONFIG_KEYS if base_cfg.get(k) != cur_cfg.get(k)]
    if drift:
        res.warnings.append(
            "config differs from baseline (" +
            ", ".join(f"{k}: {base_cfg.get(k)}->{cur_cfg.get(k)}" for k in drift) +
            ") — deltas below compare two different systems")

    if baseline.get("judge") != current.get("judge"):
        res.warnings.append(
            f"judge changed ({baseline.get('judge')} -> {current.get('judge')}) — "
            f"metric deltas are not comparable across judges")

    base_m = baseline.get("metrics", {})
    for metric, value in cur_m.items():
        if metric not in base_m:
            continue
        delta = round(value - base_m[metric], 4)
        res.deltas[metric] = delta
        if delta < -tol:
            res.passed = False
            res.failures.append(
                f"{metric} regressed {delta:+.4f} (baseline {base_m[metric]:.4f}, "
                f"tolerance {tol})")
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--current", type=Path, default=Path("reports/ragas_report.json"))
    ap.add_argument("--baseline", type=Path, default=Path("reports/baseline.json"))
    ap.add_argument("--tolerance", type=float)
    ap.add_argument("--update-baseline", action="store_true",
                    help="record the current run as the new baseline (deliberate act)")
    a = ap.parse_args()

    current = json.loads(a.current.read_text(encoding="utf-8"))
    baseline = json.loads(a.baseline.read_text(encoding="utf-8")) if a.baseline.exists() else None

    if a.update_baseline:
        a.baseline.parent.mkdir(parents=True, exist_ok=True)
        a.baseline.write_text(json.dumps(current, ensure_ascii=False, indent=2),
                              encoding="utf-8")
        print(f"baseline updated -> {a.baseline}\n"
              f"Reminder: a commit that changes quality AND the baseline is flagged "
              f"by the capstone rubric. Update baselines in their own commit.")
        return 0

    res = check_gate(current, baseline, tolerance=a.tolerance)
    print(res.render())
    return 0 if res.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
