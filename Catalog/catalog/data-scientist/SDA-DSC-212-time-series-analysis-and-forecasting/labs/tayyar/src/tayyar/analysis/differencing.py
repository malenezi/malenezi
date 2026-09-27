"""Choose the minimum differencing that achieves stationarity. Seasonal first."""
from __future__ import annotations
import pandas as pd
from .stationarity import stationarity_report


def choose_differencing(y: pd.Series, m: int = 24, max_d: int = 2,
                        max_D: int = 1, alpha: float = 0.05) -> dict:
    """Returns (d, D) and the trace. Rule: seasonal difference first, then regular,
    and stop at the first stationary verdict — over-differencing adds MA structure
    and inflates variance."""
    trace, s, D, d = [], y.dropna().astype(float), 0, 0
    r = stationarity_report(s, alpha)
    trace.append({"d": 0, "D": 0, **r})
    while D < max_D and r["verdict"] != "stationary":
        s2 = s.diff(m).dropna()
        r2 = stationarity_report(s2, alpha)
        D += 1; s = s2; r = r2
        trace.append({"d": d, "D": D, **r})
        if r["verdict"] == "stationary":
            break
    while d < max_d and r["verdict"] != "stationary":
        s2 = s.diff().dropna()
        r2 = stationarity_report(s2, alpha)
        d += 1; s = s2; r = r2
        trace.append({"d": d, "D": D, **r})
    return {"d": d, "D": D, "m": m, "final_verdict": r["verdict"],
            "trace": pd.DataFrame(trace), "series": s}


def difference(y: pd.Series, d: int = 0, D: int = 0, m: int = 24) -> pd.Series:
    s = y.copy()
    for _ in range(D):
        s = s.diff(m)
    for _ in range(d):
        s = s.diff()
    return s.dropna()
