"""The baseline you must beat. If you cannot beat it, ship it — it is free."""
from __future__ import annotations
import numpy as np, pandas as pd


def seasonal_naive(y: pd.Series, horizon: int, m: int = 24) -> pd.Series:
    """Forecast y[t+h] = y[t+h-m]. The denominator of MASE and the honest default."""
    last = y.iloc[-m:].to_numpy()
    vals = np.array([last[h % m] for h in range(horizon)])
    idx = pd.date_range(y.index[-1] + y.index.freq, periods=horizon,
                        freq=y.index.freq)
    return pd.Series(vals, index=idx, name="seasonal_naive")


def naive(y: pd.Series, horizon: int) -> pd.Series:
    idx = pd.date_range(y.index[-1] + y.index.freq, periods=horizon,
                        freq=y.index.freq)
    return pd.Series(np.repeat(y.iloc[-1], horizon), index=idx, name="naive")


def drift(y: pd.Series, horizon: int) -> pd.Series:
    slope = (y.iloc[-1] - y.iloc[0]) / (len(y) - 1)
    idx = pd.date_range(y.index[-1] + y.index.freq, periods=horizon,
                        freq=y.index.freq)
    return pd.Series(y.iloc[-1] + slope * np.arange(1, horizon + 1),
                     index=idx, name="drift")
