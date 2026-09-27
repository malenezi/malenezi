"""Module 1/8/9 — bounding the agent loop by construction.

TEACHING POINT (Module 1 §4): "the model will decide when it's done" is not
a termination condition, it is the absence of one. An agent loop must be
bounded on three axes — step count, cost, wall-clock time — set when the
run starts, not hoped for at runtime. `RunBudget` is that bound made
concrete; `check(state)` is the one-line call a router makes before it
decides whether to keep looping or escalate.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

from rafeeq.core.config import MAX_STEPS, RUN_COST_CAP_USD, WALL_CLOCK_S
from rafeeq.core.errors import BudgetExceeded


@dataclass
class RunBudget:
    """Enforces the three bounding axes for a single agent run.

    One `RunBudget` instance is created ONCE per run (at the entry point,
    not per node) so wall-clock time is measured from the run's actual
    start. Every router/node that might keep the loop going calls
    `budget.check(state)` — or the module-level `check(state, budget)`
    convenience — before deciding to continue.
    """

    max_steps: int = MAX_STEPS
    cost_cap_usd: float = RUN_COST_CAP_USD
    wall_clock_s: float = WALL_CLOCK_S
    _start: float = field(default_factory=time.monotonic, repr=False)

    def elapsed_s(self) -> float:
        return time.monotonic() - self._start

    def status(self, state: dict) -> dict:
        """Non-raising introspection — what the budget looks like right
        now, for logging/observability (M9) or a UI progress indicator."""
        step_count = int(state.get("step_count", 0))
        cost_usd = float(state.get("cost_usd", 0.0))
        elapsed = self.elapsed_s()
        return {
            "step_count": step_count,
            "max_steps": self.max_steps,
            "steps_remaining": max(0, self.max_steps - step_count),
            "cost_usd": cost_usd,
            "cost_cap_usd": self.cost_cap_usd,
            "cost_remaining_usd": max(0.0, self.cost_cap_usd - cost_usd),
            "elapsed_s": elapsed,
            "wall_clock_s": self.wall_clock_s,
            "wall_clock_remaining_s": max(0.0, self.wall_clock_s - elapsed),
            "exceeded": self.exceeded(state),
        }

    def exceeded(self, state: dict) -> str | None:
        """Return the name of the first axis that is over budget, or None
        if the run is still within bounds. Checked in a fixed order so the
        reported reason is deterministic."""
        step_count = int(state.get("step_count", 0))
        cost_usd = float(state.get("cost_usd", 0.0))
        if step_count >= self.max_steps:
            return "steps"
        if cost_usd >= self.cost_cap_usd:
            return "cost"
        if self.elapsed_s() >= self.wall_clock_s:
            return "wall_clock"
        return None

    def check(self, state: dict) -> None:
        """Raise `BudgetExceeded` if any axis is over budget. Callers
        (routers) catch this and route to `resolution="escalated"` —
        NEVER swallow it and keep looping (Module 1 mistake #5)."""
        axis = self.exceeded(state)
        if axis is None:
            return
        status = self.status(state)
        raise BudgetExceeded(
            f"Run budget exceeded on axis '{axis}'",
            axis=axis,
            step_count=status["step_count"],
            max_steps=status["max_steps"],
            cost_usd=status["cost_usd"],
            cost_cap_usd=status["cost_cap_usd"],
            elapsed_s=round(status["elapsed_s"], 3),
            wall_clock_s=status["wall_clock_s"],
        )


_default_budget: RunBudget | None = None


def get_default_budget(reset: bool = False) -> RunBudget:
    """A process-wide default `RunBudget`, lazily created. Convenient for
    scripts/tests that don't wire an explicit budget through state/config;
    real orchestration (M6+) should create and thread its own `RunBudget`
    per run instead of relying on this."""
    global _default_budget
    if _default_budget is None or reset:
        _default_budget = RunBudget()
    return _default_budget


def check(state: dict, budget: RunBudget | None = None) -> None:
    """Router-facing convenience: `rafeeq.core.budget.check(state)`.
    Raises `BudgetExceeded` if `state` (plus wall-clock elapsed on
    `budget`) breaches any bound. Pass the SAME `RunBudget` instance across
    a run's routing calls so wall-clock is measured from run start, not
    reset on every call — the default budget is a fallback for
    single-shot scripts, not a substitute for that.
    """
    (budget or get_default_budget()).check(state)
