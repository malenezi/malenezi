"""Lab 5, Tasks 2/3/4 — specialists vs the single-agent monolith, measured.

A specialist's real advantage is a SMALLER, SCOPED tool belt narrowing the
model's choice space (module overview). You can measure exactly that
offline, with the same `StubChatModel.bind_tools()` mechanism a real
`make_specialist()`-built agent uses under the hood: bind only a domain's
tools -> specialist behaviour; bind the FULL catalogue -> monolith
behaviour. Building the actual LangGraph specialist agents
(`rafeeq.agents.specialist.make_specialist`) needs `langgraph`; this file
does not, so the core lesson (accuracy delta) is measurable either way.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import TICKETS_EVAL_PATH
from rafeeq.core.llm import get_model
from rafeeq.tools.registry import ALL_TOOLS, TOOL_DOMAIN


def load_tickets_for_domain(domain: str, n: int = 40) -> list[dict]:
    """Provided: tickets whose `expected.specialist` matches `domain`."""
    out = []
    with TICKETS_EVAL_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            t = json.loads(line)
            if t.get("expected", {}).get("specialist") == domain and t.get("expected", {}).get("tools"):
                out.append(t)
            if len(out) >= n:
                break
    return out


def domain_tools(domain: str) -> list:
    """Provided: the tool objects belonging to one domain, from the
    governed catalogue (`registry.TOOL_DOMAIN`)."""
    return [t for t in ALL_TOOLS if TOOL_DOMAIN[t.name] == domain]


def tool_selection_accuracy(tickets: list[dict], tools: list) -> float:
    """TODO(lab 5.2/5.3/5.4): bind `tools` to a model
    (`get_model().bind_tools(tools)`), run every ticket's `text` through
    it, and return the fraction where the model's chosen tool name is in
    `ticket["expected"]["tools"]`. Reuse this ONE function for BOTH:

      - Task 2/3: call it with `domain_tools("orders")` /
        `domain_tools("logistics")` / `domain_tools("billing")` against
        each domain's own ticket slice — the SPECIALIST measurement.
      - Task 4: call it with the FULL `ALL_TOOLS` against a MIXED ticket
        set (tickets from more than one domain concatenated) — the
        MONOLITH baseline.

    Expect specialists noticeably higher on mixed/ambiguous tickets, and
    the monolith sometimes marginally cheaper on trivial single-domain
    ones — report both, honestly (the module's own instructor note).
    """
    raise NotImplementedError("TODO(lab 5.2/5.3/5.4): implement tool_selection_accuracy")
