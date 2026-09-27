"""The PDPL-safe BI view: aggregates and masked identifiers only.

Analysts get gold. ``rider_id`` and precise GPS never cross the serving
boundary. Three controls, applied in this order and for different reasons:

  1. **Pseudonymise** — ``sha2(rider_id)`` keeps cohort analysis possible
     ("do repeat riders take longer trips?") without exposing the identifier.
  2. **Minimise** — drop the raw column outright. A column you did not publish
     cannot leak and does not have to be found again during an erasure.
  3. **Reduce resolution** — a zone id instead of a lat/lon pair. The analyst
     question is about districts; metre resolution answers a different, more
     invasive question nobody asked.

CLI::

    python -m masar.serve.bi_view
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

SILVER_TRIPS = config.TABLES["silver.trips"].path
OUT = config.TABLES["gold.bi_trips_safe"].path

SAFE_COLUMNS = [
    "trip_id",
    "city",
    "pickup_zone_id",
    "dropoff_zone_id",
    "rider_pseudonym",
    "fare_sar",
    "distance_km",
    "duration_min",
    "surge_multiplier",
    "payment_type",
    "pickup_ts",
    "trip_date",
]


def build_bi_safe_view() -> int:
    """Build ``gold.bi_trips_safe`` from silver.

    Returns:
        Row count written.

    Raises:
        RuntimeError: if a restricted column survives into the output. The
            check is cheap and the failure mode it prevents is a notifiable
            data breach, so it runs on every build rather than in review.
    """
    from pyspark.sql import functions as F

    from masar.governance.classification import check_serving_boundary

    spark = get_spark("masar-bi-view")
    silver = spark.read.format("delta").load(SILVER_TRIPS)

    # ── TODO(lab-8): apply the three PDPL controls ────────────────────────
    #   What : add rider_pseudonym = sha2(rider_id, 256), DROP rider_id, and
    #          select only SAFE_COLUMNS (no dropoff_geohash, no lat/lon).
    #   Why  : pseudonymise for utility, drop for minimisation, coarsen for
    #          proportionality. Doing only the first leaves the raw column in
    #          the table next to its own hash, which protects nothing.
    #   Ref  : solutions/lab8_serve.py :: build_bi_safe_view
    safe = (
        silver.withColumn("rider_pseudonym", F.sha2(F.col("rider_id"), 256))
        .drop("rider_id")
        .select(*[c for c in SAFE_COLUMNS if c in silver.columns or c == "rider_pseudonym"])
    )
    # ── end TODO(lab-8) ───────────────────────────────────────────────────

    verdict = check_serving_boundary("gold.bi_trips_safe", safe.columns, allow=["rider_pseudonym"])
    print(verdict.render())
    if not verdict.ok:
        raise RuntimeError(f"PDPL boundary violation: {verdict.violations} would reach BI")

    n = safe.count()
    safe.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(OUT)
    print(f"[serve] bi_trips_safe: {n:,} rows, {len(safe.columns)} columns, no raw PII")
    return n


def main() -> None:
    """CLI entry point."""
    argparse.ArgumentParser(description="Build the PDPL-safe BI view").parse_args()
    build_bi_safe_view()


if __name__ == "__main__":
    main()
