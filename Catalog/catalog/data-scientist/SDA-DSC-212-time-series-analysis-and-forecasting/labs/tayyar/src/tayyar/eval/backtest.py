"""Rolling-origin backtest. One split is an anecdote; fifty origins are evidence.

Expanding window : train grows, keeps all history (stable regimes)
Sliding  window  : fixed length, forgets old data (drifting regimes)

The two rules that make it a backtest rather than theatre:
  1. refit at every origin (strategy="refit"); a fit-once "backtest" scores
     points the model already saw.
  2. every feature at origin t uses only data <= t.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from dataclasses import dataclass, field
from .metrics import all_metrics


@dataclass
class BacktestConfig:
    horizon: int = 24
    n_origins: int = 50
    step: int = 24
    initial_train: int = 24 * 365
    window: str = "expanding"          # or "sliding"
    m: int = 24


def origins(index: pd.DatetimeIndex, cfg: BacktestConfig):
    """Yield (train_slice, test_slice) index positions, newest origins last."""
    n = len(index)
    last = n - cfg.horizon
    first = cfg.initial_train
    stops = list(range(last, first, -cfg.step))[:cfg.n_origins][::-1]
    for stop in stops:
        start = 0 if cfg.window == "expanding" else max(0, stop - cfg.initial_train)
        yield slice(start, stop), slice(stop, stop + cfg.horizon)


def rolling_backtest(y: pd.Series, forecaster, cfg: BacktestConfig | None = None,
                     exog: pd.DataFrame | None = None, name: str = "model"):
    """`forecaster(y_train, horizon, exog_train, exog_future) -> array[horizon]`"""
    cfg = cfg or BacktestConfig()
    rows = []
    for i, (tr, te) in enumerate(origins(y.index, cfg)):
        y_tr, y_te = y.iloc[tr], y.iloc[te]
        if len(y_te) < cfg.horizon:
            continue
        try:
            f = np.asarray(forecaster(y_tr, cfg.horizon,
                                      None if exog is None else exog.iloc[tr],
                                      None if exog is None else exog.iloc[te]),
                           dtype=float)
        except Exception as e:                       # a fold that fails is data
            rows.append({"origin": y.index[te.start], "model": name,
                         "error": str(e)[:80]})
            continue
        rows.append({"origin": y.index[te.start], "model": name,
                     **all_metrics(y_te, f, y_tr, cfg.m)})
    return pd.DataFrame(rows)


def summarise(bt: pd.DataFrame) -> pd.DataFrame:
    num = bt.select_dtypes("number").columns
    return (bt.groupby("model")[list(num)].mean().round(4)
              .sort_values("MASE" if "MASE" in num else num[0]))
