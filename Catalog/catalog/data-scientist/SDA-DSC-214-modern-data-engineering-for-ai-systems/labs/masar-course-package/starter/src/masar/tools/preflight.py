"""Preflight: is every upstream component this lab depends on actually there?

Ninety percent of "the lab does not work" is an upstream table that was never
built, or was built and then emptied by a rerun. Checking takes four seconds
and saves twenty minutes of debugging the wrong layer.

CLI::

    python -m masar.tools.preflight --lab 7
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

#: lab number -> [(table, minimum rows, unique key or None)]
REQUIREMENTS: dict[int, list[tuple[str, int, str | None]]] = {
    1: [],
    2: [("bronze.trips", 1, None)],
    3: [("bronze.trips", 1, None), ("bronze.drivers", 1, None)],
    4: [("silver.trips", 1, "trip_id")],
    5: [("bronze.trips", 1, None)],
    6: [("silver.trips", 1, "trip_id")],
    7: [
        ("bronze.trips", 1, None),
        ("bronze.gps_events", 1, None),
        ("silver.trips", 1, "trip_id"),
        ("silver.vehicle_positions", 1, "event_id"),
        ("silver.drivers", 1, "driver_id"),
    ],
    8: [
        ("silver.trips", 1, "trip_id"),
        ("silver.vehicle_positions", 1, "event_id"),
        ("gold.zone_hourly_demand", 1, None),
        ("gold.trip_features", 1, "trip_id"),
    ],
}


def preflight(lab: int) -> bool:
    """Check every requirement for ``lab``; print one line each.

    Returns:
        True when everything the lab needs is present and well-formed.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("tools-preflight")
    ok = True

    for table, min_rows, key in REQUIREMENTS.get(lab, []):
        path = config.table_path(table)
        if not DeltaTable.isDeltaTable(spark, path):
            print(f"[preflight] {table:<26} MISSING at {path}")
            ok = False
            continue

        df = spark.read.format("delta").load(path)
        n = df.count()
        detail = f"{n:>12,} rows"
        status = "OK"

        if n < min_rows:
            status = f"TOO FEW (need >= {min_rows:,})"
            ok = False
        if key:
            distinct = df.select(key).distinct().count()
            detail += f"   unique {key} = {distinct:,}"
            if distinct != n and table.startswith("silver"):
                status = "GRAIN VIOLATION"
                ok = False
        if "_ingested_at" in df.columns and n:
            last = df.agg(F.max("_ingested_at").alias("m")).collect()[0]["m"]
            detail += f"   last _ingested_at {last}"

        print(f"[preflight] {table:<26} {detail}   {status}")

    print(f"[preflight] lab {lab}: {'ready' if ok else 'NOT READY — build the missing upstreams'}")
    return ok


def main() -> None:
    """CLI entry point. Exits 1 when the lab's prerequisites are missing."""
    p = argparse.ArgumentParser(description="Check a lab's upstream prerequisites")
    p.add_argument("--lab", type=int, required=True, choices=sorted(REQUIREMENTS))
    a = p.parse_args()
    raise SystemExit(0 if preflight(a.lab) else 1)


if __name__ == "__main__":
    main()
