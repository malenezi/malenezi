"""PDPL retention and erasure. Every deletion is an auditable Delta commit.

Two obligations that people conflate, and two different mechanisms:

    RETENTION  scheduled, blanket, time-based.  DELETE WHERE ts < cutoff
    ERASURE    on request, targeted, subject.   DELETE by rider_id + VACUUM

VACUUM is what makes erasure REAL. Delete alone removes the rows from the
current version; the previous versions still contain them, reachable by time
travel. Until the VACUUM past retention runs, the request has been recorded,
not honoured — and saying otherwise to a regulator is worse than not deleting.

The tension is deliberate and worth sitting with: the time travel that makes
the platform auditable is the same feature that makes erasure slow.

CLI::

    python -m masar.governance.retention --classify
    python -m masar.governance.retention --enforce-gps-retention --dry-run
    python -m masar.governance.retention --erase-rider RDR-006890 --ticket PDPL-2026-0113 --dry-run
    python -m masar.governance.retention --erase-request data/fixtures/erasure_request/pdpl_erasure_2026-06-10.json --execute
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime

from masar import config
from masar.governance.classification import CLASSIFICATION, classify_columns
from masar.spark import get_spark

GPS_RETENTION_DAYS = config.GPS_RETENTION_DAYS
RETAIN_HOURS = config.VACUUM_RETAIN_HOURS
AUDIT_LOG = f"{config.GOVERNANCE_ROOT}/erasure_audit"

#: Every table that holds a rider identifier, and how erasure reaches it.
#: ``bronze.trips`` is included on purpose: an erasure that stops at silver
#: leaves the subject's data in the landing zone, which is still processing.
ERASURE_TARGETS: dict[str, str] = {
    "bronze.trips": config.TABLES["bronze.trips"].path,
    "silver.trips": config.TABLES["silver.trips"].path,
    "silver.trips_quarantine": config.TABLES["silver.trips_quarantine"].path,
    "gold.fact_trip": config.TABLES["gold.fact_trip"].path,
}


def _hash(value: str) -> str:
    """Short SHA-256 of an identifier, for the audit log.

    The audit record must prove WHICH request was executed without itself
    becoming a register of the people who asked to be forgotten.
    """
    return hashlib.sha256(value.encode()).hexdigest()[:16]


def print_classification() -> dict[str, str]:
    """Print the column classification. The root of every other control."""
    print(f"{'column':<24} {'classification':<26} retention")
    print("-" * 70)
    from masar.governance.classification import retention_days

    for column, cls in sorted(CLASSIFICATION.items(), key=lambda kv: (kv[1], kv[0])):
        days = retention_days(column)
        window = f"{days}d" if days else "no PDPL limit"
        print(f"{column:<24} {cls:<26} {window}")
    return dict(CLASSIFICATION)


def enforce_gps_retention(dry_run: bool = True, copy_first: bool = False) -> int:
    """Blanket retention on precise location: delete positions past the window.

    Minimisation, not deletion for its own sake. Masar does not need
    metre-resolution traces from eight months ago to run a ride-hailing
    network, and keeping them is a liability with no offsetting value.

    Args:
        dry_run: count what would go, delete nothing. The default, on purpose.
        copy_first: operate on a copy of the table (``*_retention_drill``) so
            Lab 6 can run the drill without destroying the shared dataset.

    Returns:
        Rows older than the retention window.
    """
    from delta.tables import DeltaTable

    spark = get_spark("pdpl-retention")
    path = config.TABLES["silver.vehicle_positions"].path

    if copy_first:
        drill = f"{path}_retention_drill"
        spark.read.format("delta").load(path).write.format("delta").mode("overwrite").save(drill)
        print(f"[pdpl] operating on a copy: {drill}")
        path = drill

    predicate = f"event_ts < current_date() - INTERVAL {GPS_RETENTION_DAYS} DAYS"
    n = spark.read.format("delta").load(path).where(predicate).count()
    print(f"[pdpl] retention: {n:,} rows older than {GPS_RETENTION_DAYS}d in {path}")

    if not dry_run and n:
        # ── TODO(lab-6): make the retention deletion physical ─────────────
        #   What : DELETE the rows matching `predicate`, then VACUUM the table
        #          with RETAIN {RETAIN_HOURS} HOURS.
        #   Why  : the DELETE alone rewrites the current version; the old
        #          files are still on disk and still reachable by time travel.
        #          Minimisation is only satisfied once VACUUM removes them.
        #   Ref  : solutions/lab6_quality.py :: enforce_retention
        DeltaTable.forPath(spark, path).delete(predicate)
        spark.sql(f"VACUUM delta.`{path}` RETAIN {RETAIN_HOURS} HOURS")
        # ── end TODO(lab-6) ───────────────────────────────────────────────
        print(f"[pdpl] deleted {n:,} rows + VACUUM RETAIN {RETAIN_HOURS} HOURS")

    return n


def erase_rider(rider_id: str, ticket_ref: str, dry_run: bool = True) -> dict:
    """Execute a data-subject erasure request across every table in scope.

    Args:
        rider_id: the data subject's identifier.
        ticket_ref: the DPO ticket. An erasure with no ticket reference is an
            unexplained deletion, which is its own compliance problem.
        dry_run: count only.

    Returns:
        The audit record. Written to the audit log when actually executed.

    Notes:
        GPS pings are keyed by ``trip_id``/``vehicle_id``, not ``rider_id``.
        Erasing rider rows from ``silver.trips`` therefore does NOT reach the
        subject's precise location trace — that requires following the
        ``trip_id`` join first, which is exactly what
        ``erase_rider_positions`` does and why it is a separate step.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("pdpl-erasure")
    counts: dict[str, int] = {}

    for name, path in ERASURE_TARGETS.items():
        if not DeltaTable.isDeltaTable(spark, path):
            continue
        df = spark.read.format("delta").load(path)
        if "rider_id" not in df.columns:
            continue
        n = df.where(F.col("rider_id") == rider_id).count()
        counts[name] = n
        if not dry_run and n:
            DeltaTable.forPath(spark, path).delete(F.col("rider_id") == rider_id)
            spark.sql(f"VACUUM delta.`{path}` RETAIN {RETAIN_HOURS} HOURS")

    record = {
        "ticket_ref": ticket_ref,
        "rider_id_hash": _hash(rider_id),
        "executed_at": datetime.now(UTC).isoformat(),
        "rows_deleted": counts,
        "dry_run": dry_run,
        "vacuum_retain_hours": RETAIN_HOURS,
    }
    if not dry_run:
        _append_audit(record)
    print(f"[pdpl] erasure {ticket_ref}: {counts} (dry_run={dry_run})")
    return record


def erase_rider_positions(rider_id: str, dry_run: bool = True) -> int:
    """Follow the ``trip_id`` join to erase the subject's GPS trace.

    The trap this closes: ``silver.vehicle_positions`` has no ``rider_id``, so
    a rider-keyed delete misses it entirely and precise location for a person
    who asked to be forgotten survives the erasure.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("pdpl-erasure")
    trips_path = config.TABLES["silver.trips"].path
    positions_path = config.TABLES["silver.vehicle_positions"].path
    if not DeltaTable.isDeltaTable(spark, positions_path):
        return 0

    trip_ids = [
        r["trip_id"]
        for r in spark.read.format("delta")
        .load(trips_path)
        .where(F.col("rider_id") == rider_id)
        .select("trip_id")
        .distinct()
        .collect()
    ]
    if not trip_ids:
        print(f"[pdpl] no trips found for {rider_id}; nothing to erase in positions")
        return 0

    positions = spark.read.format("delta").load(positions_path)
    n = positions.where(F.col("trip_id").isin(trip_ids)).count()
    print(f"[pdpl] positions in scope via trip_id join: {n:,} pings across {len(trip_ids)} trips")
    if not dry_run and n:
        DeltaTable.forPath(spark, positions_path).delete(F.col("trip_id").isin(trip_ids))
        spark.sql(f"VACUUM delta.`{positions_path}` RETAIN {RETAIN_HOURS} HOURS")
    return n


def execute_request(request_path: str, dry_run: bool = True) -> list[dict]:
    """Execute a whole erasure-request JSON (the fixture's shape)."""
    with open(request_path) as fh:
        request = json.load(fh)
    ticket = request.get("request_id", "PDPL-UNKNOWN")
    riders = request.get("scope", {}).get("rider_ids") or [request["rider_id"]]
    records = []
    for rider in riders:
        records.append(erase_rider(rider, ticket, dry_run))
        erase_rider_positions(rider, dry_run)
    return records


def _append_audit(record: dict) -> None:
    """Append one immutable audit row. The evidence the DPO reports against."""
    spark = get_spark("pdpl-erasure")
    (
        spark.createDataFrame([(json.dumps(record),)], "record string")
        .write.format("delta")
        .mode("append")
        .save(AUDIT_LOG)
    )


def audit_table_classification(table: str) -> dict[str, str]:
    """Classify every column of a live table — a governance smoke test."""
    spark = get_spark("pdpl-classify")
    columns = spark.read.format("delta").load(config.table_path(table)).columns
    result = classify_columns(columns)
    for column, cls in result.items():
        print(f"  {column:<24} {cls}")
    return result


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="PDPL retention and erasure")
    p.add_argument("--classify", action="store_true", help="print the column classification")
    p.add_argument("--classify-table", help="classify a live table's columns")
    p.add_argument("--enforce-gps-retention", action="store_true")
    p.add_argument("--copy-first", action="store_true", help="run the drill on a copy")
    p.add_argument("--erase-rider")
    p.add_argument("--erase-request", help="path to an erasure-request JSON")
    p.add_argument("--ticket", default="PDPL-DRILL")
    p.add_argument("--dry-run", action="store_true", default=None)
    p.add_argument("--execute", action="store_true", help="actually delete (overrides --dry-run)")
    a = p.parse_args()

    dry_run = not a.execute if a.dry_run is None else (a.dry_run and not a.execute)

    if a.classify:
        print_classification()
    if a.classify_table:
        audit_table_classification(a.classify_table)
    if a.enforce_gps_retention:
        enforce_gps_retention(dry_run=dry_run, copy_first=a.copy_first)
    if a.erase_rider:
        erase_rider(a.erase_rider, a.ticket, dry_run=dry_run)
        erase_rider_positions(a.erase_rider, dry_run=dry_run)
    if a.erase_request:
        execute_request(a.erase_request, dry_run=dry_run)
    if not any(
        [a.classify, a.classify_table, a.enforce_gps_retention, a.erase_rider, a.erase_request]
    ):
        p.print_help()


if __name__ == "__main__":
    main()
