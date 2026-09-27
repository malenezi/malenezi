"""``bronze.gps_events`` -> ``silver.vehicle_positions`` (streaming).

The silver contract for positions:

  * exactly one row per ``event_id``   (watermark-bounded deduplication)
  * event-time semantics, 5 min lateness tolerance
  * ``speed_kmh`` ALWAYS in km/h       (producer 2.5.0 emits m/s)
  * ``accuracy_m <= 50``               (a worse fix is noise, not a position)
  * inside KSA bounds                  (a lat/lon in the Atlantic is a bug)

The third bullet is the whole Module 6 incident in one line of code. Producer
``2.4.0`` emits ``speed_kmh`` in km/h. Producer ``2.5.0`` emits the SAME KEY,
the SAME TYPE, and metres per second. Schema validation passes. Range checks
pass. Only a per-version distribution comparison sees it — and once seen, the
conversion belongs HERE, at the silver boundary, where the unit is normalised
once for every consumer.

CLI::

    python -m masar.stream.build_vehicle_positions
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

BRONZE_PATH = config.TABLES["bronze.gps_events"].path
SILVER_PATH = config.TABLES["silver.vehicle_positions"].path
CHECKPOINT = f"{config.CHECKPOINTS}/vehicle_positions_silver"  # its OWN checkpoint
WATERMARK = "5 minutes"
MAX_ACCURACY_M = 50.0

#: Saudi Arabia's bounding box. Anything outside is a fix, not a position.
KSA_LAT = (16.0, 33.0)
KSA_LON = (34.0, 56.0)

#: Producer versions whose `speed_kmh` field is actually metres per second.
MPS_PRODUCER_VERSIONS = ("2.5.0",)
MPS_TO_KMH = 3.6


def conform(bronze):
    """Flatten the payload, normalise units, and drop unusable fixes.

    Args:
        bronze: a streaming or batch DataFrame over ``bronze.gps_events``.

    Returns:
        A conformed DataFrame at the silver shape (not yet deduplicated).
    """
    from pyspark.sql import functions as F

    flat = bronze.select(
        "event_id",
        "vehicle_id",
        "driver_id",
        "trip_id",
        F.col("ts").alias("event_ts"),
        F.col("payload.lat").alias("lat"),
        F.col("payload.lon").alias("lon"),
        F.col("payload.speed_kmh").alias("_speed_raw"),
        F.col("payload.heading_deg").alias("heading_deg"),
        F.col("payload.accuracy_m").alias("accuracy_m"),
        "producer_version",
        "_kafka_ts",
        "_ingested_at",
        "_batch_id",
    )

    # ── TODO(lab-6): normalise the speed unit at the silver boundary ──────
    #   What : produce `speed_kmh` in km/h for EVERY producer version — the
    #          versions in MPS_PRODUCER_VERSIONS ship m/s and need x3.6.
    #   Why  : the starter below passes `_speed_raw` through unchanged, which
    #          is what the platform did before the incident was found. Leave
    #          it and every 2.5.0 vehicle looks like it is crawling; the ETA
    #          model learns a fleet that never speeds up, and no schema or
    #          range check ever complains.
    #   Ref  : solutions/lab6_quality.py :: normalise_speed
    conformed = flat.withColumn("speed_kmh", F.col("_speed_raw"))
    # ── end TODO(lab-6) ───────────────────────────────────────────────────

    return (
        conformed.drop("_speed_raw")
        .withColumn("event_lag_s", F.unix_timestamp("_kafka_ts") - F.unix_timestamp("event_ts"))
        .withColumn("is_late", F.col("event_lag_s") > F.lit(120))
        .withColumn("event_date", F.to_date("event_ts"))
        .filter(F.col("accuracy_m") <= F.lit(MAX_ACCURACY_M))
        .filter(F.col("lat").between(*KSA_LAT) & F.col("lon").between(*KSA_LON))
    )


def run(trigger_seconds: int = 30, once: bool = False) -> None:
    """Stream bronze positions into the conformed silver table.

    ``dropDuplicatesWithinWatermark`` keeps dedup state only for the lateness
    window instead of remembering every ``event_id`` ever seen. Unbounded
    dedup state is the classic way a streaming job runs fine for a week and
    then dies of an OOM on a Sunday night.
    """
    spark = get_spark("masar-vehicle-positions")
    bronze = spark.readStream.format("delta").load(BRONZE_PATH)

    deduped = (
        conform(bronze)
        .withWatermark("event_ts", WATERMARK)
        .dropDuplicatesWithinWatermark(["event_id"])
    )

    writer = (
        deduped.writeStream.format("delta")
        .queryName("vehicle_positions_silver")
        .outputMode("append")
        .partitionBy("event_date")
        .option("checkpointLocation", CHECKPOINT)
    )
    trigger = {"availableNow": True} if once else {"processingTime": f"{trigger_seconds} seconds"}
    writer.trigger(**trigger).start(SILVER_PATH).awaitTermination()


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="bronze.gps_events -> silver.vehicle_positions")
    p.add_argument("--trigger-seconds", type=int, default=30)
    p.add_argument("--once", action="store_true", help="drain available data then stop")
    a = p.parse_args()
    run(a.trigger_seconds, a.once)


if __name__ == "__main__":
    main()
