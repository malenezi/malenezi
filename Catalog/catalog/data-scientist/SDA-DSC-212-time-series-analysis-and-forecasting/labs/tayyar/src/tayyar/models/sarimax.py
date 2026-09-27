"""SARIMAX with temperature and calendar regressors.

Exogenous regressors must be KNOWN at forecast time. Temperature qualifies only
because a day-ahead weather forecast exists — use the forecast, not the realised
value, or you have built a leak that looks like skill.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

EXOG_COLS = ["cdd", "hdd", "is_weekend", "is_ramadan", "is_eid"]


def make_exog(df: pd.DataFrame, cols=EXOG_COLS) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    if "temp_c" in df:
        out["cdd"] = np.clip(df["temp_c"] - 21.0, 0, None)
        out["hdd"] = np.clip(14.0 - df["temp_c"], 0, None)
    for c in ("is_weekend", "is_ramadan", "is_eid"):
        if c in df:
            out[c] = df[c].astype(int)
    return out[[c for c in cols if c in out]]


def fit_sarimax(y: pd.Series, exog: pd.DataFrame | None = None,
                order=(2, 0, 1), seasonal_order=(1, 1, 1, 24)):
    model = SARIMAX(y.astype(float), exog=exog, order=order,
                    seasonal_order=seasonal_order,
                    enforce_stationarity=False, enforce_invertibility=False)
    return model.fit(disp=False)


def forecast_sarimax(res, horizon: int, exog_future: pd.DataFrame | None = None,
                     alpha: float = 0.10) -> pd.DataFrame:
    f = res.get_forecast(steps=horizon, exog=exog_future)
    ci = f.conf_int(alpha=alpha)
    out = pd.DataFrame({"yhat": f.predicted_mean})
    out["lo"], out["hi"] = ci.iloc[:, 0].to_numpy(), ci.iloc[:, 1].to_numpy()
    return out


def residual_diagnostics(res, lags: int = 48) -> dict:
    """A model is not done until its residuals are indistinguishable from noise."""
    from statsmodels.stats.diagnostic import acorr_ljungbox
    from scipy import stats
    r = pd.Series(res.resid).dropna()
    lb = acorr_ljungbox(r, lags=[lags], return_df=True)
    jb_stat, jb_p = stats.jarque_bera(r)[:2]
    p = float(lb["lb_pvalue"].iloc[0])
    return {"ljung_box_p": round(p, 4),
            "residual_autocorrelation": p < 0.05,
            "verdict": ("UNDER-SPECIFIED: structure remains in residuals"
                        if p < 0.05 else "OK: residuals behave like white noise"),
            "jarque_bera_p": round(float(jb_p), 4),
            "aic": round(float(res.aic), 1), "bic": round(float(res.bic), 1)}
