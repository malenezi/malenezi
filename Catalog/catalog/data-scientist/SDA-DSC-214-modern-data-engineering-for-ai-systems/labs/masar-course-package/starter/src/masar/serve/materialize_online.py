"""Materialise the latest zone feature slice into Redis.

Keyspace (CONVENTIONS.md): ``masar:features:zone:{zone_id}``.

Values are **COPIED** from ``gold.eta_features``. There is no feature logic in
this file and there must never be any. The moment this module computes
something, the online path and the training path can disagree — and they will,
subtly, in a way that shows up as "the model works offline and not live" three
weeks later. Copy the value, never recompute it.

CLI::

    python -m masar.serve.materialize_online
"""

from __future__ import annotations

import argparse
import json

from masar import config
from masar.spark import get_spark

GOLD = config.TABLES["gold.eta_features"].path
KEY = config.REDIS_ZONE_KEY

#: Only columns that are (a) zone-grained and (b) safe to serve. The label and
#: every trip-grained column are excluded — see docs/GOVERNANCE_TEMPLATE.md.
ONLINE_COLUMNS = [
    "rolling_zone_demand_15m",
    "rolling_avg_speed_10m",
    "historical_route_duration",
    "weather_condition",
]


def redis_client():
    """A decoded Redis client pointed at the configured host/port."""
    import redis

    return redis.Redis(
        host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB, decode_responses=True
    )


def latest_per_zone():
    """The newest feature row per ``pickup_zone_id`` — the online lookup grain."""
    from pyspark.sql import Window
    from pyspark.sql import functions as F

    spark = get_spark("masar-materialize-online")
    feats = spark.read.format("delta").load(GOLD)
    w = Window.partitionBy("pickup_zone_id").orderBy(F.col("feature_ts").desc())
    return (
        feats.withColumn("_rn", F.row_number().over(w))
        .filter("_rn = 1")
        .select("pickup_zone_id", "feature_ts", *ONLINE_COLUMNS)
    )


def materialize(feature_version: str = "v2") -> int:
    """Push the latest zone features to Redis.

    Args:
        feature_version: stamped into every value. A serving payload with no
            version cannot be reconciled with the model that consumes it, and
            "which features was this prediction made from?" becomes
            unanswerable at exactly the moment it matters.

    Returns:
        Number of zone keys written.
    """
    latest = latest_per_zone()
    client = redis_client()
    pipe = client.pipeline()
    n = 0

    for row in latest.collect():
        # ── TODO(lab-8): copy, do not recompute ───────────────────────────
        #   What : build the payload from the OFFLINE row's values only, add
        #          feature_ts and _feature_version, and SET it under
        #          KEY.format(zone_id=...).
        #   Why  : any arithmetic here is a second implementation of a feature
        #          that already exists in gold. Two implementations of one
        #          feature is training/serving skew with extra steps.
        #   Ref  : solutions/lab8_serve.py :: materialize_online
        payload = {c: row[c] for c in ONLINE_COLUMNS}
        payload["feature_ts"] = row["feature_ts"].isoformat()
        payload["_feature_version"] = feature_version
        pipe.set(KEY.format(zone_id=row["pickup_zone_id"]), json.dumps(payload))
        # ── end TODO(lab-8) ───────────────────────────────────────────────
        n += 1

    pipe.execute()
    print(f"[serve] materialised {n} zone keys to redis under masar:features:zone:*")
    return n


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Materialise zone features into Redis")
    p.add_argument("--feature-version", default="v2")
    a = p.parse_args()
    materialize(a.feature_version)


if __name__ == "__main__":
    main()
