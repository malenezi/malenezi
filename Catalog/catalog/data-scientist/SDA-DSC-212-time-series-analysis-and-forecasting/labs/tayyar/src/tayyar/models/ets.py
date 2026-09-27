"""Exponential smoothing / ETS baselines."""
from __future__ import annotations
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def fit_ets(y: pd.Series, seasonal_periods: int = 24, trend: str = "add",
            seasonal: str = "add", damped: bool = True):
    """Damped trend by default: an undamped linear trend extrapolated 24 h ahead
    is one of the classic ways to produce a confidently absurd forecast."""
    return ExponentialSmoothing(y.astype(float), trend=trend, damped_trend=damped,
                                seasonal=seasonal,
                                seasonal_periods=seasonal_periods,
                                initialization_method="estimated").fit()


def forecast_ets(res, horizon: int) -> pd.Series:
    return res.forecast(horizon).rename("ets")


def ets_grid(y: pd.Series, seasonal_periods: int = 24) -> pd.DataFrame:
    """Small ETS taxonomy sweep. AIC is comparable ONLY across models fitted to
    the same (untransformed, same-length) target."""
    rows = []
    for trend in ("add", None):
        for seasonal in ("add", "mul", None):
            for damped in ((True, False) if trend else (False,)):
                try:
                    r = ExponentialSmoothing(
                        y.astype(float), trend=trend, damped_trend=damped,
                        seasonal=seasonal, seasonal_periods=seasonal_periods,
                        initialization_method="estimated").fit()
                    rows.append({"trend": trend, "seasonal": seasonal,
                                 "damped": damped, "aic": round(r.aic, 1)})
                except Exception as e:
                    rows.append({"trend": trend, "seasonal": seasonal,
                                 "damped": damped, "aic": float("nan"),
                                 "error": str(e)[:60]})
    return pd.DataFrame(rows).sort_values("aic").reset_index(drop=True)
