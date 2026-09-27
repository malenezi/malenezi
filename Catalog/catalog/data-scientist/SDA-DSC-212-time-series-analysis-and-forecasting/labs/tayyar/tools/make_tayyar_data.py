"""
Tayyar (تيّار) synthetic dataset generator — SDA-DSC-212
=========================================================
Builds a reproducible, semi-synthetic hourly electricity-demand dataset for the
Saudi "Central Operating Area" (Riyadh region), 2021-01-01 .. 2023-12-31,
in the Asia/Riyadh timezone.

Design intent (documented for auditability — see DATA_CARD.md):
  * Structure is *planted*, so ground truth is known for teaching and grading.
  * Dynamics are modelled on publicly documented behaviour of hot-arid grid
    load (UCI ElectricityLoadDiagrams20112014, CC BY 4.0, is the qualitative
    reference for the shape of the daily/weekly cycle and the noise scale).
  * Saudi specifics are added explicitly: Fri-Sat weekend, Ramadan / Eid /
    National Day calendar effects, 47 C summer temperature envelope.
  * Deliberate defects are injected so Lab 1 has something to find:
    duplicate timestamps, out-of-order rows, silent gaps, sensor zeros.

Outputs (data/):
  ksa_grid_demand.csv        raw, messy   (timestamp, demand_mw, temp_c)
  ksa_grid_demand_clean.csv  reference solution (instructor only)
  ksa_grid_demand_4area.csv  four operating areas, long format
  ksa_calendar.csv           daily KSA calendar flags
  temp_forecast_14d.csv      day-ahead temperature forecast w/ realistic error
  temp_forecast_28d.csv      longer horizon variant
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

SEED = 212
RNG = np.random.default_rng(SEED)
START, END = "2021-01-01", "2023-12-31 23:00"
TZ = "Asia/Riyadh"
OUT = Path(__file__).resolve().parents[1] / "data"
OUT.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------- calendar --
# Hijri holiday windows (Gregorian anchors, 2021-2023). Approximate to +/-1 day,
# which is realistic: KSA announcements are moon-sighting dependent.
RAMADAN = [("2021-04-13", "2021-05-12"), ("2022-04-02", "2022-05-01"),
           ("2023-03-23", "2023-04-20")]
EID_FITR = [("2021-05-13", "2021-05-16"), ("2022-05-02", "2022-05-05"),
            ("2023-04-21", "2023-04-24")]
EID_ADHA = [("2021-07-19", "2021-07-23"), ("2022-07-09", "2022-07-13"),
            ("2023-06-27", "2023-07-01")]
NATIONAL_DAY = ["2021-09-23", "2022-09-23", "2023-09-23"]
FOUNDING_DAY = ["2022-02-22", "2023-02-22"]


def _span_flag(idx: pd.DatetimeIndex, spans) -> np.ndarray:
    f = np.zeros(len(idx), dtype=bool)
    d = idx.tz_localize(None).normalize() if idx.tz is not None else idx.normalize()
    for a, b in spans:
        f |= (d >= pd.Timestamp(a)) & (d <= pd.Timestamp(b))
    return f


def build_calendar(idx: pd.DatetimeIndex) -> pd.DataFrame:
    local = idx.tz_convert(TZ) if idx.tz is not None else idx
    cal = pd.DataFrame(index=idx)
    cal["hour"] = local.hour
    cal["day_of_week"] = local.dayofweek          # Mon=0 ... Fri=4, Sat=5
    cal["is_weekend"] = local.dayofweek.isin([4, 5])   # KSA: Friday + Saturday
    cal["is_ramadan"] = _span_flag(local, RAMADAN)
    cal["is_eid"] = _span_flag(local, EID_FITR) | _span_flag(local, EID_ADHA)
    cal["is_national_day"] = _span_flag(local, [(d, d) for d in NATIONAL_DAY])
    cal["is_founding_day"] = _span_flag(local, [(d, d) for d in FOUNDING_DAY])
    cal["doy"] = local.dayofyear
    return cal


# -------------------------------------------------------------- temperature --
def build_temperature(idx, amp_scale=1.0, offset=0.0):
    """Riyadh-style envelope: ~14 C January mean, ~38 C July mean, diurnal ~12 C."""
    local = idx.tz_convert(TZ)
    doy = local.dayofyear.to_numpy().astype(float)
    hour = local.hour.to_numpy().astype(float)
    annual = 26.0 + 12.5 * np.sin(2 * np.pi * (doy - 110) / 365.25)
    diurnal = 6.5 * np.sin(2 * np.pi * (hour - 9.5) / 24.0)
    # AR(1) weather noise so consecutive hours are correlated (as real weather is)
    n = len(idx)
    e = RNG.normal(0, 1.15, n)
    w = np.zeros(n)
    for i in range(1, n):
        w[i] = 0.93 * w[i - 1] + e[i]
    temp = annual + amp_scale * diurnal + 0.75 * w + offset
    # planted heatwaves: three multi-day summer excursions
    for anchor, days, bump in [("2021-07-28", 6, 3.4), ("2022-08-04", 7, 4.0),
                               ("2023-07-17", 5, 3.6)]:
        a = pd.Timestamp(anchor, tz=TZ)
        m = (local >= a) & (local < a + pd.Timedelta(days=days))
        temp = np.where(m, temp + bump, temp)
    return np.round(np.clip(temp, 1.0, 49.5), 2)


# --------------------------------------------------------------------- load --
def build_demand(idx, temp, cal, base=27500.0, growth=0.029, area_gain=1.0,
                 noise_sd=0.011, peak_shift=0.0):
    """Multiplicative construction: level x trend x annual x weekly x daily x calendar x weather x noise."""
    local = idx.tz_convert(TZ)
    t = np.arange(len(idx), dtype=float)
    years = t / (365.25 * 24)

    trend = (1 + growth) ** years                                   # ~+2.9% YoY
    doy = local.dayofyear.to_numpy().astype(float)
    annual = 1 + 0.075 * np.sin(2 * np.pi * (doy - 105) / 365.25) \
                + 0.030 * np.sin(4 * np.pi * (doy - 60) / 365.25)   # residual (non-weather) summer effect

    hour = local.hour.to_numpy().astype(float) + peak_shift
    daily = (1 + 0.150 * np.sin(2 * np.pi * (hour - 9.0) / 24.0)
               + 0.058 * np.sin(4 * np.pi * (hour - 5.0) / 24.0)
               + 0.022 * np.sin(6 * np.pi * (hour - 2.0) / 24.0))

    weekly = np.where(cal["is_weekend"].to_numpy(), 0.945, 1.012)

    # Ramadan: lower daytime, sharply higher post-Iftar evening (19:00-01:00)
    ram = cal["is_ramadan"].to_numpy()
    ram_shape = np.ones(len(idx))
    h = local.hour.to_numpy()
    ram_shape = np.where(ram & (h >= 6) & (h < 15), 0.930, ram_shape)
    ram_shape = np.where(ram & ((h >= 19) | (h < 2)), 1.075, ram_shape)
    eid = np.where(cal["is_eid"].to_numpy(), 0.905, 1.0)             # holiday trough
    natday = np.where(cal["is_national_day"].to_numpy(), 0.955, 1.0)

    # Weather response: piecewise cooling load above a ~21 C balance point
    cdd = np.clip(temp - 21.0, 0, None)
    weather = 1 + 0.0165 * cdd + 0.00012 * cdd ** 2
    # mild heating response below 14 C
    hdd = np.clip(14.0 - temp, 0, None)
    weather = weather + 0.0090 * hdd

    # AR(1) demand innovation (autocorrelated remainder -> ACF has real memory)
    n = len(idx)
    e = RNG.normal(0, noise_sd, n)
    a = np.zeros(n)
    for i in range(1, n):
        a[i] = 0.72 * a[i - 1] + e[i]

    load = base * area_gain * trend * annual * daily * weekly * ram_shape \
           * eid * natday * weather * np.exp(a)

    # structural break: 2022-10-01 industrial customer connects (+3.1% step)
    brk = local >= pd.Timestamp("2022-10-01", tz=TZ)
    load = np.where(brk, load * 1.031, load)
    return np.round(load, 1)


def inject_defects(df: pd.DataFrame) -> pd.DataFrame:
    """Make the raw file realistically messy — this is the Lab 1 teaching payload."""
    d = df.copy()
    # 1) silent gaps: 33 short (1-3 h) + one 5 h outage
    drop = []
    for _ in range(33):
        i = RNG.integers(100, len(d) - 100)
        drop += list(range(i, i + int(RNG.integers(1, 4))))
    i = int(RNG.integers(9000, 12000))
    drop += list(range(i, i + 5))
    d = d.drop(index=d.index[sorted(set(drop))[:len(set(drop))]], errors="ignore")
    # 2) sensor zeros (must be caught before a log transform)
    z = RNG.choice(len(d), 7, replace=False)
    d.iloc[z, d.columns.get_loc("demand_mw")] = 0.0
    # 3) duplicated timestamps
    dup = d.sample(19, random_state=SEED)
    d = pd.concat([d, dup])
    # 4) shuffled block: rows are not monotonic
    d = d.sample(frac=1.0, random_state=SEED).sort_index(kind="stable")
    blk = d.iloc[5000:5400].sample(frac=1.0, random_state=SEED + 1)
    d = pd.concat([d.iloc[:5000], blk, d.iloc[5400:]])
    return d


def main():
    idx = pd.date_range(START, END, freq="h", tz=TZ)
    cal = build_calendar(idx)
    temp = build_temperature(idx)
    demand = build_demand(idx, temp, cal)

    clean = pd.DataFrame({"timestamp": idx, "demand_mw": demand, "temp_c": temp})
    clean.to_csv(OUT / "ksa_grid_demand_clean.csv", index=False)

    messy = inject_defects(clean.set_index("timestamp")).reset_index()
    messy.to_csv(OUT / "ksa_grid_demand.csv", index=False)

    # ---- four operating areas (multi-series / global-model extension) --------
    areas = {"COA": dict(area_gain=1.00, growth=0.029, peak_shift=0.0),
             "EOA": dict(area_gain=0.82, growth=0.021, peak_shift=-0.6),
             "WOA": dict(area_gain=0.74, growth=0.034, peak_shift=0.4),
             "SOA": dict(area_gain=0.31, growth=0.038, peak_shift=0.2)}
    frames = []
    for name, kw in areas.items():
        t = build_temperature(idx, amp_scale=1.0,
                              offset={"COA": 0, "EOA": 1.4, "WOA": -2.1, "SOA": -1.0}[name])
        d = build_demand(idx, t, cal, **kw)
        frames.append(pd.DataFrame({"timestamp": idx, "area_id": name,
                                    "demand_mw": d, "temp_c": t}))
    pd.concat(frames).to_csv(OUT / "ksa_grid_demand_4area.csv", index=False)

    # ---- daily calendar table ----------------------------------------------
    didx = pd.date_range(START, "2023-12-31", freq="D", tz=TZ)
    dcal = build_calendar(didx).drop(columns=["hour"])
    dcal.insert(0, "date", didx.tz_localize(None).date)
    dcal.to_csv(OUT / "ksa_calendar.csv", index=False)

    # ---- temperature *forecasts* (exogenous regressors known at run time) ----
    # Forecast error grows with horizon: sd ~ 0.8 C at h+1 to ~3.0 C at h+336.
    for horizon, fname in [(14 * 24, "temp_forecast_14d.csv"),
                           (28 * 24, "temp_forecast_28d.csv")]:
        origins = pd.date_range("2023-01-01", "2023-12-01", freq="7D", tz=TZ)
        rows = []
        tser = pd.Series(temp, index=idx)
        for o in origins:
            fut = pd.date_range(o, periods=horizon, freq="h", tz=TZ)
            fut = fut[fut.isin(tser.index)]
            if len(fut) == 0:
                continue
            lead = np.arange(1, len(fut) + 1)
            sd = 0.8 + 2.2 * (lead / horizon) ** 0.7
            rows.append(pd.DataFrame({
                "origin": o, "timestamp": fut,
                "temp_c_forecast": np.round(tser.loc[fut].to_numpy()
                                            + RNG.normal(0, sd), 2)}))
        pd.concat(rows).to_csv(OUT / fname, index=False)

    print(f"clean rows      : {len(clean):,}")
    print(f"messy rows      : {len(messy):,} (duplicates + gaps + zeros injected)")
    print(f"4-area rows     : {len(idx)*4:,}")
    print(f"peak demand     : {clean.demand_mw.max():,.0f} MW")
    print(f"mean demand     : {clean.demand_mw.mean():,.0f} MW")
    print(f"temp range      : {clean.temp_c.min():.1f} .. {clean.temp_c.max():.1f} C")
    print(f"written to      : {OUT}")


if __name__ == "__main__":
    main()
