"""``gold.eta_features`` — the AI product Masar's ETA model trains and serves on.

GRAIN: exactly one row per ``trip_id``.

COLUMNS (CONVENTIONS.md — exact, and not negotiable, because the model, the
online store and the training join all agree on them)::

    trip_id, pickup_zone_id, dropoff_zone_id, hour_of_day, day_of_week,
    rolling_zone_demand_15m, rolling_avg_speed_10m, driver_recent_trip_count,
    weather_condition, distance_km, historical_route_duration, feature_ts,
    label_actual_duration_min

**THIS FILE SHIPS WITH DELIBERATE DEFECTS.** Four of these columns are
computed in a way that leaks, is stale, or does not exist at inference time.
Lab 8 Task 3 is where you find them — classify each column yourself BEFORE
reading ``solutions/lab8_serve.py``. The drill only works if you make the
call first and are then shown the arithmetic.

The tell you are looking for: an offline R² of 0.94 on trip-duration
prediction. Take thirty seconds and ask whether you believe it.

CLI::

    python -m masar.transform.build_eta_features
    python -m masar.transform.build_eta_features --fixed
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark
from masar.transform.feature_spec import ETA_FEATURE_WINDOWS, validate_windows

SILVER_TRIPS = config.TABLES["silver.trips"].path
SILVER_POSITIONS = config.TABLES["silver.vehicle_positions"].path
WEATHER = f"{config.RAW_ROOT}/weather_hourly.csv"
OUT = config.TABLES["gold.eta_features"].path

FEATURE_VERSION_LEAKY = "v1"
FEATURE_VERSION_FIXED = "v2"


def build(fixed: bool = False, **_: object) -> int:
    """Build ``gold.eta_features``.

    Args:
        fixed: when False (the default, and what Lab 8 starts from) the four
            defective windows are used as shipped. When True, every window is
            the one declared in :data:`ETA_FEATURE_WINDOWS`, the speed feature
            is computed from prior-window positions rather than the trip's own
            pings, and ``distance_km`` carries the ROUTED distance.

    Returns:
        Row count written.
    """
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    spark = get_spark("masar-eta-features")
    trips = (
        spark.read.format("delta")
        .load(SILVER_TRIPS)
        .filter(F.col("status") == "completed")
        .withColumn("pickup_epoch", F.col("pickup_ts").cast("long"))
    )
    positions = spark.read.format("delta").load(SILVER_POSITIONS)
    weather = (
        spark.read.option("header", True)
        .option("inferSchema", True)
        .csv(WEATHER)
        .withColumn("hour_ts", F.to_timestamp("hour_ts"))
    )

    # ── TODO(lab-8): repair the four leaking / stale / unavailable features ──
    #   What : with --fixed, every window below must match the declaration in
    #          masar.transform.feature_spec.ETA_FEATURE_WINDOWS, and:
    #            (A) rolling_zone_demand_15m   centred window -> strictly prior
    #            (B) driver_recent_trip_count  end=0          -> end=-1
    #            (D) rolling_avg_speed_10m     averages THIS trip's own pings,
    #                including pings recorded after dropoff. Compute it from
    #                positions in the ZONE over the prior 10 minutes instead.
    #            (E) distance_km               actual distance driven, known
    #                only at dropoff. Serve the ROUTED distance under the same
    #                column name — the contract is the name, not the provenance.
    #          The weather join key is the fifth thing to inspect: joining on
    #          date_trunc('hour', pickup_ts) uses the CURRENT hour's observed
    #          weather, which at 07:14 has not been published yet.
    #   Why  : each defect inflates the offline metric and none of them exist
    #          at prediction time. R2 0.943 -> ~0.712 after the fix, and the
    #          second number is the one that survives contact with production.
    #   Ref  : solutions/lab8_serve.py :: build_eta_features_fixed
    if fixed:
        demand_bounds = (-900, -1)
        driver_bounds = (-86_400, -1)
        weather_hour = F.date_trunc("hour", F.col("pickup_ts") - F.expr("INTERVAL 1 HOUR"))
        feature_version = FEATURE_VERSION_FIXED
    else:
        demand_bounds = (-450, 450)  # <-- (A) centred: half the window is the future
        driver_bounds = (-86_400, 0)  # <-- (B) inclusive of now
        weather_hour = F.date_trunc("hour", F.col("pickup_ts"))  # <-- (C) unpublished at t
        feature_version = FEATURE_VERSION_LEAKY
    # ── end TODO(lab-8) ───────────────────────────────────────────────────

    w_demand = (
        Window.partitionBy("city", "pickup_zone_id")
        .orderBy("pickup_epoch")
        .rangeBetween(*demand_bounds)
    )
    w_driver = Window.partitionBy("driver_id").orderBy("pickup_epoch").rangeBetween(*driver_bounds)
    # Prior 30 days on this origin-destination pair, strictly before. This one
    # was correct as shipped — note that not everything suspicious is a bug.
    w_route = (
        Window.partitionBy("pickup_zone_id", "dropoff_zone_id")
        .orderBy("pickup_epoch")
        .rangeBetween(-2_592_000, -1)
    )

    if fixed:
        # Zone speed over the PRIOR 10 minutes: available at pickup, and not a
        # function of this trip's outcome.
        zone_speed = (
            positions.join(trips.select("trip_id", "city", "pickup_zone_id"), "trip_id", "inner")
            .withColumn("event_epoch", F.col("event_ts").cast("long"))
            .groupBy("city", "pickup_zone_id", F.window("event_ts", "10 minutes").alias("w"))
            .agg(F.avg("speed_kmh").alias("zone_speed_10m"))
            .select(
                "city", "pickup_zone_id", F.col("w.end").alias("speed_ready_at"), "zone_speed_10m"
            )
        )
        speed_joined = (
            trips.join(
                zone_speed,
                (trips.city == zone_speed.city)
                & (trips.pickup_zone_id == zone_speed.pickup_zone_id)
                & (zone_speed.speed_ready_at <= trips.pickup_ts),
                "left",
            )
            .drop(zone_speed.city)
            .drop(zone_speed.pickup_zone_id)
        )
        base = speed_joined.withColumn("rolling_avg_speed_10m", F.col("zone_speed_10m"))
        distance_expr = F.col("distance_km")  # routed distance, see solution notes
    else:
        # <-- (D) averages THIS trip's own pings, including ones recorded
        #     after dropoff: the feature is a summary of the label.
        trip_speed = positions.groupBy("trip_id").agg(
            F.avg("speed_kmh").alias("rolling_avg_speed_10m")
        )
        base = trips.join(trip_speed, "trip_id", "left")
        distance_expr = F.col("distance_km")  # <-- (E) actual, not routed

    feats = (
        base.withColumn("rolling_zone_demand_15m", F.count("*").over(w_demand))
        .withColumn("driver_recent_trip_count", F.count("*").over(w_driver))
        .withColumn("historical_route_duration", F.avg("duration_min").over(w_route))
        .withColumn("hour_of_day", F.hour("pickup_ts"))
        .withColumn("day_of_week", F.dayofweek("pickup_ts"))
        .withColumn("feature_ts", F.col("pickup_ts"))
        .withColumn("_weather_hour", weather_hour)
        .join(
            weather.select(
                F.col("city").alias("w_city"),
                "hour_ts",
                F.col("condition").alias("weather_condition"),
            ),
            (F.col("city") == F.col("w_city")) & (F.col("_weather_hour") == F.col("hour_ts")),
            "left",
        )
        .select(
            "trip_id",
            "pickup_zone_id",
            "dropoff_zone_id",
            "hour_of_day",
            "day_of_week",
            "rolling_zone_demand_15m",
            "rolling_avg_speed_10m",
            "driver_recent_trip_count",
            "weather_condition",
            distance_expr.alias("distance_km"),
            "historical_route_duration",
            "feature_ts",
            F.col("duration_min").alias("label_actual_duration_min"),
        )
        .withColumn("_feature_version", F.lit(feature_version))
    )

    n = feats.count()
    feats.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(OUT)
    print(f"[gold] eta_features: {n:,} rows, feature_version={feature_version}")

    if fixed:
        problems = validate_windows(ETA_FEATURE_WINDOWS)
        if problems:
            raise RuntimeError("POINT-IN-TIME LINT FAILED:\n  " + "\n  ".join(problems))
        print("[lint] point-in-time: every declared ETA window is strictly prior")
    else:
        print(
            "[lint] WARNING: built with the shipped (leaking) windows. "
            "Run with --fixed after Lab 8 Task 3."
        )
    return n


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Build gold.eta_features")
    p.add_argument("--fixed", action="store_true", help="use the repaired, point-in-time windows")
    a = p.parse_args()
    build(fixed=a.fixed)


if __name__ == "__main__":
    main()
