"""Two independent consumers of ``silver.vehicle_positions``.

Neither knows the other exists. That is the point of an event backbone: adding
the ops console did not require changing the feature pipeline, and a bug in
the ops console cannot corrupt the feature pipeline.

They also disagree about time, correctly:

  * the ETA feature input aggregates on EVENT time — a feature must describe
    the world as it was;
  * the operations alerter uses PROCESSING time — an alert is about NOW. A
    speeding alert delivered in the right event-time window and forty minutes
    late is a report, not an alert.

CLI::

    python -m masar.stream.fanout --consumer eta
    python -m masar.stream.fanout --consumer alerts
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

SILVER_PATH = config.TABLES["silver.vehicle_positions"].path
ETA_INPUT_PATH = f"{config.GOLD}/_streaming/eta_feature_input"

SPEEDING_KMH = 140.0
DEGRADED_ACCURACY_M = 35.0
STALE_TELEMETRY_S = 600


def eta_feature_input(trigger_seconds: int = 60, once: bool = False) -> None:
    """Rolling inputs for ``gold.eta_features``, on event time.

    Produces the two rolling columns the ETA feature table consumes:
    ``rolling_zone_demand_15m`` and ``rolling_avg_speed_10m``. Sliding windows
    (15 min, every 5 min) give the feature table a value at 5-minute
    resolution without recomputing the whole history each time.
    """
    from pyspark.sql import functions as F

    spark = get_spark("masar-eta-feature-input")
    positions = spark.readStream.format("delta").load(SILVER_PATH)

    rolling = (
        positions.withWatermark("event_ts", "5 minutes")
        .groupBy(F.window("event_ts", "15 minutes", "5 minutes").alias("w"), F.col("trip_id"))
        .agg(
            F.countDistinct("vehicle_id").alias("rolling_zone_demand_15m"),
            F.avg("speed_kmh").alias("rolling_avg_speed_10m"),
        )
        .select(
            F.col("w.start").alias("window_start"),
            F.col("w.end").alias("window_end"),
            "trip_id",
            "rolling_zone_demand_15m",
            "rolling_avg_speed_10m",
        )
    )

    writer = (
        rolling.writeStream.format("delta")
        .queryName("eta_feature_input")
        .outputMode("append")
        .option("checkpointLocation", f"{config.CHECKPOINTS}/eta_feature_input")
    )
    trigger = {"availableNow": True} if once else {"processingTime": f"{trigger_seconds} seconds"}
    writer.trigger(**trigger).start(ETA_INPUT_PATH).awaitTermination()


def operations_alerts(trigger_seconds: int = 30, once: bool = False) -> None:
    """Ops console: the last two minutes of wall-clock reality, to the console."""
    from pyspark.sql import functions as F

    spark = get_spark("masar-ops-alerts")
    positions = spark.readStream.format("delta").load(SILVER_PATH)

    alerts = (
        positions.withColumn(
            "alert_type",
            F.when(F.col("speed_kmh") > SPEEDING_KMH, F.lit("SPEEDING"))
            .when(F.col("accuracy_m") > DEGRADED_ACCURACY_M, F.lit("DEGRADED_FIX"))
            .when(F.col("event_lag_s") > STALE_TELEMETRY_S, F.lit("STALE_TELEMETRY")),
        )
        .filter(F.col("alert_type").isNotNull())
        .select(
            "event_ts",
            "_kafka_ts",
            "vehicle_id",
            "driver_id",
            "trip_id",
            "alert_type",
            "speed_kmh",
            "accuracy_m",
            "event_lag_s",
        )
    )

    writer = (
        alerts.writeStream.format("console")
        .queryName("ops_alerts")
        .outputMode("append")
        .option("truncate", False)
        .option("numRows", 10)
        .option("checkpointLocation", f"{config.CHECKPOINTS}/ops_alerts")
    )
    trigger = {"availableNow": True} if once else {"processingTime": f"{trigger_seconds} seconds"}
    writer.trigger(**trigger).start().awaitTermination()


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Fan out silver.vehicle_positions")
    p.add_argument("--consumer", required=True, choices=["eta", "alerts"])
    p.add_argument("--trigger-seconds", type=int, default=30)
    p.add_argument("--once", action="store_true")
    a = p.parse_args()
    if a.consumer == "eta":
        eta_feature_input(a.trigger_seconds, a.once)
    else:
        operations_alerts(a.trigger_seconds, a.once)


if __name__ == "__main__":
    main()
