"""Build the training set by joining labels to features AS OF event time.

Each row's features must reflect only what was known at ``feature_ts``. The
join itself is the easy part; the discipline is that the features come from
the SAME table the online store is materialised from. Recompute them here
"just for training" and you have built two feature pipelines, which is the
definition of training/serving skew.

CLI::

    python -m masar.serve.training_join
"""

from __future__ import annotations

import argparse
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

ETA_FEATURES = config.TABLES["gold.eta_features"].path
SILVER_TRIPS = config.TABLES["silver.trips"].path

FEATURE_COLUMNS = [
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
]
LABEL_COLUMN = "label_actual_duration_min"


def build_training_set(
    label_col: str = LABEL_COLUMN, features_table: str = "gold.eta_features"
) -> DataFrame:
    """Join gold features to their label, ready for a time-ordered split.

    Args:
        label_col: the target column. It lives in the feature table already
            (``label_actual_duration_min``); joining it back from silver is
            supported so a different label can be swapped in without a rebuild.
        features_table: canonical name or lakehouse path. The assessments build
            scratch feature tables outside the registry so they cannot disturb
            a participant's real lakehouse, so both forms are accepted.

    Returns:
        One row per ``trip_id``: features, label, ``feature_ts``, and the
        feature version that produced them.
    """
    from pyspark.sql import functions as F

    spark = get_spark("masar-training-join")
    feats = spark.read.format("delta").load(config.resolve_table(features_table))

    if label_col in feats.columns:
        joined = feats.withColumnRenamed(label_col, "label")
    else:
        labels = (
            spark.read.format("delta")
            .load(SILVER_TRIPS)
            .select("trip_id", F.col(label_col).alias("label"))
        )
        joined = feats.join(labels, "trip_id", "inner")

    return joined.withColumn("_trained_on_feature_version", F.col("_feature_version"))


def time_split(df: DataFrame, test_days: int = 2):
    """Split by TIME, never at random.

    A random split leaks the future into training through nothing more exotic
    than row order: tomorrow's trips teach the model about today's. Split on
    ``feature_ts`` and the test set is genuinely unseen — which is why the
    honest metric is lower, and why it holds up.

    Returns:
        ``(train, test, cutoff_timestamp)``.
    """
    from pyspark.sql import functions as F

    max_ts = df.agg(F.max("feature_ts").alias("m")).collect()[0]["m"]
    cutoff = max_ts - __import__("datetime").timedelta(days=test_days)
    return df.filter(F.col("feature_ts") < cutoff), df.filter(F.col("feature_ts") >= cutoff), cutoff


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Build the ETA training set")
    p.add_argument("--test-days", type=int, default=2)
    a = p.parse_args()
    df = build_training_set()
    train, test, cutoff = time_split(df, a.test_days)
    print(
        f"[train-join] rows={df.count():,}  train={train.count():,}  "
        f"test={test.count():,}  (time split at {cutoff})"
    )
    df.show(3, truncate=False)


if __name__ == "__main__":
    main()
