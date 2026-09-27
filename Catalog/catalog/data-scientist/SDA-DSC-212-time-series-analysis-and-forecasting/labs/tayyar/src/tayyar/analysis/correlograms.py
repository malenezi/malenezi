"""ACF / PACF — the model fingerprint."""
from __future__ import annotations
import numpy as np, pandas as pd
from statsmodels.tsa.stattools import acf, pacf

FINGERPRINT = pd.DataFrame([
    ["Tails off (geometric decay)", "Cuts off after lag p", "AR(p)"],
    ["Cuts off after lag q",        "Tails off",            "MA(q)"],
    ["Tails off",                   "Tails off",            "ARMA(p,q) — use AIC/BIC"],
    ["Slow, near-linear decay",     "Large spike at lag 1",  "Non-stationary — difference first"],
    ["Spikes at lags m, 2m, 3m",    "Spike at lag m",        "Seasonal AR — set P, m"],
], columns=["ACF", "PACF", "Read as"])


def correlogram_table(y: pd.Series, nlags: int = 72, alpha: float = 0.05) -> pd.DataFrame:
    s = y.dropna().astype(float)
    a, aci = acf(s, nlags=nlags, alpha=alpha, fft=True)
    p, pci = pacf(s, nlags=nlags, alpha=alpha)
    band = 1.96 / np.sqrt(len(s))
    return pd.DataFrame({"lag": np.arange(nlags + 1), "acf": a, "pacf": p,
                         "acf_significant": np.abs(a) > band,
                         "pacf_significant": np.abs(p) > band})


def suggest_orders(tbl: pd.DataFrame, m: int = 24) -> dict:
    """A first *candidate*, never a verdict — always confirm with residual diagnostics."""
    sig_p = tbl.loc[tbl.pacf_significant & (tbl.lag.between(1, 5)), "lag"]
    sig_a = tbl.loc[tbl.acf_significant & (tbl.lag.between(1, 5)), "lag"]
    P = int(tbl.loc[tbl.pacf_significant & (tbl.lag == m)].shape[0] > 0)
    return {"p": int(sig_p.max()) if len(sig_p) else 0,
            "q": int(sig_a.max()) if len(sig_a) else 0,
            "P": P, "Q": P, "m": m}
