"""Build ``silver.trips`` from bronze — the Spark path.

dbt owns the canonical silver build (``dbt/masar/models/marts/silver/``).
This module exists for two reasons and no others:

  * the DAG needs a callable that produces silver whether or not dbt is
    installed and configured, so no lab ever blocks on a dbt profile;
  * Lab 7's failure-injection drill needs a task that can be made to fail on
    demand, mid-MERGE, and then recover on a full re-run.

The logic mirrors ``stg_trips.sql`` + ``silver_trips.sql`` exactly. If you
change one, change the other — or, better, delete this one once your dbt
project is green and let the DAG shell out to ``dbt run``.

CLI::

    python -m masar.transform.build_silver
"""

from __future__ import annotations

import argparse
import os

from masar import config
from masar.spark import get_spark

BRONZE_TRIPS = config.TABLES["bronze.trips"].path
BRONZE_DRIVERS = config.TABLES["bronze.drivers"].path
SILVER_TRIPS = config.TABLES["silver.trips"].path
SILVER_DRIVERS = config.TABLES["silver.drivers"].path
LOOKBACK_DAYS = config.LOOKBACK_DAYS


def _maybe_fail(task_id: str) -> None:
    """Raise if ``MASAR_INJECT_FAILURE`` names this task (Lab 7 Task 5).

    The injected failure must land MID-TASK, after the reads and before the
    write, because the property being demonstrated is that a failed task
    leaves no half-written Delta table — and a failure at the very start
    would not test that at all.
    """
    if os.environ.get("MASAR_INJECT_FAILURE", "").strip() == task_id:
        raise RuntimeError(f"INJECTED FAILURE: simulated OOM during MERGE ({task_id})")


def build_silver_drivers(**_: object) -> int:
    """Conform ``bronze.drivers`` into ``silver.drivers``.

    ``hire_date`` arrives in three observed formats. Parse each one you have
    SEEN and coalesce; do not add a branch for a format you are guessing at,
    because an unused branch that later matches the wrong thing is worse than
    a null you can detect.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    spark = get_spark("build-silver")
    if not DeltaTable.isDeltaTable(spark, BRONZE_DRIVERS):
        raise RuntimeError(f"{BRONZE_DRIVERS} does not exist — run land_bronze first")

    bronze = spark.read.format("delta").load(BRONZE_DRIVERS)
    latest = Window.partitionBy("driver_id").orderBy(F.col("_ingested_at").desc())
    city = F.coalesce(
        *[F.when(F.col("city") == code, F.lit(name)) for code, name in config.CITY_CODES.items()],
        F.initcap(F.trim(F.col("city"))),
    )

    drivers = (
        bronze.withColumn("_rn", F.row_number().over(latest))
        .filter("_rn = 1")
        .select(
            F.col("driver_id").cast("string").alias("driver_id"),
            F.col("full_name_en").cast("string").alias("full_name_en"),
            city.alias("city"),
            F.coalesce(
                F.to_date("hire_date", "yyyy-MM-dd"),
                F.to_date("hire_date", "dd/MM/yyyy"),
                F.to_date("hire_date", "MMM d, yyyy"),
            ).alias("hire_date"),
            F.col("rating").cast("double").alias("rating"),
            F.lower(F.trim(F.col("status"))).alias("status"),
            F.col("national_id_hash").cast("string").alias("national_id_hash"),
            F.col("phone_hash").cast("string").alias("phone_hash"),
            F.col("_ingested_at"),
        )
        .filter(F.col("driver_id").isNotNull())
    )

    n = drivers.count()
    drivers.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(
        SILVER_DRIVERS
    )
    print(f"[silver] drivers: {n:,} rows")
    return n


def build_silver_trips(**_: object) -> int:
    """Conform, deduplicate and MERGE bronze trips into ``silver.trips``.

    Three properties, each earned by one specific decision:

      * **conformed** — city codes become city names, both timestamp formats
        are parsed, Asia/Riyadh wall-clock becomes UTC, once, here.
      * **deduplicated** — bronze is append-only, so the same ``trip_id`` can
        appear in several batches. Keep the LATEST landed version per key;
        ``DISTINCT`` would keep an arbitrary one, which on a correction batch
        means keeping the stale row half the time.
      * **idempotent** — MERGE on ``trip_id``. Re-running the whole DAG cannot
        double-count, which is what makes "just re-run it" a safe answer.

    Returns:
        Row count in ``silver.trips`` after the merge.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("build-silver")
    if not DeltaTable.isDeltaTable(spark, BRONZE_TRIPS):
        raise RuntimeError(f"{BRONZE_TRIPS} does not exist — run land_bronze first")

    bronze = spark.read.format("delta").load(BRONZE_TRIPS)

    pickup = F.to_utc_timestamp(
        F.coalesce(
            F.to_timestamp("pickup_ts", "yyyy-MM-dd HH:mm:ss"),
            F.to_timestamp("pickup_ts", "dd/MM/yyyy HH:mm"),
        ),
        "Asia/Riyadh",
    )
    dropoff = F.to_utc_timestamp(
        F.coalesce(
            F.to_timestamp("dropoff_ts", "yyyy-MM-dd HH:mm:ss"),
            F.to_timestamp("dropoff_ts", "dd/MM/yyyy HH:mm"),
        ),
        "Asia/Riyadh",
    )
    city = F.coalesce(
        *[F.when(F.col("city") == code, F.lit(name)) for code, name in config.CITY_CODES.items()],
        F.initcap(F.trim(F.col("city"))),
    )

    typed = bronze.select(
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
        F.col("duration_min").cast("double").alias("reported_duration_min"),
        F.col("fare_sar").cast("double").alias("fare_sar"),
        F.col("surge_multiplier").cast("double").alias("surge_multiplier"),
        F.lower(F.trim(F.col("payment_type"))).alias("payment_type"),
        F.lower(F.trim(F.col("status"))).alias("status"),
        F.nullif(F.trim(F.col("dropoff_geohash")), F.lit("")).alias("dropoff_geohash"),
        F.col("_batch_id"),
        F.col("_ingested_at"),
    ).filter(F.col("trip_id").isNotNull())

    # ── TODO(lab-3): keep the LATEST landed version per trip_id ───────────
    #   What : replace the naive `dropDuplicates(["trip_id"])` below with a
    #          row_number() window partitioned by trip_id, ordered by
    #          _ingested_at desc, _batch_id desc, keeping _rn = 1.
    #   Why  : bronze holds every batch, including the correction batch that
    #          fixed a fare. dropDuplicates keeps an ARBITRARY row, so half
    #          the corrections silently lose. The window keeps the newest.
    #          Run Lab 1 Task 3's double-landing first and you will see it.
    #   Hint : you will need `from pyspark.sql import Window` in this function.
    #   Ref  : solutions/lab3_elt.py :: dedupe_latest_per_key
    deduped = typed.dropDuplicates(["trip_id"])
    # ── end TODO(lab-3) ───────────────────────────────────────────────────

    silver = (
        deduped.withColumn("trip_date", F.to_date(F.from_utc_timestamp("pickup_ts", "Asia/Riyadh")))
        .withColumn(
            "duration_min",
            F.round((F.unix_timestamp("dropoff_ts") - F.unix_timestamp("pickup_ts")) / 60.0, 2),
        )
        .withColumn(
            "fare_per_km",
            F.round(F.col("fare_sar") / F.nullif(F.col("distance_km"), F.lit(0.0)), 3),
        )
        .withColumn("pickup_hour", F.hour(F.from_utc_timestamp("pickup_ts", "Asia/Riyadh")))
        .withColumn("day_of_week", F.dayofweek(F.from_utc_timestamp("pickup_ts", "Asia/Riyadh")))
        .withColumn(
            "is_night",
            F.when(F.hour(F.from_utc_timestamp("pickup_ts", "Asia/Riyadh")) < 6, 1).otherwise(0),
        )
        .withColumn("_loaded_at", F.current_timestamp())
        .filter(F.col("status") == "completed")  # silver = conformed, valid, completed
        .filter(F.col("dropoff_ts") > F.col("pickup_ts"))
        .filter(F.col("fare_sar") > 0)
        .filter(F.col("distance_km") > 0)
    )

    _maybe_fail("build_silver")

    if not DeltaTable.isDeltaTable(spark, SILVER_TRIPS):
        silver.write.format("delta").partitionBy("city").mode("overwrite").option(
            "overwriteSchema", "true"
        ).save(SILVER_TRIPS)
    else:
        (
            DeltaTable.forPath(spark, SILVER_TRIPS)
            .alias("t")
            .merge(silver.alias("s"), "t.trip_id = s.trip_id")
            .whenMatchedUpdateAll()
            .whenNotMatchedInsertAll()
            .execute()
        )

    total = spark.read.format("delta").load(SILVER_TRIPS).count()
    distinct = spark.read.format("delta").load(SILVER_TRIPS).select("trip_id").distinct().count()
    print(f"[silver] trips: merged, total {total:,} (unique trip_id {distinct:,})")
    if total != distinct:
        raise RuntimeError(
            f"GRAIN VIOLATION in silver.trips: {total:,} rows, {distinct:,} distinct trip_id"
        )
    return total


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Build silver from bronze (Spark path)")
    p.add_argument("--target", default="all", choices=["all", "trips", "drivers"])
    a = p.parse_args()
    if a.target in ("all", "drivers"):
        build_silver_drivers()
    if a.target in ("all", "trips"):
        build_silver_trips()


if __name__ == "__main__":
    main()
