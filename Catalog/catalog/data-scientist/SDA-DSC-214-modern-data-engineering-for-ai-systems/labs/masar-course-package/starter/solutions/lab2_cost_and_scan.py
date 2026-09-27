"""Lab 2 solution — the cost model's real prices, and the pruned scan query.

Blocks completed here:
  * ``src/masar/econ/cost_model.py`` :: the price sheet
  * ``src/masar/econ/scan_cost.py``  :: the partition-filtered variant
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from masar.econ.cost_model import (
    MASAR_JOBS,
    MASAR_TOTAL_GB,
    Prices,
    break_even_utilisation,
    lakehouse_monthly_cost,
    saving_pct,
    warehouse_monthly_cost,
)

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame


# --------------------------------------------------------------------------
# TODO(lab-2) in src/masar/econ/cost_model.py :: main
# --------------------------------------------------------------------------
def masar_prices() -> Prices:
    """The price sheet, with every figure sourced.

    These are the published list prices used to build the reference numbers.
    Participants must replace them with their OWN cloud's prices and cite
    provider, region and read-date in LAB2_NOTES.md — the citation is the
    deliverable, not the number. A cost model you cannot source is a rumour
    with a spreadsheet attached.

    Sources used for the reference figures:
      storage_gb_month  0.023  — S3 Standard, first 50 TB, me-south-1 list price
      core_hour         0.060  — general-purpose 4-core on-demand / 4 cores
      spot_multiplier   0.350  — published spot discount midpoint (~65% off)
      warehouse_*       0.180 / 0.210 — coupled MPP node-hour and attached storage
    """
    return Prices(
        storage_gb_month=0.023,
        core_hour=0.060,
        spot_multiplier=0.350,
        warehouse_core_hour=0.180,
        warehouse_storage_gb_month=0.210,
    )


def masar_cost_summary() -> dict:
    """The full Lab 2 comparison, as a dict for LAB2_NOTES.md.

    The number that matters is not the saving; it is ``break_even_core_hours``
    against ``actual_core_hours``. Masar runs ~510 core-hours a month against a
    break-even near 318,000 — three orders of magnitude of headroom. That is
    the honest form of the claim, and it also tells you when it would stop
    being true: a genuinely 24/7 workload.
    """
    prices = masar_prices()
    lh = lakehouse_monthly_cost(MASAR_TOTAL_GB, MASAR_JOBS, prices)
    wh = warehouse_monthly_cost(MASAR_TOTAL_GB, nodes=8, cores_per_node=16, p=prices)
    return {
        "lakehouse": lh,
        "warehouse": wh,
        "saving_pct": saving_pct(lh, wh),
        "break_even_core_hours": break_even_utilisation(MASAR_TOTAL_GB, 8, 16, prices),
        "actual_core_hours": round(sum(j.monthly_core_hours() for j in MASAR_JOBS), 1),
        "idle_share_of_warehouse": wh["idle_share"],
    }


# --------------------------------------------------------------------------
# TODO(lab-2) in src/masar/econ/scan_cost.py :: compare_scans
# --------------------------------------------------------------------------
def pruned_partition_query(df_all: DataFrame) -> DataFrame:
    """Variant C: column pruning PLUS partition and range predicates.

    Three mechanisms stack, and they are not the same mechanism:

      1. ``select(...)``      column pruning — Parquet reads only those column
                              chunks off storage.
      2. ``city == 'Riyadh'`` PARTITION pruning — ``city`` is the partition
                              column, so whole directories are skipped before
                              a single file is opened.
      3. ``pickup_ts`` range  row-group pruning — Delta's min/max statistics
                              skip row groups whose range cannot match.

    Only (2) removes files. That is why variant B and variant C can read the
    same columns and still differ by an order of magnitude in bytes scanned.
    """
    from pyspark.sql import functions as F

    return df_all.select("trip_id", "city", "pickup_ts", "fare_sar").filter(
        (F.col("city") == "Riyadh")
        & (F.col("pickup_ts") >= F.lit("2026-06-01"))
        & (F.col("pickup_ts") < F.lit("2026-06-02"))
    )
