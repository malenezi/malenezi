#!/usr/bin/env python3
"""
environment_check.py — SDA-DSC-213 Experimentation, A/B Testing and Causal Inference
SDAIA Academy · Injaz course package

Run this BEFORE the course starts (instructor: T-minus 1 week; participants:
T-minus 2 days). It answers four questions and nothing else:

  1. Is the Python version new enough?
  2. Is every REQUIRED package importable?  (a missing one is FAIL)
  3. Which OPTIONAL packages are missing?   (missing is FINE — every lab has a
     no-DoWhy path that runs on the core stack alone)
  4. Are the datasets present, the right size, and do they still contain the
     planted ground truths the labs are built to recover?

Usage:
    python environment_check.py               # from the course_assets root
    python environment_check.py --quiet       # summary lines only
    python environment_check.py --root /path/to/course_assets

Exit code 0 = PASS (safe to teach), non-zero = FAIL (fix before the course).
"""

from __future__ import annotations

import argparse
import importlib
import os
import sys
import time
from pathlib import Path

MIN_PYTHON = (3, 10)
RECOMMENDED_PYTHON = "3.12"

# --------------------------------------------------------------------------
# What must be here
# --------------------------------------------------------------------------

REQUIRED_PACKAGES = [
    ("numpy", "1.26"),
    ("pandas", "2.1"),
    ("scipy", "1.11"),
    ("statsmodels", "0.14"),
    ("matplotlib", "3.8"),
    ("sklearn", "1.3"),      # pip name: scikit-learn
    ("pyarrow", "14.0"),
]

# Missing optional packages are NOT a failure. They unlock convenience paths
# (DoWhy's identify->estimate->refute API, EconML's causal forest, the
# linearmodels panel IV estimator) that every lab also provides by hand.
OPTIONAL_PACKAGES = [
    ("dowhy", "Lab 6 DoWhy workflow — fallback: causal_utils.InjazDAG + statsmodels"),
    ("econml", "Capstone CATE extension — fallback: subgroup regressions"),
    ("linearmodels", "Panel IV convenience — fallback: causal_utils.iv_2sls"),
    ("networkx", "DAG drawing in Lab 6 — fallback: the printed adjustment set"),
    ("jupyterlab", "Notebook UI — fallback: VS Code, classic notebook, or Colab"),
]

PIP_NAME = {"sklearn": "scikit-learn"}

# file -> expected row count
DATASETS = {
    "simulated_potential_outcomes.parquet": 20_000,
    "injaz_users_pool.csv": 200_000,
    "injaz_users.csv": 20_000,
    "injaz_experiment_results.csv": 80_000,
    "injaz_experiment_results_srm_broken.csv": 78_747,
    "injaz_pre_period.csv": 50_000,
    "injaz_traffic_forecast.csv": 90,
    "injaz_sessions.csv.gz": 339_017,
    "injaz_regions_panel.csv": 312,
    "injaz_regions_panel_pretrend.csv": 312,
    "collider_sim.parquet": 50_000,
    "injaz_autofill_ab.csv": 70_000,
}

SUPPORT_FILES = [
    "data/DATA_DICTIONARY.md",
    "data/GROUND_TRUTH.json",
    "data/make_data.py",
    "causal_utils/__init__.py",
    "requirements.txt",
    "requirements-core.txt",
]

# --------------------------------------------------------------------------
# Output helpers
# --------------------------------------------------------------------------

_USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def _c(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _USE_COLOR else text


OK = _c("  OK  ", "32")
WARN = _c(" WARN ", "33")
BAD = _c(" FAIL ", "31")


class Report:
    def __init__(self, quiet: bool = False):
        self.quiet = quiet
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def head(self, title: str) -> None:
        if not self.quiet:
            print(f"\n{title}\n" + "-" * len(title))

    def ok(self, msg: str) -> None:
        if not self.quiet:
            print(f"[{OK}] {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        if not self.quiet:
            print(f"[{WARN}] {msg}")

    def fail(self, msg: str) -> None:
        self.failures.append(msg)
        print(f"[{BAD}] {msg}")


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check_python(r: Report) -> None:
    r.head("1. Python")
    v = sys.version_info
    label = f"{v.major}.{v.minor}.{v.micro}"
    if (v.major, v.minor) < MIN_PYTHON:
        r.fail(f"Python {label} — the course needs "
               f"{MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ (recommended {RECOMMENDED_PYTHON})")
    else:
        r.ok(f"Python {label}  (minimum {MIN_PYTHON[0]}.{MIN_PYTHON[1]}, "
             f"recommended {RECOMMENDED_PYTHON})")
    r.ok(f"interpreter: {sys.executable}")


def check_packages(r: Report) -> None:
    r.head("2. Required packages")
    for name, minimum in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(name)
        except Exception as exc:                       # noqa: BLE001
            pip = PIP_NAME.get(name, name)
            r.fail(f"{name:<14} NOT IMPORTABLE — run `pip install {pip}>={minimum}`  ({exc})")
            continue
        ver = getattr(mod, "__version__", "?")
        r.ok(f"{name:<14} {ver:<12} (need >= {minimum})")

    r.head("3. Optional packages — missing here is FINE")
    missing = []
    for name, note in OPTIONAL_PACKAGES:
        try:
            mod = importlib.import_module(name)
            r.ok(f"{name:<14} {getattr(mod, '__version__', 'installed'):<12} {note}")
        except Exception:                              # noqa: BLE001
            missing.append(name)
            if not r.quiet:
                print(f"[ skip ] {name:<14} {'not installed':<12} {note}")
    if missing:
        print(f"        -> {len(missing)} optional package(s) missing: "
              f"{', '.join(missing)}")
        print("        -> This is NOT a failure. Every lab runs on the core "
              "stack alone; the")
        print("           DoWhy/EconML cells are clearly marked optional and "
              "have a hand-rolled")
        print("           equivalent in causal_utils immediately below them.")


def check_toolkit(r: Report, root: Path) -> None:
    r.head("4. Course toolkit (causal_utils)")
    sys.path.insert(0, str(root))
    try:
        import causal_utils as cu
    except Exception as exc:                           # noqa: BLE001
        r.fail(f"cannot import causal_utils from {root} ({exc})")
        return
    r.ok(f"causal_utils {cu.__version__} imported from {Path(cu.__file__).parent}")
    expected = ["hash_assign", "srm_check", "balance_table",
                "sample_size_proportions", "run_length", "cuped_adjust",
                "two_proportion_test", "regression_effect", "correct_pvalues",
                "match_nearest", "did_twfe", "event_study", "iv_2sls",
                "decision_plot", "decision_memo", "AnalysisPlan", "freeze_plan"]
    missing = [f for f in expected if not hasattr(cu, f)]
    if missing:
        r.fail(f"causal_utils is missing: {', '.join(missing)}")
    else:
        r.ok(f"all {len(expected)} public toolkit functions present")


def check_datasets(r: Report, root: Path) -> None:
    r.head("5. Datasets")
    import pandas as pd

    data_dir = root / "data"
    if not data_dir.is_dir():
        r.fail(f"no data directory at {data_dir} — run `cd data && python make_data.py`")
        return

    for fname, expected_rows in DATASETS.items():
        path = data_dir / fname
        if not path.exists():
            r.fail(f"{fname:<45} MISSING — regenerate with "
                   f"`cd data && python make_data.py`")
            continue
        try:
            if path.suffix == ".parquet":
                n = len(pd.read_parquet(path, columns=None))
            else:
                n = len(pd.read_csv(path, usecols=[0]))
        except Exception as exc:                       # noqa: BLE001
            r.fail(f"{fname:<45} UNREADABLE ({exc})")
            continue
        mb = path.stat().st_size / 1e6
        if n != expected_rows:
            r.fail(f"{fname:<45} {n:>8,} rows — expected {expected_rows:,}. "
                   f"Regenerate with make_data.py (seeds are fixed).")
        else:
            r.ok(f"{fname:<45} {n:>8,} rows  {mb:>7.1f} MB")

    r.head("6. Supporting files")
    for rel in SUPPORT_FILES:
        p = root / rel
        if p.exists():
            r.ok(f"{rel}")
        else:
            r.fail(f"{rel} MISSING")


def check_ground_truth(r: Report, root: Path) -> None:
    """Three fast assertions against the planted truths.

    These are the numbers the labs are built to recover. If they have drifted,
    the datasets were regenerated with different seeds and every expected
    output in the answer key is wrong.
    """
    r.head("7. Ground-truth smoke tests (3 assertions)")
    import numpy as np
    import pandas as pd

    d = root / "data"

    # --- Smoke test 1: Module 1 selection bias -----------------------------
    # Planted ATE = +4.93 pp; the self-selected comparison must be badly biased.
    try:
        po = pd.read_parquet(d / "simulated_potential_outcomes.parquet",
                             columns=["tau_individual", "treated_self_selected",
                                      "y_observed_self_selected"])
        ate = float(po["tau_individual"].mean())
        t = po["treated_self_selected"] == 1
        naive = float(po.loc[t, "y_observed_self_selected"].mean()
                      - po.loc[~t, "y_observed_self_selected"].mean())
        assert abs(ate - 0.0493) < 0.002, f"ATE {ate:.4f} != 0.0493"
        assert abs(naive - 0.1930) < 0.005, f"naive {naive:.4f} != 0.1930"
        r.ok(f"[1/3] Module 1  true ATE = {ate:+.4f} (expect +0.0493 ± 0.002); "
             f"naive self-selected = {naive:+.4f} (expect +0.1930 ± 0.005) "
             f"-> selection bias {naive - ate:+.4f}")
    except AssertionError as exc:
        r.fail(f"[1/3] Module 1 potential-outcomes truth has drifted: {exc}")
    except Exception as exc:                           # noqa: BLE001
        r.fail(f"[1/3] Module 1 smoke test could not run: {exc}")

    # --- Smoke test 2: uploader A/B lift among TRIGGERED users -------------
    # Planted +2.2 pp on triggered users. Analysing all 80k assigned users
    # instead of the ~49.6k triggered ones is the Day 2 trap and yields ~1.6 pp.
    try:
        ex = pd.read_csv(d / "injaz_experiment_results.csv",
                         usecols=["variant", "triggered", "completed"])
        tr = ex[ex["triggered"] == 1]
        lift = float(tr.loc[tr.variant == "treatment", "completed"].mean()
                     - tr.loc[tr.variant == "control", "completed"].mean())
        all_lift = float(ex.loc[ex.variant == "treatment", "completed"].mean()
                         - ex.loc[ex.variant == "control", "completed"].mean())
        assert abs(lift - 0.0220) < 0.003, f"triggered lift {lift:.4f} != 0.0220"
        assert all_lift < lift - 0.003, "the all-assigned dilution trap has vanished"
        r.ok(f"[2/3] Module 4  uploader lift (triggered) = {lift:+.4f} "
             f"(expect +0.0220 ± 0.003); all-assigned = {all_lift:+.4f} "
             f"-> dilution trap intact")
    except AssertionError as exc:
        r.fail(f"[2/3] Uploader experiment truth has drifted: {exc}")
    except Exception as exc:                           # noqa: BLE001
        r.fail(f"[2/3] Uploader smoke test could not run: {exc}")

    # --- Smoke test 3: the collider ---------------------------------------
    # Two independent causes; conditioning on their common effect must open a
    # spurious negative association.
    try:
        co = pd.read_parquet(d / "collider_sim.parquet")
        uncond = float(np.corrcoef(co["digital_literacy"],
                                   co["service_simplicity"])[0, 1])
        sub = co[co["completed"] == 1]
        cond = float(np.corrcoef(sub["digital_literacy"],
                                 sub["service_simplicity"])[0, 1])
        assert abs(uncond) < 0.02, f"unconditional corr {uncond:.4f} is not ~0"
        assert cond < -0.10, f"conditional corr {cond:.4f} is not clearly negative"
        r.ok(f"[3/3] Module 6  collider corr = {uncond:+.4f} unconditional "
             f"(expect ~0.00) -> {cond:+.4f} conditional on completed==1 "
             f"(expect ~-0.198)")
    except AssertionError as exc:
        r.fail(f"[3/3] Collider truth has drifted: {exc}")
    except Exception as exc:                           # noqa: BLE001
        r.fail(f"[3/3] Collider smoke test could not run: {exc}")


# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=None,
                    help="course_assets root (default: this script's directory)")
    ap.add_argument("--quiet", action="store_true", help="summary lines only")
    args = ap.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent
    started = time.time()

    print("=" * 78)
    print("SDA-DSC-213 · Experimentation, A/B Testing and Causal Inference")
    print("Environment and data check · SDAIA Academy · Injaz course package")
    print(f"root: {root}")
    print("=" * 78)

    r = Report(quiet=args.quiet)
    check_python(r)
    check_packages(r)
    check_toolkit(r, root)
    check_datasets(r, root)
    check_ground_truth(r, root)

    elapsed = time.time() - started
    print("\n" + "=" * 78)
    if r.failures:
        print(_c(f"RESULT: FAIL — {len(r.failures)} blocking problem(s) "
                 f"in {elapsed:.1f}s", "31"))
        for f in r.failures:
            print(f"  - {f}")
        print("\nFix these before the course. Most are solved by either")
        print("  pip install -r requirements-core.txt")
        print("or")
        print("  cd data && python make_data.py")
        print("=" * 78)
        return 1

    print(_c(f"RESULT: PASS — environment is ready to teach ({elapsed:.1f}s)", "32"))
    print(f"  required packages : all importable")
    print(f"  datasets          : {len(DATASETS)} files, all present with the "
          f"expected row counts")
    print(f"  ground truth      : 3/3 smoke assertions passed")
    if r.warnings:
        print(f"  warnings          : {len(r.warnings)} (non-blocking)")
        for w in r.warnings:
            print(f"      - {w}")
    print("\nOptional packages (dowhy, econml, linearmodels) are not required: "
          "every lab\nhas a core-stack path. Install them if you want the "
          "DoWhy refuter API and the\nEconML causal forest in the capstone "
          "extensions.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
