"""ADF + KPSS, reconciled. The two tests have *opposite* null hypotheses."""
from __future__ import annotations
import warnings
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

# ADF  H0: unit root (non-stationary)   -> small p = STATIONARY
# KPSS H0: stationary                   -> small p = NON-STATIONARY
RECONCILE = {
    (True,  True):  ("stationary",
                     "Both agree: no differencing needed."),
    (False, False): ("non-stationary",
                     "Both agree: difference the series."),
    (True,  False): ("difference-stationary",
                     "ADF stationary, KPSS not: a deterministic/level shift remains "
                     "— difference once and re-test."),
    (False, True):  ("trend-stationary",
                     "ADF non-stationary, KPSS stationary: detrend rather than "
                     "difference (or use a trend regressor)."),
}


def stationarity_report(y: pd.Series, alpha: float = 0.05,
                        regression: str = "c") -> dict:
    s = y.dropna().astype(float)
    adf_stat, adf_p, *_ = adfuller(s, autolag="AIC")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kpss_stat, kpss_p, *_ = kpss(s, regression=regression, nlags="auto")
    adf_stationary = adf_p < alpha
    kpss_stationary = kpss_p > alpha
    verdict, action = RECONCILE[(adf_stationary, kpss_stationary)]
    return {"adf_stat": round(adf_stat, 3), "adf_p": round(adf_p, 4),
            "adf_says_stationary": adf_stationary,
            "kpss_stat": round(kpss_stat, 3), "kpss_p": round(kpss_p, 4),
            "kpss_says_stationary": kpss_stationary,
            "verdict": verdict, "action": action}


def format_report(r: dict) -> str:
    return (f"ADF  stat={r['adf_stat']:>8}  p={r['adf_p']:<7} -> "
            f"{'stationary' if r['adf_says_stationary'] else 'unit root'}\n"
            f"KPSS stat={r['kpss_stat']:>8}  p={r['kpss_p']:<7} -> "
            f"{'stationary' if r['kpss_says_stationary'] else 'non-stationary'}\n"
            f"VERDICT: {r['verdict']}\nACTION : {r['action']}")
