"""Materialise a partitioned ``silver.trips`` for the Lab 2 scan benchmark.

Lab 2 happens on Day 1, before the dbt ELT of Lab 3 exists. The benchmark
still needs a typed, partitioned silver table to read — so this module builds
a minimal one straight from ``bronze.trips``.

It is deliberately NOT the real silver build (that is
``masar.transform.build_silver`` plus the dbt models). It exists so the cost
lesson does not have to wait for the modelling lesson.

CLI::

    python -m masar.econ.prepare_benchmark_input
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

BRONZE_TRIPS = config.TABLES["bronze.trips"].path
SILVER_TRIPS = config.TABLES["silver.trips"].path


def prepare(source: str = BRONZE_TRIPS, target: str = SILVER_TRIPS) -> int:
    """Type, conform and partition bronze trips into a benchmark-ready table.

    Args:
        source: bronze trips path.
        target: silver trips path.

    Returns:
        Row count written.

    Notes:
        Partitioned by ``city`` — five values, not 42,038. Partitioning by
        ``trip_id`` would create one directory per trip and turn every query
        into a metadata storm; that is the small-files trap Module 2 names and
        Module 4 makes you measure.
    """
    from pyspark.sql import functions as F

    spark = get_spark("prepare-benchmark-input")
    bronze = spark.read.format("delta").load(source)

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

    typed = (
        bronze.select(
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
        )
        .filter(F.col("trip_id").isNotNull())
        .dropDuplicates(["trip_id"])
    )

    n = typed.count()
    (
        typed.write.format("delta")
        .partitionBy("city")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(target)
    )
    print(f"[econ] wrote {n:,} rows to {target}, partitioned by city")
    return n


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Build a benchmark-ready silver.trips")
    p.add_argument("--source", default=BRONZE_TRIPS)
    p.add_argument("--target", default=SILVER_TRIPS)
    args = p.parse_args()
    prepare(args.source, args.target)


if __name__ == "__main__":
    main()
