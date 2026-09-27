"""Lab 2, Task 2 — Plan-and-Execute for the refund workflow.

The enterprise argument (module overview): a plan is LOGGABLE and
APPROVABLE before any tool runs — the plan is the control point. Fill in
the TODOs; everything here runs under plain python3 against the default
`StubChatModel`, no langgraph required.
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.llm import get_model


class Plan(BaseModel):
    steps: list[str] = Field(description="Ordered, concrete sub-tasks")


_REFUND_PLAN_STEPS = [
    "Look up the order and confirm SLA breach / refund eligibility",
    "Determine the refund amount and the applicable autonomy band",
    "Issue the refund, or record an approval request if above the limit",
    "Notify the customer in their language",
]


def make_plan(objective: str) -> Plan:
    """TODO(lab 2.2a): ask the model for a structured `Plan` via
    `get_model().with_structured_output(Plan)`. `StubChatModel` cannot
    truly plan — when it returns an EMPTY `steps` list (or raises), fall
    back to `Plan(steps=_REFUND_PLAN_STEPS)` so this function never
    returns an unusable plan. Log nothing here — logging is
    `log_plan`'s job (Task 2's "log the plan" requirement), kept
    separate so a caller can choose to skip execution after seeing the
    plan (the approval gate, Task below) without a partial log entry.
    """
    raise NotImplementedError("TODO(lab 2.2a): implement make_plan")


def plan_approval_gate(plan: Plan, *, auto_approve_threshold: int = 5) -> dict[str, Any]:
    """TODO(lab 2.2b): return `{"requires_human": bool, "reason": str}`.
    A plan with MORE steps than `auto_approve_threshold` requires human
    approval (an unexpectedly long plan is itself a signal something is
    off) — otherwise auto-approve. This is the ONE function a real
    human-in-the-loop integration replaces (turn "auto-approve" into
    "wait for a person").
    """
    raise NotImplementedError("TODO(lab 2.2b): implement plan_approval_gate")


def log_plan(objective: str, plan: Plan, gate_decision: dict[str, Any] | None = None) -> dict[str, Any]:
    """Provided: the audit record. BEFORE any step executes (call this
    right after `make_plan`+`plan_approval_gate`, never after)."""
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "objective": objective,
        "plan": plan.steps,
        "gate_decision": gate_decision,
    }


def run_plan_execute(objective: str, *, verbose: bool = True) -> dict[str, Any]:
    """TODO(lab 2.2c): wire it together.

    1. `plan = make_plan(objective)`
    2. `gate = plan_approval_gate(plan)`
    3. `log_plan(objective, plan, gate)` — BEFORE any step runs
    4. If `gate["requires_human"]`, return `{"plan": plan.steps, "past":
       [], "executed": False, "plan_gate": gate}` without executing.
    5. Otherwise execute each step with a plain model call (one call per
       step, appending `(step, result.content)` to a `past` list), and
       return `{"plan": plan.steps, "past": past, "executed": True,
       "plan_gate": gate}`.
    """
    raise NotImplementedError("TODO(lab 2.2c): implement run_plan_execute")
