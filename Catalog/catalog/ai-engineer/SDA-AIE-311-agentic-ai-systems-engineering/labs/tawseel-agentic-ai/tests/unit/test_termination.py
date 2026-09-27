"""Module 1 — Lab 1's adversarial termination test, written against the
PURE router (`rafeeq.core.graph.route` / `route_with_tools`) so it runs
with NO langgraph installed.

TEACHING POINT this test exists to prove: "the model will decide when
it's done" is not a termination condition — an agent that always wants to
keep calling tools (an adversarial input that never satisfies the goal)
MUST still halt within `MAX_STEPS`, because the step budget is checked in
code, not hoped for in a prompt. See `tests/unit/run_without_pytest.py`
for the stdlib mirror.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_STEPS
from rafeeq.core.graph import route, route_with_tools


class _AlwaysWantsToActMessage:
    """A fake last message that ALWAYS carries a tool call — the
    adversarial condition Lab 1 asks for: a goal that is never satisfied,
    so the ONLY thing that can stop the loop is the step budget."""

    tool_calls = [{"name": "track_shipment", "args": {"order_id": "TW-2026-00000"}, "id": "call_1"}]


class _FinalAnswerMessage:
    tool_calls: list = []


def _state_at_step(step_count: int, last_message) -> dict:
    return {"step_count": step_count, "messages": [last_message]}


class TestAdversarialTerminatesWithinMaxSteps:
    def test_never_satisfies_goal_still_halts_at_budget(self):
        """Drive `route` step by step with a message that ALWAYS wants to
        act. It must return 'reason' (keep going) below the budget and
        END at/after it — the loop cannot run past MAX_STEPS regardless
        of what the (adversarial) model keeps asking for."""
        halted_at = None
        for step_count in range(0, MAX_STEPS + 5):     # deliberately overshoot the budget
            state = _state_at_step(step_count, _AlwaysWantsToActMessage())
            decision = route(state)
            if decision == "reason":
                assert step_count < MAX_STEPS, "route kept looping past the step budget"
            else:
                halted_at = step_count
                break
        assert halted_at is not None, "route never halted on an adversarial always-acting input"
        assert halted_at <= MAX_STEPS

    def test_halts_exactly_at_max_steps_not_later(self):
        state = _state_at_step(MAX_STEPS, _AlwaysWantsToActMessage())
        assert route(state) != "reason"

    def test_one_step_below_budget_still_allowed_to_continue(self):
        state = _state_at_step(MAX_STEPS - 1, _AlwaysWantsToActMessage())
        assert route(state) == "reason"

    def test_route_with_tools_same_adversarial_guarantee(self):
        """`route_with_tools` (the Module 3+ tool-using variant) must make
        the identical bounding guarantee — a second implementation of the
        same rule is still just as required to honour it."""
        state = _state_at_step(MAX_STEPS, _AlwaysWantsToActMessage())
        assert route_with_tools(state) != "tools"

    @pytest.mark.parametrize("step_count", list(range(0, MAX_STEPS)))
    def test_every_step_below_budget_keeps_looping_on_adversarial_input(self, step_count):
        state = _state_at_step(step_count, _AlwaysWantsToActMessage())
        assert route(state) == "reason"


class TestGoalReachedTerminatesEarly:
    def test_final_answer_with_no_tool_calls_ends_immediately(self):
        """The OTHER termination condition: a genuine final answer ends
        the loop long before the budget, so termination is not achieved
        ONLY by exhausting the budget on a well-behaved input."""
        state = _state_at_step(1, _FinalAnswerMessage())
        assert route(state) != "reason"
