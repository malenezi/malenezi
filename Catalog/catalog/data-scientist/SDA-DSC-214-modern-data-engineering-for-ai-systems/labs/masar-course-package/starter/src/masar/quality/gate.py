"""The quality gate at the bronze -> silver promotion boundary.

Three outcomes, decided by each expectation's ``meta.response_class``:

    FAIL_FAST failed   raise. Nothing is promoted, the batch is blocked, the
                       DAG task fails and every downstream task is skipped.
    QUARANTINE failed  split. Bad rows go to ``silver.trips_quarantine`` WITH
                       THEIR REASON, good rows are promoted. Alert either way.
    everything passed  promote. Alert nothing.

The gate never promotes a row it could not justify, and never blocks a batch
for a fault it could isolate. Getting that distinction right is the difference
between a control people trust and a control people disable.

CLI::

    python -m masar.quality.gate --batch data/fixtures/dirty_batch/trips_2026-06-05_dirty.csv
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from masar import config
from masar.quality.rules import FAIL_FAST
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import Column, DataFrame

SILVER = config.TABLES["silver.trips"].path
QUARANTINE_PATH = config.TABLES["silver.trips_quarantine"].path


class GateBlocked(RuntimeError):
    """Raised on FAIL_FAST. The DAG task fails; nothing is promoted."""


@dataclass
class GateResult:
    """What the gate did, in numbers a runbook can be written against."""

    promoted: int
    quarantined: int
    blocked: bool
    reasons: dict[str, int] = field(default_factory=dict)
    batch_id: str = ""

    def render(self) -> str:
        """One line for the DAG log."""
        if self.blocked:
            return f"[gate] batch {self.batch_id}: BLOCKED {self.reasons}"
        return (
            f"[gate] batch {self.batch_id}: promoted {self.promoted:,}, "
            f"quarantined {self.quarantined:,} {self.reasons}"
        )


def alert(msg: str) -> None:
    """Emit a data alert. Wire this to Slack/PagerDuty in production.

    It prints. That is deliberate: the interesting engineering question is
    WHICH events deserve an alert, not which transport carries it, and a
    printed alert that fires on the right condition beats an integrated one
    that fires on everything.
    """
    print(f"[DATA-ALERT] {msg}", flush=True)


def failed_by_class(gx_result: Any, response_class: str) -> list[str]:
    """Expectation ids that FAILED and carry ``response_class`` in their meta.

    Args:
        gx_result: a Great Expectations validation result (or any mapping with
            the same ``results`` shape, which is what the tests use).
        response_class: ``FAIL_FAST`` or ``QUARANTINE``.

    Returns:
        ``["column:expectation_type", ...]`` for every matching failure.
    """
    if gx_result is None:
        return []
    results = gx_result["results"] if not hasattr(gx_result, "results") else gx_result.results
    failed = []
    for r in results:
        r = dict(r)
        if r.get("success"):
            continue
        cfg = dict(r.get("expectation_config", {}))
        if dict(cfg.get("meta", {})).get("response_class") != response_class:
            continue
        column = dict(cfg.get("kwargs", {})).get("column", "<table>")
        failed.append(f"{column}:{cfg.get('expectation_type')}")
    return failed


def quarantine_predicates() -> dict[str, Column]:
    """Compile :data:`masar.quality.rules.QUARANTINE_RULES` into Spark columns.

    GX tells you WHICH RULE failed on a batch; Spark tells you WHICH ROWS
    failed it. Both are needed to quarantine with a reason, so the rule name
    is shared between them — one catalogue, two evaluators, no drift.
    """
    from pyspark.sql import functions as F

    def _isin(column: str, values: list[str]) -> Column:
        return F.col(column).isNotNull() & ~F.col(column).isin(*values)

    return {
        "fare_non_positive": F.col("fare_sar") <= 0,
        "fare_implausible": F.col("fare_sar") > 5000,
        "duration_non_positive": F.col("duration_min") <= 0,
        "duration_implausible": F.col("duration_min") > 600,
        "distance_non_positive": F.col("distance_km") <= 0,
        "distance_implausible": F.col("distance_km") > 400,
        "city_not_in_ksa_set": _isin("city", config.KSA_CITIES),
        "status_unknown": _isin("status", config.TRIP_STATUS),
        "payment_type_unknown": _isin("payment_type", config.PAYMENT_TYPES),
        "surge_out_of_range": ~F.col("surge_multiplier").between(1.0, 5.0),
        "dropoff_before_pickup": F.col("dropoff_ts") <= F.col("pickup_ts"),
    }


def gate_and_promote(
    candidate: DataFrame,
    gx_result: Any = None,
    batch_id: str = "adhoc",
    target: str = SILVER,
    quarantine_path: str = QUARANTINE_PATH,
) -> GateResult:
    """Run the gate on a candidate batch and promote what deserves promoting.

    Args:
        candidate: the batch, already conformed to the silver schema.
        gx_result: a GX validation result. ``None`` skips the expectation-level
            check and relies on the row-level predicates alone — useful in
            Lab 4, before GX exists.
        batch_id: written into every quarantined row so the evidence trail
            survives.
        target: silver table path.
        quarantine_path: quarantine table path.

    Raises:
        GateBlocked: when any FAIL_FAST expectation failed, or the batch has
            duplicate/null business keys.

    Returns:
        A :class:`GateResult`.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("quality-gate")

    # ---- 1. FAIL FAST on integrity -------------------------------------
    integrity_failures = failed_by_class(gx_result, FAIL_FAST)
    null_keys = candidate.filter(F.col("trip_id").isNull()).count()
    dupe_keys = candidate.groupBy("trip_id").count().filter("count > 1").count()
    if null_keys:
        integrity_failures.append(f"trip_id:null_count={null_keys}")
    if dupe_keys:
        integrity_failures.append(f"trip_id:duplicate_groups={dupe_keys}")

    if integrity_failures:
        alert(f"FAIL-FAST: batch {batch_id} blocked. Integrity failed: {integrity_failures}")
        raise GateBlocked(
            f"FAIL-FAST: integrity expectations failed {integrity_failures}; "
            f"batch {batch_id} blocked, nothing promoted"
        )

    # ---- 2. QUARANTINE partial value failures ---------------------------
    # ── TODO(lab-6): tag each row with EVERY rule it violates ─────────────
    #   What : build an array column `_quarantine_reasons` holding the name of
    #          each predicate in `quarantine_predicates()` that the row trips.
    #   Why  : a quarantine table without reasons is a landfill. "120 rows
    #          rejected" starts an investigation; "120 rows: fare_non_positive"
    #          ends one. Collect ALL reasons, not the first — a row can be
    #          wrong in more than one way and you want to know that.
    #   Ref  : solutions/lab6_quality.py :: reason_array
    reason = F.array_remove(
        F.array(
            *[
                F.when(predicate, F.lit(name)).otherwise(F.lit(None))
                for name, predicate in quarantine_predicates().items()
            ]
        ),
        None,
    )
    # ── end TODO(lab-6) ───────────────────────────────────────────────────

    tagged = candidate.withColumn("_quarantine_reasons", reason)
    bad = tagged.filter(F.size("_quarantine_reasons") > 0).cache()
    good = tagged.filter(F.size("_quarantine_reasons") == 0).drop("_quarantine_reasons").cache()
    n_bad, n_good = bad.count(), good.count()

    detail: dict[str, int] = {}
    if n_bad:
        (
            bad.withColumn("_quarantined_at", F.current_timestamp())
            .withColumn("_batch_id", F.lit(batch_id))
            .write.format("delta")
            .mode("append")
            .option("mergeSchema", "true")
            .save(quarantine_path)
        )
        detail = {
            row["r"]: row["count"]
            for row in bad.select(F.explode("_quarantine_reasons").alias("r"))
            .groupBy("r")
            .count()
            .collect()
        }
        alert(f"QUARANTINED {n_bad:,} rows to silver.trips_quarantine -> {detail}")

    # ---- 3. Promote the good rows, idempotently (MERGE from Lab 4) ------
    if n_good:
        if not DeltaTable.isDeltaTable(spark, target):
            good.write.format("delta").partitionBy("city").save(target)
        else:
            (
                DeltaTable.forPath(spark, target)
                .alias("t")
                .merge(good.alias("s"), "t.trip_id = s.trip_id")
                .whenMatchedUpdateAll()
                .whenNotMatchedInsertAll()
                .execute()
            )

    result = GateResult(
        promoted=n_good, quarantined=n_bad, blocked=False, reasons=detail, batch_id=batch_id
    )
    print(result.render())
    bad.unpersist()
    good.unpersist()
    return result


def load_candidate(path: str) -> DataFrame:
    """Read a candidate batch from CSV or Parquet and conform it to silver.

    The fixtures ship as CSV (and the labs also refer to Parquet copies), so
    the loader accepts both and applies the same typing the ELT applies. It is
    a thin reimplementation of ``stg_trips.sql`` — deliberately, so Lab 6 can
    run without Lab 3's dbt project being green.
    """
    from pyspark.sql import functions as F

    spark = get_spark("quality-gate")
    if path.endswith(".parquet") or path.endswith(".parquet/"):
        raw = spark.read.parquet(path)
    else:
        raw = spark.read.option("header", True).option("inferSchema", False).csv(path)

    pickup = F.coalesce(
        F.to_timestamp("pickup_ts", "yyyy-MM-dd HH:mm:ss"),
        F.to_timestamp("pickup_ts", "dd/MM/yyyy HH:mm"),
    )
    dropoff = F.coalesce(
        F.to_timestamp("dropoff_ts", "yyyy-MM-dd HH:mm:ss"),
        F.to_timestamp("dropoff_ts", "dd/MM/yyyy HH:mm"),
    )
    city = F.coalesce(
        *[F.when(F.col("city") == code, F.lit(name)) for code, name in config.CITY_CODES.items()],
        F.initcap(F.trim(F.col("city"))),
    )
    return raw.select(
        F.col("trip_id").cast("string").alias("trip_id"),
        F.col("rider_id").cast("string").alias("rider_id"),
        F.col("driver_id").cast("string").alias("driver_id"),
        F.col("vehicle_id").cast("string").alias("vehicle_id"),
        city.alias("city"),
        F.col("pickup_zone_id").cast("string").alias("pickup_zone_id"),
        F.col("dropoff_zone_id").cast("string").alias("dropoff_zone_id"),
        pickup.alias("pickup_ts"),
        dropoff.alias("dropoff_ts"),
        F.col("distance_km").cast("double").alias("distance_km"),
        F.round((F.unix_timestamp(dropoff) - F.unix_timestamp(pickup)) / 60.0, 2).alias(
            "duration_min"
        ),
        F.col("fare_sar").cast("double").alias("fare_sar"),
        F.col("surge_multiplier").cast("double").alias("surge_multiplier"),
        F.lower(F.trim(F.col("payment_type"))).alias("payment_type"),
        F.lower(F.trim(F.col("status"))).alias("status"),
        F.nullif(F.trim(F.col("dropoff_geohash")), F.lit("")).alias("dropoff_geohash"),
    )


def gate_and_promote_task(**context: Any) -> dict:
    """Airflow/runner task wrapper: gate the current bronze batch into silver.

    Reads the un-promoted slice of ``bronze.trips`` (everything landed since
    silver's high-water mark), runs the gate, and returns the result as a dict
    so it can be pushed to XCom.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("quality-gate")
    bronze_path = config.TABLES["bronze.trips"].path
    if not DeltaTable.isDeltaTable(spark, bronze_path):
        raise RuntimeError(f"{bronze_path} does not exist — run land_bronze first")

    batch_id = str(context.get("run_id") or context.get("ds") or "adhoc")
    bronze = spark.read.format("delta").load(bronze_path)

    # Bronze is append-only, so the same trip_id can appear in several
    # batches. Keep the LATEST landed version per key before gating.
    from pyspark.sql import Window

    latest = Window.partitionBy("trip_id").orderBy(
        F.col("_ingested_at").desc(), F.col("_batch_id").desc()
    )
    deduped = bronze.withColumn("_rn", F.row_number().over(latest)).filter("_rn = 1").drop("_rn")

    candidate = _conform(deduped)
    result = gate_and_promote(candidate, gx_result=None, batch_id=batch_id)
    return {
        "promoted": result.promoted,
        "quarantined": result.quarantined,
        "reasons": result.reasons,
    }


def _conform(bronze_df: DataFrame) -> DataFrame:
    """Type and conform a bronze frame to the silver column set."""
    from pyspark.sql import functions as F

    pickup = F.coalesce(
        F.to_timestamp("pickup_ts", "yyyy-MM-dd HH:mm:ss"),
        F.to_timestamp("pickup_ts", "dd/MM/yyyy HH:mm"),
    )
    dropoff = F.coalesce(
        F.to_timestamp("dropoff_ts", "yyyy-MM-dd HH:mm:ss"),
        F.to_timestamp("dropoff_ts", "dd/MM/yyyy HH:mm"),
    )
    city = F.coalesce(
        *[F.when(F.col("city") == code, F.lit(name)) for code, name in config.CITY_CODES.items()],
        F.initcap(F.trim(F.col("city"))),
    )
    return bronze_df.select(
        F.col("trip_id").cast("string").alias("trip_id"),
        F.col("rider_id").cast("string").alias("rider_id"),
        F.col("driver_id").cast("string").alias("driver_id"),
        F.col("vehicle_id").cast("string").alias("vehicle_id"),
        city.alias("city"),
        F.col("pickup_zone_id").cast("string").alias("pickup_zone_id"),
        F.col("dropoff_zone_id").cast("string").alias("dropoff_zone_id"),
        pickup.alias("pickup_ts"),
        dropoff.alias("dropoff_ts"),
        F.col("distance_km").cast("double").alias("distance_km"),
        F.round((F.unix_timestamp(dropoff) - F.unix_timestamp(pickup)) / 60.0, 2).alias(
            "duration_min"
        ),
        F.col("fare_sar").cast("double").alias("fare_sar"),
        F.col("surge_multiplier").cast("double").alias("surge_multiplier"),
        F.lower(F.trim(F.col("payment_type"))).alias("payment_type"),
        F.lower(F.trim(F.col("status"))).alias("status"),
        F.nullif(F.trim(F.col("dropoff_geohash")), F.lit("")).alias("dropoff_geohash"),
        F.col("_batch_id"),
        F.col("_ingested_at"),
    ).filter(F.col("status") == "completed")


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Run the bronze->silver quality gate")
    p.add_argument("--batch", help="candidate batch file (CSV or Parquet)")
    p.add_argument("--batch-id", default="adhoc")
    p.add_argument("--from-bronze", action="store_true", help="gate the current bronze.trips")
    a = p.parse_args()

    if a.from_bronze or not a.batch:
        gate_and_promote_task(run_id=a.batch_id)
        return
    gate_and_promote(load_candidate(a.batch), gx_result=None, batch_id=a.batch_id)


if __name__ == "__main__":
    main()
