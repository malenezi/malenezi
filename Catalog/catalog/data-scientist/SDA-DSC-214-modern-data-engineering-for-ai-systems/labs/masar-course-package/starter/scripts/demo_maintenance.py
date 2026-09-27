"""Instructor demo — OPTIMIZE / ZORDER and a SAFE VACUUM, with numbers.

Used by the Lab-4 solution walkthrough (`labs/solutions/LAB_04_SOLUTION.md`,
"5. erasure + maintenance")::

    python - < scripts/demo_maintenance.py

Note what this script does NOT do: it never disables
``spark.databricks.delta.retentionDurationCheck``. The retention number is a
governance decision (audit window, PDPL erasure SLA, storage cost), and the
DRY RUN comes first so the room sees what would be deleted before anything is.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from masar import config  # noqa: E402
from masar.spark import get_spark  # noqa: E402

TABLE = config.TABLES["silver.trips"].path
RETAIN_HOURS = 168  # 7 days: one audit week, inside the PDPL erasure SLA


def _detail(spark, tag: str) -> None:
    """Print numFiles / size / average file size for the table."""
    d = spark.sql(f"DESCRIBE DETAIL delta.`{TABLE}`").collect()[0]
    mb = d["sizeInBytes"] / 1048576
    kb = d["sizeInBytes"] / max(d["numFiles"], 1) / 1024
    print(f"  {tag:8s} numFiles={d['numFiles']:>4}  sizeMB={mb:7.1f}  avgFileKB={kb:8.1f}")


def main() -> None:
    """Measure, compact, measure again, then dry-run the vacuum."""
    spark = get_spark("lab4-demo-maintenance")

    print("[demo] before maintenance")
    _detail(spark, "before")

    print("\n[demo] OPTIMIZE ... ZORDER BY (city, pickup_ts)")
    metrics = spark.sql(f"OPTIMIZE delta.`{TABLE}` ZORDER BY (city, pickup_ts)").collect()[0]
    print(f"  metrics: {metrics['metrics']}")
    _detail(spark, "after")

    print(f"\n[demo] VACUUM DRY RUN, RETAIN {RETAIN_HOURS} HOURS — nothing is deleted")
    files = spark.sql(f"VACUUM delta.`{TABLE}` RETAIN {RETAIN_HOURS} HOURS DRY RUN").count()
    print(f"  {files} file(s) would be reclaimed once past the retention window")
    print(
        "\n[demo] The retention number is a decision, not a default:\n"
        f"       {RETAIN_HOURS}h = the audit window, inside the PDPL erasure SLA, "
        "and the storage bill we accept for it.\n"
        "       retentionDurationCheck stays ENABLED. RETAIN 0 HOURS is how you\n"
        "       destroy the history you are about to be asked for."
    )


if __name__ == "__main__":
    main()
