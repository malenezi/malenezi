"""Train the ETA baseline — and expose the metric that tells you it is lying.

The model is not the point. The NUMBER is the point: Lab 8 builds the feature
table twice, trains twice, and reads the difference. R² 0.943 on trip-duration
prediction is not a good result, it is a confession; R² 0.712 after the fix is
what the platform can actually deliver at 07:14:33 with the data that exists
at 07:14:33.

``--corr-only`` skips training and prints each feature's correlation with the
label. A feature at |r| > 0.9 has some explaining to do.

CLI::

    python -m masar.serve.train_eta --features gold.eta_features --split time --test-days 2
    python -m masar.serve.train_eta --corr-only --features gold.eta_features
"""

from __future__ import annotations

import argparse

from masar import config
from masar.serve.training_join import FEATURE_COLUMNS, LABEL_COLUMN, build_training_set, time_split
from masar.spark import get_spark
from masar.transform.feature_spec import correlation_is_suspicious

NUMERIC_FEATURES = [
    "hour_of_day",
    "day_of_week",
    "rolling_zone_demand_15m",
    "rolling_avg_speed_10m",
    "driver_recent_trip_count",
    "distance_km",
    "historical_route_duration",
]


def correlations(table: str = "gold.eta_features") -> dict[str, float]:
    """Pearson r of each numeric feature against the label.

    Returns:
        ``{feature: r}``, sorted by |r| descending. Print it before you train:
        it costs one Spark job and it has caught more leakage than any review.
    """
    from pyspark.sql import functions as F

    spark = get_spark("masar-train-eta")
    df = spark.read.format("delta").load(config.resolve_table(table))
    out: dict[str, float] = {}
    for column in NUMERIC_FEATURES:
        if column not in df.columns:
            continue
        r = df.select(
            F.corr(F.col(column).cast("double"), F.col(LABEL_COLUMN)).alias("r")
        ).collect()[0]["r"]
        if r is not None:
            out[column] = float(r)

    print(f"pearson r with {LABEL_COLUMN}")
    for column, r in sorted(out.items(), key=lambda kv: -abs(kv[1])):
        flag = (
            "   <-- a feature this correlated is not a feature"
            if correlation_is_suspicious(r)
            else ""
        )
        print(f"  {column:<28} {r:>7.4f}{flag}")
    return out


def train(table: str = "gold.eta_features", test_days: int = 2, split: str = "time") -> dict:
    """Fit a gradient-boosted baseline and report R² and MAE.

    Args:
        table: feature table to train on.
        test_days: size of the held-out tail.
        split: ``time`` (correct) or ``random`` (shown so you can watch the
            metric inflate for a second, unrelated reason).

    Returns:
        ``{"rows", "train", "test", "r2", "mae", "importances"}``.
    """
    import numpy as np
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_absolute_error, r2_score

    df = build_training_set(features_table=table)
    if split == "time":
        train_df, test_df, cutoff = time_split(df, test_days)
    else:
        train_df, test_df = df.randomSplit([0.75, 0.25], seed=20260601)
        cutoff = "random (leaks by row order — for contrast only)"

    features = [c for c in NUMERIC_FEATURES if c in df.columns]
    train_pd = train_df.select(*features, "label").toPandas().dropna()
    test_pd = test_df.select(*features, "label").toPandas().dropna()

    print(
        f"[train] rows={df.count():,}  train={len(train_pd):,}  test={len(test_pd):,}  "
        f"(split at {cutoff})"
    )
    model = GradientBoostingRegressor(random_state=20260601)
    model.fit(train_pd[features], train_pd["label"])
    pred = model.predict(test_pd[features])

    r2 = float(r2_score(test_pd["label"], pred))
    mae = float(mean_absolute_error(test_pd["label"], pred))
    importances = dict(
        sorted(
            zip(features, (float(x) for x in np.asarray(model.feature_importances_)), strict=True),
            key=lambda kv: -kv[1],
        )
    )

    print(f"[train] model=GradientBoostingRegressor  target={LABEL_COLUMN}")
    print(f"[train] R2  = {r2:.3f}")
    print(f"[train] MAE = {mae:.2f} min")
    print("[train] top features by gain:")
    for name, gain in list(importances.items())[:6]:
        print(f"          {name:<28} {gain:.3f}")
    if r2 > 0.90:
        print(
            "[train] WARNING: an R2 above 0.90 on trip duration is a red flag, "
            "not a result. Audit the feature windows before celebrating."
        )
    return {
        "rows": df.count(),
        "train": len(train_pd),
        "test": len(test_pd),
        "r2": r2,
        "mae": mae,
        "importances": importances,
    }


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Train the Masar ETA baseline")
    p.add_argument("--features", default="gold.eta_features")
    p.add_argument("--split", default="time", choices=["time", "random"])
    p.add_argument("--test-days", type=int, default=2)
    p.add_argument("--corr-only", action="store_true", help="print correlations, do not train")
    a = p.parse_args()
    if a.corr_only:
        correlations(a.features)
        return
    train(a.features, a.test_days, a.split)
    _ = FEATURE_COLUMNS  # documented contract; kept visible for the reader


if __name__ == "__main__":
    main()
