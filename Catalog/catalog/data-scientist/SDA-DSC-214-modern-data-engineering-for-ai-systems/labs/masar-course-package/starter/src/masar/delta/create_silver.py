"""Harden ``silver.trips`` into a self-validating Delta table.

Two decisions live here, and both are the kind that look small and are not:

  * **Partitioning.** ``city`` has five values. ``trip_id`` has 42,038. Choose
    the second and every write produces 42,038 directories, every read pays a
    metadata storm, and the object-storage request bill triples. Partition on
    a column with tens-to-hundreds of values, never on the business key.
  * **CHECK constraints.** A constraint is enforced on EVERY future write, by
    the table, forever. That is qualitatively different from a downstream job
    that validates *if someone remembers to call it*. The table defends its own
    contract.

CLI::

    python -m masar.delta.create_silver
"""

from __future__ import annotations

import argparse
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

SILVER = config.TABLES["silver.trips"].path

#: The silver contract, as constraints the storage layer enforces itself.
CONSTRAINTS: dict[str, str] = {
    "positive_fare": "fare_sar > 0",
    "valid_duration": "dropoff_ts > pickup_ts",
    "known_city": "city IN ('Riyadh','Jeddah','Dammam','Mecca','Medina')",
}


def create_silver_trips(staged_df: DataFrame, path: str = SILVER) -> None:
    """Write a staged frame as the partitioned silver Delta table.

    Only needed when ``silver.trips`` does not already exist — dbt normally
    builds it (Lab 3). Lab 4 uses this to create the table it then constrains.
    """
    (
        staged_df.write.format("delta")
        .partitionBy("city")  # low cardinality: 5 cities, not 42,038 trip ids
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(path)
    )
    print(f"[delta] wrote silver.trips to {path}, partitioned by city")


def add_constraints(path: str = SILVER) -> dict[str, str]:
    """Add every CHECK constraint, skipping any the existing rows violate.

    Delta validates a new constraint against the data already in the table, so
    ``ALTER TABLE ... ADD CONSTRAINT`` fails loudly if history does not comply.
    That is correct behaviour and the message is the useful part — it tells you
    how many rows you would have been promoting all along.

    Returns:
        ``{constraint_name: "added" | "skipped: N rows violate"}``.
    """
    spark = get_spark("delta-constraints")
    outcome: dict[str, str] = {}

    for name, expr in CONSTRAINTS.items():
        bad = spark.sql(f"SELECT count(*) AS n FROM delta.`{path}` WHERE NOT ({expr})").first()["n"]
        if bad:
            outcome[name] = f"skipped: {bad} rows violate"
            print(f"[skip] {name}: {bad:,} existing rows violate `{expr}` — clean them first")
            continue

        # ── TODO(lab-4): add the CHECK constraint ─────────────────────────
        #   What : ALTER the Delta table to add CHECK (<expr>) named <name>.
        #   Why  : a constraint on the table is enforced on every future
        #          write by every writer — Spark, dbt, a notebook, a stray
        #          job someone runs at 02:00. Validation in one pipeline
        #          protects one pipeline.
        #   Ref  : solutions/lab4_delta.py :: add_constraints
        spark.sql(f"ALTER TABLE delta.`{path}` ADD CONSTRAINT {name} CHECK ({expr})")
        # ── end TODO(lab-4) ────────────────────────────────────────────────

        outcome[name] = "added"
        print(f"[ok]   {name}: CHECK ({expr})")

    return outcome


def show_properties(path: str = SILVER) -> None:
    """Print table properties — the constraints appear as ``delta.constraints.*``."""
    get_spark("delta-constraints").sql(f"SHOW TBLPROPERTIES delta.`{path}`").show(truncate=False)


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Constrain silver.trips")
    p.add_argument("--path", default=SILVER)
    p.add_argument("--show", action="store_true", help="only print table properties")
    args = p.parse_args()
    if args.show:
        show_properties(args.path)
        return
    add_constraints(args.path)
    show_properties(args.path)


if __name__ == "__main__":
    main()
