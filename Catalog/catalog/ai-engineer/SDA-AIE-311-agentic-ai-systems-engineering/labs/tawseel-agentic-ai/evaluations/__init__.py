"""The evaluation layer for the Tawseel Agentic AI Engineering Kit.

Everything under `evaluations/` is Layer A (SPEC §1): plain Python 3.11 +
stdlib + pydantic-free, runnable with zero third-party dependencies so the
same harness scores a deterministic `StubTarget` here in the build
sandbox and a real LangGraph-based agent in the classroom. Nothing in this
package imports `langgraph`/`langchain-*` at module import time — targets
that need them (`targets.MonolithTarget`, `targets.SupervisorTarget`)
lazy-import inside their `__call__` and fail with a clear message instead
of an ImportError at import time.

Sub-packages:
  - `oracles.py`   — pure functions that grade a CONCRETE EFFECT (a tool
                      call, a state change), never the model's prose.
  - `metrics.py`    — the 12-dimension dashboard aggregated from results.
  - `targets.py`    — target adapters (stub / monolith / supervisor / recorded).
  - `harness.py`    — the cross-module harness reused Day 1 to Day 5.
  - `dashboard.py`  — renders reports/DASHBOARD.md.
  - `tawseelbench/` — TawseelBench: the tau-bench-shaped Tawseel benchmark.
  - `tool_calling/`, `policy_compliance/`, `task_success/`, `security/`,
    `cost_latency/` — thin, focused wrappers over the harness, one per
    evaluation dimension, each stating the module's own target numbers.
"""
