"""Diebold-Mariano: is model A really better than B, or did it get lucky?

H0: the two forecasts have equal expected loss.
A 0.4% MAE gap over 50 origins with p = 0.31 is not a champion — it is noise,
and the correct decision is to ship the simpler or cheaper model.
"""
from __future__ import annotations
import numpy as np
from scipy import stats


def diebold_mariano(y, f1, f2, h: int = 1, loss: str = "mae") -> dict:
    y, f1, f2 = (np.asarray(a, float) for a in (y, f1, f2))
    e1, e2 = y - f1, y - f2
    if loss == "mae":
        d = np.abs(e1) - np.abs(e2)
    elif loss == "mse":
        d = e1 ** 2 - e2 ** 2
    else:
        raise ValueError("loss must be 'mae' or 'mse'")
    n = len(d)
    dbar = d.mean()
    # Newey-West long-run variance with h-1 autocovariance lags
    gamma0 = np.sum((d - dbar) ** 2) / n
    lrv = gamma0
    for k in range(1, h):
        g = np.sum((d[k:] - dbar) * (d[:-k] - dbar)) / n
        lrv += 2 * (1 - k / h) * g
    dm = dbar / np.sqrt(lrv / n) if lrv > 0 else np.nan
    # Harvey-Leybourne-Newbold small-sample correction
    corr = np.sqrt((n + 1 - 2 * h + h * (h - 1) / n) / n)
    dm_hln = dm * corr
    p = float(2 * (1 - stats.t.cdf(abs(dm_hln), df=n - 1)))
    return {"dm_stat": round(float(dm_hln), 3), "p_value": round(p, 4),
            "mean_loss_diff": round(float(dbar), 4), "n": n,
            "significant_at_5pct": p < 0.05,
            "verdict": ("model 1 significantly better" if p < 0.05 and dbar < 0
                        else "model 2 significantly better" if p < 0.05
                        else "no significant difference — prefer the simpler model")}
