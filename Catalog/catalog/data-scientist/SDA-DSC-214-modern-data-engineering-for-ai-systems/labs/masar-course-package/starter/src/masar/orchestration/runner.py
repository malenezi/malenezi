"""A dependency-ordered DAG runner with no Airflow dependency.

Airflow is the right tool in production and a poor prerequisite for a lab: its
constrained dependency tree is the single most common reason a Day-5 exercise
never starts. So the task graph is declared HERE, in ~200 lines, and Airflow's
DAG file (``orchestration/dags/masar_medallion.py``) imports the same task
callables and re-declares the same edges.

The three properties that matter are properties of the GRAPH and the TASKS,
not of the scheduler:

  * **dependency ordering** — gold cannot start until silver SUCCEEDS;
  * **idempotency** — every task is safe to re-run, so retries cannot corrupt;
  * **atomicity per task** — a failed task leaves no half-written Delta table.

Together they mean a full re-run recovers from ANY failure with no duplicates.
That claim is testable, and Lab 7 Task 5 tests it: inject a failure, snapshot,
re-run, diff.

CLI::

    python -m masar.orchestration.runner --dag masar_medallion --list
    python -m masar.orchestration.runner --run
    python -m masar.orchestration.runner --run --inject-failure build_silver
"""

from __future__ import annotations

import argparse
import os
import time
import traceback
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

DAG_ID = "masar_medallion"

# Task states, deliberately the same words Airflow uses so a participant who
# later opens the Airflow UI recognises what they are looking at.
SUCCESS = "SUCCESS"
FAILED = "FAILED"
UPSTREAM_FAILED = "UPSTREAM_FAILED"
SKIPPED = "SKIPPED"


@dataclass
class Task:
    """One node in the graph.

    Attributes:
        task_id: stable identifier; also what ``--inject-failure`` names.
        callable_path: ``module:function``, imported lazily so that listing
            the graph never imports PySpark.
        upstream: task ids that must SUCCEED first.
        retries: attempts after the first.
        retry_delay_s: seconds between attempts (short here; Airflow's
            production default is minutes).
        doc: one line, shown by ``--list``.
    """

    task_id: str
    callable_path: str
    upstream: tuple[str, ...] = ()
    retries: int = 2
    retry_delay_s: float = 2.0
    doc: str = ""

    def resolve(self) -> Callable[..., Any]:
        """Import and return the task callable."""
        module_name, func_name = self.callable_path.split(":")
        module = __import__(module_name, fromlist=[func_name])
        return getattr(module, func_name)


#: The Masar medallion graph::
#:
#:   land_bronze -> quality_gate -> build_silver -> observability -+-> gold_zone_hourly_demand -+
#:                                                                 +-> gold_driver_daily       +-> optimize_vacuum
#:                                                                 +-> gold_trip_features      +
TASKS: tuple[Task, ...] = (
    Task(
        "land_bronze",
        "masar.ingest.land_bronze:land_all",
        (),
        doc="Land every raw feed into bronze, append-only, with lineage.",
    ),
    Task(
        "quality_gate",
        "masar.quality.gate:gate_and_promote_task",
        ("land_bronze",),
        retries=0,  # a blocked batch must NOT be retried into acceptance
        doc="Fail-fast on integrity, quarantine partial failures, promote the rest.",
    ),
    Task(
        "build_silver",
        "masar.transform.build_silver:build_silver_trips",
        ("quality_gate",),
        doc="Conform, dedupe and MERGE bronze trips into silver.trips.",
    ),
    Task(
        "build_silver_drivers",
        "masar.transform.build_silver:build_silver_drivers",
        ("quality_gate",),
        doc="Conform the driver roster into silver.drivers.",
    ),
    Task(
        "observability",
        "masar.quality.observe:observability_task",
        ("build_silver", "build_silver_drivers"),
        doc="Freshness, volume, schema drift, distribution drift.",
    ),
    Task(
        "gold_zone_hourly_demand",
        "masar.transform.build_gold:build_zone_hourly_demand",
        ("observability",),
        doc="BI demand mart, grain (city, zone, date, hour).",
    ),
    Task(
        "gold_driver_daily",
        "masar.transform.build_gold:build_driver_daily",
        ("observability",),
        doc="BI driver mart, grain (driver_id, date).",
    ),
    Task(
        "gold_trip_features",
        "masar.transform.build_gold:build_trip_features",
        ("observability",),
        doc="AI feature table, grain trip_id, strictly-prior windows.",
    ),
    Task(
        "optimize_vacuum",
        "masar.delta.maintain:optimize_and_vacuum",
        ("gold_zone_hourly_demand", "gold_driver_daily", "gold_trip_features"),
        retries=0,
        doc="Compact small files and reclaim storage past retention.",
    ),
)

TASKS_BY_ID: dict[str, Task] = {t.task_id: t for t in TASKS}


@dataclass
class TaskRun:
    """The outcome of one task in one DAG run."""

    task_id: str
    state: str
    attempts: int = 0
    duration_s: float = 0.0
    error: str = ""
    result: Any = None


@dataclass
class DagRun:
    """The outcome of a whole DAG run."""

    dag_id: str
    runs: dict[str, TaskRun] = field(default_factory=dict)
    started_at: float = 0.0
    duration_s: float = 0.0
    dry_run: bool = False

    @property
    def success(self) -> bool:
        """True when nothing failed.

        A dry run succeeds if every callable resolved — its tasks are SKIPPED
        by design, and reporting that as a failure would make ``--dry-run``
        useless as a CI check that the DAG still imports.
        """
        states = [r.state for r in self.runs.values()]
        if self.dry_run:
            return all(st == SKIPPED for st in states)
        return all(st == SUCCESS for st in states)

    def render(self) -> str:
        """The run log, in the shape Lab 7's expected output uses."""
        lines = []
        for task_id in self.runs:
            task = TASKS_BY_ID.get(task_id, Task(task_id, ""))
            run = self.runs.get(task.task_id)
            if run is None:
                continue
            detail = ""
            if run.state == SUCCESS:
                detail = f"({run.duration_s:.1f}s)"
            elif run.state == FAILED:
                detail = run.error.splitlines()[-1] if run.error else ""
            elif self.dry_run:
                detail = f"-> {TASKS_BY_ID[task.task_id].callable_path}"
            lines.append(f"[{task.task_id:<24}] {run.state:<16} {detail}")
        verdict = "success" if self.success else "failed"
        mode = " [dry run: callables resolved, nothing executed]" if self.dry_run else ""
        lines.append(f"DAG {self.dag_id}: {verdict}{mode} (total {self.duration_s:.1f}s)")
        return "\n".join(lines)


def topological_order(tasks: tuple[Task, ...] | None = None) -> list[str]:
    """Return task ids in a valid execution order.

    Args:
        tasks: the graph to order. Defaults to :data:`TASKS` — resolved at CALL
            time, not at import time, so a test (or a fork) that replaces the
            module-level graph is actually honoured. A default argument bound
            at import would silently ignore it.

    Raises:
        ValueError: on an unknown upstream or a dependency cycle. Both are
            configuration errors that would otherwise surface as a task that
            mysteriously never runs.
    """
    tasks = TASKS if tasks is None else tasks
    pending = {t.task_id: set(t.upstream) for t in tasks}
    known = set(pending)
    for task_id, ups in pending.items():
        unknown = ups - known
        if unknown:
            raise ValueError(f"task {task_id!r} depends on unknown task(s) {sorted(unknown)}")

    order: list[str] = []
    while pending:
        ready = sorted(tid for tid, ups in pending.items() if not ups)
        if not ready:
            raise ValueError(f"dependency cycle among {sorted(pending)}")
        for task_id in ready:
            order.append(task_id)
            del pending[task_id]
        for ups in pending.values():
            ups.difference_update(ready)
    return order


def describe(tasks: tuple[Task, ...] | None = None) -> str:
    """Render the graph as a tree, the way ``airflow tasks list --tree`` does."""
    tasks = TASKS if tasks is None else tasks
    by_id = {t.task_id: t for t in tasks}
    lines = [f"DAG: {DAG_ID}", ""]
    depth: dict[str, int] = {}
    for task_id in topological_order(tasks):
        task = by_id[task_id]
        depth[task_id] = 0 if not task.upstream else max(depth[u] for u in task.upstream) + 1
        indent = "    " * depth[task_id]
        lines.append(f"{indent}<Task: {task_id}>")
        lines.append(f"{indent}    {task.doc}")
    lines.append("")
    lines.append("execution order: " + " -> ".join(topological_order(tasks)))
    return "\n".join(lines)


def run_dag(
    inject_failure: str | None = None,
    only: list[str] | None = None,
    dry_run: bool = False,
    context: dict | None = None,
) -> DagRun:
    """Execute the graph in dependency order.

    Args:
        inject_failure: task id to make fail on purpose (Lab 7 Task 5). Sets
            ``MASAR_INJECT_FAILURE`` so the task itself raises MID-WORK, after
            its reads and before its write — which is what proves that a
            failed task leaves no half-written table.
        only: run just these task ids (and mark the rest SKIPPED). Their
            upstreams are NOT run — this is a debugging aid, not a shortcut,
            and the runner says so.
        dry_run: resolve every callable and print the order without executing.
        context: passed as keyword arguments to every task, like Airflow's
            context dict. ``run_id`` and ``ds`` are the two tasks look for.

    Returns:
        A :class:`DagRun`.
    """
    context = context or {}
    dag_run = DagRun(dag_id=DAG_ID, started_at=time.time(), dry_run=dry_run)
    previous_inject = os.environ.get("MASAR_INJECT_FAILURE")
    if inject_failure:
        os.environ["MASAR_INJECT_FAILURE"] = inject_failure
        print(f"[runner] failure injection armed for task {inject_failure!r}")

    try:
        for task_id in topological_order():
            task = TASKS_BY_ID[task_id]

            if only and task_id not in only:
                dag_run.runs[task_id] = TaskRun(task_id, SKIPPED)
                continue

            failed_upstream = [
                u
                for u in task.upstream
                if dag_run.runs.get(u) and dag_run.runs[u].state in (FAILED, UPSTREAM_FAILED)
            ]
            if failed_upstream:
                dag_run.runs[task_id] = TaskRun(task_id, UPSTREAM_FAILED)
                print(f"[{task_id:<24}] {UPSTREAM_FAILED}  (skipped: {failed_upstream})")
                continue

            if dry_run:
                task.resolve()  # import it: a broken import is a broken DAG
                dag_run.runs[task_id] = TaskRun(task_id, SKIPPED)
                continue

            dag_run.runs[task_id] = _run_task(task, context)

    finally:
        if previous_inject is None:
            os.environ.pop("MASAR_INJECT_FAILURE", None)
        else:
            os.environ["MASAR_INJECT_FAILURE"] = previous_inject

    dag_run.duration_s = time.time() - dag_run.started_at
    return dag_run


def _run_task(task: Task, context: dict) -> TaskRun:
    """Run one task with retries, returning its outcome rather than raising."""
    fn = task.resolve()
    started = time.time()
    last_error = ""

    for attempt in range(task.retries + 1):
        try:
            result = fn(**context)
            duration = time.time() - started
            print(f"[{task.task_id:<24}] {SUCCESS:<16} ({duration:.1f}s)")
            return TaskRun(task.task_id, SUCCESS, attempt + 1, duration, result=result)
        except Exception as exc:  # noqa: BLE001 - the runner reports, it does not crash
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < task.retries:
                print(
                    f"[{task.task_id:<24}] FAILED  retry {attempt + 1} of {task.retries} "
                    f"in {task.retry_delay_s:.0f}s … {last_error}"
                )
                time.sleep(task.retry_delay_s)
            else:
                print(f"[{task.task_id:<24}] {FAILED}")
                traceback.print_exc()

    return TaskRun(task.task_id, FAILED, task.retries + 1, time.time() - started, last_error)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns the process exit code."""
    p = argparse.ArgumentParser(
        description="Run the Masar medallion DAG without Airflow",
        epilog="Lab 7 Task 5: --inject-failure build_silver, snapshot, then re-run clean.",
    )
    p.add_argument("--dag", default=DAG_ID, help="dag id (only masar_medallion exists)")
    p.add_argument("--list", action="store_true", help="print the task graph and exit")
    p.add_argument("--run", action="store_true", help="execute the DAG")
    p.add_argument("--dry-run", action="store_true", help="resolve callables, execute nothing")
    p.add_argument(
        "--inject-failure",
        metavar="TASK_ID",
        default=None,
        help="make this task fail on purpose (idempotent-recovery drill)",
    )
    p.add_argument("--only", nargs="*", default=None, help="run only these task ids")
    p.add_argument("--run-id", default=None, help="run identifier passed to every task")
    p.add_argument("--ds", default=None, help="business date passed to every task (YYYY-MM-DD)")
    a = p.parse_args(argv)

    if a.dag != DAG_ID:
        p.error(f"unknown dag {a.dag!r}; this repository ships {DAG_ID!r}")

    if a.list or not (a.run or a.dry_run):
        print(describe())
        return 0

    if a.inject_failure and a.inject_failure not in TASKS_BY_ID:
        p.error(f"unknown task {a.inject_failure!r}; choose from {sorted(TASKS_BY_ID)}")

    from masar import config

    context = {
        "run_id": a.run_id or f"manual__{time.strftime('%Y%m%dT%H%M%S')}",
        "ds": a.ds or config.BUSINESS_DATE,
        "business_date": a.ds or config.BUSINESS_DATE,
    }
    dag_run = run_dag(
        inject_failure=a.inject_failure, only=a.only, dry_run=a.dry_run, context=context
    )
    print()
    print(dag_run.render())
    return 0 if dag_run.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
