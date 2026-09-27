"""Module 9 — the cost model: attribution, blended cost/contact, SAR view.

"The agent costs too much" is not actionable; "the refund intent costs
0.04 USD because the supervisor and billing specialist each re-send the
full history through the frontier model" is (module overview). This
module turns a `tracing.Run` into that second sentence: `cost_of_run`
attributes every span's token spend by MODEL, by COMPONENT (span name),
and — when the run carries an `intent` — by INTENT/ticket class.

Money discipline (SPEC §7): model spend is USD (`PRICE` in
`core.llm`, what the gateway bills); refunds are SAR (what Tawseel pays
customers). This module only ever computes the former; `SAR_PER_USD` is
a fixed display peg for a board-friendly figure, never a real currency
conversion of anything Tawseel actually pays.

Dependency-free (Layer A): stdlib + `rafeeq.core.llm.PRICE` only.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

from rafeeq.core.llm import PRICE

from rafeeq.observability.tracing import Run, Span

# Saudi Riyal has been pegged to the US Dollar at this rate since 1986.
# Used ONLY to render one board-friendly SAR-equivalent of a USD spend
# figure alongside the real number — see `evaluations/metrics.py`'s own
# (identical) constant and docstring for the same money-discipline rule.
SAR_PER_USD = 3.75


def _price_for(model_name: str | None) -> dict[str, float]:
    if not model_name:
        return PRICE["stub"]
    return PRICE.get(model_name, PRICE["gpt-4o-mini"])


def _span_cost_usd(span: Span) -> float:
    """A span's own USD cost. Prefers an explicit `extra["cost_usd"]`
    (set by a caller that already computed it precisely, e.g. from real
    gateway usage) over recomputing from tokens * PRICE — recomputing is
    the fallback every span with tokens but no explicit cost gets."""
    explicit = span.extra.get("cost_usd")
    if isinstance(explicit, (int, float)):
        return float(explicit)
    if not (span.tokens_in or span.tokens_out):
        return 0.0
    price = _price_for(span.model)
    return (span.tokens_in / 1000.0) * price["input"] + (span.tokens_out / 1000.0) * price["output"]


def _spans_of(trace: Run | dict[str, Any]) -> Iterable[Span]:
    root = trace.root if isinstance(trace, Run) else Span.from_dict(trace["root"])
    return root.walk()


def _intent_of(trace: Run | dict[str, Any]) -> str | None:
    root_extra = trace.root.extra if isinstance(trace, Run) else trace.get("root", {}).get("extra", {})
    return root_extra.get("intent")


@dataclass
class CostBreakdown:
    total_usd: float = 0.0
    by_component: dict[str, float] = field(default_factory=dict)
    by_model: dict[str, float] = field(default_factory=dict)
    by_intent: dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_usd": round(self.total_usd, 6),
            "by_component": {k: round(v, 6) for k, v in self.by_component.items()},
            "by_model": {k: round(v, 6) for k, v in self.by_model.items()},
            "by_intent": {k: round(v, 6) for k, v in self.by_intent.items()},
        }


def cost_of_run(trace: Run | dict[str, Any]) -> CostBreakdown:
    """Attribute a run's total USD spend by model, by component (span
    name), and by intent (from the run's own `root.extra["intent"]`, when
    present — a run started without an intent tag just has an empty
    `by_intent`, which is a fine answer for e.g. an ad-hoc script run).
    Accepts either a live `tracing.Run` or its `.to_dict()`/persisted-JSON
    shape, so a caller can cost either a run still in memory or one
    re-loaded from `reports/traces/<run_id>.json`."""
    breakdown = CostBreakdown()
    intent = _intent_of(trace)
    for span in _spans_of(trace):
        usd = _span_cost_usd(span)
        if usd <= 0:
            continue
        breakdown.total_usd += usd
        breakdown.by_component[span.name] = breakdown.by_component.get(span.name, 0.0) + usd
        model_key = span.model or "unattributed"
        breakdown.by_model[model_key] = breakdown.by_model.get(model_key, 0.0) + usd
        if intent:
            breakdown.by_intent[intent] = breakdown.by_intent.get(intent, 0.0) + usd
    return breakdown


def blended_cost_per_contact(runs: Iterable[Run | dict[str, Any]]) -> float:
    """The single number finance actually tracks: total USD spend across
    a batch of runs (contacts) divided by contact count. `runs` may be
    empty (a fresh environment with no traces yet) — returns 0.0, not a
    ZeroDivisionError."""
    runs = list(runs)
    if not runs:
        return 0.0
    total = sum(cost_of_run(r).total_usd for r in runs)
    return total / len(runs)


def _fmt_usd(v: float) -> str:
    return f"${v:.5f}"


def _fmt_sar(v: float) -> str:
    return f"{v * SAR_PER_USD:.4f} SAR"


def cost_report(runs: list[Run | dict[str, Any]], title: str = "Rafeeq cost report") -> str:
    """Render a markdown cost-attribution report over a batch of runs:
    totals by model/component/intent, plus the blended cost/contact in
    both currencies — the artefact `docs/OBSERVABILITY.md` points to and
    Lab 9 Task 2 asks participants to produce."""
    n = len(runs)
    breakdowns = [cost_of_run(r) for r in runs]
    total_usd = sum(b.total_usd for b in breakdowns)
    blended = (total_usd / n) if n else 0.0

    by_component: dict[str, float] = {}
    by_model: dict[str, float] = {}
    by_intent: dict[str, float] = {}
    for b in breakdowns:
        for k, v in b.by_component.items():
            by_component[k] = by_component.get(k, 0.0) + v
        for k, v in b.by_model.items():
            by_model[k] = by_model.get(k, 0.0) + v
        for k, v in b.by_intent.items():
            by_intent[k] = by_intent.get(k, 0.0) + v

    lines = [f"### {title}", "", f"n = {n} run(s)", "",
             f"- **Total spend:** {_fmt_usd(total_usd)} ({_fmt_sar(total_usd)})",
             f"- **Blended cost/contact:** {_fmt_usd(blended)} ({_fmt_sar(blended)})", ""]

    def _table(heading: str, data: dict[str, float]) -> list[str]:
        out = [f"#### {heading}", "", "| Key | USD | Share |", "|---|---|---|"]
        for key, usd in sorted(data.items(), key=lambda kv: -kv[1]):
            share = (usd / total_usd * 100.0) if total_usd else 0.0
            marker = "  <- the fix" if data and key == max(data, key=data.get) else ""
            out.append(f"| {key} | {_fmt_usd(usd)} | {share:.1f}%{marker} |")
        out.append("")
        return out

    lines += _table("By model", by_model)
    lines += _table("By component", by_component)
    if by_intent:
        lines += _table("By intent", by_intent)
    return "\n".join(lines)
