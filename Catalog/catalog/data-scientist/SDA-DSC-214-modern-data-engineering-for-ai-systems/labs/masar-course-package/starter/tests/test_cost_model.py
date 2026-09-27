"""The cost model — Module 2's argument, checked arithmetically.

These tests do not assert that the lakehouse is cheaper. They assert that the
model says WHY: that compute dominates, that idle hours are what a coupled
cluster bills you for, and that there is a utilisation at which the argument
reverses. A cost model that cannot express its own falsification is advocacy.
"""

from __future__ import annotations

import pytest

from masar.econ.cost_model import (
    HOURS_PER_MONTH,
    MASAR_JOBS,
    MASAR_TOTAL_GB,
    Job,
    Prices,
    break_even_utilisation,
    lakehouse_monthly_cost,
    saving_pct,
    warehouse_monthly_cost,
)


def test_job_core_hours_are_the_billing_unit():
    """cores x hours x runs — the only quantity the compute bill is a function of."""
    job = Job("nightly_elt", cores=16, runtime_hours=0.5, runs_per_month=30)
    assert job.monthly_core_hours() == pytest.approx(240.0)
    assert job.monthly_compute(Prices(core_hour=0.10)) == pytest.approx(24.0)


def test_spot_applies_only_to_jobs_that_claim_it():
    """Spot is a property of the WORKLOAD (restartable), not of the price sheet."""
    prices = Prices(core_hour=0.10, spot_multiplier=0.35)
    on_demand = Job("feature_build", cores=8, runtime_hours=1.0, runs_per_month=4)
    spot = Job("feature_build", cores=8, runtime_hours=1.0, runs_per_month=4, spot=True)
    assert spot.monthly_compute(prices) == pytest.approx(on_demand.monthly_compute(prices) * 0.35)


def test_lakehouse_totals_are_internally_consistent():
    """storage + compute == total, and compute_share is that ratio."""
    result = lakehouse_monthly_cost(MASAR_TOTAL_GB, MASAR_JOBS)
    assert result["storage"] + result["compute"] == pytest.approx(result["total"], rel=1e-6)
    # compute_share is rounded to 3dp for readability, so compare absolutely.
    assert result["compute_share"] == pytest.approx(result["compute"] / result["total"], abs=1e-3)


def test_storage_scales_linearly_and_compute_does_not():
    """Doubling retained data doubles storage and leaves compute untouched.

    This is the shape of the whole argument: keeping bronze history costs you a
    linear, small amount, and buys you the ability to reprocess. Deleting it to
    save money trades a rounding error for that ability.
    """
    single = lakehouse_monthly_cost(MASAR_TOTAL_GB, MASAR_JOBS)
    double = lakehouse_monthly_cost(MASAR_TOTAL_GB * 2, MASAR_JOBS)
    assert double["storage"] == pytest.approx(single["storage"] * 2)
    assert double["compute"] == pytest.approx(single["compute"])


def test_warehouse_bills_every_hour_of_the_month():
    """The coupled cluster's compute is nodes x cores x 730h, run or not."""
    result = warehouse_monthly_cost(
        1000, nodes=4, cores_per_node=8, p=Prices(warehouse_core_hour=0.10)
    )
    assert result["compute"] == pytest.approx(4 * 8 * HOURS_PER_MONTH * 0.10)
    # ~0.9h of real work a day against 730 billed hours.
    assert result["idle_share"] > 0.95


def test_break_even_is_far_above_masar_actual_utilisation():
    """Masar's real utilisation is orders of magnitude below break-even.

    This is the honest form of "the lakehouse is cheaper": it is cheaper AT
    THIS UTILISATION, and the model states the utilisation at which it stops
    being true. A steady 24/7 workload would flip the answer.
    """
    break_even = break_even_utilisation(MASAR_TOTAL_GB, nodes=8, cores_per_node=16)
    actual = sum(j.monthly_core_hours() for j in MASAR_JOBS)
    assert actual < break_even
    assert break_even / actual > 100


def test_saving_turns_negative_above_break_even_utilisation():
    """Past break-even the decoupled platform stops winning, and the model says so.

    This is the test that makes the model falsifiable rather than promotional.
    `break_even_utilisation` reports the monthly core-hours at which an
    always-on coupled cluster of the same shape becomes cheaper; run a workload
    just above that line and the saving must go negative. If it did not, the
    break-even function would be decorative.
    """
    break_even = break_even_utilisation(MASAR_TOTAL_GB, nodes=8, cores_per_node=16)
    # A steady 24/7 workload sized just past the break-even line.
    cores = int(break_even / HOURS_PER_MONTH) + 50
    always_on = [Job("streaming_24x7", cores=cores, runtime_hours=1.0, runs_per_month=730)]

    lh = lakehouse_monthly_cost(MASAR_TOTAL_GB, always_on)
    wh = warehouse_monthly_cost(MASAR_TOTAL_GB, nodes=8, cores_per_node=16)
    assert saving_pct(lh, wh) < 0

    # And just below it, the lakehouse still wins — the line is a real boundary.
    under = [Job("streaming_24x7", cores=cores - 100, runtime_hours=1.0, runs_per_month=730)]
    assert saving_pct(lakehouse_monthly_cost(MASAR_TOTAL_GB, under), wh) > 0


def test_empty_platform_does_not_divide_by_zero():
    """No data, no jobs, no crash. Edge cases must not break the model."""
    result = lakehouse_monthly_cost(0, [])
    assert result["total"] == 0
    assert result["compute_share"] == 0.0
