"""PA-3 setup: build the PA-3 variant of ``gold.eta_features``.

================================ WARNING ==================================
THIS SCRIPT BUILDS A DELIBERATELY BROKEN ASSESSMENT ARTEFACT.
The table it produces carries the five defects listed in the PA-3 answer key
(`labs/assessments/PA-3_Feature_Leakage_Audit.md`, section 5a), on purpose.
DO NOT USE IT — or the builder it calls — AS A REFERENCE for point-in-time
feature engineering.
===========================================================================

EXACTLY the 13 CONVENTIONS columns. Idempotent: the sandbox is deleted and
rebuilt on every run, so it is safe to re-run between cohorts.

Run::

    python -m scripts.assessments.pa3_setup

The build itself lives in :mod:`masar.transform.build_eta_features_pa3`, so
there is one copy of the defect set rather than two that can drift apart.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# Allow `python scripts/assessments/pa3_setup.py` as well as `-m`.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from masar.transform.build_eta_features_pa3 import OUT, build  # noqa: E402


def main() -> None:
    """Wipe the PA-3 sandbox and rebuild the broken feature table."""
    shutil.rmtree(Path(OUT).parent, ignore_errors=True)
    n = build(OUT)
    print(f"[pa3-setup] eta_features: {n:,} rows, 13 columns -> {OUT}")
    print(
        "[pa3-setup] sandbox ready; broken builder at src/masar/transform/build_eta_features_pa3.py"
    )


if __name__ == "__main__":
    main()
