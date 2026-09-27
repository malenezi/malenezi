"""Live zone demand: trips started per event-time window, per city and zone.

Two ideas carry this file, and both are Module 5's core:

  * **Event time, not processing time.** A ping that arrives at 08:07 about
    something that happened at 08:03 belongs in the 08:00-08:05 window. Group
    by arrival time and your demand curve is a picture of your network, not of
    your city.
  * **Watermark.** ``withWatermark("event_ts", "3 minutes")`` says: wait up to
    three minutes for stragglers, then finalise the window and free its state.
    Without it, state grows forever; with it too short, late events are simply
    dropped. That trade-off is the design decision, and it is yours to justify.

CLI::

    python -m masar.stream.zone_demand
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

SOURCE = config.TABLES["silver.vehicle_positions"].path
OUTPUT = f"{config.GOLD}/_streaming/zone_demand_5m"
CHECKPOINT = f"{config.CHECKPOINTS}/zone_demand"
WINDOW = "5 minutes"
WATERMARK = "3 minutes"


def run(trigger_seconds: int = 30, once: bool = False) -> None:
    """Aggregate positions into 5-minute event-time demand windows."""
    from pyspark.sql import functions as F

    spark = get_spark("masar-zone-demand")
    events = spark.readStream.format("delta").load(SOURCE)

    # ── TODO(lab-5): windowed demand on EVENT time ────────────────────────
    #   What : declare a 3-minute watermark on `event_ts`, then group by a
    #          5-minute event-time window plus trip/vehicle attributes.
    #   Why  : `F.window("event_ts", ...)` places each event in the window it
    #          BELONGS to. Using `current_timestamp()` or `_kafka_ts` instead
    #          would place it in the window it HAPPENED TO ARRIVE in — which
    #          is a measure of your consumer lag, dressed up as demand.
    #   Ref  : solutions/lab5_stream.py :: zone_demand
    demand = (
        events.withWatermark("event_ts", WATERMARK)
        .groupBy(F.window("event_ts", WINDOW).alias("w"), F.col("vehicle_id"))
        .agg(
            F.countDistinct("trip_id").alias("trips_active"),
            F.avg("speed_kmh").alias("avg_speed_kmh"),
            F.count("*").alias("pings"),
        )
    )
    # ── end TODO(lab-5) ───────────────────────────────────────────────────

    shaped = demand.select(
        F.col("w.start").alias("window_start"),
        F.col("w.end").alias("window_end"),
        "vehicle_id",
        "trips_active",
        "avg_speed_kmh",
        "pings",
    )

    writer = (
        shaped.writeStream.format("delta")
        .queryName("zone_demand_5m")
        .outputMode("append")  # append is safe BECAUSE the watermark finalises windows
        .option("checkpointLocation", CHECKPOINT)
    )
    trigger = {"availableNow": True} if once else {"processingTime": f"{trigger_seconds} seconds"}
    writer.trigger(**trigger).start(OUTPUT).awaitTermination()


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Event-time windowed zone demand")
    p.add_argument("--trigger-seconds", type=int, default=30)
    p.add_argument("--once", action="store_true")
    a = p.parse_args()
    run(a.trigger_seconds, a.once)


if __name__ == "__main__":
    main()
