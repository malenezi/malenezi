"""The runner's failure semantics — Lab 7's thesis, tested without Spark.

Three claims are made about this pipeline, and two of them are properties of
the RUNNER rather than of any task:

  * a failed task must halt everything downstream (dependency ordering);
  * a task whose upstreams succeeded must still run (no over-eager skipping);
  * a full re-run after the fault is removed must succeed.

The tasks are swapped for trivial stand-ins so the whole drill runs in
milliseconds. Idempotency itself is a property of the real tasks and is proved
in the lab with `masar.tools.snapshot`; what is tested here is the machinery
that makes proving it possible.
"""

from __future__ import annotations

import os
import sys
import types

import pytest

from masar.orchestration import runner as R
from masar.orchestration.runner import FAILED, SKIPPED, SUCCESS, UPSTREAM_FAILED, Task, run_dag


@pytest.fixture
def fake_graph(monkeypatch):
    """Replace every task callable with a stand-in that honours the injection.

    The GRAPH is untouched — same task ids, same edges, same retry policy — so
    the test exercises the real topology, not a toy one.
    """
    module = types.ModuleType("masar_fake_tasks")

    def make(task_id: str):
        def run(**_ctx):
            if os.environ.get("MASAR_INJECT_FAILURE") == task_id:
                raise RuntimeError(f"INJECTED FAILURE: simulated fault in {task_id}")
            return task_id

        return run

    for task in R.TASKS:
        setattr(module, task.task_id, make(task.task_id))
    monkeypatch.setitem(sys.modules, "masar_fake_tasks", module)

    fake = tuple(
        Task(
            t.task_id,
            f"masar_fake_tasks:{t.task_id}",
            t.upstream,
            retries=0,  # keep the test fast; retry behaviour is its own test
            retry_delay_s=0.0,
            doc=t.doc,
        )
        for t in R.TASKS
    )
    monkeypatch.setattr(R, "TASKS", fake)
    monkeypatch.setattr(R, "TASKS_BY_ID", {t.task_id: t for t in fake})
    return fake


def test_clean_run_succeeds(fake_graph):
    """Every task runs, in order, and the DAG reports success."""
    result = run_dag(context={"run_id": "test-clean"})
    assert result.success
    assert all(r.state == SUCCESS for r in result.runs.values())


def test_injected_failure_halts_everything_downstream(fake_graph):
    """THE property: gold is never built from a broken silver.

    Without this, the gold build runs against a consistent-but-stale snapshot,
    no error is raised, and the feature table is quietly missing the last two
    hours of trips. Every night.
    """
    result = run_dag(inject_failure="build_silver", context={"run_id": "test-fail"})

    assert not result.success
    assert result.runs["build_silver"].state == FAILED
    for downstream in (
        "observability",
        "gold_trip_features",
        "gold_driver_daily",
        "gold_zone_hourly_demand",
        "optimize_vacuum",
    ):
        assert result.runs[downstream].state == UPSTREAM_FAILED


def test_tasks_upstream_of_the_failure_still_ran(fake_graph):
    """The failure must not retroactively invalidate work that already succeeded."""
    result = run_dag(inject_failure="build_silver", context={"run_id": "test-fail"})
    assert result.runs["land_bronze"].state == SUCCESS
    assert result.runs["quality_gate"].state == SUCCESS


def test_a_sibling_of_the_failure_is_not_skipped(fake_graph):
    """`build_silver_drivers` shares an upstream with `build_silver`, not a dependency.

    Skipping it too would be over-eager: an orchestrator that treats siblings
    as dependants wastes a whole run on one unrelated fault.
    """
    result = run_dag(inject_failure="build_silver", context={"run_id": "test-fail"})
    assert result.runs["build_silver_drivers"].state == SUCCESS


def test_full_rerun_recovers(fake_graph):
    """Remove the fault, re-run EVERYTHING, and the DAG succeeds.

    Not "the failed tasks". The whole thing. If a full re-run is safe, every
    operational problem is tractable; if it is not, every operational problem
    is an archaeology project.
    """
    failed = run_dag(inject_failure="build_silver", context={"run_id": "r1"})
    assert not failed.success

    recovered = run_dag(context={"run_id": "r2"})
    assert recovered.success


def test_injection_does_not_leak_into_the_environment(fake_graph):
    """A drill must not arm the next run. The env var is restored either way."""
    before = os.environ.get("MASAR_INJECT_FAILURE")
    run_dag(inject_failure="build_silver", context={"run_id": "leak"})
    assert os.environ.get("MASAR_INJECT_FAILURE") == before


def test_dry_run_resolves_callables_and_reports_success(fake_graph):
    """`--dry-run` is a CI check that the DAG still imports; SKIPPED is not failure."""
    result = run_dag(dry_run=True, context={"run_id": "dry"})
    assert result.success
    assert all(r.state == SKIPPED for r in result.runs.values())
    assert "dry run" in result.render()


def test_only_runs_the_named_tasks(fake_graph):
    """`--only` is a debugging aid; everything else is explicitly SKIPPED."""
    result = run_dag(only=["land_bronze"], context={"run_id": "only"})
    assert result.runs["land_bronze"].state == SUCCESS
    assert result.runs["build_silver"].state == SKIPPED


def test_retries_are_attempted_then_the_task_fails(monkeypatch):
    """A retried task records its attempts and still fails when the fault is real."""
    module = types.ModuleType("masar_flaky")
    calls = {"n": 0}

    def always_fails(**_ctx):
        calls["n"] += 1
        raise RuntimeError("transient-looking but not")

    module.always_fails = always_fails
    monkeypatch.setitem(sys.modules, "masar_flaky", module)

    graph = (Task("only_task", "masar_flaky:always_fails", (), retries=2, retry_delay_s=0.0),)
    monkeypatch.setattr(R, "TASKS", graph)
    monkeypatch.setattr(R, "TASKS_BY_ID", {t.task_id: t for t in graph})

    result = run_dag(context={})
    assert not result.success
    assert calls["n"] == 3  # first attempt + 2 retries
    assert result.runs["only_task"].attempts == 3
