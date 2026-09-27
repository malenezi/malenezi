"""Lab 1, Task 5 — the adversarial termination test.

Write ONE test proving your `route()` (Task 3) halts within `MAX_STEPS`
on an input that NEVER satisfies the goal — a fake last message that
always carries a tool call, so the ONLY thing that can stop the loop is
the step budget, never "the model decided it was done".

Run it (no pytest required — plain unittest):

    PYTHONPATH=src python3 -m unittest labs.lab01.start.test_termination -v

Compare against the real one once you are green:
`tests/unit/test_termination.py`.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
_LAB_START = Path(__file__).resolve().parent
for _p in (_SRC, _REPO_ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from rafeeq.core.config import MAX_STEPS  # the SAME constant your route() must respect

# TODO(lab 1.5a): import YOUR route() from graph.py once Task 3 is done.
# from graph import route   # (this file's own directory is on sys.path)


class _AlwaysWantsToActMessage:
    """A fake last message that ALWAYS carries a tool call — the
    adversarial condition: a goal that is never satisfied."""

    tool_calls = [{"name": "track_shipment", "args": {"order_id": "TW-2026-00000"}, "id": "call_1"}]


class TestAdversarialTerminatesWithinMaxSteps(unittest.TestCase):
    def test_never_satisfies_goal_still_halts_at_budget(self) -> None:
        """TODO(lab 1.5b): drive route() step by step (step_count = 0..
        MAX_STEPS+5, deliberately overshooting) with a state whose last
        message is `_AlwaysWantsToActMessage()`. Assert:

          - below MAX_STEPS, route() returns "reason" (keeps looping)
          - at/after MAX_STEPS, route() does NOT return "reason"
          - the loop halts at or before MAX_STEPS, never later

        This is the troubleshooting row "Agent never loops" turned
        inside-out: prove the OPPOSITE failure (never halting) cannot
        happen either.
        """
        raise NotImplementedError("TODO(lab 1.5b): write the adversarial termination test")


if __name__ == "__main__":
    unittest.main()
