"""PA-3 artefact — the PA-3 variant builder for ``gold.eta_features``.

================================ WARNING ==================================
THIS FILE IS A DELIBERATELY BROKEN ASSESSMENT ARTEFACT.
It is the artefact under test in `labs/assessments/PA-3_Feature_Leakage_Audit.md`
and it ships with its defects intact, on purpose. DO NOT USE IT AS A
REFERENCE for point-in-time feature engineering, and do not copy its window
bounds anywhere. The Lab-8 drill lives in `masar.transform.build_eta_features`
(a DIFFERENT defect mix) and the point-in-time patterns live in
`masar.transform.feature_spec`.
===========================================================================

GRAIN: exactly one row per ``trip_id``.
COLUMNS: exactly the 13 CONVENTIONS columns of ``gold.eta_features`` — the
contract is fixed and a fix may not drop a column.

**Two columns deliberately swap class relative to Lab 8.** A participant who
memorised the Lab-8 answer key gets both wrong:

===========================  ==================  ==========================
Column                       Lab-8 starter       PA-3 variant (this file)
===========================  ==================  ==========================
``rolling_avg_speed_10m``    LEAKAGE             **VALID** (other vehicles,
                                                 strictly before feature_ts)
``historical_route_duration`` VALID              **LEAKAGE** (upper bound 0)
===========================  ==================  ==========================

Five defects live in this builder (PA-3 answer key, section 5a):

  1. ``rolling_zone_demand_15m`` — ``rangeBetween(-900, 0)``. The inclusive
     upper bound admits every trip starting in the SAME SECOND in the same
     zone. Correct bound: ``(-900, -1)``.
  2. ``historical_route_duration`` — ``rangeBetween(-2592000, 0)`` puts the
     trip's own ``duration_min`` (the label) inside its own 30-day route
     average. Correct bound: ``(-2592000, -1)``.
  3. ``weather_condition`` — joined to the trip's OWN hour, which lands after
     the hour it describes. Must be shifted to the last observed hour on
     BOTH the training and the serving side.
  4. ``distance_km`` — the METERED distance, written at ``dropoff_ts``. Must
     be re-sourced as the planned route distance at booking.
  5. ``label_actual_duration_min`` — present, and materialised downstream via
     ``ONLINE_COLUMNS`` in the model card. Must be stripped from the online
     payload.

Note that ``driver_recent_trip_count`` is NOT a builder defect: its offline
bound ``(-86400, -1)`` is correct. Its failure is STALENESS on the online
path, which is a serving-cadence problem, not a window problem.

CLI::

    python -m masar.transform.build_eta_features_pa3          # build the broken variant
    python -m masar.transform.build_eta_features_pa3 --fixed  # the participant's deliverable

``--fixed`` is intentionally NOT implemented here: implementing it is
PA-3 sub-criteria P1–P6. See the assessment brief.

PySpark is imported inside the functions so that
``import masar.transform.build_eta_features_pa3`` works with no Spark
installed.
"""

from __future__ import annotations

import argparse

from masar import config

SILVER_TRIPS = config.TABLES["silver.trips"].path
SILVER_POSITIONS = config.TABLES["silver.vehicle_positions"].path
WEATHER = f"{config.RAW_ROOT}/weather_hourly.csv"
OUT = config.resolve_table("_assessments/pa3/eta_features")

#: The 13 CONVENTIONS columns, in order. The contract, not a suggestion.
ETA_FEATURE_COLUMNS = (
    "trip_id",
    "pickup_zone_id",
    "dropoff_zone_id",
    "hour_of_day",
    "day_of_week",
    "rolling_zone_demand_15m",
    "rolling_avg_speed_10m",
    "driver_recent_trip_count",
    "weather_condition",
    "distance_km",
    "historical_route_duration",
    "feature_ts",
    "label_actual_duration_min",
)


def build(out: str = OUT) -> int:
    """Build the PA-3 variant of ``gold.eta_features`` — WITH its five defects.

    Args:
        out: destination path. Defaults to the PA-3 sandbox, which is wiped
            and rebuilt by ``scripts/assessments/pa3_setup.py``.

    Returns:
        The row count written.
    """
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    from masar.spark import get_spark

    spark = get_spark("pa3-eta-features")

    trips = (
        spark.read.format("delta")
        .load(SILVER_TRIPS)
        .filter(F.col("status") == "completed")
        .withColumn("pickup_epoch", F.col("pickup_ts").cast("long"))
    )
    pos = spark.read.format("delta").load(SILVER_POSITIONS)
    weather = (
        spark.read.option("header", True)
        .option("inferSchema", True)
        .csv(WEATHER)
        .withColumn("hour_ts", F.to_timestamp("hour_ts"))
    )

    # (A) DEFECT 1 - zone demand: inclusive upper bound admits same-second trips.
    w_demand = (
        Window.partitionBy("city", "pickup_zone_id").orderBy("pickup_epoch").rangeBetween(-900, 0)
    )

    # (B) driver recent trips: bound is correct; the STALENESS is an online problem.
    w_driver = Window.partitionBy("driver_id").orderBy("pickup_epoch").rangeBetween(-86400, -1)

    # (C) DEFECT 2 - historical route duration: upper bound 0 puts the trip's own
    #     duration inside its own 30-day route average.
    w_route = (
        Window.partitionBy("pickup_zone_id", "dropoff_zone_id")
        .orderBy("pickup_epoch")
        .rangeBetween(-2592000, 0)
    )

    # (D) rolling average speed - CORRECT in this variant: other vehicles in the
    #     pickup zone, strictly before feature_ts, this trip excluded.
    zone_speed = (
        pos.alias("p")
        .join(
            trips.alias("t2").select(
                F.col("trip_id").alias("t2_trip"),
                F.col("pickup_zone_id").alias("t2_zone"),
            ),
            F.col("p.trip_id") == F.col("t2_trip"),
            "inner",
        )
        .select(
            F.col("p.trip_id").alias("src_trip"),
            "t2_zone",
            F.col("p.event_ts").alias("ping_ts"),
            F.col("p.speed_kmh"),
        )
    )

    feats = (
        trips.withColumn("rolling_zone_demand_15m", F.count("*").over(w_demand))
        .withColumn("driver_recent_trip_count", F.count("*").over(w_driver))
        .withColumn("historical_route_duration", F.avg("duration_min").over(w_route))
        .withColumn("hour_of_day", F.hour("pickup_ts"))
        .withColumn("day_of_week", F.dayofweek("pickup_ts"))
        .withColumn("feature_ts", F.col("pickup_ts"))
    )

    speed_10m = (
        feats.alias("f")
        .join(
            zone_speed.alias("z"),
            (F.col("f.pickup_zone_id") == F.col("z.t2_zone"))
            & (F.col("z.src_trip") != F.col("f.trip_id"))
            & (F.col("z.ping_ts") < F.col("f.feature_ts"))
            & (F.col("z.ping_ts") >= F.expr("f.feature_ts - INTERVAL 10 MINUTES")),
            "left",
        )
        .groupBy("f.trip_id")
        .agg(F.avg("z.speed_kmh").alias("rolling_avg_speed_10m"))
    )

    result = (
        feats.join(speed_10m, "trip_id", "left")
        # DEFECT 3 - weather joined to the trip's OWN hour; the file lands after it.
        .join(
            weather.select(
                F.col("city").alias("w_city"),
                "hour_ts",
                F.col("condition").alias("weather_condition"),
            ),
            (F.col("city") == F.col("w_city"))
            & (F.date_trunc("hour", F.col("pickup_ts")) == F.col("hour_ts")),
            "left",
        )
        # DEFECT 4 - distance_km is the METERED distance, written at dropoff_ts.
        # DEFECT 5 - the label is present and is materialised downstream.
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
            "distance_km",
            "historical_route_duration",
            "feature_ts",
            F.col("duration_min").alias("label_actual_duration_min"),
        )
    )

    assert tuple(result.columns) == ETA_FEATURE_COLUMNS, result.columns
    result.write.format("delta").mode("overwrite").save(out)
    n = spark.read.format("delta").load(out).count()
    print(
        f"[gold] eta_features (pa3, as shipped): {n:,} rows, {len(ETA_FEATURE_COLUMNS)} columns -> {out}"
    )
    return n


def build_fixed(out: str = OUT) -> int:
    """The point-in-time-correct rebuild — PA-3's deliverable, not shipped.

    Repairing this is the assessment (sub-criteria P1-P6): strictly-prior
    window bounds, planned route distance at booking, weather shifted to the
    last observed hour on both sides, the label out of ``ONLINE_COLUMNS``,
    and a temporal train/test split. The output must still be exactly the 13
    columns in :data:`ETA_FEATURE_COLUMNS`.
    """
    raise NotImplementedError(
        "PA-3: implementing the point-in-time-correct builder is the assessment. "
        "See labs/assessments/PA-3_Feature_Leakage_Audit.md, section 3, task 3. "
        "The answer key is not shipped in the repository."
    )


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="PA-3 eta_features builder (SHIPPED BROKEN)")
    p.add_argument("--out", default=OUT, help="destination path (default: the PA-3 sandbox)")
    p.add_argument("--fixed", action="store_true", help="build the repaired variant")
    a = p.parse_args()
    if a.fixed:
        build_fixed(a.out)
    else:
        build(a.out)


if __name__ == "__main__":
    main()
