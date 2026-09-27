"""OPTIMIZE and VACUUM as a scheduled DAG task, not a manual afterthought.

Streaming ingest and frequent MERGEs both produce small files. Small files are
not a tidiness problem — they are a cost and latency problem: every file is a
metadata entry, a request against object storage, and a task in the scheduler.

    OPTIMIZE  compacts small files and, with ZORDER, co-locates related rows so
              min/max statistics prune far more aggressively.
    VACUUM    reclaims storage for files no longer referenced by any version
              inside the retention window.

``RETAIN 168 HOURS`` (7 days) is a GOVERNANCE decision, documented in
``docs/GOVERNANCE_TEMPLATE.md``. It is never 0: retention 0 destroys the audit
history the PDPL erasure evidence depends on and can break readers mid-query.

CLI::

    python -m masar.delta.maintain               # optimize + vacuum everything
    python -m masar.delta.maintain --dry-run     # show what VACUUM would remove
"""

from __future__ import annotations

import argparse

from masar import config
from masar.spark import get_spark

#: table path -> ZORDER columns. ZORDER on the columns queries FILTER by,
#: not the columns they select. Two or three; more dilutes the clustering.
TABLES: dict[str, list[str]] = {
    config.TABLES["bronze.gps_events"].path: ["vehicle_id", "trip_id"],
    config.TABLES["silver.trips"].path: ["city", "pickup_ts"],
    config.TABLES["silver.vehicle_positions"].path: ["vehicle_id", "event_ts"],
    config.TABLES["gold.zone_hourly_demand"].path: ["city", "pickup_zone_id"],
    config.TABLES["gold.driver_daily"].path: ["driver_id"],
    config.TABLES["gold.trip_features"].path: ["city", "pickup_zone_id"],
}

RETAIN_HOURS = config.VACUUM_RETAIN_HOURS


def _num_files(spark, path: str) -> int:
    """File count from ``DESCRIBE DETAIL`` — the number OPTIMIZE moves."""
    return spark.sql(f"DESCRIBE DETAIL delta.`{path}`").collect()[0]["numFiles"]


def optimize_and_vacuum(dry_run: bool = False, **_: object) -> dict[str, dict]:
    """Compact and vacuum every registered table; report files before/after.

    Missing tables are skipped with a note rather than raising: on Day 3 the
    streaming tables do not exist yet, and a maintenance task that refuses to
    run because an unrelated table is absent is a maintenance task nobody runs.

    Args:
        dry_run: run ``VACUUM ... DRY RUN`` instead of deleting. Always do this
            first in production — the output is the list of files you are about
            to make unrecoverable.

    Returns:
        ``{path: {"files_before", "files_after"}}`` for every table processed.
    """
    from delta.tables import DeltaTable

    spark = get_spark("delta-maintain")
    report: dict[str, dict] = {}

    for path, zorder in TABLES.items():
        if not DeltaTable.isDeltaTable(spark, path):
            print(f"[maintain] {path}: not a Delta table yet — skipped")
            continue

        before = _num_files(spark, path)
        spark.sql(f"OPTIMIZE delta.`{path}` ZORDER BY ({', '.join(zorder)})")

        # ── TODO(lab-4): reclaim storage safely ───────────────────────────
        #   What : VACUUM the table with RETAIN {RETAIN_HOURS} HOURS.
        #   Why  : 168h keeps 7 days of time travel — enough to answer "what
        #          did the model see last Tuesday?" and to prove an erasure
        #          took effect. RETAIN 0 HOURS is the destructive shortcut
        #          that ends the audit trail and can break concurrent readers.
        #   Ref  : solutions/lab4_delta.py :: vacuum_table
        suffix = " DRY RUN" if dry_run else ""
        spark.sql(f"VACUUM delta.`{path}` RETAIN {RETAIN_HOURS} HOURS{suffix}")
        # ── end TODO(lab-4) ───────────────────────────────────────────────

        after = _num_files(spark, path)
        report[path] = {"files_before": before, "files_after": after}
        print(f"[maintain] {path}: numFiles {before} -> {after}")

    return report


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="OPTIMIZE + VACUUM the Masar Delta tables")
    p.add_argument("--dry-run", action="store_true", help="VACUUM DRY RUN: delete nothing")
    args = p.parse_args()
    optimize_and_vacuum(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
