"""Module 2 — run ReAct, Plan-and-Execute, and Reflection on the SAME
ticket set and return the cost/latency/quality comparison table Lab 2
asks participants to fill in (`BENCHMARKS.md`).

Deliberately Layer A: every pattern this module drives
(`reasoning.react.react_loop_explicit`, `reasoning.plan_execute.run_plan_execute`,
`reasoning.reflection.reflect_and_revise`, `reasoning.refund_prompt_only.naive_refund_handler`)
needs only `pydantic` + `rafeeq.core.llm.get_model` (the `StubChatModel` by
default, SPEC §2) — no langgraph. `compare_patterns()` runs, end to end,
under plain python3 in this build sandbox.

TEACHING POINT on the cost column: in the default `stub`/`replay` model
mode no real API call is made (SPEC §2 — zero cost by design), so `cost_usd`
here is a SIMULATED cost: token counts estimated from the actual
input/output text (`rafeeq.core.llm.estimate_tokens`) priced at the
configured cheap-model rate (`rafeeq.core.llm.PRICE`), as if each call had
gone to that real model. That is exactly the cost model Module 2 asks
participants to build and is the same technique `RAFEEQ_MODEL_MODE=live`
would report for real, just computed without spending anything.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from typing import Any, Iterable

from rafeeq.core.config import TICKETS_EVAL_PATH, get_settings
from rafeeq.core.llm import estimate_cost_usd
from rafeeq.reasoning.plan_execute import run_plan_execute
from rafeeq.reasoning.react import react_loop_explicit
from rafeeq.reasoning.reflection import reflect_and_revise
from rafeeq.reasoning.refund_prompt_only import naive_refund_handler


def load_tickets(path=TICKETS_EVAL_PATH, limit: int | None = None) -> list[dict[str, Any]]:
    """Load `tickets_eval.jsonl` (SPEC §4 shape). Returns `[]` rather than
    raising if the file is not present yet — comparison degrades to "no
    tickets measured" instead of crashing the import chain."""
    if not path.exists():
        return []
    tickets = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                tickets.append(json.loads(line))
    return tickets[:limit] if limit else tickets


def _score(final_text: str, expected: dict[str, Any] | None) -> float:
    """Cheap, deterministic quality proxy against `tickets_eval.jsonl`'s
    `expected` block: 1.0 if every `must_mention` string appears in the
    output and no `must_not` string does; partial credit (0.5) if
    `must_mention` is present but a `must_not` term leaked; 0.0 otherwise.
    Not a substitute for `evaluations/oracles.py` (owned elsewhere) — a
    lightweight, dependency-free stand-in so this module's table is
    meaningful without it.
    """
    if not expected:
        return 0.0
    text = final_text or ""
    must_mention = expected.get("must_mention") or []
    must_not = expected.get("must_not") or []
    mentions_ok = all(term in text for term in must_mention) if must_mention else True
    leaks = any(term in text for term in must_not)
    if mentions_ok and not leaks:
        return 1.0
    if mentions_ok and leaks:
        return 0.5
    return 0.0


def _cost_for(num_calls: int, input_text: str, output_text: str) -> float:
    model_name = get_settings().cheap_model_name
    per_call = estimate_cost_usd(model_name, input_text, output_text)
    return round(per_call * max(num_calls, 0), 6)


@dataclass
class PatternResult:
    pattern: str
    ticket_id: str
    steps_or_passes: int
    tool_calls: int
    redundant_tool_calls: int
    latency_s: float
    cost_usd: float
    quality: float


@dataclass
class ComparisonTable:
    rows: list[PatternResult] = field(default_factory=list)

    def summary(self) -> dict[str, dict[str, float]]:
        """Aggregate per-pattern averages — the table Lab 2 asks
        participants to paste into `BENCHMARKS.md`."""
        by_pattern: dict[str, list[PatternResult]] = {}
        for r in self.rows:
            by_pattern.setdefault(r.pattern, []).append(r)
        out: dict[str, dict[str, float]] = {}
        for pattern, rows in by_pattern.items():
            n = len(rows)
            out[pattern] = {
                "tickets": n,
                "avg_steps": round(sum(r.steps_or_passes for r in rows) / n, 2),
                "avg_tool_calls": round(sum(r.tool_calls for r in rows) / n, 2),
                "avg_redundant_tool_calls": round(sum(r.redundant_tool_calls for r in rows) / n, 2),
                "avg_latency_s": round(sum(r.latency_s for r in rows) / n, 4),
                "avg_cost_usd": round(sum(r.cost_usd for r in rows) / n, 6),
                "success_rate": round(sum(1 for r in rows if r.quality >= 1.0) / n, 3),
            }
        return out

    def render(self) -> str:
        summary = self.summary()
        if not summary:
            return "No tickets available to compare (data/tickets_eval.jsonl not found)."
        cols = ["pattern", "tickets", "avg_steps", "avg_tool_calls",
                "avg_redundant_tool_calls", "avg_latency_s", "avg_cost_usd", "success_rate"]
        lines = [" | ".join(cols), " | ".join("-" * len(c) for c in cols)]
        for pattern, stats in summary.items():
            row = [pattern] + [str(stats[c]) for c in cols[1:]]
            lines.append(" | ".join(row))
        return "\n".join(lines)


def _run_react(ticket: dict[str, Any]) -> PatternResult:
    start = time.perf_counter()
    trace = react_loop_explicit(ticket["text"], verbose=False)
    latency = time.perf_counter() - start
    cost = _cost_for(trace.step_count + 1, ticket["text"], trace.final_answer)
    quality = _score(trace.final_answer, ticket.get("expected"))
    return PatternResult(
        pattern="react", ticket_id=ticket.get("ticket_id", ""),
        steps_or_passes=trace.step_count, tool_calls=len(trace.steps),
        redundant_tool_calls=trace.redundant_tool_calls, latency_s=round(latency, 4),
        cost_usd=cost, quality=quality,
    )


def _run_plan_execute(ticket: dict[str, Any]) -> PatternResult:
    start = time.perf_counter()
    result = run_plan_execute(ticket["text"], verbose=False)
    latency = time.perf_counter() - start
    steps = result.get("plan", [])
    final_text = "; ".join(r for _step, r in result.get("past", []))
    num_calls = 1 + len(result.get("past", []))            # 1 planning call + N execute calls
    cost = _cost_for(num_calls, ticket["text"], final_text)
    quality = _score(final_text, ticket.get("expected"))
    return PatternResult(
        pattern="plan_execute", ticket_id=ticket.get("ticket_id", ""),
        steps_or_passes=len(steps), tool_calls=len(result.get("past", [])),
        redundant_tool_calls=0,     # Plan-and-Execute does not revisit steps by design
        latency_s=round(latency, 4), cost_usd=cost, quality=quality,
    )


def _run_plan_execute_with_reflection(ticket: dict[str, Any]) -> PatternResult:
    start = time.perf_counter()
    result = run_plan_execute(ticket["text"], verbose=False)
    draft = "; ".join(r for _step, r in result.get("past", [])) or ticket["text"]
    reflected = reflect_and_revise(draft, context=ticket["text"])
    latency = time.perf_counter() - start
    num_calls = 1 + len(result.get("past", [])) + reflected["passes_used"] * 2
    cost = _cost_for(num_calls, ticket["text"], reflected["draft"])
    quality = _score(reflected["draft"], ticket.get("expected"))
    return PatternResult(
        pattern="plan_execute_reflection", ticket_id=ticket.get("ticket_id", ""),
        steps_or_passes=len(result.get("plan", [])), tool_calls=len(result.get("past", [])),
        redundant_tool_calls=0, latency_s=round(latency, 4), cost_usd=cost, quality=quality,
    )


def _run_prompt_only(ticket: dict[str, Any]) -> PatternResult:
    """The Module 7 anti-pattern, included here purely for the cost/
    determinism contrast Lab 7 asks for — NOT a pattern to recommend."""
    start = time.perf_counter()
    result = naive_refund_handler(ticket["text"])
    latency = time.perf_counter() - start
    cost = _cost_for(1, ticket["text"], result["content"])
    quality = _score(result["content"], ticket.get("expected"))
    return PatternResult(
        pattern="prompt_only_anti_pattern", ticket_id=ticket.get("ticket_id", ""),
        steps_or_passes=1, tool_calls=len(result["tool_calls"]),
        redundant_tool_calls=0, latency_s=round(latency, 4), cost_usd=cost, quality=quality,
    )


def compare_patterns(
    tickets: Iterable[dict[str, Any]] | None = None,
    *,
    limit: int = 10,
    include_prompt_only: bool = True,
) -> ComparisonTable:
    """Run ReAct, Plan-and-Execute, Plan-and-Execute+Reflection, and
    (optionally) the Module 7 prompt-only anti-pattern on the same ticket
    set, returning a `ComparisonTable`. Defaults to the first `limit`
    tickets of `data/tickets_eval.jsonl`."""
    tickets = list(tickets) if tickets is not None else load_tickets(limit=limit)
    table = ComparisonTable()
    for ticket in tickets:
        table.rows.append(_run_react(ticket))
        table.rows.append(_run_plan_execute(ticket))
        table.rows.append(_run_plan_execute_with_reflection(ticket))
        if include_prompt_only:
            table.rows.append(_run_prompt_only(ticket))
    return table


if __name__ == "__main__":  # pragma: no cover - manual classroom demo
    result = compare_patterns(limit=10)
    print(result.render())
