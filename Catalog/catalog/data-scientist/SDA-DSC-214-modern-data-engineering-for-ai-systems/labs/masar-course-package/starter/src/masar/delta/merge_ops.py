"""Idempotent MERGE upserts and PDPL-compliant deletes.

Both are atomic Delta commits: auditable in ``DESCRIBE HISTORY``, retryable
without corruption, and invisible to concurrent readers until they land. That
combination is what makes "just re-run the whole thing" a safe answer to an
incident instead of a second incident.

CLI::

    python -m masar.delta.merge_ops --corrections data/fixtures/corrections/trips_corrections_2026-06-03.csv
    python -m masar.delta.merge_ops --erase-request data/fixtures/erasure_request/pdpl_erasure_2026-06-10.json
"""

from __future__ import annotations

import argparse
import glob
import json
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

SILVER = config.TABLES["silver.trips"].path


def _resolve(path: str) -> str:
    """Accept a file, a glob, or a directory of fixtures and return one path."""
    matches = sorted(glob.glob(path)) or sorted(glob.glob(f"{path.rstrip('/')}/*.csv"))
    if not matches:
        raise FileNotFoundError(f"no corrections file matched {path!r}")
    return matches[0]


def load_corrections(path: str, target: str = SILVER) -> DataFrame:
    """Read a corrections CSV using the TARGET table's schema.

    Reading the source with the target's schema is the cheap way to enforce
    the contract on the input as well as the output: a corrections file with a
    renamed or extra column fails here, at the boundary, rather than three
    steps later as a puzzling type error.
    """
    spark = get_spark("merge-ops")
    target_schema = spark.read.format("delta").load(target).schema
    return spark.read.option("header", True).schema(target_schema).csv(_resolve(path))


def upsert_corrections(corrections_df: DataFrame, target: str = SILVER) -> dict:
    """MERGE corrections into silver, keyed on ``trip_id``.

    Idempotency comes from the key, not from luck: running this twice updates
    the same rows to the same values, so the second run is a no-op in effect
    (it still creates a Delta version — that is the audit trail, not a bug).

    Raises:
        ValueError: when the source has duplicate ``trip_id`` values. A MERGE
            against an ambiguous source is undefined behaviour, and Delta is
            right to refuse it; catching it here gives a better message.

    Returns:
        The commit's ``operationMetrics``, so a caller can assert on the
        number of rows updated and inserted.
    """
    from delta.tables import DeltaTable

    spark = get_spark("merge-ops")
    dupes = corrections_df.groupBy("trip_id").count().filter("count > 1").count()
    if dupes:
        raise ValueError(f"{dupes} duplicate trip_id in corrections: MERGE would be ambiguous")

    # ── TODO(lab-4): the idempotent upsert ────────────────────────────────
    #   What : MERGE `corrections_df` into the Delta table at `target` on
    #          t.trip_id = s.trip_id; update matched rows, insert new ones.
    #   Why  : keyed MERGE is what makes re-running safe. An append would
    #          double the corrected trips; a delete-then-insert would leave a
    #          window in which readers see neither version.
    #   Ref  : solutions/lab4_delta.py :: upsert_corrections
    table = DeltaTable.forPath(spark, target)
    (
        table.alias("t")
        .merge(corrections_df.alias("s"), "t.trip_id = s.trip_id")
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )
    # ── end TODO(lab-4) ───────────────────────────────────────────────────

    last = (
        spark.sql(f"DESCRIBE HISTORY delta.`{target}` LIMIT 1")
        .select("version", "operation", "operationMetrics")
        .first()
    )
    m = dict(last["operationMetrics"] or {})
    print(
        f"v{last['version']} {last['operation']}  "
        f"updated={m.get('numTargetRowsUpdated')} inserted={m.get('numTargetRowsInserted')}"
    )
    return m


def erase_rider(rider_id: str, target: str = SILVER) -> dict:
    """PDPL right to erasure: remove one data subject's rows.

    The delete is an atomic, logged commit. It removes the rows from the
    CURRENT version immediately — but the previous versions still contain
    them, which is the point of time travel and the problem with erasure.
    Physical removal happens at the next ``VACUUM`` past the retention window.
    Until then the request has not been honoured, only recorded.

    Returns:
        ``{"rider_id", "removed", "remaining"}``.
    """
    from delta.tables import DeltaTable
    from pyspark.sql import functions as F

    spark = get_spark("merge-ops")
    table = DeltaTable.forPath(spark, target)
    before = spark.read.format("delta").load(target).filter(F.col("rider_id") == rider_id).count()
    table.delete(F.col("rider_id") == rider_id)
    after = spark.read.format("delta").load(target).filter(F.col("rider_id") == rider_id).count()
    print(
        f"erasure committed for {rider_id}: {before} rows removed, {after} remain in the "
        f"CURRENT version; run VACUUM past retention to purge history"
    )
    return {"rider_id": rider_id, "removed": before, "remaining": after}


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Delta MERGE upserts and PDPL deletes")
    p.add_argument("--corrections", help="path to a corrections CSV (file, glob or directory)")
    p.add_argument("--erase-request", help="path to a PDPL erasure request JSON")
    p.add_argument("--target", default=SILVER)
    args = p.parse_args()

    if args.corrections:
        upsert_corrections(load_corrections(args.corrections, args.target), args.target)
    if args.erase_request:
        with open(args.erase_request) as fh:
            request = json.load(fh)
        # The fixture carries a list of rider_ids under scope; a single-rider
        # request may instead carry `rider_id` at the top level.
        riders = request.get("scope", {}).get("rider_ids") or [request["rider_id"]]
        for rider in riders:
            erase_rider(rider, args.target)
    if not (args.corrections or args.erase_request):
        p.print_help()


if __name__ == "__main__":
    main()
