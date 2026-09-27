"""Loading and cleaning the Tayyar hourly demand series.

The one rule this module enforces: a time series has a *declared* frequency.
`parse_dates` gives you timestamps; `asfreq` gives you a calendar — and it is
`asfreq` that turns a silent gap into a visible NaN.
"""
from __future__ import annotations
import pandas as pd
from pathlib import Path

TZ = "Asia/Riyadh"
FREQ = "h"


def load_demand(path: str | Path, tz: str = TZ, freq: str = FREQ,
                max_impute_hours: int = 3) -> pd.DataFrame:
    """Raw messy CSV -> clean, tz-aware, gap-materialised hourly frame.

    Steps, in the only order that is safe:
      1. parse timestamps      2. drop duplicate timestamps (keep last)
      3. sort                  4. set index + localise
      5. asfreq  <- materialises missing hours as NaN
      6. treat sensor zeros as missing
      7. interpolate short gaps; leave long gaps NaN and flag them
    """
    df = pd.read_csv(path, parse_dates=["timestamp"])
    n_raw = len(df)
    df = df.drop_duplicates(subset="timestamp", keep="last")
    df = df.sort_values("timestamp").set_index("timestamp")
    if df.index.tz is None:
        df.index = df.index.tz_localize(tz, ambiguous="infer",
                                        nonexistent="shift_forward")
    else:
        df.index = df.index.tz_convert(tz)
    df = df.asfreq(freq)                       # <- the line that reveals gaps

    df.loc[df["demand_mw"] == 0, "demand_mw"] = pd.NA   # sensor dropouts
    df["demand_mw"] = pd.to_numeric(df["demand_mw"])

    missing = df["demand_mw"].isna()
    df.attrs["n_raw_rows"] = n_raw
    df.attrs["n_missing"] = int(missing.sum())
    df.attrs["longest_gap_h"] = int(_longest_run(missing))

    df["is_imputed"] = False
    short = _short_gap_mask(missing, max_impute_hours)
    df.loc[short, "demand_mw"] = df["demand_mw"].interpolate("time")[short]
    df.loc[short, "is_imputed"] = True
    df["temp_c"] = df["temp_c"].interpolate("time").ffill().bfill()

    assert df.index.is_monotonic_increasing and df.index.is_unique
    assert df.index.freq is not None, "frequency must be declared"
    return df


def _longest_run(mask: pd.Series) -> int:
    grp = (~mask).cumsum()[mask]
    return int(grp.value_counts().max()) if len(grp) else 0


def _short_gap_mask(missing: pd.Series, max_h: int) -> pd.Series:
    grp = (~missing).cumsum()
    sizes = missing.groupby(grp).transform("sum")
    return missing & (sizes <= max_h)


def load_calendar(path: str | Path, tz: str = TZ) -> pd.DataFrame:
    cal = pd.read_csv(path, parse_dates=["date"])
    cal["date"] = cal["date"].dt.tz_localize(tz)
    return cal.set_index("date")


def join_calendar(df: pd.DataFrame, cal: pd.DataFrame) -> pd.DataFrame:
    keys = [c for c in ("is_weekend", "is_ramadan", "is_eid",
                        "is_national_day", "is_founding_day") if c in cal]
    daily = cal[keys]
    out = df.copy()
    day = out.index.normalize()
    for k in keys:
        out[k] = daily[k].reindex(day).to_numpy()
    return out
