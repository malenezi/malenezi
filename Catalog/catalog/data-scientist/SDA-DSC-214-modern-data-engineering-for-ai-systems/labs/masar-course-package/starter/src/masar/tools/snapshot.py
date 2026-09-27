"""Snapshot the whole lakehouse: row counts plus content checksums.

Lab 7's recovery drill is a diff of three snapshots — before the injected
failure, during it, and after a full re-run. Row counts alone are not enough:
two tables can have the same count and different contents, which is exactly
what a non-idempotent write produces when it overwrites instead of merging.
So each table also gets an order-independent checksum.

CLI::

    python -m masar.tools.snapshot --out /tmp/before.json
    diff <(jq -S . /tmp/before.json) <(jq -S . /tmp/after.json)
"""

from __future__ import annotations

import argparse
import json

from masar import config
from masar.spark import get_spark

#: Tables the drill compares. Bronze is excluded on purpose: re-landing
#: appends by design, so its count legitimately changes between snapshots.
SNAPSHOT_TABLES = [
    "silver.trips",
    "silver.trips_quarantine",
    "silver.vehicle_positions",
    "gold.zone_hourly_demand",
    "gold.driver_daily",
    "gold.trip_features",
    "gold.eta_features",
]


def checksum(table: str) -> str | None:
    """Order-independent checksum of a table's business content.

    Built-in and metadata columns (``_built_at``, ``_loaded_at``,
    ``_ingested_at``) are excluded: they change on every run by design, and a
    checksum that includes them would report a difference for every rebuild
    and therefore report nothing at all.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("tools-snapshot")
    path = config.table_path(table)
    if not DeltaTable.isDeltaTable(spark, path):
        return None

    df = spark.read.format("delta").load(path)
    business = [c for c in df.columns if not c.startswith("_")]
    if not business:
        return None
    row_hash = F.md5(
        F.concat_ws("|", *[F.coalesce(F.col(c).cast("string"), F.lit("~")) for c in business])
    )
    # XOR-free but order-independent: sum the hashes as big integers mod 2^63.
    digest = (
        df.select(F.conv(F.substring(row_hash, 1, 15), 16, 10).cast("decimal(38,0)").alias("h"))
        .agg(F.sum("h").alias("s"))
        .collect()[0]["s"]
    )
    return None if digest is None else f"{int(digest) % (2**63):016x}"


def snapshot(tables: list[str] | None = None) -> dict:
    """Row count and checksum for every table in the drill."""
    from delta.tables import DeltaTable

    spark = get_spark("tools-snapshot")
    tables = tables or SNAPSHOT_TABLES
    counts: dict[str, int] = {}
    checksums: dict[str, str] = {}

    for table in tables:
        path = config.table_path(table)
        if not DeltaTable.isDeltaTable(spark, path):
            continue
        counts[table] = spark.read.format("delta").load(path).count()
        digest = checksum(table)
        if digest:
            checksums[table] = digest

    return {**counts, "checksums": checksums}


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Snapshot lakehouse counts and checksums")
    p.add_argument("--out", default=None, help="write JSON here instead of stdout")
    p.add_argument("--tables", nargs="*", default=None)
    a = p.parse_args()

    result = snapshot(a.tables)
    text = json.dumps(result, indent=2, sort_keys=True)
    if a.out:
        with open(a.out, "w") as fh:
            fh.write(text + "\n")
        print(f"[snapshot] wrote {a.out}")
    print(text)


if __name__ == "__main__":
    main()
