"""Pinball (quantile) loss — the proper score for a quantile forecast.

  L_tau(y, q) = tau * (y - q)         if y >= q
                (1 - tau) * (q - y)   otherwise

Minimising it at tau recovers the tau-th percentile. Asymmetric on purpose:
at tau=0.9, under-predicting is penalised 9x more than over-predicting.
"""
from __future__ import annotations
import numpy as np


def pinball_loss(y_true, q_pred, tau: float) -> float:
    y, q = np.asarray(y_true, float), np.asarray(q_pred, float)
    d = y - q
    return float(np.mean(np.maximum(tau * d, (tau - 1) * d)))


def mean_pinball(y_true, quantile_preds: dict) -> float:
    """quantile_preds: {tau: array}. The CRPS-like average over the quantile grid."""
    return float(np.mean([pinball_loss(y_true, p, t)
                          for t, p in quantile_preds.items()]))


def interval_score(y_true, lo, hi, alpha: float = 0.10) -> float:
    """Winkler score: width + penalty for every miss. Lower is better; it is the
    single number that trades coverage against sharpness."""
    y, lo, hi = map(lambda a: np.asarray(a, float), (y_true, lo, hi))
    w = hi - lo
    pen = (2 / alpha) * ((lo - y) * (y < lo) + (y - hi) * (y > hi))
    return float(np.mean(w + pen))


def coverage(y_true, lo, hi) -> float:
    y, lo, hi = map(lambda a: np.asarray(a, float), (y_true, lo, hi))
    return float(np.mean((y >= lo) & (y <= hi)))
