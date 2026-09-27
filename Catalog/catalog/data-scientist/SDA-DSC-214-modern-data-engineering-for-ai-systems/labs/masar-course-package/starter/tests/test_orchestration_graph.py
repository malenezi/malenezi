"""The DAG graph — dependency ordering, without running a single task.

Lab 7's thesis is that three properties make a pipeline recoverable:
dependency ordering, idempotency, and per-task atomicity. Only the first is a
property of the GRAPH, and it is the one a unit test can hold onto.
"""

from __future__ import annotations

import pytest

from masar.orchestration.runner import (
    DAG_ID,
    TASKS,
    TASKS_BY_ID,
    Task,
    describe,
    topological_order,
)


def test_every_upstream_reference_resolves():
    """A typo'd upstream is a task that silently never runs."""
    known = set(TASKS_BY_ID)
    for task in TASKS:
        assert set(task.upstream) <= known, f"{task.task_id} has an unknown upstream"


def test_graph_is_acyclic_and_covers_every_task():
    """Topological order exists and includes everything exactly once."""
    order = topological_order()
    assert len(order) == len(TASKS)
    assert set(order) == set(TASKS_BY_ID)


def test_gold_never_precedes_silver():
    """THE property. Gold must not start until silver has SUCCEEDED.

    Without this edge, the gold build runs against a consistent-but-stale
    Delta snapshot: no error is raised, and the feature table is simply
    missing the last two hours of trips. Every night.
    """
    order = topological_order()
    silver = order.index("build_silver")
    for gold_task in ("gold_zone_hourly_demand", "gold_driver_daily", "gold_trip_features"):
        assert order.index(gold_task) > silver


def test_the_gate_sits_between_bronze_and_silver():
    """Silver may only be built from gated data, or every control is decorative."""
    order = topological_order()
    assert order.index("land_bronze") < order.index("quality_gate") < order.index("build_silver")


def test_maintenance_runs_last():
    """OPTIMIZE/VACUUM must wait for every writer, or it compacts a moving target."""
    order = topological_order()
    assert order[-1] == "optimize_vacuum"
    assert set(TASKS_BY_ID["optimize_vacuum"].upstream) == {
        "gold_zone_hourly_demand",
        "gold_driver_daily",
        "gold_trip_features",
    }


def test_the_gate_does_not_retry():
    """A batch blocked for a deterministic integrity failure must not be retried.

    Retrying a deterministic rejection is a slower way of ignoring it, and
    with enough retries somebody concludes the gate is flaky.
    """
    assert TASKS_BY_ID["quality_gate"].retries == 0


def test_transform_tasks_do_retry():
    """Transient failures (a timeout, a transient OOM) deserve a retry.

    They are safe to retry precisely BECAUSE the tasks are idempotent — that
    is the property the retry policy is cashing in.
    """
    assert TASKS_BY_ID["build_silver"].retries >= 1
    assert TASKS_BY_ID["gold_trip_features"].retries >= 1


def test_every_task_callable_is_importable():
    """A broken import is a broken DAG, and it should fail here, not at 02:00."""
    for task in TASKS:
        module_name, func_name = task.callable_path.split(":")
        module = __import__(module_name, fromlist=[func_name])
        assert callable(getattr(module, func_name)), f"{task.callable_path} is not callable"


def test_every_task_documents_itself():
    """`--list` is how a participant reads the pipeline; blank docs make it useless."""
    for task in TASKS:
        assert task.doc.strip(), f"{task.task_id} has no doc"


def test_describe_renders_the_graph():
    """The tree view must name the DAG and the execution order."""
    text = describe()
    assert DAG_ID in text
    assert "execution order:" in text
    for task in TASKS:
        assert task.task_id in text


def test_cycle_is_rejected_with_a_useful_message():
    """A dependency cycle is a configuration error and must be named as one."""
    cyclic = (
        Task("a", "masar.spark:get_spark", ("b",)),
        Task("b", "masar.spark:get_spark", ("a",)),
    )
    with pytest.raises(ValueError, match="cycle"):
        topological_order(cyclic)


def test_unknown_upstream_is_rejected_with_a_useful_message():
    """Naming a task that does not exist must fail loudly, not silently skip."""
    broken = (Task("a", "masar.spark:get_spark", ("nope",)),)
    with pytest.raises(ValueError, match="unknown task"):
        topological_order(broken)


def test_airflow_dag_declares_the_same_task_ids(repo_root):
    """The Airflow DAG and the local runner must never disagree about the graph.

    They share the task CALLABLES by import, but the task ids and edges are
    written twice — once as TaskFlow functions, once as `Task` entries. A
    divergence would mean `make pipeline` and `airflow dags test` build
    different pipelines, which is the worst possible kind of "works on my
    machine". Airflow is not installed for this test, so the DAG file is
    parsed rather than imported.
    """
    import ast
    import re

    source = (repo_root / "orchestration" / "dags" / "masar_medallion.py").read_text()
    ast.parse(source)  # a DAG that does not parse is a DAG that does not load

    declared = set(re.findall(r'task_id="([a-z_]+)"', source))
    assert declared == set(TASKS_BY_ID)
