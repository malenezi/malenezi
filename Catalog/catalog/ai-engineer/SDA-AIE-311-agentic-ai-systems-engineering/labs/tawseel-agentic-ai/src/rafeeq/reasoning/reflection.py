"""Module 2 — Reflection: a bounded critic pass before returning.

Unchanged in substance from the instructor package: after producing a
candidate answer, a critic evaluates it against CONCRETE, checkable
criteria and revises if needed, bounded by `MAX_REFLECTIONS` (core.config)
so the loop cannot run forever (Module 1's bounding discipline, recurring
here). Reflect only on high-stakes, hard-to-reverse outputs (money,
compliance) — not on every "where is my order" answer (module placement
rule).

Needs only `pydantic` + `rafeeq.core.llm.get_model` — runs under plain
python3 with the default `StubChatModel`, no langgraph required.
"""
from __future__ import annotations

from pydantic import BaseModel

from rafeeq.core.config import MAX_REFLECTIONS
from rafeeq.core.llm import get_model

try:  # pragma: no cover - exercised only when langchain-core is installed
    from langchain_core.messages import SystemMessage, HumanMessage
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    from dataclasses import dataclass as _dataclass

    @_dataclass
    class SystemMessage:  # type: ignore[no-redef]
        content: str
        type: str = "system"

    @_dataclass
    class HumanMessage:  # type: ignore[no-redef]
        content: str
        type: str = "human"


CRITERIA = ("1) refund amount within stated eligibility; "
            "2) reply in the customer's language; "
            "3) cites the applicable Tawseel policy; "
            "4) no PII beyond what the customer supplied.")


class Critique(BaseModel):
    passes: bool
    issues: list[str]


def reflect(candidate: str, context: str) -> Critique:
    critic = get_model().with_structured_output(Critique)
    return critic.invoke([
        SystemMessage(content=f"Critique the draft against: {CRITERIA}"),
        HumanMessage(content=f"Context:\n{context}\n\nDraft:\n{candidate}")])


def reflect_and_revise(draft: str, context: str, *, verbose: bool = False) -> dict:
    """Bounded critique-and-revise loop. Returns a dict (not just the
    final draft) so callers — notably `compare.py` — can report how many
    reflection passes actually ran and whether the loop exhausted its
    bound without ever passing (still returns the best-effort draft
    either way; Module 1's "bounded, not silent" discipline applies to
    reflection loops too)."""
    passes_used = 0
    final_passed = False
    for i in range(MAX_REFLECTIONS):
        c = reflect(draft, context)
        passes_used = i + 1
        if verbose:
            print(f"[reflection] pass {passes_used}: passes={c.passes} issues={c.issues}")
        if c.passes:
            final_passed = True
            break
        draft = get_model().invoke([              # revise against concrete issues
            SystemMessage(content="Revise the draft to fix EXACTLY these issues."),
            HumanMessage(content=f"Issues: {c.issues}\n\nDraft:\n{draft}")]).content
    return {
        "draft": draft,                            # bounded: return best effort
        "passes_used": passes_used,
        "final_passed": final_passed,
        "max_reflections": MAX_REFLECTIONS,
    }
