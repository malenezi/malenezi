#!/usr/bin/env python3
"""Run the Masar medallion DAG without Airflow.

Same task graph, same callables, same dependency ordering as
``orchestration/dags/masar_medallion.py`` — declared once in
``masar.orchestration.runner`` and imported by both, so the two can never
disagree about what the pipeline is.

Use it when Airflow will not install (a locked-down laptop, a constraint-file
resolution that will not finish, an afternoon you would rather spend on data
engineering). No lab in this course ever blocks on an orchestrator.

Examples::

    python orchestration/run_local.py --list
    python orchestration/run_local.py --run
    python orchestration/run_local.py --run --inject-failure build_silver
    python orchestration/run_local.py --run --only gold_trip_features
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make `masar` importable from a plain clone, before `pip install -e .`.
# The DAG has to run on the machine as it is, not as it should be.
_SRC = Path(__file__).resolve().parent.parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from masar.orchestration.runner import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
