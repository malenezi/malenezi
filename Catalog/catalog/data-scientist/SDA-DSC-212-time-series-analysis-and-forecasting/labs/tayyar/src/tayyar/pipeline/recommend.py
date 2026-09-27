"""Constraint-weighted scoring: accuracy is one column, not the decision."""
from __future__ import annotations
import pandas as pd

DEFAULT_WEIGHTS = {"accuracy": 0.40, "calibration": 0.20, "latency": 0.15,
                   "explainability": 0.15, "maintainability": 0.10}


def score(profiles: pd.DataFrame, weights: dict | None = None) -> pd.DataFrame:
    """profiles: index=model, columns=criteria scored 0-1 (higher is better)."""
    w = pd.Series(weights or DEFAULT_WEIGHTS)
    w = w / w.sum()
    cols = [c for c in w.index if c in profiles.columns]
    out = profiles.copy()
    out["weighted_score"] = (profiles[cols] * w[cols]).sum(axis=1).round(3)
    return out.sort_values("weighted_score", ascending=False)


def flip_conditions(ranked: pd.DataFrame, weights: dict | None = None) -> list[str]:
    """What would have to change for the runner-up to win. State it in the record."""
    w = weights or DEFAULT_WEIGHTS
    top, second = ranked.index[0], ranked.index[1]
    gap = ranked.loc[top, "weighted_score"] - ranked.loc[second, "weighted_score"]
    out = []
    for c, wt in w.items():
        if c not in ranked.columns:
            continue
        d = ranked.loc[second, c] - ranked.loc[top, c]
        need = gap / wt if wt else float("inf")
        if 0 < need <= 1:
            out.append(f"If {second}'s {c} improves by {need:.2f} (or {top}'s "
                       f"falls by the same), {second} becomes champion.")
    out.append(f"Score gap {top} over {second}: {gap:.3f}.")
    return out
