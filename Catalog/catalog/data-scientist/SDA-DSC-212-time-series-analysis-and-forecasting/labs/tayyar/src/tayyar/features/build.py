"""Leakage-safe temporal feature engineering.

Every feature in this module is computable at forecast origin `t` using only
information available at or before `t`. That is the whole discipline.

The three traps this file exists to prevent:
  1. rolling windows that include the target hour  -> always .shift(1) first
  2. centred windows                               -> center=False, always
  3. scalers/encoders fit on the full series       -> fit on train only
"""
from __future__ import annotations
import numpy as np, pandas as pd

DEFAULT_LAGS = (1, 2, 3, 24, 25, 48, 168, 169, 336)
DEFAULT_WINDOWS = (24, 168)


def add_calendar_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    idx = out.index
    out["hour"] = idx.hour
    out["day_of_week"] = idx.dayofweek
    out["month"] = idx.month
    out["day_of_year"] = idx.dayofyear
    out["year"] = idx.year
    # KSA weekend is Friday(4) + Saturday(5) in pandas dayofweek (Mon=0)
    if "is_weekend" not in out:
        out["is_weekend"] = idx.dayofweek.isin([4, 5])
    for c in ("is_weekend", "is_ramadan", "is_eid", "is_national_day"):
        if c in out:
            out[c] = out[c].astype(int)
    return out


def add_fourier_terms(df: pd.DataFrame, period: int, k: int, prefix: str) -> pd.DataFrame:
    """Smooth seasonality with 2k columns instead of `period` dummies."""
    out = df.copy()
    t = np.arange(len(out))
    for i in range(1, k + 1):
        out[f"{prefix}_sin{i}"] = np.sin(2 * np.pi * i * t / period)
        out[f"{prefix}_cos{i}"] = np.cos(2 * np.pi * i * t / period)
    return out


def add_lag_features(df: pd.DataFrame, col: str = "demand_mw",
                     lags=DEFAULT_LAGS) -> pd.DataFrame:
    out = df.copy()
    for L in lags:
        out[f"{col}_lag{L}"] = out[col].shift(L)
    return out


def add_rolling_features(df: pd.DataFrame, col: str = "demand_mw",
                         windows=DEFAULT_WINDOWS) -> pd.DataFrame:
    """NOTE the .shift(1): the window must end at t-1, never include t."""
    out = df.copy()
    base = out[col].shift(1)                       # <-- the leakage guard
    for w in windows:
        r = base.rolling(w, min_periods=max(2, w // 4), center=False)
        out[f"{col}_rmean{w}"] = r.mean()
        out[f"{col}_rstd{w}"] = r.std()
        out[f"{col}_rmin{w}"] = r.min()
        out[f"{col}_rmax{w}"] = r.max()
    return out


def build_features(df: pd.DataFrame, target: str = "demand_mw",
                   lags=DEFAULT_LAGS, windows=DEFAULT_WINDOWS,
                   use_temp: bool = True) -> pd.DataFrame:
    """Full leakage-safe design matrix. `temp_c` is treated as KNOWN at forecast
    time (a day-ahead weather forecast is available) — that assumption is
    explicit here and must be tested with a *forecast* temperature, not the
    realised one, in production."""
    out = add_calendar_features(df)
    out = add_fourier_terms(out, 24, 3, "d")
    out = add_fourier_terms(out, 24 * 7, 2, "w")
    out = add_fourier_terms(out, 24 * 365, 2, "y")
    out = add_lag_features(out, target, lags)
    out = add_rolling_features(out, target, windows)
    if use_temp and "temp_c" in out:
        out["cdd"] = np.clip(out["temp_c"] - 21.0, 0, None)
        out["hdd"] = np.clip(14.0 - out["temp_c"], 0, None)
        out["temp_lag24"] = out["temp_c"].shift(24)
    return out


def assert_no_leakage(df: pd.DataFrame, target: str = "demand_mw",
                      corr_threshold: float = 0.9999) -> None:
    """Fails loudly if any feature is a disguised copy of the target at time t.

    Two checks:
      A. no feature correlates ~1.0 with the target (a shifted-by-zero copy)
      B. shuffling the *future* rows must not change any feature value
    """
    y = df[target]
    feats = [c for c in df.columns if c != target and
             pd.api.types.is_numeric_dtype(df[c])]
    bad = []
    sub = df[[target] + feats].dropna()
    for c in feats:
        if sub[c].std() == 0:
            continue
        r = abs(np.corrcoef(sub[target], sub[c])[0, 1])
        if r > corr_threshold:
            bad.append((c, round(float(r), 6)))
    if bad:
        raise AssertionError(f"LEAKAGE: features near-identical to target: {bad}")

    probe = df.copy()
    cut = len(probe) // 2
    fut = probe.iloc[cut:].copy()
    fut[target] = fut[target].sample(frac=1.0, random_state=0).to_numpy()
    rebuilt = build_features(pd.concat([probe.iloc[:cut], fut])[[target] +
                             [c for c in ("temp_c",) if c in probe]])
    past_cols = [c for c in rebuilt.columns if c in df.columns and
                 pd.api.types.is_numeric_dtype(df[c])]
    a = df.iloc[:cut][past_cols].tail(200)
    b = rebuilt.iloc[:cut][past_cols].tail(200)
    diff = [c for c in past_cols if not np.allclose(a[c].to_numpy(dtype=float),
                                                    b[c].to_numpy(dtype=float),
                                                    equal_nan=True)]
    if diff:
        raise AssertionError(f"LEAKAGE: past features changed when the future "
                             f"was shuffled: {diff}")
    print(f"assert_no_leakage: PASS ({len(feats)} features checked)")
