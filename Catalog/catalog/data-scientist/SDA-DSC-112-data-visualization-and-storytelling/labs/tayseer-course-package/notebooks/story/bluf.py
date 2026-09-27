
"""story/bluf.py — the one-page top-line an executive reads in 90 seconds.

BLUF first, evidence second, methodology on request. This inverts the analyst's
instinct (method -> results -> conclusion) into the decision-maker's need
(conclusion -> evidence -> method-on-request).

The test is not "is it complete?" It is: can a peer ACT on this in 90 seconds,
without the deck?
"""
from __future__ import annotations


def render_bluf(recommendation: str, because: str, stakes: str, ask: str,
                evidence: list[str], risks: list[str] | None = None,
                appendix: list[str] | None = None) -> str:
    lines = [
        "# Recommendation",
        "",
        f"**{recommendation}**",
        "",
        f"**Why now:** {stakes}",
        "",
        f"**Rationale:** {because}",
        "",
        "**Evidence (one line each):**",
    ]
    lines += [f"- {e}" for e in evidence]
    if risks:
        lines += ["", "**Risks and how they are managed:**"]
        lines += [f"- {r}" for r in risks]
    lines += ["", f"**The ask:** {ask}"]
    if appendix:
        lines += ["", "**In the appendix, on request:** " + "; ".join(appendix) + "."]
    lines += ["", "_Full analysis and dashboard in appendix; "
                  "methodology available on request._"]
    return "\n".join(lines)


def word_count(memo: str) -> int:
    return len([w for w in memo.split() if w.strip("-*_#")])


def reading_seconds(memo: str, wpm: int = 220) -> float:
    """An executive reads a memo, they do not study it. 220 wpm is generous."""
    return round(60 * word_count(memo) / wpm, 1)
