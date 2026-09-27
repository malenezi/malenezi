
"""story/rehearsal_score.py — the fixed critique rubric, applied to two recorded rounds.

Score delivery the SAME way each round so the DELTA is the learning signal. The rubric
is weighted (see `rehearsal_scores.csv`), so a round total is the weighted percentage of
the maximum, not a raw average.
"""
from __future__ import annotations

import pandas as pd

CRITERIA = {
    "Opening / BLUF": 0.20,
    "One message per slide": 0.15,
    "Chart delivery": 0.20,
    "Q&A handling": 0.20,
    "Time discipline": 0.15,
    "Presence": 0.10,
}
MAX_SCORE = 5


def score_round(scores: dict, notes: str = "") -> dict:
    """Score one round. Every criterion must be present — partial rubrics hide regressions."""
    missing = set(CRITERIA) - set(scores)
    assert not missing, f"score every criterion; missing {sorted(missing)}"
    weighted = sum(scores[c] / MAX_SCORE * w for c, w in CRITERIA.items())
    return {"scores": dict(scores),
            "pct": round(100 * weighted / sum(CRITERIA.values())),
            "notes": notes}


def score_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Recompute round totals from the raw rubric rows (participant x round x criterion)."""
    out = (df.groupby(["participant_id", "round"])
             .apply(lambda d: 100 * (d.score_0_5 / MAX_SCORE * d.weight).sum()
                              / d.weight.sum(), include_groups=False)
             .reset_index(name="round_total_pct"))
    return out


def delta(df: pd.DataFrame) -> pd.DataFrame:
    """Round-to-round improvement per participant — the benchmark is the delta."""
    totals = score_frame(df).pivot(index="participant_id", columns="round",
                                   values="round_total_pct")
    totals.columns = [f"round_{c}_pct" for c in totals.columns]
    totals["delta_pp"] = totals.iloc[:, 1] - totals.iloc[:, 0]
    return totals.round(1)


def biggest_mover(df: pd.DataFrame) -> pd.Series:
    """Which criterion moved most between rounds? (Usually: opening with the BLUF.)"""
    by_c = df.pivot_table(index="criterion", columns="round", values="score_0_5")
    by_c.columns = [f"round_{c}" for c in by_c.columns]
    by_c["delta"] = by_c.iloc[:, 1] - by_c.iloc[:, 0]
    return by_c.sort_values("delta", ascending=False).round(2)
