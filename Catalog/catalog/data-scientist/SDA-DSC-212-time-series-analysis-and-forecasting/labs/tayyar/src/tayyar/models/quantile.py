"""Quantile LightGBM: a prediction interval, not a point guess."""
from __future__ import annotations
import numpy as np, pandas as pd, lightgbm as lgb

BASE = dict(objective="quantile", n_estimators=350, learning_rate=0.06,
            num_leaves=63, min_child_samples=30, verbose=-1, random_state=212)


class QuantileLGBM:
    """Fits one model per quantile. Quantile crossing (q95 < q50) is possible and
    is fixed by row-wise sorting — never by pretending it did not happen."""

    def __init__(self, quantiles=(0.05, 0.50, 0.95), horizon: int = 24,
                 params: dict | None = None):
        self.quantiles = tuple(quantiles)
        self.horizon = horizon
        self.params = {**BASE, **(params or {})}
        self.models_: dict[tuple, lgb.LGBMRegressor] = {}

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.feature_names_ = list(X.columns)
        for h in range(1, self.horizon + 1):
            yh = y.shift(-h)
            ok = yh.notna() & X.notna().all(axis=1)
            for q in self.quantiles:
                m = lgb.LGBMRegressor(**{**self.params, "alpha": q})
                m.fit(X.loc[ok], yh.loc[ok])
                self.models_[(h, q)] = m
        return self

    def predict_interval(self, X_origin: pd.DataFrame) -> pd.DataFrame:
        rows = []
        for h in range(1, self.horizon + 1):
            d = {"h": h}
            for q in self.quantiles:
                d[f"q{int(q*100):02d}"] = self.models_[(h, q)].predict(
                    X_origin[self.feature_names_])[-1]
            rows.append(d)
        out = pd.DataFrame(rows).set_index("h")
        qcols = [c for c in out.columns if c.startswith("q")]
        out[qcols] = np.sort(out[qcols].to_numpy(), axis=1)   # de-cross
        return out
