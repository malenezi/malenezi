"""Lab 2, Task 3 — a bounded Reflection gate on a high-stakes output.

Reflect only on the refund draft (money, hard to reverse) — never on
"where is my order" (module placement rule). Fill in the TODOs.
"""
from __future__ import annotations

import sys
from pathlib import Path

from pydantic import BaseModel

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import MAX_REFLECTIONS
from rafeeq.core.llm import get_model

CRITERIA = ("1) refund amount within stated eligibility; "
            "2) reply in the customer's language; "
            "3) cites the applicable Tawseel policy; "
            "4) no PII beyond what the customer supplied.")


class Critique(BaseModel):
    passes: bool
    issues: list[str]


def reflect(candidate: str, context: str) -> Critique:
    """Provided: one critic pass against `CRITERIA`."""
    critic = get_model().with_structured_output(Critique)
    return critic.invoke([("system", f"Critique the draft against: {CRITERIA}"),
                           ("human", f"Context:\n{context}\n\nDraft:\n{candidate}")])


def reflect_and_revise(draft: str, context: str, *, verbose: bool = False) -> dict:
    """TODO(lab 2.3): bounded critique-and-revise loop.

    For up to `MAX_REFLECTIONS` passes:
      1. `c = reflect(draft, context)`
      2. If `c.passes` is True, stop — return the CURRENT draft.
      3. Otherwise, revise: `draft = get_model().invoke([...]).content`
         asking the model to fix EXACTLY `c.issues`, and try again.

    Return `{"draft": draft, "passes_used": int, "final_passed": bool,
    "max_reflections": MAX_REFLECTIONS}` either way — this is Module 1's
    "bounded, not silent" discipline applied to a reflection loop: if the
    bound is exhausted without ever passing, return the best-effort draft
    anyway, never loop past `MAX_REFLECTIONS` (see
    `labs/sim/sim_react_thrash.py`'s sibling failure mode, and the
    troubleshooting row "Reflection never stops" below).
    """
    raise NotImplementedError("TODO(lab 2.3): implement reflect_and_revise")
