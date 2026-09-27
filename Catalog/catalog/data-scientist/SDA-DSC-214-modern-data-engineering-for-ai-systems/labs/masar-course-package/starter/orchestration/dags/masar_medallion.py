"""The Masar Mini-Lakehouse as one dependency-ordered, idempotent Airflow DAG.

::

    land_bronze ─► quality_gate ─► build_silver ─┬─► gold_zone_hourly_demand ─┐
                                   build_drivers ─┤   gold_driver_daily        ├─► optimize_vacuum
                                    observability ┴─► gold_trip_features ──────┘

Three properties make this production-grade, and all three were built in
earlier modules rather than invented here:

  * **dependency ordering** — gold cannot start until silver's task SUCCEEDS.
    Without the edge, ``build_trip_features`` runs at 02:07 while
    ``build_silver_trips`` is still merging at 02:09. Delta hands it a
    *consistent* snapshot, so nothing errors — the feature table is simply
    missing the last two hours of trips. Every night.
  * **idempotency** — every task is safe to re-run, so retries and backfills
    cannot corrupt or double-count.
  * **atomicity per task** — a failed task leaves no half-written Delta table.

Together they mean a full re-run recovers from ANY failure with no duplicates.

**This DAG is optional.** ``orchestration/run_local.py`` runs the identical
graph with the identical callables and no Airflow at all, so a failed Airflow
install never blocks Lab 7. Install Airflow with the official constraint file::

    pip install 'apache-airflow==2.9.3' \
      --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.11.txt"
    export AIRFLOW_HOME="$PWD/orchestration/airflow"
    export AIRFLOW__CORE__DAGS_FOLDER="$PWD/orchestration/dags"
"""

from __future__ import annotations

from datetime import datetime, timedelta

import pendulum
from airflow.decorators import dag, task

from masar.delta.maintain import optimize_and_vacuum
from masar.ingest.land_bronze import land_all
from masar.quality.gate import gate_and_promote_task
from masar.quality.observe import observability_task
from masar.transform.build_gold import (
    build_driver_daily,
    build_trip_features,
    build_zone_hourly_demand,
)
from masar.transform.build_silver import build_silver_drivers, build_silver_trips

RIYADH = pendulum.timezone("Asia/Riyadh")

DEFAULT_ARGS = {
    "owner": "masar-data-platform",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "retry_exponential_backoff": True,
    "execution_timeout": timedelta(minutes=45),
    # Each run is independent BECAUSE every task is idempotent. Set this True
    # and one bad night blocks every subsequent night until someone clears it.
    "depends_on_past": False,
}


@dag(
    dag_id="masar_medallion",
    description="Masar Mini-Lakehouse: bronze -> gate -> silver -> gold -> maintain",
    schedule="0 2 * * *",  # nightly 02:00 Asia/Riyadh
    start_date=datetime(2026, 6, 1, tzinfo=RIYADH),
    catchup=False,  # backfills are explicit and parameterised, never accidental
    max_active_runs=1,  # no two runs mutating silver concurrently
    default_args=DEFAULT_ARGS,
    tags=["masar", "lakehouse", "medallion"],
    params={"business_date": "{{ ds }}", "lookback_days": 3},
)
def masar_medallion():
    """Build the Masar medallion once, in the right order, idempotently."""

    @task(task_id="land_bronze")
    def t_land(**context) -> dict:
        """Append every raw feed to bronze with lineage. Re-runnable by design."""
        return land_all(business_date=context["params"]["business_date"])

    @task(task_id="quality_gate", retries=0)
    def t_gate(_landed: dict, **context) -> dict:
        """Fail-fast on integrity, quarantine partial failures, promote the rest.

        ``retries=0`` on purpose: a batch blocked for an integrity failure must
        not be retried into acceptance. Retrying a deterministic rejection is
        just a slower way of ignoring it.
        """
        return gate_and_promote_task(**context)

    @task(task_id="build_silver")
    def t_silver(_gated: dict, **context) -> int:
        """Conform, deduplicate and MERGE bronze trips into silver.trips."""
        return build_silver_trips(**context)

    @task(task_id="build_silver_drivers")
    def t_drivers(_gated: dict, **context) -> int:
        """Conform the driver roster into silver.drivers."""
        return build_silver_drivers(**context)

    @task(task_id="observability")
    def t_obs(_trips: int, _drivers: int, **context) -> dict:
        """Freshness, volume, schema drift, distribution drift — all four."""
        return observability_task(**context)

    @task(task_id="gold_zone_hourly_demand")
    def t_demand(_obs: dict, **context) -> int:
        """BI demand mart. GRAIN: (city, pickup_zone_id, date, hour)."""
        return build_zone_hourly_demand(**context)

    @task(task_id="gold_driver_daily")
    def t_driver_daily(_obs: dict, **context) -> int:
        """BI driver mart. GRAIN: (driver_id, date)."""
        return build_driver_daily(**context)

    @task(task_id="gold_trip_features")
    def t_features(_obs: dict, **context) -> int:
        """AI feature table. GRAIN: trip_id. Strictly-prior windows only."""
        return build_trip_features(**context)

    @task(task_id="optimize_vacuum", retries=0, trigger_rule="all_success")
    def t_maintain(_a: int, _b: int, _c: int, **context) -> dict:
        """Compact small files, reclaim storage past the retention window."""
        return optimize_and_vacuum(**context)

    # The dependency graph. TaskFlow infers each edge from the data passed
    # between tasks, so the ordering cannot drift away from the code that
    # depends on it — the single most important property in this file.
    landed = t_land()
    gated = t_gate(landed)
    trips = t_silver(gated)
    drivers = t_drivers(gated)
    observed = t_obs(trips, drivers)
    t_maintain(t_demand(observed), t_driver_daily(observed), t_features(observed))


dag = masar_medallion()
