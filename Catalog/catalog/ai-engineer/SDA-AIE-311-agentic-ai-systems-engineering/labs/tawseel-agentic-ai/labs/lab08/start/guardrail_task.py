"""Lab 8, Tasks 1/2 — input and output guardrails.

Fill in the TODOs. TEACHING POINT to internalise before you write a line:
an input guardrail is a FILTER, not a WALL — it flags and masks, it never
itself authorises or denies. The BLOCKING decision belongs to the output
guard, consulting `action_risk.classify` — structure, not a filter, is
what a crafted phrasing cannot talk past.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.security.action_risk import classify

_FLAGS = re.IGNORECASE | re.UNICODE

# TODO(lab 8.1a): add at least 2 more (family, pattern) pairs of your own
# — one Arabic, one English — covering a family NOT already here (e.g.
# "role_play": pretend to be a system administrator / تظاهر بأنك مسؤول).
INJECTION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("instruction_override", re.compile(r"ignore\s+(all|any|every|the)?\s*(previous|prior)?\s*instructions?", _FLAGS)),
    ("instruction_override", re.compile(r"تجاهل\s*(كل|جميع)?\s*(التعليمات|الأوامر)", _FLAGS)),
    ("false_authority", re.compile(r"(system\s*override|i\s*am\s*(the\s*)?(admin|developer|your\s*creator))", _FLAGS)),
]

PII_PATTERNS: dict[str, re.Pattern[str]] = {
    "national_id": re.compile(r"\b\d{10}\b"),
    "phone": re.compile(r"\b05\d{8}\b"),
}


@dataclass
class GuardResult:
    allow: bool
    flags: list[str]
    cleaned: str
    risk_score: float


def screen_input(text: str) -> GuardResult:
    """TODO(lab 8.1b): flag every matched injection pattern (append
    `f"injection:{family}"` to `flags`), flag every matched PII pattern
    (append `f"pii:{label}"`), then MASK every PII match in a `cleaned`
    copy of the text (`pattern.sub(f"[{label}_REDACTED]", cleaned)` —
    mask BEFORE anything reaches memory, Module 4's lesson reused here).
    `risk_score` = `min(1.0, 0.3 * len(injection flags) + 0.15 *
    bool(pii flags))`. `allow` is ALWAYS `True` — this function never
    blocks, only flags (see the module teaching point above).
    """
    raise NotImplementedError("TODO(lab 8.1b): implement screen_input")


def guard_tool_call(tool_name: str, args: dict[str, Any], actor_customer_id: str | None = None) -> dict | None:
    """TODO(lab 8.2): the STRUCTURAL stop. Consult
    `classify(tool_name, args)` (the real action-risk matrix, SPEC §5):

    1. If `decision.prohibited` -> return `{"error": "prohibited_action",
       "tool_name": tool_name}`.
    2. If `decision.requires_human_approval` -> return `{"error":
       "human_approval_required", "tool_name": tool_name}`.
    3. Otherwise return `None` (allow the call through).

    Task 3 asks you to prove this holds EVEN WHEN `screen_input` above is
    disabled entirely — because this function never reads `screen_input`'s
    verdict in the first place. That IS the layered-defence property.
    """
    raise NotImplementedError("TODO(lab 8.2): implement guard_tool_call")
