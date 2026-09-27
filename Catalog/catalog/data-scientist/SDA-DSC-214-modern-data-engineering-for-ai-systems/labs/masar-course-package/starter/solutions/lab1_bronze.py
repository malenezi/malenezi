"""Lab 1 solution — landing raw feeds into bronze, and profiling them.

Blocks completed here:
  * ``src/masar/ingest/land_bronze.py``  :: the append-only write
  * ``src/masar/ingest/profile_bronze.py`` :: the missing-rate expressions
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import Column, DataFrame


# --------------------------------------------------------------------------
# TODO(lab-1) in src/masar/ingest/land_bronze.py :: _append
# --------------------------------------------------------------------------
def append_bronze(df: DataFrame, table: str, path: str) -> None:
    """Append-only write with the schema locked.

    Three options, three reasons:

      ``mode("append")``          bronze is an immutable ledger of what
                                  arrived. Overwrite destroys the evidence a
                                  later correction depends on.
      ``mergeSchema=false``       an upstream schema change must be LOUD. With
                                  mergeSchema on, a new column is absorbed
                                  silently and the drift Module 6 exists to
                                  catch never surfaces.
      ``option("path", ...)``     registers the table at the canonical path,
      ``+ saveAsTable``           so `bronze.trips` means the same thing in
                                  every process and to dbt.
    """
    (
        df.write.format("delta")
        .mode("append")
        .option("mergeSchema", "false")
        .option("path", path)
        .saveAsTable(table)
    )


# --------------------------------------------------------------------------
# TODO(lab-1) in src/masar/ingest/profile_bronze.py :: profile
# --------------------------------------------------------------------------
def missing_rate_exprs(df: DataFrame, n: int) -> list[Column]:
    """One missing-rate expression per column, counting '' as missing.

    The trap: bronze lands CSV with ``inferSchema=False``, so every column is
    a STRING and an absent ``dropoff_geohash`` is the empty string, not NULL.
    A profiler that counts only ``isNull()`` reports Masar's 3.1% geohash
    defect as 0.0% — and a defect that profiles clean is a defect that reaches
    the feature table as a plausible-looking zero.

    Args:
        df: the landed bronze frame.
        n: its row count (passed in so the caller counts once, not per column).

    Returns:
        Aliased columns, one per input column, each a rate in ``[0, 1]``.
    """
    from pyspark.sql import functions as F

    exprs: list[Column] = []
    for c in df.columns:
        col = F.col(f"`{c}`")
        missing = F.when(col.isNull() | (col.cast("string") == F.lit("")), 1).otherwise(0)
        exprs.append(F.round(F.sum(missing) / F.lit(n), 4).alias(c))
    return exprs


# --------------------------------------------------------------------------
# Lab 1 acceptance: the three swamp risks worth naming in LAB1_NOTES.md
# --------------------------------------------------------------------------
SWAMP_RISKS = [
    (
        "3.1% empty dropoff_geohash",
        "Lands as '' not NULL, so naive profiling reports it clean. Downstream "
        "it becomes a zone that does not exist, and the demand mart under-counts "
        "one zone by 3% forever.",
    ),
    (
        "two timestamp formats in one column",
        "~2% of rows use dd/MM/yyyy HH:mm. Landing with inferSchema=True would "
        "null exactly those rows — destroying the evidence before anyone looked "
        "at it. Bronze lands STRING; parsing happens at the silver boundary.",
    ),
    (
        "duplicate trip_id across batches",
        "Bronze is append-only, so re-landing a day doubles its rows. That is "
        "CORRECT: the batches are distinguishable by _batch_id and silver can "
        "deterministically keep the latest. Overwriting would have hidden it.",
    ),
    (
        "no _source_file would mean no lineage",
        "'Which file produced this row?' is the first question a regulator "
        "asks, and the only cheap moment to answer it is at landing time.",
    ),
]
