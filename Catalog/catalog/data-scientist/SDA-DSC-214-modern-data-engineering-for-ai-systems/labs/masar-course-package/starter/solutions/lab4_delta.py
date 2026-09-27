"""Lab 4 solution — constraints, idempotent MERGE, erasure, and VACUUM.

Blocks completed here:
  * ``src/masar/delta/create_silver.py`` :: add_constraints
  * ``src/masar/delta/merge_ops.py``     :: upsert_corrections
  * ``src/masar/delta/maintain.py``      :: vacuum_table
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

CONSTRAINTS = {
    "positive_fare": "fare_sar > 0",
    "valid_duration": "dropoff_ts > pickup_ts",
    "known_city": "city IN ('Riyadh','Jeddah','Dammam','Mecca','Medina')",
}


# --------------------------------------------------------------------------
# TODO(lab-4) in src/masar/delta/create_silver.py :: add_constraints
# --------------------------------------------------------------------------
def add_constraints(spark, path: str) -> dict[str, str]:
    """Add every CHECK constraint, skipping ones existing rows would violate.

    A CHECK constraint is enforced by the TABLE, on every future write, by
    every writer — Spark, dbt, a notebook, the stray job somebody runs at
    02:00. Validation inside one pipeline protects one pipeline.

    Delta validates a new constraint against the data already present, so the
    ALTER fails loudly if history does not comply. That failure is useful
    information: it tells you how many rows you have been promoting all along.
    """
    outcome: dict[str, str] = {}
    for name, expr in CONSTRAINTS.items():
        bad = spark.sql(f"SELECT count(*) AS n FROM delta.`{path}` WHERE NOT ({expr})").first()["n"]
        if bad:
            outcome[name] = f"skipped: {bad} rows violate"
            continue
        spark.sql(f"ALTER TABLE delta.`{path}` ADD CONSTRAINT {name} CHECK ({expr})")
        outcome[name] = "added"
    return outcome


# --------------------------------------------------------------------------
# TODO(lab-4) in src/masar/delta/merge_ops.py :: upsert_corrections
# --------------------------------------------------------------------------
def upsert_corrections(spark, corrections_df: DataFrame, target: str) -> None:
    """MERGE corrections into silver, keyed on trip_id.

    Idempotency comes from the KEY, not from luck. Running this twice updates
    the same rows to the same values; the second run creates a new Delta
    version (that is the audit trail, not a bug) but changes no data.

    ``whenMatchedUpdateAll`` is safe here for two reasons, both checked before
    the call: the source has exactly the target's schema, and exactly one row
    per key. Skip either check and a MERGE quietly does something undefined.

    The alternatives and why they lose:
      * append              -> the corrected trips exist twice
      * delete-then-insert  -> a window in which readers see neither version
      * overwrite           -> the whole table rewritten to fix five rows
    """
    from delta.tables import DeltaTable

    dupes = corrections_df.groupBy("trip_id").count().filter("count > 1").count()
    if dupes:
        raise ValueError(f"{dupes} duplicate trip_id in corrections: MERGE would be ambiguous")

    (
        DeltaTable.forPath(spark, target)
        .alias("t")
        .merge(corrections_df.alias("s"), "t.trip_id = s.trip_id")
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )


# --------------------------------------------------------------------------
# TODO(lab-4) in src/masar/delta/maintain.py :: optimize_and_vacuum
# --------------------------------------------------------------------------
def vacuum_table(spark, path: str, retain_hours: int = 168, dry_run: bool = False) -> None:
    """Reclaim storage past the retention window.

    ``RETAIN 168 HOURS`` = 7 days of time travel. It is a GOVERNANCE decision,
    written down in GOVERNANCE.md, and it is a trade-off with two real sides:

      * shorter -> less storage, less audit history, and an erasure request is
        satisfied sooner (VACUUM is what makes a delete physical);
      * longer  -> more storage, more ability to answer "what did the model
        see last Tuesday?", and personal data lingers in history longer.

    ``RETAIN 0 HOURS`` is not the aggressive end of that trade-off. It ends the
    audit trail entirely and can break a reader that is mid-query against a
    version you just removed. Delta refuses it unless you disable the retention
    check — treat having to disable a safety check as the answer.

    Always run DRY RUN first in production: its output is the list of files you
    are about to make unrecoverable.
    """
    suffix = " DRY RUN" if dry_run else ""
    spark.sql(f"VACUUM delta.`{path}` RETAIN {retain_hours} HOURS{suffix}")


def optimize_table(spark, path: str, zorder: list[str]) -> tuple[int, int]:
    """OPTIMIZE with ZORDER, returning file counts before and after.

    ZORDER on the columns queries FILTER by, not the columns they SELECT. Two
    or three columns; more dilutes the clustering until it does nothing.

    Returns:
        ``(files_before, files_after)`` — the number for BENCHMARKS.md.
    """
    before = spark.sql(f"DESCRIBE DETAIL delta.`{path}`").collect()[0]["numFiles"]
    spark.sql(f"OPTIMIZE delta.`{path}` ZORDER BY ({', '.join(zorder)})")
    after = spark.sql(f"DESCRIBE DETAIL delta.`{path}`").collect()[0]["numFiles"]
    return before, after


#: The Lab 4 discussion answers worth having written down.
LAB4_ANSWERS = {
    "what makes MERGE idempotent": (
        "The unique key. Matched rows are updated to the same values, so a "
        "repeat run is a semantic no-op even though it commits a new version."
    ),
    "why RESTORE does not erase": (
        "RESTORE creates a NEW version whose contents equal an old one. History "
        "is preserved — which is why recovery is safe, and why erasure needs "
        "VACUUM rather than RESTORE."
    ),
    "why not RETAIN 0 HOURS": (
        "It destroys the time-travel history that the audit trail and the "
        "erasure evidence both depend on, and can break concurrent readers."
    ),
    "why partition by city not trip_id": (
        "5 values versus 42,038. Partitioning by the business key creates one "
        "directory per row: a metadata storm, a tripled request bill, and a "
        "dashboard that goes from 800 ms to 40 s."
    ),
}
