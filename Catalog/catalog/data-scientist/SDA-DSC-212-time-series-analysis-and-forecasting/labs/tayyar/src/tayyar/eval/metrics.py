"""Metrics that survive real data.

MAPE explodes near zero and punishes under-forecasts less than over-forecasts.
MASE does neither: it divides by the in-sample seasonal-naive MAE, so
  MASE < 1  ->  you beat the free baseline
  MASE > 1  ->  you should have shipped the baseline
"""
from __future__ import annotations
import numpy as np


def mae(y, f):  return float(np.mean(np.abs(np.asarray(y,float) - np.asarray(f,float))))
def rmse(y, f): return float(np.sqrt(np.mean((np.asarray(y,float) - np.asarray(f,float))**2)))


def mape(y, f) -> float:
    y, f = np.asarray(y, float), np.asarray(f, float)
    ok = y != 0
    return float(np.mean(np.abs((y[ok] - f[ok]) / y[ok])) * 100)


def smape(y, f) -> float:
    y, f = np.asarray(y, float), np.asarray(f, float)
    d = (np.abs(y) + np.abs(f)) / 2
    ok = d != 0
    return float(np.mean(np.abs(y[ok] - f[ok]) / d[ok]) * 100)


def mase(y, f, y_train, m: int = 24) -> float:
    """Scale = MAE of the seasonal-naive forecast computed IN-SAMPLE (on y_train)."""
    y_train = np.asarray(y_train, float)
    scale = np.mean(np.abs(y_train[m:] - y_train[:-m]))
    if scale == 0:
        return float("nan")
    return mae(y, f) / scale


def wape(y, f) -> float:
    y, f = np.asarray(y, float), np.asarray(f, float)
    return float(np.sum(np.abs(y - f)) / np.sum(np.abs(y)) * 100)


def bias(y, f) -> float:
    return float(np.mean(np.asarray(f, float) - np.asarray(y, float)))


def all_metrics(y, f, y_train=None, m: int = 24) -> dict:
    out = {"MAE": round(mae(y, f), 1), "RMSE": round(rmse(y, f), 1),
           "MAPE_%": round(mape(y, f), 3), "sMAPE_%": round(smape(y, f), 3),
           "WAPE_%": round(wape(y, f), 3), "bias": round(bias(y, f), 1)}
    if y_train is not None:
        out["MASE"] = round(mase(y, f, y_train, m), 4)
    return out
