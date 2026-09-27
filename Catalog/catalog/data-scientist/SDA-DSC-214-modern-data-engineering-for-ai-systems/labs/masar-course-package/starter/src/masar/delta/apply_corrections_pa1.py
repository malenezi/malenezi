"""PA-1 artefact — apply the daily corrections file to the PA-1 trips table.

================================ WARNING ==================================
THIS FILE IS A DELIBERATELY BROKEN ASSESSMENT ARTEFACT.
It is the artefact under test in `labs/assessments/PA-1_Delta_Recovery.md`
and it ships with its defects intact, on purpose. DO NOT USE IT AS A
REFERENCE for how to write a Delta MERGE or a maintenance job — every
pattern in it is one the course teaches you to reject. The correct patterns
live in `masar.delta.merge_ops` and `masar.delta.maintain`.
===========================================================================

Three faults are present (PA-1 marking scheme, section 1):

  1. Non-idempotent MERGE. The match condition includes ``_ingested_at``,
     which is stamped with ``current_timestamp()`` on the SOURCE at read
     time, so it can never equal the value a previous run wrote to the
     TARGET. ``whenMatched`` therefore never fires and every run falls
     through to ``whenNotMatchedInsertAll`` — appending a fresh copy of all
     five corrections each night.
  2. ``VACUUM ... RETAIN 0 HOURS`` with ``retentionDurationCheck`` disabled
     in :func:`maintain`, which destroys time travel and can delete files
     out from under a concurrent reader.
  3. No source-side duplicate-key guard, so a corrections file containing a
     repeated ``trip_id`` would make ``whenMatchedUpdateAll`` ambiguous.

Participants repair this file in place on branch ``pa1/<name>``.

Sandbox only: it reads and writes ``./lakehouse/_assessments/pa1/trips``,
never the cohort's real ``silver.trips``.

CLI::

    python -m masar.delta.apply_corrections_pa1 \
        --corrections data/fixtures/corrections/trips_corrections_2026-06-03.csv
    python -m masar.delta.apply_corrections_pa1 --maintain

PySpark and delta-spark are imported inside the functions so that
``import masar.delta.apply_corrections_pa1`` works on a machine with no
Spark installed (``scripts/doctor.py`` and the unit tests depend on that).
"""

from __future__ import annotations

import argparse

from masar import config

TABLE = f"{config.LAKEHOUSE_ROOT}/_assessments/pa1/trips"

#: The corrections fixture PA-1 hands the participant (5 rows).
DEFAULT_CORRECTIONS = f"{config.FIXTURES_ROOT}/corrections/trips_corrections_2026-06-03.csv"


def apply_corrections(path: str = DEFAULT_CORRECTIONS) -> None:
    """Apply the daily corrections file to the PA-1 trips table.

    DEFECT 1 (non-idempotent MERGE): ``_ingested_at`` is stamped on the source
    and then used in the match condition. Nothing ever matches; every run
    inserts. DEFECT 3 (no duplicate-key guard) is the missing ``dropDuplicates``
    / count assertion on ``corr`` before the merge.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    from masar.spark import get_spark

    spark = get_spark("pa1-corrections")
    schema = spark.read.format("delta").load(TABLE).schema
    corr = (
        spark.read.option("header", True)
        .schema(schema)
        .csv(path)
        .withColumn("_ingested_at", F.current_timestamp())
    )

    target = DeltaTable.forPath(spark, TABLE)
    (
        target.alias("t")
        .merge(
            corr.alias("s"),
            "t.trip_id = s.trip_id AND t._ingested_at = s._ingested_at",
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )
    print("corrections applied")


def maintain() -> None:
    """Nightly maintenance.

    DEFECT 2: the retention safety check is disabled and the table is
    vacuumed with zero retention, so every file not referenced by the current
    snapshot is deleted immediately — time travel gone, concurrent readers at
    risk. There is no ``DRY RUN`` first, and no stated retention rationale.
    """
    from masar.spark import get_spark

    spark = get_spark("pa1-maintenance")
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
    spark.sql(f"OPTIMIZE delta.`{TABLE}` ZORDER BY (city, pickup_ts)")
    spark.sql(f"VACUUM delta.`{TABLE}` RETAIN 0 HOURS")
    print("maintenance done")


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="PA-1 corrections job (SHIPPED BROKEN)")
    p.add_argument("--corrections", nargs="?", const=DEFAULT_CORRECTIONS)
    p.add_argument("--maintain", action="store_true")
    a = p.parse_args()
    if a.corrections:
        apply_corrections(a.corrections)
    if a.maintain:
        maintain()
    if not a.corrections and not a.maintain:
        p.print_help()


if __name__ == "__main__":
    main()
