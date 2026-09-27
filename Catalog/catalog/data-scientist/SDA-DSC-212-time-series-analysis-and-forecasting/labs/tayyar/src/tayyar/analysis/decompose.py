"""Decomposition: what structure exists, and what must a model capture?"""
from __future__ import annotations
import numpy as np, pandas as pd
from statsmodels.tsa.seasonal import STL, MSTL


def seasonal_strength(seasonal: pd.Series, remainder: pd.Series) -> float:
    """Hyndman & Athanasopoulos strength: 1 - Var(R) / Var(S + R), clipped to [0,1]."""
    v = np.nanvar(seasonal + remainder)
    return float(np.clip(1 - np.nanvar(remainder) / v, 0, 1)) if v > 0 else 0.0


def trend_strength(trend: pd.Series, remainder: pd.Series) -> float:
    v = np.nanvar(trend + remainder)
    return float(np.clip(1 - np.nanvar(remainder) / v, 0, 1)) if v > 0 else 0.0


def mstl_decompose(y: pd.Series, periods=(24, 24 * 7)) -> dict:
    """Multiple-seasonality STL. `periods` are *observations per cycle*."""
    s = y.astype(float)
    if s.isna().any():          # STL/MSTL cannot handle NaN — interpolate first
        s = s.interpolate("time").ffill().bfill()
    res = MSTL(s, periods=periods).fit()
    seas = res.seasonal
    if isinstance(seas, pd.Series):
        seas = seas.to_frame()
    out = {"trend": res.trend, "remainder": res.resid, "seasonal": seas,
           "strength": {}}
    for col, p in zip(seas.columns, periods):
        out["strength"][f"seasonal_{p}"] = seasonal_strength(seas[col], res.resid)
    out["strength"]["trend"] = trend_strength(res.trend, res.resid)
    return out


def stl_decompose(y: pd.Series, period: int = 24, robust: bool = True):
    return STL(y.astype(float), period=period, robust=robust).fit()
