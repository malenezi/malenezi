"""Profile a landed bronze table for swamp smells, before anyone trusts it.

A lake becomes a swamp the moment data lands faster than anyone characterises
it. This pass is cheap, runs in seconds, and produces the three things a
participant needs for LAB1_NOTES.md: a missing-rate per column, a duplicate-key
count, and the format/domain surprises hiding in the low-cardinality columns.

The pure-Python equivalent (same definitions, no JVM) is
``masar.ingest.profiling`` — it is what the unit tests exercise.

CLI::

    python -m masar.ingest.profile_bronze bronze/trips      --key trip_id
    python -m masar.ingest.profile_bronze bronze/gps_events --key event_id
    python -m masar.ingest.profile_bronze bronze/drivers    --key driver_id
"""

from __future__ import annotations

import argparse

from masar import config
from masar.ingest.profiling import DOMAIN_COLUMNS, NULL_RATE_THRESHOLDS, TIMESTAMP_COLUMNS
from masar.spark import get_spark


def profile(table_path: str, key: str | None = None, show_domains: bool = True) -> dict:
    """Profile a Delta table at ``table_path``.

    Args:
        table_path: filesystem path, e.g. ``./lakehouse/bronze/trips``.
        key: business key to check for duplicates.
        show_domains: also print value frequencies for low-cardinality columns.

    Returns:
        ``{"rows", "columns", "missing_rate", "duplicate_key_groups"}`` so a
        DAG task or a test can assert on the numbers rather than the printout.
    """
    from pyspark.sql import functions as F

    spark = get_spark("profile-bronze")
    df = spark.read.format("delta").load(table_path)
    n = df.count()
    print(f"\n=== {table_path} ===")
    print(f"rows={n:,}  columns={len(df.columns)}  partitions={df.rdd.getNumPartitions()}")
    if n == 0:
        print("(empty table — nothing to profile)")
        return {"rows": 0, "columns": df.columns, "missing_rate": {}, "duplicate_key_groups": 0}

    # ── TODO(lab-1): missing rate per column ──────────────────────────────
    #   What : compute, for every column, the fraction of rows that are
    #          missing — where missing means NULL **or** the empty string.
    #   Why  : bronze lands CSV as STRING, so an absent `dropoff_geohash` is
    #          '' and not NULL. Count only NULLs and Masar's 3.1% geohash
    #          defect profiles as 0.0% — a defect that profiles clean reaches
    #          the feature table as a plausible-looking zero.
    #   Ref  : solutions/lab1_bronze.py :: missing_rate_exprs
    missing_exprs = []
    for c in df.columns:
        col = F.col(f"`{c}`")
        missing = F.when(col.isNull() | (col.cast("string") == F.lit("")), 1).otherwise(0)
        missing_exprs.append(F.round(F.sum(missing) / F.lit(n), 4).alias(c))
    # ── end TODO(lab-1) ───────────────────────────────────────────────────

    rates = df.select(missing_exprs).first().asDict()
    print("-- missing rate per column --")
    for column, rate in rates.items():
        threshold = NULL_RATE_THRESHOLDS.get(column)
        flag = "  <-- SMELL" if threshold is not None and (rate or 0) > threshold else ""
        print(f"  {column:<24} {rate:>8.2%}{flag}")

    dupe_groups = 0
    if key and key in df.columns:
        dupes = df.groupBy(key).count().filter("count > 1")
        dupe_groups = dupes.count()
        print(f"duplicate {key} groups: {dupe_groups:,}")
        if dupe_groups:
            dupes.orderBy(F.desc("count")).show(5, truncate=False)

    for c in TIMESTAMP_COLUMNS:
        if c in df.columns:
            iso = df.filter(F.col(c).rlike(r"^\d{4}-\d{2}-\d{2}")).count()
            eu = df.filter(F.col(c).rlike(r"^\d{2}/\d{2}/\d{4}")).count()
            print(f"{c}: iso-like={iso:,}  dd/mm/yyyy-like={eu:,}  other={n - iso - eu:,}")

    if show_domains:
        for c in DOMAIN_COLUMNS:
            if c in df.columns:
                print(f"-- distinct {c} --")
                df.groupBy(c).count().orderBy(F.desc("count")).show(10, truncate=False)

    return {
        "rows": n,
        "columns": df.columns,
        "missing_rate": rates,
        "duplicate_key_groups": dupe_groups,
    }


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Profile a bronze Delta table")
    p.add_argument("table", help="path under the lakehouse root, e.g. bronze/trips")
    p.add_argument("--key", default=None, help="business key to check for duplicates")
    p.add_argument("--no-domains", action="store_true", help="skip value-frequency listings")
    args = p.parse_args()
    profile(f"{config.LAKEHOUSE_ROOT}/{args.table}", key=args.key, show_domains=not args.no_domains)


if __name__ == "__main__":
    main()
