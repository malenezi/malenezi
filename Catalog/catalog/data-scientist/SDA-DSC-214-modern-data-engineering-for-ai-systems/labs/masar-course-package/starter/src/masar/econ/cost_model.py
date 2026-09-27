"""Transparent storage-vs-compute cost model for the Masar platform.

All prices are INPUTS. The point is not to produce a number, it is to SEE
which axis dominates and to be able to defend every figure in an architecture
review. A spreadsheet nobody can audit is not a cost model; it is a rumour.

Pure Python: no Spark, no network. That is deliberate — the model has to run
in a meeting, on a laptop, in five seconds.

Sources (Lab 2 Task 1 — replace the placeholders and cite them in LAB2_NOTES.md):
    storage_gb_month : <provider> standard object storage, <region>, list price, read <date>
    core_hour        : <provider> general-purpose 4-core node, <region>, on-demand, read <date>
    spot_multiplier  : <provider> published spot/preemptible discount, read <date>
"""

from __future__ import annotations

from dataclasses import dataclass, replace

HOURS_PER_MONTH = 730.0


@dataclass(frozen=True)
class Prices:
    """Unit prices, in USD. Frozen so a scenario cannot mutate the baseline.

    Attributes:
        storage_gb_month: object storage, $/GB-month. Cheap, linear, boring —
            which is exactly why keeping history is affordable in a lakehouse.
        core_hour: decoupled compute, $/core-hour, on-demand.
        spot_multiplier: spot price as a fraction of on-demand. 0.35 means
            spot is ~65% cheaper. Only safe for restartable work.
        warehouse_core_hour: coupled MPP warehouse, $/core-hour. Higher,
            AND billed 24/7 because the cluster cannot be turned off without
            taking the storage offline with it.
        warehouse_storage_gb_month: storage inside the warehouse node — an
            order of magnitude above object storage, because it is really
            attached block storage sized for the cluster.
    """

    storage_gb_month: float = 0.023
    core_hour: float = 0.06
    spot_multiplier: float = 0.35
    warehouse_core_hour: float = 0.18
    warehouse_storage_gb_month: float = 0.21


@dataclass(frozen=True)
class Job:
    """One scheduled workload on the decoupled platform.

    Attributes:
        name: the job as the team names it (``nightly_elt``), not a job id.
        cores: cores requested for the run.
        runtime_hours: wall-clock hours of a single run.
        runs_per_month: how often it runs. 720 = hourly.
        spot: whether the job tolerates preemption. Restartable ELT does;
            a job holding a 40-minute uncommitted shuffle does not.
    """

    name: str
    cores: int
    runtime_hours: float
    runs_per_month: int
    spot: bool = False

    def monthly_core_hours(self) -> float:
        """Core-hours this job consumes per month — the unit the bill is in."""
        return self.cores * self.runtime_hours * self.runs_per_month

    def monthly_compute(self, p: Prices) -> float:
        """Monthly compute cost in USD, honouring the spot discount if claimed."""
        rate = p.core_hour * (p.spot_multiplier if self.spot else 1.0)
        return self.monthly_core_hours() * rate


def lakehouse_monthly_cost(
    total_gb: float, jobs: list[Job], p: Prices | None = None
) -> dict[str, float]:
    """Decoupled cost: pay per byte KEPT plus per second of compute that RUNS.

    Args:
        total_gb: everything stored — bronze history included. Bronze history
            is the cheap part; deleting it to "save money" trades a rounding
            error for the ability to reprocess.
        jobs: the scheduled workloads.
        p: price sheet; defaults to :class:`Prices`.

    Returns:
        ``{"storage", "compute", "total", "compute_share"}``, USD/month,
        rounded to cents. ``compute_share`` is the lever: if it is 0.9, cutting
        storage is theatre.
    """
    p = p or Prices()
    storage = total_gb * p.storage_gb_month
    compute = sum(j.monthly_compute(p) for j in jobs)
    total = storage + compute
    return {
        "storage": round(storage, 2),
        "compute": round(compute, 2),
        "total": round(total, 2),
        "compute_share": round(compute / total, 3) if total else 0.0,
    }


def warehouse_monthly_cost(
    total_gb: float, nodes: int, cores_per_node: int, p: Prices | None = None
) -> dict[str, float]:
    """Coupled cost: the cluster is sized for the DATA and it runs 24/7.

    Storage and compute cannot scale independently, so idle hours are billed
    and retaining history forces you to buy compute you do not need. That
    coupling — not the sticker price — is the expensive part.

    Args:
        total_gb: data held in the warehouse.
        nodes: cluster size.
        cores_per_node: cores per node.
        p: price sheet.

    Returns:
        The same keys as :func:`lakehouse_monthly_cost`, plus ``idle_share``:
        the fraction of billed hours in which no query is running, assuming
        ~0.9h of real work per day.
    """
    p = p or Prices()
    compute = nodes * cores_per_node * HOURS_PER_MONTH * p.warehouse_core_hour
    storage = total_gb * p.warehouse_storage_gb_month
    total = storage + compute
    busy_hours = 0.9 * 30
    return {
        "storage": round(storage, 2),
        "compute": round(compute, 2),
        "total": round(total, 2),
        "compute_share": round(compute / total, 3) if total else 0.0,
        "idle_share": round(1 - busy_hours / HOURS_PER_MONTH, 3),
    }


def break_even_utilisation(
    total_gb: float, nodes: int, cores_per_node: int, p: Prices | None = None
) -> float:
    """Monthly core-hours at which the lakehouse stops being cheaper.

    Above this many core-hours per month, an always-on coupled cluster of the
    same shape costs less than paying per second: the workload is steady 24/7
    and elasticity is buying you nothing. Knowing this number is what turns
    "lakehouses are cheaper" from a slogan into an engineering claim.

    Returns:
        Core-hours per month, rounded to one decimal. Compare it against
        ``sum(j.monthly_core_hours() for j in jobs)``.
    """
    p = p or Prices()
    wh = warehouse_monthly_cost(total_gb, nodes, cores_per_node, p)
    lakehouse_storage = total_gb * p.storage_gb_month
    budget_for_compute = wh["total"] - lakehouse_storage
    return round(budget_for_compute / p.core_hour, 1)


def saving_pct(lakehouse: dict[str, float], warehouse: dict[str, float]) -> float:
    """Percentage saved by the lakehouse. Negative means the warehouse wins."""
    if not warehouse["total"]:
        return 0.0
    return round(100 * (1 - lakehouse["total"] / warehouse["total"]), 1)


# Masar's three scheduled workloads, sized from the Module 2 lecture.
MASAR_JOBS: list[Job] = [
    Job("nightly_elt", cores=16, runtime_hours=0.33, runs_per_month=30),
    Job("hourly_stream_compact", cores=4, runtime_hours=0.10, runs_per_month=720),
    Job("weekly_feature_build", cores=32, runtime_hours=0.50, runs_per_month=4, spot=True),
]

# 36 months of raw GPS + trips + the curated layers built on them.
MASAR_TOTAL_GB = 12_000


def main() -> None:
    """CLI: ``python -m masar.econ.cost_model``."""
    # ── TODO(lab-2): put YOUR cloud's real prices here ────────────────────
    #   What : replace every field of `prices` with a list price you looked
    #          up yourself, and cite provider + region + date in LAB2_NOTES.md.
    #   Why  : a cost model built on defaults you did not check is a number
    #          you cannot defend when finance asks where it came from.
    #   Ref  : solutions/lab2_cost_and_scan.py :: masar_prices()
    prices = Prices()
    # ── end TODO(lab-2) ───────────────────────────────────────────────────

    lh = lakehouse_monthly_cost(MASAR_TOTAL_GB, MASAR_JOBS, prices)
    wh = warehouse_monthly_cost(MASAR_TOTAL_GB, nodes=8, cores_per_node=16, p=prices)

    print(f"data volume : {MASAR_TOTAL_GB:,} GB")
    print(f"lakehouse   : {lh}")
    print(f"warehouse   : {wh}")
    print(f"saving      : {saving_pct(lh, wh):.1f}%")
    print(
        f"break-even core-hours/month : {break_even_utilisation(MASAR_TOTAL_GB, 8, 16, prices):,.1f}"
    )
    print(f"actual core-hours/month     : {sum(j.monthly_core_hours() for j in MASAR_JOBS):,.1f}")

    # Sensitivity: Masar opens a fourth city and GPS volume doubles.
    doubled = lakehouse_monthly_cost(MASAR_TOTAL_GB * 2, MASAR_JOBS, replace(prices))
    print(f"2x data     : {doubled}")
    print("             storage is steady and small; compute is the lever you pull.")


if __name__ == "__main__":
    main()
