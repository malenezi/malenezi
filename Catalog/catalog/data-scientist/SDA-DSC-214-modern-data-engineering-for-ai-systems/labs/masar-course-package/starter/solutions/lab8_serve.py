"""Lab 8 solution — the leakage fix, online materialisation, the PDPL boundary.

Blocks completed here:
  * ``src/masar/transform/build_eta_features.py`` :: build_eta_features_fixed
  * ``src/masar/serve/materialize_online.py``     :: materialize_online
  * ``src/masar/serve/bi_view.py``                :: build_bi_safe_view

Read ``THE_FOUR_DEFECTS`` only AFTER classifying the columns yourself. The
drill's value is in making the call and then seeing the arithmetic — being
told first removes the part that transfers.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from masar.transform.feature_spec import ETA_FEATURE_WINDOWS

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame


THE_FOUR_DEFECTS = """
(A) rolling_zone_demand_15m — LEAKAGE
    Shipped as rangeBetween(-450, +450): a CENTRED window. Half of it is the
    future. At 07:14:33 the feature counts trips that start at 07:19 — which
    the platform cannot know, and which correlate with the label because busy
    zones are slow zones.
    Fix: rangeBetween(-900, -1). Prior 15 minutes, strictly before.

(B) driver_recent_trip_count — LEAKAGE (subtle)
    Shipped as rangeBetween(-86400, 0). Inclusive of 0 means inclusive of this
    trip's own timestamp, so on ties it counts trips the driver started in the
    same second. Small effect, same class of bug, and the one people argue is
    fine. It is not: the fix costs one character.
    Fix: rangeBetween(-86400, -1).

(C) weather_condition — STALE / UNAVAILABLE
    Joined on date_trunc('hour', pickup_ts): the CURRENT hour's OBSERVED
    weather. At 07:14 the 07:00 observation has not been published yet. The
    model trains on weather it will never have at inference.
    Fix: join the PRIOR hour's observation (or a forecast, if one exists).

(D) rolling_avg_speed_10m — LEAKAGE (the worst one)
    Shipped as avg(speed_kmh) over THIS TRIP's own pings — including pings
    recorded 21 minutes after pickup, i.e. after the trip ended. The feature is
    a summary of the journey whose duration is the label. Its correlation with
    the label is -0.72 and every point of that is the model reading the answer.
    Fix: average positions in the ZONE over the prior 10 minutes.

(E) distance_km — UNAVAILABLE ONLINE
    The raw feed's distance_km is the ACTUAL distance driven, known only at
    dropoff. At prediction time the platform has the ROUTED distance from the
    routing engine. The column NAME is the contract, so keep it and change the
    provenance — do not quietly train on the actual and serve the routed.

Result: R2 0.943 -> ~0.712, MAE 1.81 -> ~4.58 min.

That is the CORRECT outcome and you should be pleased. The first number was
never real; it was the model reading the answer. The second is what the
platform can deliver at 07:14:33 with the data that exists at 07:14:33 — and
it is the one that survives contact with production.
"""


# --------------------------------------------------------------------------
# TODO(lab-8) in src/masar/transform/build_eta_features.py :: build
# --------------------------------------------------------------------------
def fixed_window_bounds() -> dict[str, tuple[int, int]]:
    """The repaired window bounds, matching the declared feature spec."""
    return {name: (w.start, w.end) for name, w in ETA_FEATURE_WINDOWS.items()}


def build_eta_features_fixed(spark, trips: DataFrame, positions: DataFrame, weather: DataFrame):
    """The repaired feature build, in one place for reference.

    Note what did NOT change: the column names. The feature table's schema is
    the contract shared by the training join, the online store and the model.
    Repairing a feature means changing how it is COMPUTED, never what it is
    called — rename it and every consumer breaks for a reason unrelated to the
    bug you fixed.
    """
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    bounds = fixed_window_bounds()

    w_demand = (
        Window.partitionBy("city", "pickup_zone_id")
        .orderBy("pickup_epoch")
        .rangeBetween(*bounds["rolling_zone_demand_15m"])
    )
    w_driver = (
        Window.partitionBy("driver_id")
        .orderBy("pickup_epoch")
        .rangeBetween(*bounds["driver_recent_trip_count"])
    )
    w_route = (
        Window.partitionBy("pickup_zone_id", "dropoff_zone_id")
        .orderBy("pickup_epoch")
        .rangeBetween(*bounds["historical_route_duration"])
    )

    # (D) zone speed over the PRIOR 10 minutes — available at pickup, and not a
    # function of this trip's outcome.
    zone_speed = (
        positions.join(trips.select("trip_id", "city", "pickup_zone_id"), "trip_id", "inner")
        .groupBy("city", "pickup_zone_id", F.window("event_ts", "10 minutes").alias("w"))
        .agg(F.avg("speed_kmh").alias("zone_speed_10m"))
        .select("city", "pickup_zone_id", F.col("w.end").alias("ready_at"), "zone_speed_10m")
    )

    # (C) the PRIOR hour's weather observation — the one that exists at pickup.
    prior_hour = F.date_trunc("hour", F.col("pickup_ts") - F.expr("INTERVAL 1 HOUR"))

    return (
        trips.join(
            zone_speed,
            (trips.city == zone_speed.city)
            & (trips.pickup_zone_id == zone_speed.pickup_zone_id)
            & (zone_speed.ready_at <= trips.pickup_ts),
            "left",
        )
        .withColumn("rolling_avg_speed_10m", F.col("zone_speed_10m"))
        .withColumn("rolling_zone_demand_15m", F.count("*").over(w_demand))
        .withColumn("driver_recent_trip_count", F.count("*").over(w_driver))
        .withColumn("historical_route_duration", F.avg("duration_min").over(w_route))
        .withColumn("_weather_hour", prior_hour)
        .join(
            weather.select(
                F.col("city").alias("w_city"),
                "hour_ts",
                F.col("condition").alias("weather_condition"),
            ),
            (F.col("city") == F.col("w_city")) & (F.col("_weather_hour") == F.col("hour_ts")),
            "left",
        )
        .withColumn("_feature_version", F.lit("v2"))
    )


# --------------------------------------------------------------------------
# TODO(lab-8) in src/masar/serve/materialize_online.py :: materialize
# --------------------------------------------------------------------------
def materialize_online(
    rows, client, key_template: str, online_columns: list[str], feature_version: str = "v2"
) -> int:
    """Copy the offline values to Redis. No arithmetic. None.

    The rule is absolute and it is the whole lesson: **copy the value, never
    recompute it.** Any calculation on this side is a second implementation of
    a feature that already exists in gold, and two implementations of one
    feature is training/serving skew with extra steps. It will not disagree at
    first. It will disagree after someone fixes a rounding bug in one of them.

    ``_feature_version`` is stamped in because a serving payload with no
    version cannot be reconciled with the model that consumed it — and
    "which features produced this prediction?" becomes unanswerable at exactly
    the moment somebody needs the answer.
    """
    pipe = client.pipeline()
    n = 0
    for row in rows:
        payload = {c: row[c] for c in online_columns}
        payload["feature_ts"] = row["feature_ts"].isoformat()
        payload["_feature_version"] = feature_version
        pipe.set(key_template.format(zone_id=row["pickup_zone_id"]), json.dumps(payload))
        n += 1
    pipe.execute()
    return n


# --------------------------------------------------------------------------
# TODO(lab-8) in src/masar/serve/bi_view.py :: build_bi_safe_view
# --------------------------------------------------------------------------
def build_bi_safe_view(silver: DataFrame, safe_columns: list[str]) -> DataFrame:
    """Three PDPL controls, applied in order, each doing a different job.

      1. **Pseudonymise.** ``sha2(rider_id, 256)`` keeps cohort analysis
         possible without exposing the identifier.
      2. **Minimise.** DROP the raw column. Keeping it beside its own hash
         protects nothing; a column you did not publish cannot leak and does
         not have to be found again during an erasure.
      3. **Reduce resolution.** Zone ids, not coordinates. The analyst question
         is about districts. Metre resolution answers a more invasive question
         nobody asked.

    Be honest in LAB8_NOTES.md about what this COSTS: an analyst can no longer
    join a rider to a support ticket, or map a dropoff to a building. Both are
    real capabilities and both are gone. Governance that costs nothing usually
    protects nothing.
    """
    from pyspark.sql import functions as F

    return (
        silver.withColumn("rider_pseudonym", F.sha2(F.col("rider_id"), 256))
        .drop("rider_id")
        .select(*safe_columns)
    )


LAB8_ANSWERS = {
    "what is feature leakage": (
        "Using information unavailable at prediction time. It inflates the "
        "offline metric and collapses live — and it presents as success, which "
        "is why it is the most expensive bug in applied ML."
    ),
    "how to keep online and offline consistent": (
        "Materialise/copy from the offline table. Never re-implement the "
        "feature on the serving path."
    ),
    "what makes numbers reconcile": "Conformed dimensions: one dim_date, one dim_zone.",
    "when an external store is justified": (
        "A MEASURED millisecond-latency or high-concurrency requirement — and "
        "then only as a derived copy with a continuous consistency check."
    ),
    "should BI read raw rider ids": (
        "No. Aggregate or pseudonymise at the boundary; PDPL applies to the "
        "serving layer as much as to the lake."
    ),
}
