"""Land raw Masar source files into the bronze zone.

Bronze rules, enforced here and nowhere else:

  * **append-only** — bronze is an immutable ledger of what ARRIVED, not a
    model of what is true. Overwrite it and a bug found in week six becomes
    unfixable for weeks one to five, because the evidence is gone.
  * **as-received** — no casting, no cleaning, no dropping. Everything lands
    as STRING. ``inferSchema=True`` would *guess* at the two timestamp formats
    and silently null the 2% that do not match its guess.
  * **lineage** — every bronze table carries ``_ingested_at``, ``_source_file``
    and ``_batch_id``. Without them you cannot answer "which file produced
    this row?", which is the first question a regulator asks.

Landing the same day twice is CORRECT and the labs make you do it: the two
batches are distinguishable by ``_batch_id``, so silver can deterministically
keep the latest version per ``trip_id`` without ever having lost the earlier
one.

CLI::

    python -m masar.ingest.land_bronze --feed trips --date 2026-06-01
    python -m masar.ingest.land_bronze --feed all   --date 2026-06-01
"""

from __future__ import annotations

import argparse
import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

BRONZE = config.BRONZE
RAW = config.RAW_ROOT


def _batch_id(feed: str, business_date: str) -> str:
    """Deterministic-prefix, unique-suffix batch id: traceable AND collision-free.

    The prefix (``trips_2026-06-01_``) makes a batch greppable by feed and
    business date; the UUID suffix makes two runs of the same day distinct,
    which is exactly the property Lab 1 Task 3 relies on.
    """
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"{feed}_{business_date}_{stamp}_{uuid.uuid4().hex[:8]}"


def _with_lineage(df: DataFrame, batch_id: str) -> DataFrame:
    """Attach the three lineage columns every bronze table carries."""
    from pyspark.sql import functions as F

    return (
        df.withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_file", F.input_file_name())
        .withColumn("_batch_id", F.lit(batch_id))
    )


def _append(df: DataFrame, table: str, path: str) -> int:
    """Append-only write, registering the table in the catalog at ``path``.

    Args:
        df: the lineage-tagged frame.
        table: canonical name, e.g. ``bronze.trips``.
        path: canonical storage path.

    Returns:
        The table's TOTAL row count after the append — not the batch size,
        because the number participants must reason about in Lab 1 is the
        ledger's height, not this run's contribution.
    """
    spark = get_spark("land-bronze")
    spark.sql("CREATE DATABASE IF NOT EXISTS bronze")
    n = df.count()

    # ── TODO(lab-1): make this write append-only, with schema locked ──────
    #   What : write `df` as Delta in APPEND mode to `path`, registered as
    #          `table`, with mergeSchema disabled.
    #   Why  : `mode("overwrite")` destroys the ledger; `mergeSchema=true`
    #          lets an upstream schema change slip in unannounced, which is
    #          precisely the drift Module 6 exists to catch.
    #   Ref  : solutions/lab1_bronze.py :: append_bronze
    (
        df.write.format("delta")
        .mode("append")  # NEVER overwrite: bronze is an immutable ledger
        .option("mergeSchema", "false")  # drift must be loud, not absorbed
        .option("path", path)
        .saveAsTable(table)
    )
    # ── end TODO(lab-1) ───────────────────────────────────────────────────

    total = spark.read.format("delta").load(path).count()
    print(f"Landed {n:,} rows -> {path}  (append, total now {total:,})")
    return total


def _read_csv(path: str) -> DataFrame:
    """Read a raw CSV exactly as delivered: header on, everything a STRING."""
    spark = get_spark("land-bronze")
    return (
        spark.read.option("header", True)
        .option("mode", "PERMISSIVE")  # keep malformed rows, do NOT drop them
        .option("inferSchema", False)  # as-received; typing happens in silver
        .csv(path)
    )


def land_trips(business_date: str | None = None, **_: object) -> int:
    """Land ``data/raw/trips_<date>.csv`` into ``bronze.trips``.

    Args:
        business_date: ``YYYY-MM-DD``; defaults to ``MASAR_BUSINESS_DATE``.

    Returns:
        Total rows in ``bronze.trips`` after the append.
    """
    date = business_date or config.BUSINESS_DATE
    batch_id = _batch_id("trips", date)
    raw = _read_csv(config.raw_path("trips", date))
    return _append(_with_lineage(raw, batch_id), "bronze.trips", f"{BRONZE}/trips")


def land_gps(business_date: str | None = None, **_: object) -> int:
    """Land the NDJSON GPS feed into ``bronze.gps_events``.

    The pings arrive with a nested ``payload`` struct. Bronze keeps the struct
    AS RECEIVED — flattening is a silver decision, and flattening early is how
    you lose the ability to prove what the device actually sent.
    """
    date = business_date or config.BUSINESS_DATE
    batch_id = _batch_id("gps", date)
    spark = get_spark("land-bronze")
    raw = spark.read.json(config.raw_path("gps", date))  # schema-on-read
    return _append(_with_lineage(raw, batch_id), "bronze.gps_events", f"{BRONZE}/gps_events")


def land_drivers(**_: object) -> int:
    """Land the driver roster. ``hire_date`` has MIXED formats — keep it a string."""
    batch_id = _batch_id("drivers", datetime.now(UTC).strftime("%Y-%m-%d"))
    raw = _read_csv(config.raw_path("drivers"))
    return _append(_with_lineage(raw, batch_id), "bronze.drivers", f"{BRONZE}/drivers")


def land_vehicles(**_: object) -> int:
    """Land the vehicle roster (reference data; small, slowly changing)."""
    batch_id = _batch_id("vehicles", datetime.now(UTC).strftime("%Y-%m-%d"))
    raw = _read_csv(config.raw_path("vehicles"))
    return _append(_with_lineage(raw, batch_id), "bronze.vehicles", f"{BRONZE}/vehicles")


def land_zones(**_: object) -> int:
    """Land the zone reference data (bilingual labels + centroids)."""
    batch_id = _batch_id("zones", datetime.now(UTC).strftime("%Y-%m-%d"))
    raw = _read_csv(config.raw_path("zones"))
    return _append(_with_lineage(raw, batch_id), "bronze.zones", f"{BRONZE}/zones")


def land_payments(business_date: str | None = None, **_: object) -> int:
    """Land the daily payment settlements into ``bronze.payments``."""
    date = business_date or config.BUSINESS_DATE
    batch_id = _batch_id("payments", date)
    raw = _read_csv(config.raw_path("payments", date))
    return _append(_with_lineage(raw, batch_id), "bronze.payments", f"{BRONZE}/payments")


FEEDS = {
    "trips": land_trips,
    "gps": land_gps,
    "drivers": land_drivers,
    "vehicles": land_vehicles,
    "zones": land_zones,
    "payments": land_payments,
}


def land_all(business_date: str | None = None, **_: object) -> dict[str, int]:
    """Land every feed for one business date. The DAG's ``land_bronze`` task."""
    date = business_date or config.BUSINESS_DATE
    return {
        "trips": land_trips(date),
        "gps": land_gps(date),
        "payments": land_payments(date),
        "drivers": land_drivers(),
        "vehicles": land_vehicles(),
        "zones": land_zones(),
    }


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Land a Masar raw feed into bronze")
    p.add_argument("--feed", required=True, choices=[*FEEDS, "all"])
    p.add_argument("--date", default=config.BUSINESS_DATE, help="business date YYYY-MM-DD")
    args = p.parse_args()

    if args.feed == "all":
        land_all(args.date)
    elif args.feed in ("drivers", "vehicles", "zones"):
        FEEDS[args.feed]()
    else:
        FEEDS[args.feed](args.date)


if __name__ == "__main__":
    main()
