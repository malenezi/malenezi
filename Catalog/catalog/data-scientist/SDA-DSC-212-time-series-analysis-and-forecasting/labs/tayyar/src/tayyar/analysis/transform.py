"""Additive or multiplicative? Decide on evidence, not on taste."""
from __future__ import annotations
import numpy as np, pandas as pd


def additive_or_multiplicative(y: pd.Series, period: int = 24 * 7) -> dict:
    """If the seasonal swing grows with the level, the series is multiplicative.

    Evidence = correlation between per-cycle level and per-cycle amplitude.
    corr > 0.4  -> multiplicative (model log(y) additively)
    """
    g = y.groupby(np.arange(len(y)) // period)
    level, swing = g.mean(), g.max() - g.min()
    ok = level.notna() & swing.notna()
    corr = float(np.corrcoef(level[ok], swing[ok])[0, 1])
    return {"level_swing_corr": round(corr, 3),
            "decision": "multiplicative" if corr > 0.4 else "additive",
            "transform": "log" if corr > 0.4 else "none"}


def apply_transform(y: pd.Series, kind: str) -> pd.Series:
    if kind == "log":
        if (y <= 0).any():
            raise ValueError("log transform requires strictly positive values "
                             "— inspect zeros/negatives (sensor dropouts) first")
        return np.log(y)
    return y


def invert_transform(y: pd.Series | np.ndarray, kind: str):
    return np.exp(y) if kind == "log" else y
