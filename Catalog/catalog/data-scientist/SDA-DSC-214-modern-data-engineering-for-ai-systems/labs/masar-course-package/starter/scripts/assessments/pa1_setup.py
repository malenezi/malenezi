"""PA-1 setup: build a Delta table with (a) destroyed time travel and
(b) a non-idempotent corrections job.

================================ WARNING ==================================
THIS SCRIPT BUILDS A DELIBERATELY BROKEN ASSESSMENT ARTEFACT.
It produces the starting state for `labs/assessments/PA-1_Delta_Recovery.md`:
a table with ten duplicate rows and no readable history. Every pattern in it
is one the course teaches you to reject. DO NOT USE IT AS A REFERENCE.
===========================================================================

Run:  python -m scripts.assessments.pa1_setup
Idempotent: the sandbox is deleted and rebuilt on every run.

Takes ~90 seconds and produces the broken starting state for every
participant. Distribute the resulting directory, or have each participant run
`make pa1-setup`.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from masar import config  # noqa: E402

SOURCE = config.TABLES["silver.trips"].path  # the cohort's real silver table
SANDBOX = f"{config.LAKEHOUSE_ROOT}/_assessments/pa1/trips"
CORRECT = f"{config.FIXTURES_ROOT}/corrections/trips_corrections_2026-06-03.csv"


def main() -> None:
    """Wipe the PA-1 sandbox and rebuild it in its broken state."""
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    from masar.spark import get_spark

    spark = get_spark("pa1-setup")
    shutil.rmtree(Path(SANDBOX).parent, ignore_errors=True)

    # ---- v0: a clean copy of silver.trips (schema and grain identical) -----
    src = spark.read.format("delta").load(SOURCE)
    src.write.format("delta").mode("overwrite").save(SANDBOX)
    spark.sql(f"ALTER TABLE delta.`{SANDBOX}` ADD CONSTRAINT positive_fare CHECK (fare_sar > 0)")

    tgt = DeltaTable.forPath(spark, SANDBOX)
    schema = spark.read.format("delta").load(SANDBOX).schema
    corr = spark.read.option("header", True).schema(schema).csv(CORRECT)

    # ---- v1: a legitimate, idempotent correction (so history is meaningful)
    (
        tgt.alias("t")
        .merge(corr.alias("s"), "t.trip_id = s.trip_id")
        .whenMatchedUpdateAll()
        .execute()
    )

    # ---- v2, v3: the NON-IDEMPOTENT job, run twice ------------------------
    # The match condition includes a per-run column, so nothing ever matches
    # and every run falls through to whenNotMatchedInsertAll.
    for _ in range(2):
        stamped = corr.withColumn("_ingested_at", F.current_timestamp())
        (
            tgt.alias("t")
            .merge(
                stamped.alias("s"),
                "t.trip_id = s.trip_id AND t._ingested_at = s._ingested_at",
            )
            .whenMatchedUpdateAll()
            .whenNotMatchedInsertAll()
            .execute()
        )

    # ---- v4: time travel destroyed ----------------------------------------
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
    spark.sql(f"VACUUM delta.`{SANDBOX}` RETAIN 0 HOURS")
    spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "true")

    n = spark.read.format("delta").load(SANDBOX).count()
    d = spark.read.format("delta").load(SANDBOX).select("trip_id").distinct().count()
    print(f"[pa1-setup] rows={n:,} distinct trip_id={d:,} (expect {n - d:,} duplicate rows)")
    print(f"[pa1-setup] sandbox ready at {SANDBOX}")
    print("[pa1-setup] broken job at src/masar/delta/apply_corrections_pa1.py")


if __name__ == "__main__":
    main()
