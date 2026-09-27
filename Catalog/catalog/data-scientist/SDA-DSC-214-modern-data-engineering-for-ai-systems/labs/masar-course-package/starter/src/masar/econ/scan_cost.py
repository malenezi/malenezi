"""Measure the columnar / data-skipping advantage instead of assuming it.

Decoupled compute is billed for the BYTES IT SCANS, so "columnar is faster" is
not an aesthetic claim — it is the line item. This module runs the same
question three ways and reports what each one actually read:

    A. naive full read              every column, filter applied after
    B. column-pruned                only the three columns the question needs
    C. pruned + partition filter    whole directories skipped before any read

All three return the same answer. Only one of them is cheap.

CLI::

    python -m masar.econ.scan_cost lakehouse/silver/trips
"""

from __future__ import annotations

import argparse
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

SILVER = config.TABLES["silver.trips"].path


def scan_metrics(df: DataFrame) -> dict[str, int]:
    """Execute a plan and read back the scan metrics Spark recorded.

    ``number of files read`` and ``size of files read`` come from the file-scan
    node of the executed plan. They are the honest measure of what decoupled
    compute paid for — wall-clock time on a warm page cache is not.

    Args:
        df: an unexecuted DataFrame. It is counted here to force execution.

    Returns:
        A dict of metric name to accumulated value across every scan node.
        Metric names differ slightly between Spark builds, so callers should
        look up several candidates (see :func:`compare_scans`).
    """
    df.count()  # force execution; metrics do not exist before the job runs
    plan = df._jdf.queryExecution().executedPlan()
    out: dict[str, int] = {}

    def walk(node) -> None:
        it = node.metrics().iterator()
        while it.hasNext():
            entry = it.next()
            key, metric = entry._1(), entry._2()
            label = metric.name().get() if metric.name().isDefined() else key
            for name in {key, label}:
                if any(token in name for token in ("file", "Files", "numOutputRows", "size")):
                    out[name] = out.get(name, 0) + metric.value()
        kids = node.children().iterator()
        while kids.hasNext():
            walk(kids.next())

    walk(plan)
    return out


def _metric(m: dict[str, int], *names: str) -> int:
    """First metric present under any of ``names``; 0 when none are."""
    for name in names:
        if name in m:
            return m[name]
    return 0


def compare_scans(silver_path: str = SILVER) -> list[dict]:
    """Run the three variants and print bytes scanned for each.

    Returns:
        One dict per variant, so LAB2_NOTES.md can be filled from data rather
        than from memory.
    """
    from pyspark.sql import functions as F

    spark = get_spark("scan-cost")
    df_all = spark.read.format("delta").load(silver_path)
    total_cols = len(df_all.columns)

    naive = df_all.filter(F.col("city") == "Riyadh")
    pruned = df_all.select("trip_id", "city", "fare_sar").filter(F.col("city") == "Riyadh")

    # ── TODO(lab-2): add the partition-filtered variant ───────────────────
    #   What : build variant C — the same three columns PLUS a predicate on
    #          the partition column and a narrow `pickup_ts` range.
    #   Why  : `city` is the partition column, so a predicate on it lets Spark
    #          skip whole directories without opening a single Parquet file.
    #          The `pickup_ts` range then prunes row groups via min/max stats.
    #          This is the variant that shows the cost difference; without it
    #          you are only measuring column pruning.
    #   Ref  : solutions/lab2_cost_and_scan.py :: pruned_partition_query
    pruned_part = df_all.select("trip_id", "city", "pickup_ts", "fare_sar").filter(
        (F.col("city") == "Riyadh")
        & (F.col("pickup_ts") >= F.lit("2026-06-01"))
        & (F.col("pickup_ts") < F.lit("2026-06-02"))
    )
    # ── end TODO(lab-2) ───────────────────────────────────────────────────

    results = []
    for label, query, cols in (
        ("naive full read", naive, total_cols),
        ("column-pruned", pruned, 3),
        ("pruned + partition filter", pruned_part, 4),
    ):
        m = scan_metrics(query)
        files = _metric(m, "number of files read", "numFiles")
        size = _metric(m, "size of files read", "filesSize")
        rows = _metric(m, "numOutputRows")
        results.append(
            {"variant": label, "rows": rows, "columns": cols, "files": files, "bytes": size}
        )
        print(
            f"{label:28s} rows={rows:>9,} cols={cols:>2}/{total_cols} "
            f"files={files:>4} bytes={size:>12,}"
        )

    base = results[0]["bytes"] or 1
    for r in results[1:]:
        print(f"  {r['variant']}: {100 * (1 - r['bytes'] / base):.1f}% fewer bytes than naive")

    print("\n--- physical plan of the pruned query ---")
    pruned.explain("formatted")
    print("\n--- physical plan of the pruned + partition-filtered query ---")
    pruned_part.explain("formatted")
    return results


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Measure bytes scanned for three query shapes")
    p.add_argument("path", nargs="?", default=SILVER, help="path to a Delta table")
    args = p.parse_args()
    compare_scans(args.path)


if __name__ == "__main__":
    main()
