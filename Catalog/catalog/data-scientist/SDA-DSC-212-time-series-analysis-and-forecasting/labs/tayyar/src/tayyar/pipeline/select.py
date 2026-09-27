"""End-to-end candidate evaluation and champion selection."""
from __future__ import annotations
import numpy as np, pandas as pd
from ..eval.backtest import BacktestConfig, rolling_backtest, summarise
from ..eval.diebold_mariano import diebold_mariano


def evaluate_candidates(y: pd.Series, candidates: dict, cfg: BacktestConfig,
                        exog: pd.DataFrame | None = None) -> pd.DataFrame:
    return pd.concat([rolling_backtest(y, fn, cfg, exog, name=n)
                      for n, fn in candidates.items()], ignore_index=True)


def champion(bt: pd.DataFrame, metric: str = "MASE") -> str:
    return summarise(bt).index[0]


def significance_matrix(per_origin: dict, y_true: np.ndarray, h: int = 24) -> pd.DataFrame:
    names = list(per_origin)
    rows = []
    for a in names:
        for b in names:
            if a >= b:
                continue
            r = diebold_mariano(y_true, per_origin[a], per_origin[b], h=h)
            rows.append({"model_1": a, "model_2": b, **r})
    return pd.DataFrame(rows)
