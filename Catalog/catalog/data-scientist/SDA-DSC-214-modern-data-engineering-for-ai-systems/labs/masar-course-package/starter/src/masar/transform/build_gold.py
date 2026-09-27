"""Gold marts and the general feature table. Pure, idempotent transforms.

Grain is a contract. It is DOCUMENTED in each docstring, ENFORCED by the write
strategy, and ASSERTED by :func:`_assert_grain` after every build. All three,
every time — a grain that lives only in a docstring is a grain that drifts.

Two write strategies, chosen by shape:

  * ``replaceWhere`` partition overwrite, when the grain nests inside a date
    partition. Rebuilding the last three days replaces exactly those days.
  * ``MERGE`` on the grain key, when it does not. Idempotent by construction.

Either way, running a task twice must produce identical row counts. Lab 7's
acceptance test is exactly that, and it is not optional.

CLI::

    python -m masar.transform.build_gold --mart all
"""

from __future__ import annotations

import argparse
import os

from masar import config
from masar.spark import get_spark

SILVER_TRIPS = config.TABLES["silver.trips"].path
SILVER_POSITIONS = config.TABLES["silver.vehicle_positions"].path
SILVER_DRIVERS = config.TABLES["silver.drivers"].path
GOLD = config.GOLD
LOOKBACK_DAYS = config.LOOKBACK_DAYS


def _maybe_fail(task_id: str) -> None:
    """Raise if ``MASAR_INJECT_FAILURE`` names this task (Lab 7 Task 5)."""
    if os.environ.get("MASAR_INJECT_FAILURE", "").strip() == task_id:
        raise RuntimeError(f"INJECTED FAILURE: simulated failure in {task_id}")


def _assert_grain(path: str, keys: list[str]) -> int:
    """A grain assertion is a data-contract test. Failing it fails the task.

    Raises:
        RuntimeError: when the table has more rows than distinct grain keys —
            which means the write strategy is not idempotent and a retry has
            been double-counting, probably for a while.

    Returns:
        Row count.
    """
    spark = get_spark("build-gold")
    df = spark.read.format("delta").load(path)
    total = df.count()
    distinct = df.select(*keys).distinct().count()
    if total != distinct:
        raise RuntimeError(
            f"GRAIN VIOLATION in {path}: {total:,} rows but only {distinct:,} distinct "
            f"{keys}. The write strategy is not idempotent."
        )
    print(f"[gold] {path.split('/')[-1]}: {total:,} rows, grain {keys} verified")
    return total


def build_zone_hourly_demand(**_: object) -> int:
    """``gold.zone_hourly_demand``.

    GRAIN : exactly one row per (city, pickup_zone_id, date, hour)
    SOURCE: ``silver.trips`` — never bronze; the gate is upstream of silver
    WRITE : ``replaceWhere`` over the last LOOKBACK_DAYS => idempotent rebuild
    """
    from pyspark.sql import functions as F

    spark = get_spark("build-gold")
    trips = spark.read.format("delta").load(SILVER_TRIPS)

    demand = (
        trips.filter(F.col("status") == "completed")
        .withColumn("date", F.to_date("pickup_ts"))
        .withColumn("hour", F.hour("pickup_ts"))
        .groupBy("city", "pickup_zone_id", "date", "hour")
        .agg(
            F.count("*").alias("trips"),
            F.countDistinct("driver_id").alias("active_drivers"),
            F.avg("fare_sar").alias("avg_fare_sar"),
            F.avg("duration_min").alias("avg_duration_min"),
            F.avg("distance_km").alias("avg_distance_km"),
            F.avg("surge_multiplier").alias("avg_surge"),
        )
        .withColumn("_built_at", F.current_timestamp())
    )

    _maybe_fail("gold_zone_hourly_demand")
    path = f"{GOLD}/zone_hourly_demand"

    # ── TODO(lab-7): make the rebuild idempotent ──────────────────────────
    #   What : write partitioned by `date` in overwrite mode with
    #          replaceWhere restricted to the LOOKBACK_DAYS window, and
    #          restrict `demand` to the same window before writing.
    #   Why  : the starter below overwrites the WHOLE table. That is
    #          idempotent (good) but rebuilds all history every night (bad,
    #          and O(all data) forever). `replaceWhere` replaces exactly the
    #          partitions you recomputed — the correct production shape.
    #          What you must NOT do is append: a retry then double-counts,
    #          the dashboard doubles, and surge fires at 2x on a Tuesday.
    #   Ref  : solutions/lab7_pipeline.py :: write_demand_replace_where
    demand.write.format("delta").mode("overwrite").partitionBy("date").option(
        "overwriteSchema", "true"
    ).save(path)
    # ── end TODO(lab-7) ───────────────────────────────────────────────────

    return _assert_grain(path, ["city", "pickup_zone_id", "date", "hour"])


def build_driver_daily(**_: object) -> int:
    """``gold.driver_daily``.

    GRAIN : exactly one row per (driver_id, date)
    SOURCE: ``silver.trips`` joined to ``silver.drivers``
    WRITE : MERGE on the grain key — the grain does not align cleanly to one
            partition column across the lookback, and MERGE is idempotent by
            construction (Lab 4).
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("build-gold")
    trips = spark.read.format("delta").load(SILVER_TRIPS)
    drivers = spark.read.format("delta").load(SILVER_DRIVERS)

    daily = (
        trips.withColumn("date", F.to_date("pickup_ts"))
        .groupBy("driver_id", "date")
        .agg(
            F.count("*").alias("trips"),
            F.sum(F.when(F.col("status") == "completed", 1).otherwise(0)).alias("trips_completed"),
            F.sum(F.when(F.col("status").startswith("cancelled"), 1).otherwise(0)).alias(
                "trips_cancelled"
            ),
            F.sum("fare_sar").alias("gross_earnings_sar"),
            F.sum("distance_km").alias("distance_km"),
            F.sum("duration_min").alias("on_trip_minutes"),
            F.avg("surge_multiplier").alias("avg_surge"),
        )
        .join(drivers.select("driver_id", "city", "rating", "status"), "driver_id", "left")
        .withColumn("completion_rate", F.round(F.col("trips_completed") / F.col("trips"), 4))
        .withColumn("_built_at", F.current_timestamp())
    )

    _maybe_fail("gold_driver_daily")
    path = f"{GOLD}/driver_daily"

    if not DeltaTable.isDeltaTable(spark, path):
        daily.write.format("delta").partitionBy("date").save(path)
    else:
        (
            DeltaTable.forPath(spark, path)
            .alias("t")
            .merge(daily.alias("s"), "t.driver_id = s.driver_id AND t.date = s.date")
            .whenMatchedUpdateAll()
            .whenNotMatchedInsertAll()
            .execute()
        )

    return _assert_grain(path, ["driver_id", "date"])


def build_trip_features(**_: object) -> int:
    """``gold.trip_features``.

    GRAIN : exactly one row per trip_id
    SOURCE: ``silver.trips``
    RULE  : POINT-IN-TIME CORRECT. Every window is strictly BEFORE pickup_ts.

    ``rangeBetween(-3600, -1)`` — the ``-1`` is not cosmetic.
    ``rangeBetween(-3600, 0)`` is inclusive of the current row's own ordering
    value, so on ties it admits every other trip that started in the same
    second: information from the future, in a feature, silently.
    """
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    from masar.transform.feature_spec import FeatureWindow

    spark = get_spark("build-gold")
    trips = spark.read.format("delta").load(SILVER_TRIPS)

    t = trips.filter(F.col("status") == "completed").withColumn(
        "pickup_epoch", F.col("pickup_ts").cast("long")
    )

    # ── TODO(lab-7): make both windows strictly prior ─────────────────────
    #   What : set the upper bound of BOTH windows to -1 and declare each one
    #          through FeatureWindow(...).assert_point_in_time() so the build
    #          FAILS if someone widens it later.
    #   Why  : the starter uses 0 as the upper bound. `rangeBetween` is
    #          inclusive, so 0 admits same-second trips — the model reads a
    #          few rows of the future, the offline metric rises, and live
    #          performance does not. Lab 8 quantifies the damage; this is
    #          where you prevent it.
    #   Ref  : solutions/lab7_pipeline.py :: point_in_time_windows
    zone_bounds = (-3600, 0)
    driver_bounds = (-86400, 0)
    # ── end TODO(lab-7) ───────────────────────────────────────────────────

    w_zone = (
        Window.partitionBy("city", "pickup_zone_id")
        .orderBy(F.col("pickup_epoch"))
        .rangeBetween(*zone_bounds)
    )
    w_driver = (
        Window.partitionBy("driver_id").orderBy(F.col("pickup_epoch")).rangeBetween(*driver_bounds)
    )

    feats = (
        t.withColumn("zone_demand_prev_hr", F.count("*").over(w_zone))
        .withColumn("zone_avg_fare_prev_hr", F.avg("fare_sar").over(w_zone))
        .withColumn("driver_trips_prev_24h", F.count("*").over(w_driver))
        .withColumn("start_hour", F.hour("pickup_ts"))
        .withColumn("day_of_week", F.dayofweek("pickup_ts"))
        .withColumn("is_night", (F.hour("pickup_ts") < 6) | (F.hour("pickup_ts") >= 22))
        .select(
            "trip_id",
            "city",
            "pickup_zone_id",
            "dropoff_zone_id",
            "driver_id",
            "vehicle_id",
            F.col("pickup_ts").alias("feature_ts"),
            "start_hour",
            "day_of_week",
            "is_night",
            "surge_multiplier",
            "zone_demand_prev_hr",
            "zone_avg_fare_prev_hr",
            "driver_trips_prev_24h",
        )
        .withColumn("_feature_version", F.lit("v1"))
        .withColumn("_built_at", F.current_timestamp())
    )

    _maybe_fail("gold_trip_features")
    path = f"{GOLD}/trip_features"
    feats.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(path)

    n = _assert_grain(path, ["trip_id"])
    _lint_point_in_time(
        {
            "zone_demand_prev_hr": FeatureWindow("zone_demand_prev_hr", *zone_bounds),
            "driver_trips_prev_24h": FeatureWindow("driver_trips_prev_24h", *driver_bounds),
        }
    )
    return n


def _lint_point_in_time(windows: dict) -> None:
    """Structural leakage lint: fail the build when a window is not strictly prior.

    A lint that runs at build time catches the bug before the model does. A
    review comment catches it only if the reviewer is having a good day.
    """
    from masar.transform.feature_spec import validate_windows

    problems = validate_windows(windows)
    for window in windows.values():
        print(f"[lint] {window.explain()}")
    if problems:
        raise RuntimeError("POINT-IN-TIME LINT FAILED:\n  " + "\n  ".join(problems))
    print("[lint] point-in-time: all declared windows are strictly prior")


MARTS = {
    "zone_hourly_demand": build_zone_hourly_demand,
    "driver_daily": build_driver_daily,
    "trip_features": build_trip_features,
}


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Build the gold marts")
    p.add_argument("--mart", default="all", choices=[*MARTS, "all"])
    a = p.parse_args()
    for name, fn in MARTS.items():
        if a.mart in (name, "all"):
            fn()


if __name__ == "__main__":
    main()
