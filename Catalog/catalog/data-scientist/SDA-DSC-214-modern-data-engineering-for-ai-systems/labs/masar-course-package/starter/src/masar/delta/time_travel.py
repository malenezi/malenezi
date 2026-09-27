"""Read a past table state for audit, diffing, and reproducible training sets.

Time travel is what makes a data platform auditable rather than merely
observable: "what did the model see on 15 June?" is answerable, exactly,
months later, without a backup.

Note what ``RESTORE`` does and does not do: it creates a NEW version whose
contents equal an old one. It does not erase history. That is why recovery is
safe — and why erasure needs VACUUM, not RESTORE.

CLI::

    python -m masar.delta.time_travel --history
    python -m masar.delta.time_travel --version 2
    python -m masar.delta.time_travel --diff 2 3
    python -m masar.delta.time_travel --restore 2
"""

from __future__ import annotations

import argparse
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

SILVER = config.TABLES["silver.trips"].path


def history(limit: int = 20, path: str = SILVER) -> None:
    """Print the commit log: who/what/when for every change to the table."""
    spark = get_spark("time-travel")
    (
        spark.sql(f"DESCRIBE HISTORY delta.`{path}` LIMIT {limit}")
        .select("version", "timestamp", "operation", "operationMetrics")
        .show(truncate=False)
    )


def as_of_version(v: int, path: str = SILVER) -> DataFrame:
    """The table exactly as it was at version ``v``."""
    return get_spark("time-travel").read.format("delta").option("versionAsOf", v).load(path)


def as_of_date(ts: str, path: str = SILVER) -> DataFrame:
    """The table as of a wall-clock timestamp, e.g. ``'2026-06-15 00:00:00'``."""
    return get_spark("time-travel").read.format("delta").option("timestampAsOf", ts).load(path)


def diff_versions(
    v_old: int, v_new: int, key: str = "trip_id", col: str = "fare_sar", path: str = SILVER
) -> int:
    """Show which rows changed between two versions, and by how much.

    This is the audit answer to "the fare on this trip changed — when, and to
    what?", produced from the table itself rather than from a changelog
    somebody had to remember to write.

    Returns:
        The number of rows whose ``col`` differs between the two versions.
    """
    from pyspark.sql import functions as F

    old = as_of_version(v_old, path).select(key, F.col(col).alias(f"{col}_old"))
    new = as_of_version(v_new, path).select(key, F.col(col).alias(f"{col}_new"))
    changed = (
        old.join(new, key)
        .filter(F.col(f"{col}_old") != F.col(f"{col}_new"))
        .withColumn("delta", F.round(F.col(f"{col}_new") - F.col(f"{col}_old"), 2))
    )
    n = changed.count()
    print(f"rows with a changed {col} between v{v_old} and v{v_new}: {n:,}")
    changed.show(truncate=False)
    return n


def restore(v: int, path: str = SILVER) -> None:
    """Restore the table to version ``v``.

    Creates a NEW version whose contents equal v — history is preserved, so
    the restore itself is auditable and reversible.
    """
    spark = get_spark("time-travel")
    spark.sql(f"RESTORE TABLE delta.`{path}` TO VERSION AS OF {v}")
    print(f"restored to v{v}; this creates a NEW version, it does not erase history")


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Delta time travel for silver.trips")
    p.add_argument("--path", default=SILVER)
    p.add_argument("--history", action="store_true")
    p.add_argument("--version", type=int, help="row count at this version")
    p.add_argument("--timestamp", help="row count as of this timestamp")
    p.add_argument("--diff", nargs=2, type=int, metavar=("OLD", "NEW"))
    p.add_argument("--column", default="fare_sar", help="column to diff")
    p.add_argument("--restore", type=int)
    a = p.parse_args()

    did_something = False
    if a.history:
        history(path=a.path)
        did_something = True
    if a.version is not None:
        print(f"rows at v{a.version}: {as_of_version(a.version, a.path).count():,}")
        did_something = True
    if a.timestamp:
        print(f"rows at {a.timestamp}: {as_of_date(a.timestamp, a.path).count():,}")
        did_something = True
    if a.diff:
        diff_versions(*a.diff, col=a.column, path=a.path)
        did_something = True
    if a.restore is not None:
        restore(a.restore, a.path)
        did_something = True
    if not did_something:
        p.print_help()


if __name__ == "__main__":
    main()
