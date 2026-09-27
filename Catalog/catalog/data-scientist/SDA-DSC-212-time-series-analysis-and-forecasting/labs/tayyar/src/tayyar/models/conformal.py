"""Split-conformal and CQR: coverage you can actually promise.

Guarantee: under exchangeability of the calibration and test residuals, the
interval covers the truth with probability >= 1 - alpha, MARGINALLY.
Marginal is not conditional: 90% on average can hide 78% on the hot afternoons
that are the only hours anybody cares about. Always report both.
"""
from __future__ import annotations
import numpy as np, pandas as pd


def conformal_quantile(scores: np.ndarray, alpha: float = 0.10) -> float:
    """The finite-sample-corrected (1-alpha) quantile of the calibration scores."""
    n = len(scores)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    k = min(max(k, 1), n)
    return float(np.sort(scores)[k - 1])


class SplitConformal:
    """Symmetric interval around any point forecaster."""
    def __init__(self, alpha: float = 0.10):
        self.alpha, self.qhat_ = alpha, None

    def calibrate(self, y_cal, yhat_cal):
        self.qhat_ = conformal_quantile(np.abs(np.asarray(y_cal, float) -
                                               np.asarray(yhat_cal, float)),
                                        self.alpha)
        return self

    def interval(self, yhat):
        yhat = np.asarray(yhat, float)
        return yhat - self.qhat_, yhat + self.qhat_


class CQR:
    """Conformalised Quantile Regression: keeps the *shape* of the quantile model
    (wide where the model is uncertain) and rescales it to hit nominal coverage."""
    def __init__(self, alpha: float = 0.10):
        self.alpha, self.qhat_ = alpha, None

    def calibrate(self, y_cal, lo_cal, hi_cal):
        y, lo, hi = map(lambda a: np.asarray(a, float), (y_cal, lo_cal, hi_cal))
        self.qhat_ = conformal_quantile(np.maximum(lo - y, y - hi), self.alpha)
        return self

    def interval(self, lo, hi):
        lo, hi = np.asarray(lo, float), np.asarray(hi, float)
        return lo - self.qhat_, hi + self.qhat_


def coverage_report(y, lo, hi, by: pd.Series | None = None) -> pd.DataFrame:
    """Marginal AND conditional coverage in one table. Ship both or ship neither."""
    y, lo, hi = map(lambda a: np.asarray(a, float), (y, lo, hi))
    inside = (y >= lo) & (y <= hi)
    rows = [{"group": "ALL", "n": len(y), "coverage": round(inside.mean(), 4),
             "mean_width": round(float(np.mean(hi - lo)), 1)}]
    if by is not None:
        for g, m in pd.Series(np.asarray(by)).groupby(np.asarray(by)):
            sel = (np.asarray(by) == g)
            rows.append({"group": g, "n": int(sel.sum()),
                         "coverage": round(inside[sel].mean(), 4),
                         "mean_width": round(float(np.mean((hi - lo)[sel])), 1)})
    return pd.DataFrame(rows)
