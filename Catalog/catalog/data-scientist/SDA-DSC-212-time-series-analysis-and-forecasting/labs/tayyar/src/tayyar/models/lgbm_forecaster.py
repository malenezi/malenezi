"""Direct multi-step LightGBM forecaster.

Recursive vs direct:
  recursive — one model, feed forecasts back as lags. Cheap; errors compound.
  direct    — one model per horizon h, target y[t+h]. H models; no compounding.
This class is *direct*, because at h=24 the compounding of a recursive chain is
exactly where day-ahead load forecasts fall apart.

Trees interpolate. A gradient-boosted model can never forecast a record-high
demand it has not seen — which is why the classical/level models stay in the
candidate set for a growing series.
"""
from __future__ import annotations
import numpy as np, pandas as pd, lightgbm as lgb

DEFAULT_PARAMS = dict(objective="l1", n_estimators=400, learning_rate=0.06,
                      num_leaves=63, min_child_samples=30, subsample=0.9,
                      subsample_freq=1, colsample_bytree=0.85, verbose=-1,
                      random_state=212)


class DirectLGBMForecaster:
    def __init__(self, horizon: int = 24, params: dict | None = None):
        self.horizon = horizon
        self.params = {**DEFAULT_PARAMS, **(params or {})}
        self.models_: dict[int, lgb.LGBMRegressor] = {}
        self.feature_names_: list[str] = []

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.feature_names_ = list(X.columns)
        for h in range(1, self.horizon + 1):
            yh = y.shift(-h)                       # target is h steps AHEAD
            ok = yh.notna() & X.notna().all(axis=1)
            m = lgb.LGBMRegressor(**self.params)
            m.fit(X.loc[ok], yh.loc[ok])
            self.models_[h] = m
        return self

    def predict(self, X_origin: pd.DataFrame) -> pd.DataFrame:
        """X_origin: one row per forecast origin. Returns origin x horizon."""
        preds = {h: m.predict(X_origin[self.feature_names_])
                 for h, m in self.models_.items()}
        return pd.DataFrame(preds, index=X_origin.index)

    def forecast(self, X_origin_row: pd.DataFrame, freq="h") -> pd.Series:
        row = X_origin_row.tail(1)
        vals = [self.models_[h].predict(row[self.feature_names_])[0]
                for h in range(1, self.horizon + 1)]
        idx = pd.date_range(row.index[-1] + pd.Timedelta(1, "h"),
                            periods=self.horizon, freq=freq)
        return pd.Series(vals, index=idx, name="lgbm")

    def feature_importance(self, top: int = 20) -> pd.DataFrame:
        imp = np.mean([m.booster_.feature_importance(importance_type="gain")
                       for m in self.models_.values()], axis=0)
        return (pd.DataFrame({"feature": self.feature_names_, "gain": imp})
                .sort_values("gain", ascending=False).head(top)
                .reset_index(drop=True))
