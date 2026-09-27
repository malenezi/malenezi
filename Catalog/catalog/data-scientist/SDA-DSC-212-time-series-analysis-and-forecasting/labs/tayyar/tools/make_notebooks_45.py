"""Generate the Lab 4 and Lab 5 notebooks (start + solution).

Same house style as tools/make_notebooks.py — see notebooks/_SPEC.md.
Lab 4 ships two planted leaks in the START notebook; Lab 5 ships two planted
interval bugs. Both are diagnosed and repaired in the solution.
"""
import json, pathlib

NB = pathlib.Path("notebooks"); NB.mkdir(exist_ok=True)


def _lines(t):
    """Notebook source is a list of lines that must keep their newline terminators."""
    ls = t.rstrip().split(chr(10))
    return [l + chr(10) for l in ls[:-1]] + [ls[-1]]

def md(t): return {"cell_type": "markdown", "metadata": {}, "source": _lines(t)}
def code(t): return {"cell_type": "code", "execution_count": None, "metadata": {},
                     "outputs": [], "source": _lines(t)}
def write(name, cells):
    # nbformat >= 4.5 requires a cell id; a stable per-notebook slug keeps the
    # regenerated JSON diff-clean and nbformat.validate silent.
    cells = [{**c, "id": f"c{i:02d}"} for i, c in enumerate(cells, 1)]
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3",
          "language": "python", "name": "python3"},
          "language_info": {"name": "python", "version": "3.12"}},
          "nbformat": 4, "nbformat_minor": 5}
    (NB / name).write_text(json.dumps(nb, indent=1))

HDR = """# SDA-DSC-212 — Time Series Analysis and Forecasting
## Lab {n} — {title}

**Duration** {dur} minutes · **Work in pairs** · `git checkout lab{n}-{tag}`

> The one rule for this whole course: every feature, every split and every scaler
> must be computable using only data that existed at the forecast origin.
"""

SETUP = """import sys, warnings
sys.path.insert(0, "../src")
warnings.filterwarnings("ignore")

import numpy as np, pandas as pd, matplotlib.pyplot as plt
pd.set_option("display.width", 120)
plt.rcParams.update({"figure.figsize": (11, 4), "figure.dpi": 110,
                     "axes.grid": True, "grid.alpha": 0.25})

DATA = "../data"
"""

LOAD = '''from tayyar.data.load import load_demand, load_calendar, join_calendar

df = join_calendar(load_demand(f"{DATA}/ksa_grid_demand.csv"),
                   load_calendar(f"{DATA}/ksa_calendar.csv"))
y = df["demand_mw"].astype(float)
print(f"{len(df):,} hourly rows   {df.index.min():%Y-%m-%d} -> {df.index.max():%Y-%m-%d}")'''

# ============================================================= LAB 4 ==========
L4_TASKS = """### Tasks

| min | task |
|---|---|
| 5 | Find the **two leaks** in the starter code you inherited. Write them down in `LEAKS.md`. **Do not fix them yet.** |
| 12 | Build the leakage-safe design matrix with `build_features` — ACF-chosen lags, shifted rolling windows, KSA calendar flags, Fourier terms. Verify with `assert_no_leakage`. |
| 12 | Direct multi-step targets for H = 24 with `DirectLGBMForecaster`. Split **by time**. Say out loud why direct, not recursive. |
| 8 | Forecast the test window day by day. MAE and MAPE against the seasonal-naive baseline; overlay one day. |
| 8 | Feature importance by gain and by family. Interpret the top five. Importance is associational, never causal. |
| 5 | The four-design leakage demonstration. Finish `LEAKS.md`. Commit. |
"""

STARTER4 = '''# ---------------------------------------------------------------------------
# The starter code you inherited
#
# A colleague left this behind on their last day, with the note:
#   "day-ahead demand model, MAPE well under 2%, ready for the control room."
#
# It runs. It reports that number. Two lines in this cell make it a lie.
# Find both before you write any new code.
# ---------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
import lightgbm as lgb

# Target: demand at hour t. Day-ahead means every feature must be known 24 hours
# before t — so the lags all start at 24. That much the colleague got right.
work = df[["demand_mw", "temp_c"]].copy()
work["hour"] = work.index.hour
work["dow"]  = work.index.dayofweek
for L in (24, 25, 48, 168):
    work[f"lag{L}"] = work["demand_mw"].shift(L)
work["roll24"]     = work["demand_mw"].rolling(24, center=True, min_periods=1).mean()
work["roll24_max"] = work["demand_mw"].rolling(24, center=True, min_periods=1).max()
work = work.dropna()

FEATS = ["temp_c", "hour", "dow", "lag24", "lag25", "lag48", "lag168",
         "roll24", "roll24_max"]
Xa, Xb, ya, yb = train_test_split(work[FEATS], work["demand_mw"],
                                  test_size=0.2, random_state=0, shuffle=True)

starter = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.06, num_leaves=63,
                            verbose=-1, random_state=1).fit(Xa, ya)
starter_mape = float(np.mean(np.abs((yb - starter.predict(Xb)) / yb)) * 100)
print(f"inherited starter — day-ahead MAPE: {starter_mape:.2f}%")'''

QUIZ4_Q = """### Mini-quiz

Answer these in your pair before you look at the next cell.

1. Why is `train_test_split(..., shuffle=True)` fatal on a time series?
2. What does the `.shift(1)` before `.rolling(...)` prevent?
3. Recursive or direct — which one compounds its own errors?
4. Why can a boosted tree never forecast a record high?
5. What tells you which lags to include?
"""

QUIZ4_A = """### Mini-quiz — answers

1. **Why is `train_test_split(shuffle=True)` fatal?** Because test points can precede
   training points. The model is scored on hours it effectively saw the neighbourhood of.
   It leaks the future into the past, and no amount of feature hygiene repairs it.
2. **What does `.shift(1)` before rolling prevent?** The window including the target hour
   itself — self-leak. `y.rolling(24).mean()` at time `t` contains `y[t]`; `y.shift(1).rolling(24).mean()`
   ends at `t-1`, which is all you have at the forecast origin.
3. **Which compounds errors?** Recursive. Each step is fed its own previous prediction as a lag,
   so an error at step 1 is an input error at step 2.
4. **Why can a boosted tree never forecast a record high?** Trees partition the training range and
   predict a constant in each leaf. They interpolate; they cannot extrapolate beyond the range they
   were trained on. A new all-time peak is outside every leaf value.
5. **What tells you which lags to include?** The ACF — the significant lags. Here: 1, 2, 3
   (short memory), 24, 25 (yesterday), 48, 168, 169, 336 (the weekly rhythm).
"""

COMMIT4 = """### Task 6 — `LEAKS.md` and commit

`LEAKS.md` has two sections by now:

1. **The two leaks in the inherited starter**, each with the line that causes it and the
   mechanism in one sentence.
2. **The four-design table** above, with the sentence a reviewer needs:
   *the number that would have been reported to the control room was 2.3x better than the
   truth, and nothing in the code looked wrong.*

```
git add -A && git commit -m "feat(features): leakage-safe design matrix + direct LightGBM day-ahead forecaster"
```"""


def lab4(sol: bool):
    tag = "solution" if sol else "start"
    c = [md(HDR.format(n=4, title="LightGBM Feature-Based Forecaster", dur=50, tag=tag)),
         md(L4_TASKS), code(SETUP), code(LOAD)]

    # ---------------------------------------------------------------- task 1 --
    c.append(md("""### Task 1 — the starter code you inherited

Run the next cell. It works, and the number it prints would get a model promoted.

Your job for the next five minutes is **not** to fix it. It is to name, precisely, the
two lines that make that number meaningless — and write them into `LEAKS.md`."""))
    c.append(code(STARTER4))
    if sol:
        c.append(md("""**Leak 1 — the split.** `train_test_split(..., shuffle=True)` draws the test set
uniformly at random from three years of hourly data. Roughly 80% of the test rows sit
*earlier* in time than the last training row, and every test hour has its immediate
neighbours in the training set. The model is being asked to interpolate inside a period
it has already seen, which is not the question the control room is asking.

**Leak 2 — the feature.** `rolling(24, center=True)` puts the window *around* `t`, not
behind it: with an even window pandas centres it on hours `t-12 … t+11`. The column named
"the average of the past 24 hours" contains the **target hour itself** and eleven hours of
its future. `roll24_max` is worse — it hands over the peak. The lags are all 24 or more, so
the day-ahead framing is right; one mis-specified window destroys it anyway.

The next cell proves both rather than asserting them."""))
        c.append(code('''# Proof 1 — the "test set" is not in the future
print("train window :", f"{Xa.index.min():%Y-%m-%d} -> {Xa.index.max():%Y-%m-%d}")
print("test  window :", f"{Xb.index.min():%Y-%m-%d} -> {Xb.index.max():%Y-%m-%d}")
n_before = int((Xb.index < Xa.index.max()).sum())
print(f"test rows earlier than the last training row   : {n_before:,} of {len(Xb):,} "
      f"({n_before/len(Xb):.0%})")
train_stamps = set(Xa.index)
both = sum((t - pd.Timedelta(1, "h")) in train_stamps and
           (t + pd.Timedelta(1, "h")) in train_stamps for t in Xb.index)
print(f"test rows with BOTH neighbouring hours in train: {both:,} of {len(Xb):,} "
      f"({both/len(Xb):.0%})")

# Proof 2 — the centred window looks forward, past the target hour
t = work.index[12000]
win = work.loc[t - pd.Timedelta(12, "h"): t + pd.Timedelta(11, "h"), "demand_mw"]
print()
print(f"origin t                                   : {t:%Y-%m-%d %H:%M}")
print(f'work["roll24"] at t                        : {work.loc[t, "roll24"]:,.1f}')
print(f"mean of demand over t-12h .. t+11h          : {win.mean():,.1f}")
print(f'work["roll24_max"] at t                    : {work.loc[t, "roll24_max"]:,.1f}')
print(f"max  of demand over t-12h .. t+11h          : {win.max():,.1f}")
print(f'the target itself, demand at t             : {work.loc[t, "demand_mw"]:,.1f}')
print()
print("A feature the model could only compute 11 hours after the hour it predicts.")'''))
        c.append(md("""**`LEAKS.md`, section 1**

```
## Leaks in the inherited starter (labs/lab4)

1. Shuffled split — `train_test_split(..., shuffle=True)` on an hourly series.
   About 80% of the test rows precede the last training row, and every test hour
   is bracketed by training hours. The reported error measures interpolation
   inside seen history, not forecasting.
   Fix: split by time. Train through 2023-09-30, test after it.

2. Centred rolling window — `rolling(24, center=True)` on demand_mw.
   At hour t the window spans t-12 .. t+11, so "the past 24-hour average"
   contains the target hour ITSELF and eleven hours of its future. roll24_max
   leaks the peak outright.
   Fix: .shift(1) BEFORE .rolling(..., center=False), so the window ends at t-1.
```"""))
    else:
        c.append(code('''# TODO (5 min) — do not change the cell above yet.
#
# Two lines in the starter make the printed MAPE meaningless. One is about *how the
# data was split*; the other is about *what one feature can see*.
#
# 1. Print the first and last timestamp of Xa (train) and Xb (test).
#    How many test rows are EARLIER than the last training row?
#
# 2. Pick any timestamp t in `work`. Compare work.loc[t, "roll24"] against
#    the mean of demand_mw over the window you think it covers. Slide the window
#    until the two agree exactly. Which hours does it actually contain — and is
#    the hour you are trying to predict one of them?
#
# Write both up in LEAKS.md: the offending line, the mechanism, one sentence each.
#
# HINT: a feature is legal only if you could compute it at the forecast origin with a
#       clock on the wall. "Centred" is a word that should stop you every time.'''))

    # ---------------------------------------------------------------- task 2 --
    c.append(md("""### Task 2 — the leakage-safe design matrix

Four families, all computable at the forecast origin:

- **lags** — the significant ACF lags from Lab 2: 1, 2, 3 (short memory), 24, 25
  (yesterday's same hour and the hour after), 48, 168, 169, 336 (the weekly rhythm).
- **rolling** — `.shift(1)` **before** `.rolling(..., center=False)`, windows of 24 and 168 hours.
- **calendar** — hour, day of week, month, day of year, and the KSA flags. The weekend here is
  **Friday (4) and Saturday (5)** in pandas `dayofweek`, where Monday = 0. A model built with the
  Western Sat/Sun assumption learns the wrong two days.
- **Fourier** — smooth daily (period 24), weekly (168) and annual (8760) seasonality in a
  handful of sine/cosine columns instead of hundreds of dummies."""))
    if sol:
        c.append(code('''from tayyar.features.build import (build_features, assert_no_leakage,
                                    DEFAULT_LAGS, DEFAULT_WINDOWS)

print("lags    :", DEFAULT_LAGS)
print("windows :", DEFAULT_WINDOWS)

feat = build_features(df[["demand_mw", "temp_c", "is_weekend",
                          "is_ramadan", "is_eid", "is_national_day"]])
Xcols = [c for c in feat.columns if c != "demand_mw"]
X, yy = feat[Xcols].astype(float), feat["demand_mw"]

print(f"\\ndesign matrix : {len(feat):,} rows x {len(Xcols)} features")
print("families      :",
      {"lag":     sum("_lag" in c for c in Xcols),
       "rolling": sum("_r" in c and c.startswith("demand") for c in Xcols),
       "fourier": sum(c[:2] in ("d_", "w_", "y_") for c in Xcols),
       "weather": sum(c in ("temp_c", "cdd", "hdd", "temp_lag24") for c in Xcols)})'''))
        c.append(code('''# The two things that make it safe, checked rather than assumed.

# 1. the rolling window ends at t-1
manual = yy.shift(1).rolling(24, min_periods=6, center=False).mean()
print("rmean24 == shift(1).rolling(24).mean() :",
      bool(np.allclose(manual.dropna(), feat["demand_mw_rmean24"].dropna())))

# 2. the KSA weekend is Friday and Saturday
wk = feat.groupby("day_of_week")["is_weekend"].mean()
print("is_weekend by dayofweek (Mon=0)        :", wk.round(2).to_dict())

# 3. no feature is a disguised copy of the target, and no past feature moves
#    when the future is shuffled
assert_no_leakage(feat[["demand_mw"] + Xcols])'''))
        c.append(md("""`assert_no_leakage` does two things. The cheap check is a correlation screen — no feature
may sit at |r| ≈ 1 with the target. The check that actually matters is the second one: it
shuffles the second half of the target, rebuilds the features, and demands that every
feature in the **first** half is unchanged. A feature that moves when the future moves is
a feature that reads the future. The centred window from Task 1 fails this instantly.

The long lags cost rows: `demand_mw_lag336` is undefined for the first 336 hours, so those
rows drop out of training. That is expected and correct — it is the price of a two-week
memory, not a bug."""))
    else:
        c.append(code('''from tayyar.features.build import (build_features, assert_no_leakage,
                                    DEFAULT_LAGS, DEFAULT_WINDOWS)

# TODO (12 min)
#   1. feat = build_features(...) on the columns
#      ["demand_mw","temp_c","is_weekend","is_ramadan","is_eid","is_national_day"]
#   2. Xcols = every column except the target; X = feat[Xcols].astype(float)
#   3. Report the shape: how many rows, how many features?
#   4. Prove the rolling guard yourself: compare feat["demand_mw_rmean24"] against
#      yy.shift(1).rolling(24, min_periods=6, center=False).mean()
#   5. Prove the weekend flag: group is_weekend by day_of_week and check it fires
#      on 4 (Friday) and 5 (Saturday), NOT on 5 and 6.
#   6. assert_no_leakage(feat[["demand_mw"] + Xcols])
#
# It must print exactly:  assert_no_leakage: PASS (44 features checked)
#
# HINT: the long lags create leading NaNs — 336 hours of them. Do not "fix" that by
#       back-filling, which invents history. Drop the rows.'''))

    # ---------------------------------------------------------------- task 3 --
    c.append(md("""### Task 3 — direct multi-step, split by time

**Recursive** is one model that predicts one step ahead and is then fed its own prediction
back in as a lag, 24 times. It is compact and it guarantees a coherent path — but the errors
compound, and after a few steps the "lags" it is consuming are predictions, whose
distribution is not the distribution of the real lags it was trained on.

**Direct** is one model per horizon `h`, each trained on the target shifted by `-h`. Nothing
compounds, because nothing is fed back. The costs are `H` models to fit and store, and no
guarantee that the 24 horizons form a coherent day — hour 13 is not constrained to sit
sensibly next to hour 14.

At a 24-hour day-ahead horizon the compounding is exactly where recursive chains fall apart,
so **direct is the robust default here**. `DirectLGBMForecaster` is direct."""))
    if sol:
        c.append(code('''from tayyar.models.lgbm_forecaster import DirectLGBMForecaster

CUT_TRAIN = "2023-09-30 23:00"          # everything after this hour is unseen

Xtr = X[:CUT_TRAIN].dropna()
ytr = yy[Xtr.index]
Xte = X[CUT_TRAIN:]

print(f"train : {Xtr.index.min():%Y-%m-%d} -> {Xtr.index.max():%Y-%m-%d}   ({len(Xtr):,} rows)")
print(f"test  : {Xte.index.min():%Y-%m-%d} -> {Xte.index.max():%Y-%m-%d}   ({len(Xte):,} rows)")
print(f"no training hour is later than the test window :",
      bool(Xtr.index.max() <= Xte.index.min()))
print(f"overlap : {len(Xtr.index.intersection(Xte.index))} hour — the cut hour itself. "
      f"pandas label slicing is inclusive at BOTH ends; state that, never assume it.")

lgbm = DirectLGBMForecaster(horizon=24).fit(Xtr, ytr)
print(f"\\nfitted {len(lgbm.models_)} models — one per horizon h = 1..24")
print("horizon h is trained on y.shift(-h): the target is h hours AHEAD of the features.")'''))
        c.append(md("""23,707 training rows out of 26,280 hours: the 336-hour lag and the 2023-10-01 cut
account for the difference. The fit is 24 separate LightGBM models and takes a minute or two.

The one-hour overlap is worth pausing on. `X[:"2023-09-30 23:00"]` and `X["2023-09-30 23:00":]`
both contain the cut hour, because pandas label slicing is closed at both ends. It is harmless
here — the first forecast origin in Task 4 is 1 November — but an off-by-one at a split
boundary is precisely the class of defect this course is about, and the only defence is to
print it rather than assume it."""))
    else:
        c.append(code('''from tayyar.models.lgbm_forecaster import DirectLGBMForecaster

# TODO (12 min)
#   1. CUT_TRAIN = "2023-09-30 23:00". Xtr = X[:CUT_TRAIN].dropna(); ytr = yy[Xtr.index]
#      Xte = X[CUT_TRAIN:]
#   2. Print both windows and check that no training hour is later than the test window.
#      Then print len(Xtr.index.intersection(Xte.index)) and explain the answer —
#      pandas label slicing is inclusive at BOTH ends.
#      Splitting by time is the fix for leak 1.
#   3. lgbm = DirectLGBMForecaster(horizon=24).fit(Xtr, ytr)
#   4. Confirm 24 models were fitted, and read fit() in the source: what is the
#      target for model h?
#
# Then write two sentences in LEAKS.md: recursive vs direct, and why direct at h=24.
#
# HINT: the fit takes a minute or two — 24 models. That cost IS the direct strategy;
#       recursive would be one model and a loop, and would compound its own error.'''))

    # ---------------------------------------------------------------- task 4 --
    c.append(md("""### Task 4 — forecast the test window, one day at a time

One forecast origin per day at 23:00, 60 days of November and December 2023. At each origin
the model sees one row of features and emits 24 hours. The baseline is seasonal-naive:
tomorrow is a copy of the last 24 hours. `MASE < 1` means you beat that free baseline."""))
    if sol:
        c.append(code('''from tayyar.eval.metrics import all_metrics

test_idx = X[CUT_TRAIN:].index
starts = list(range(len(test_idx) - 25, 24 * 30, -24))[:60][::-1]

rows_model, rows_base, days = [], [], []
for s in starts:
    origin = test_idx[s]
    pos = X.index.get_loc(origin)
    Xo = X.iloc[[pos]]
    actual = yy.iloc[pos + 1: pos + 25]
    if len(actual) < 24 or Xo.isna().any().any():
        continue
    fc = np.array([lgbm.models_[h].predict(Xo)[0] for h in range(1, 25)])
    last24 = yy.iloc[pos - 23: pos + 1].to_numpy()
    bl = np.array([last24[h % 24] for h in range(24)])
    hist = yy.iloc[max(0, pos - 24 * 365): pos]          # in-sample scale for MASE
    rows_model.append(all_metrics(actual, fc, hist, 24))
    rows_base.append(all_metrics(actual, bl, hist, 24))
    days.append({"origin": origin, "actual": actual, "fc": fc, "bl": bl})

res = pd.DataFrame({"LightGBM (direct)": pd.DataFrame(rows_model).mean(),
                    "Seasonal-naive":    pd.DataFrame(rows_base).mean()}).T
print(f"{len(days)} daily origins, "
      f"{days[0]['origin']:%Y-%m-%d} -> {days[-1]['origin']:%Y-%m-%d}\\n")
print(res[["MAE", "RMSE", "MAPE_%", "WAPE_%", "MASE", "bias"]].round(3))'''))
        c.append(code('''k = 20
d = days[k]
tt = pd.date_range(d["origin"] + pd.Timedelta(1, "h"), periods=24, freq="h")

fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(tt, d["actual"].to_numpy(), color="#1F3864", lw=2.0, label="actual")
ax.plot(tt, d["fc"], color="#C00000", lw=1.8, label="LightGBM (direct)")
ax.plot(tt, d["bl"], color="#7F7F7F", lw=1.2, ls="--", label="seasonal-naive")
ax.set_title(f"Day-ahead forecast from origin {d['origin']:%Y-%m-%d %H:%M}")
ax.set_ylabel("MW"); ax.legend(frameon=False, ncols=3, fontsize=8)
plt.tight_layout()'''))
        c.append(md("""**Expected**

```
                     MAE      RMSE   MAPE_%  WAPE_%   MASE    bias
LightGBM (direct)  719.075   904.303  2.328   2.385   0.445  -14.060
Seasonal-naive    1244.025  1464.803  4.117   4.189   0.770   74.795
```

A MASE of 0.445 means the model makes about 45% of the error of the free baseline. Note the
baseline's own MASE is 0.77, not 1.0 — the MASE denominator is the seasonal-naive error
computed *in-sample* over the previous year, and December is a calmer month than the summer
that dominates that year. Baselines are not constants; always report the one you actually ran.

Also note the bias: -14 MW on a ~30,000 MW system, so the model is essentially unbiased
across the window. The seasonal-naive baseline is not — it lags a rising series."""))
    else:
        c.append(code('''from tayyar.eval.metrics import all_metrics

# TODO (8 min) — one forecast origin per day at 23:00 across the test window.
#
#   test_idx = X[CUT_TRAIN:].index
#   starts   = list(range(len(test_idx) - 25, 24 * 30, -24))[:60][::-1]
#
#   for each origin:
#     pos    = X.index.get_loc(origin)
#     Xo     = X.iloc[[pos]]                     # one row of features
#     actual = yy.iloc[pos+1 : pos+25]           # the 24 hours that follow
#     fc     = [lgbm.models_[h].predict(Xo)[0] for h in 1..24]
#     bl     = seasonal-naive: a copy of the previous 24 hours
#     hist   = yy.iloc[max(0, pos-24*365) : pos]  # the in-sample MASE scale
#     all_metrics(actual, fc, hist, 24)
#
#   Average the per-origin metrics for both models and print MAE, MAPE_%, MASE, bias.
#   Then overlay actual / model / baseline for one day.
#
# HINT: skip any origin where Xo has a NaN — that is a real forecast failure, not a
#       row to quietly fill. And never let `actual` touch the feature row.'''))

    # ---------------------------------------------------------------- task 5 --
    c.append(md("""### Task 5 — what the model leaned on"""))
    if sol:
        c.append(code('''from tayyar.models.explain import importance_by_family

imp = lgbm.feature_importance(25)          # mean GAIN across the 24 horizon models
print(imp.head(10).to_string(index=False))
print()
print(importance_by_family(imp).to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 4.6))
top = imp.head(14).iloc[::-1]
ax.barh(top.feature, top.gain, color="#1F3864")
ax.set_title("LightGBM feature importance (mean gain over 24 horizon models)")
ax.set_xlabel("mean gain")
plt.tight_layout()'''))
        c.append(md("""**Read the top five aloud.**

- `demand_mw_lag3` — the level three hours back. The single strongest anchor: whatever the
  grid was doing recently is where tomorrow starts from.
- `d_cos1` — the first daily cosine. A smooth, continuous encoding of time-of-day that lets a
  tree cut the day into shape rather than into 24 unrelated buckets.
- `demand_mw_rmean168` — the trailing weekly mean. The slow level: heat wave, industrial ramp,
  seasonal drift.
- `hour` — the raw hour, cutting the sharp edges the Fourier terms smooth over (the evening ramp).
- `demand_mw_rmean24` — yesterday's trailing mean. The short-run level.

Rolled up: rolling 33.1%, lags 29.0%, Fourier 25.8%, calendar 7.3%, weather 4.9%. Roughly
two-thirds of the gain is the series' own recent history; the calendar and Fourier terms shape
it; temperature adds under 5% *given* those (it is largely already encoded in the recent level).

**Say this in the room, every time.** Gain is *associational*. It measures how much this model,
with this feature set, on this data, reduced its loss by splitting on a column. It is not a
causal effect, it is not a sensitivity, and it does not survive a change in the feature set —
drop `demand_mw_rmean24` and `demand_mw_lag3` will simply absorb its gain. Two correlated
features split one column's importance between them and both look weak. Never hand a gain
table to an engineer as "what drives demand"."""))
    else:
        c.append(code('''from tayyar.models.explain import importance_by_family

# TODO (8 min)
#   1. imp = lgbm.feature_importance(25)   -- this is mean GAIN, not split count.
#      Why gain? Split count rewards high-cardinality columns for being splittable.
#   2. print the top 10, then importance_by_family(imp)
#   3. horizontal bar chart of the top 14
#   4. Interpret the top FIVE out loud to your pair — one sentence each, in domain terms.
#
# HINT: the sentence that must be said before anyone acts on this table is
#       "these are associations, not causes". Ask yourselves what happens to
#       demand_mw_lag3's gain if you delete demand_mw_rmean24.'''))

    # ------------------------------------------------- leakage demonstration --
    c.append(md("""### The leakage demonstration — one model, four evaluation designs

Same LightGBM, same data, same day-ahead target. Only the *evaluation design* changes, plus
one feature. `tools/leak_demo.py` produces these; the recorded run is in `leak_results.json`."""))
    c.append(code('''import json

leak = json.load(open("../leak_results.json"))
designs = [
    ("A", "shuffle split + leaky features", leak["A_shuffle_plus_leaky_features"]),
    ("B", "shuffle split, clean features",  leak["B_shuffle_clean_features"]),
    ("C", "time-ordered split, clean",      leak["C_time_split_clean"]),
    ("D", "rolling-origin backtest, clean", leak["D_rolling_origin_clean"]),
]
for k, name, v in designs:
    print(f"{k}  {name:<34s} {v:5.2f}% MAPE")
print(f"\\nD spread across origins: {leak['D_spread'][0]:.2f}% .. {leak['D_spread'][1]:.2f}%")
print(f"the leaked design reports a model "
      f"{leak['D_rolling_origin_clean'] / leak['A_shuffle_plus_leaky_features']:.1f}x "
      f"more accurate than it actually is.")

fig, ax = plt.subplots(figsize=(8.6, 4))
labs = [f"{k}  {n}".replace(" + ", "\\n+ ").replace(", ", ",\\n") for k, n, _ in designs]
vals = [v for _, _, v in designs]
bars = ax.bar(labs, vals, color=["#A11B2A", "#C2601B", "#D9A441", "#1E7A4D"], width=.62)
for r, v in zip(bars, vals):
    ax.text(r.get_x() + r.get_width() / 2, v + .06, f"{v:.2f}%",
            ha="center", fontweight="bold")
ax.set_ylabel("day-ahead MAPE (%)"); ax.set_ylim(0, max(vals) * 1.25)
ax.set_title("One model, one dataset, one target — four evaluation designs")
plt.tight_layout()'''))
    if sol:
        c.append(md("""**A -> B** is the cost of the leaky features alone: 1.61% -> 2.00%, still on a shuffled split.

**B -> C** is the cost of the split alone: 2.00% -> 3.54%. The split is the larger of the two
frauds, and it is the one that leaves no trace in the feature code.

**C -> D** is honesty about variance: a single time-ordered split is one anecdote (3.54%);
sixty rolling origins say 3.66% with a spread from 2.31% to 4.89%. The spread is the number
you quote to a regulator, because it is the range the control room will actually live in.

**A vs D** is the headline: the design that would have been reported is **2.3x** better than
the truth. Nothing in the model was wrong. Everything in the evaluation was.

(These four numbers use a plain single-horizon LightGBM rather than the direct 24-model
forecaster of Task 3, which is why D at 3.66% is a little worse than the 2.33% you measured
above. The comparison that matters is between the four designs, not against Task 4.)"""))
    else:
        c.append(md("""In `LEAKS.md`, answer with numbers from the table above:

- how much of the inflation came from the leaky **features** (A -> B)?
- how much came from the **split** (B -> C)?
- what does the spread of D tell you that the single number C hides?
- how many times better than the truth was the number your colleague would have reported?"""))

    c.append(md(QUIZ4_A if sol else QUIZ4_Q))
    c.append(md(COMMIT4))

    if sol:
        c.append(md("""### Instructor notes

**Protect the full 50 minutes.** With Lab 6 this is one of the two most overrun-prone slots in
the course. If you are behind, cut Task 5's chart, never Task 1.

- **Run Task 1 as a race.** First pair to name both leaks *precisely* — the line and the
  mechanism, not "something's wrong with the split" — wins. It takes the room four minutes
  and it is the highest-retention four minutes of Day 2. Do not hint before minute three.
- **Branch `sim-centred-roll`** ships the centred window as the only defect, with an
  otherwise-correct time split. Use it with a fast group: the MAPE is merely *good* rather than
  absurd, which is how this defect actually arrives in production.
- **Branch `sim-heatwave`** holds out a week containing a record high. The raw-target model
  under-forecasts the peak by a wide margin and the room can see the ceiling in the plot —
  trees interpolate, they cannot extrapolate past the training range. Two legitimate
  mitigations: model a differenced or relative target (percentage of the trailing weekly mean,
  say) so the extrapolation happens in the level rather than the tree; or accept the ceiling
  and keep a classical/level model in the candidate set for exactly these weeks. Do not let
  anyone "fix" it by adding more trees.
- **"What does this feature see?"** Put four columns on the board — `demand_mw_lag1`,
  `demand_mw_rmean24`, `is_eid`, `temp_c` — and have each pair rule each one legal or illegal at
  a 24-hour origin. `temp_c` is the deliberately ambiguous one: it is legal *only* if you
  substitute a day-ahead weather **forecast** in production, and the docstring in
  `features/build.py` says so. A model validated on realised temperature and deployed on
  forecast temperature will quietly degrade. This argument is worth five minutes.

**Troubleshooting**

| symptom | cause |
|---|---|
| MAPE below 0.7% | a leak survived. Look for a centred window, a `shift(-h)` in the features, or a scaler fitted on everything. |
| model under-forecasts a heat spike | not a bug. Trees cannot extrapolate beyond the training range. |
| most rows disappeared | `demand_mw_lag336` leaves 336 leading NaNs. Expected — drop them, never back-fill. |
| weekend flag on the wrong days | pandas `dayofweek` is Monday=0. The KSA weekend is 4 (Friday) and 5 (Saturday). |
| `assert_no_leakage` reports a different feature count | a boolean column slipped in; cast the flags to int. |

**Fast finishers.** Refit with `objective="l2"` instead of the default `"l1"` and compare the
bias on the peak hours; or drop the whole rolling family and watch the lag family absorb its
gain — the cleanest possible demonstration that importance is not a causal quantity."""))

    write(f"lab4_{tag}.ipynb", c)


# ============================================================= LAB 5 ==========
L5_TASKS = """### Tasks

| min | task |
|---|---|
| 5 | Find the **two bugs** in the starter interval you inherited. Note both in `INTERVALS.md`. |
| 10 | Reuse the Lab 4 feature matrix. Split train / calibration / test **by time**. Fit `QuantileLGBM` at τ ∈ {0.05, 0.50, 0.95} and repair quantile crossing. |
| 10 | Coverage and mean width of the raw band on the test window. It will come out **below** 90%. |
| 10 | Calibrate with `CQR` on the held-out October window. Re-apply. Coverage should snap to ≈ 0.90. |
| 10 | Report coverage **marginally and conditionally** with `coverage_report`. Pinball losses and the Winkler score. Plot one calibrated day. |
| 5 | Recommend one method in `INTERVALS.md`. Commit. |

> **Day boundary.** Tasks 1–3 close Day 2; the room goes home holding an interval that
> visibly under-covers. Tasks 4–6 open Day 3.
"""

LOAD5 = '''from tayyar.data.load import load_demand, load_calendar, join_calendar
from tayyar.features.build import build_features

df = join_calendar(load_demand(f"{DATA}/ksa_grid_demand.csv"),
                   load_calendar(f"{DATA}/ksa_calendar.csv"))
feat = build_features(df[["demand_mw", "temp_c", "is_weekend",
                          "is_ramadan", "is_eid", "is_national_day"]])
Xcols = [c for c in feat.columns if c != "demand_mw"]
X, yy = feat[Xcols].astype(float), feat["demand_mw"]

CUT_TRAIN, CUT_CAL = "2023-09-30 23:00", "2023-10-31 23:00"
print(f"{len(feat):,} rows x {len(Xcols)} features (the Lab 4 design matrix)")'''

STARTER5 = '''# ---------------------------------------------------------------------------
# The starter code you inherited
#
# "Day-ahead point forecast with a 90% interval. I checked the coverage."
#
# It runs and it produces an interval. Two lines make the reported coverage
# worthless — one about WHAT is being estimated, one about WHERE it is measured.
# ---------------------------------------------------------------------------
import lightgbm as lgb

Y24 = yy.shift(-24)                                  # the day-ahead target
ok = X.notna().all(axis=1) & Y24.notna()
Xfit, Yfit = X[ok][:CUT_TRAIN], Y24[ok][:CUT_TRAIN]

point = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.06, num_leaves=63,
                          verbose=-1, random_state=212).fit(Xfit, Yfit)

fitted = point.predict(Xfit)
resid = Yfit - fitted
se = resid.std() / np.sqrt(len(resid))               # "the standard error"
half = 1.645 * se                                    # "90%"

lo_s, hi_s = fitted - half, fitted + half
cov_s = float(np.mean((Yfit >= lo_s) & (Yfit <= hi_s)))

print(f"residual sd            : {resid.std():8,.1f} MW")
print(f"reported 90% band width: {2 * half:8,.1f} MW")
print(f"reported coverage      : {cov_s:8.3f}")'''

QUIZ5_Q = """### Mini-quiz

Answer these in your pair before you look at the next cell.

1. For a *future observation*, do you need a prediction interval or a confidence interval?
2. What does minimising pinball loss at τ = 0.9 recover?
3. What exactly does split-conformal guarantee, and under what assumption?
4. Why can two independently-fitted quantile models be incoherent?
5. Two intervals both cover 90%. Which one ships?
"""

QUIZ5_A = """### Mini-quiz — answers

1. **Prediction interval.** A confidence interval covers the conditional *mean* and shrinks
   like 1/√n towards zero; a prediction interval must also contain the irreducible noise of a
   single future observation, so it is wider and does not shrink to nothing however much data
   you have. Bug (a) in the starter was exactly this substitution.
2. **The 90th percentile.** Pinball loss is asymmetric on purpose: at τ = 0.9 an
   under-prediction is penalised nine times more than an over-prediction, and the minimiser
   is the conditional 0.9 quantile.
3. **Marginal (1−α) coverage**, under **exchangeability** of the calibration and test
   nonconformity scores. Marginal — averaged over everything. It says nothing about coverage
   on any particular subgroup, and exchangeability is a real assumption that a regime change
   breaks.
4. **They can cross.** Three separate fits share no monotonicity constraint, so q95 can land
   below q50 for some rows — an incoherent distribution. Fix by sorting each row, or by fitting
   with a monotone constraint. Never by ignoring it.
5. **The sharper one.** Coverage is the constraint; width is the objective. The Winkler
   (interval) score is the single number that trades the two, which is why we report it.
"""

COMMIT5 = """### Task 6 — `INTERVALS.md` and commit

Write the recommendation, not the method tour. Four short sections:

1. **The two bugs in the starter**, with the mechanism of each in one sentence.
2. **The numbers**: raw quantile band 0.786 coverage at 2,418 MW mean width; after CQR
   0.902 at 3,235 MW; q̂ = 409 MW.
3. **The recommendation**: quantile LightGBM calibrated by CQR on a rolling recent window,
   at α = 0.10. Reason: it keeps the shape of the quantile model (wide where the model is
   genuinely uncertain) and rescales it to hit nominal coverage, with a distribution-free
   finite-sample guarantee, for the cost of one held-out month.
4. **The caveat, in the same paragraph as the recommendation, not a footnote**: marginal
   0.902 hides 0.845 on the 12:00–18:00 peak. Reserve is sized on those hours. Ship the
   conditional table with the headline or ship neither, and move to adaptive conformal
   before this interval is used to size anything.

```
git add -A && git commit -m "feat(models): quantile LightGBM + CQR-calibrated day-ahead intervals"
```"""


def lab5(sol: bool):
    tag = "solution" if sol else "start"
    c = [md(HDR.format(n=5, title="Calibrated Day-Ahead Intervals", dur=50, tag=tag)),
         md(L5_TASKS), code(SETUP), code(LOAD5)]

    # ---------------------------------------------------------------- task 1 --
    c.append(md("""### Task 1 — the starter interval you inherited

Run the next cell. It produces a 90% band and a coverage number. Five minutes: name the two
bugs precisely, and write them into `INTERVALS.md`. Do not fix them yet."""))
    c.append(code(STARTER5))
    if sol:
        c.append(md("""**Bug (a) — it is a confidence interval, not a prediction interval.**
`resid.std() / np.sqrt(n)` is the standard error of the *mean*. It answers "where is the
conditional average?" and it shrinks towards zero as n grows — with 23,700 training rows the
band comes out about 13 MW wide on a 30,000 MW system. The control room is not asking about the
average of a hypothetical population of tomorrows; it is asking where *tomorrow* will land, so
the interval must also carry the irreducible noise of a single observation. That is a
prediction interval, and it does not shrink with n.

**Bug (b) — coverage is measured on the training set.** `fitted` are in-sample predictions from
a 300-tree model, so the residuals it is scored against are the residuals it was fitted to
minimise. Whatever coverage that reports is an upper bound on the truth, not an estimate of it.

Bug (a) is loud: a 13 MW band is visibly absurd the moment you read the width. Bug (b) is
silent — nothing in that printout tells you the coverage figure was measured on the very rows
the model was fitted to minimise error on, and a healthy-looking 0.90 from a training set is
how this defect actually ships. Separate the two and both become measurable."""))
        c.append(code('''Xtest, Ytest = X[ok][CUT_CAL:], Y24[ok][CUT_CAL:]
pred_test = point.predict(Xtest)

def cov(y, lo, hi):
    return float(np.mean((np.asarray(y) >= lo) & (np.asarray(y) <= hi)))

rows = []
for label, hw in [("(a) confidence: 1.645 * sd / sqrt(n)", 1.645 * se),
                  ("(b) prediction: 1.645 * sd",           1.645 * resid.std())]:
    rows.append({"band": label, "width_MW": round(2 * hw, 1),
                 "coverage_TRAIN": round(cov(Yfit, fitted - hw, fitted + hw), 3),
                 "coverage_TEST":  round(cov(Ytest, pred_test - hw, pred_test + hw), 3)})
print(pd.DataFrame(rows).to_string(index=False))'''))
        c.append(md("""Read the table by column. Down the first column, bug (a): the confidence band is
narrower than the prediction band by a factor of √n and covers almost nothing. Across the
row, bug (b): the honest prediction band covers close to nominal on the rows it was fitted on
and materially less on rows it has never seen. That gap is the entire reason the calibration
window in Task 2 is held out.

A third defect follows from bug (a)'s formula and is worth naming: a constant half-width
assumes the uncertainty is the same at 04:00 in February and at 15:00 in July. It is not.
That is what the quantile model in Task 2 fixes."""))
        c.append(md("""**`INTERVALS.md`, section 1**

```
## Bugs in the inherited starter (labs/lab5)

(a) Confidence interval where a prediction interval is required.
    half = 1.645 * resid.std() / sqrt(n) is the standard error of the MEAN.
    It shrinks like 1/sqrt(n) and omits the irreducible noise of a single
    future observation. Correct object: a prediction interval, which does not
    shrink to zero.

(b) Coverage estimated on the training set.
    `fitted` are in-sample predictions of a 300-tree model, scored against the
    residuals it was fitted to minimise. The figure is an upper bound, not an
    estimate. Correct: a held-out calibration window, disjoint in time.
```"""))
    else:
        c.append(code('''# TODO (5 min) — do not change the cell above yet.
#
# Bug 1 is about WHAT the interval estimates. Write down, in one line each:
#   - what does resid.std() / sqrt(n) estimate?
#   - what does a control room need an interval around tomorrow's demand to contain?
#   - what happens to that band as n grows to a million rows? Should it?
#
# Bug 2 is about WHERE coverage is measured. Compute the same band's coverage on
# the test window (X[ok][CUT_CAL:]) and compare it with the printed number.
#
# Then separate the two: tabulate coverage on TRAIN and on TEST for
#   (a) half = 1.645 * resid.std() / sqrt(n)     and
#   (b) half = 1.645 * resid.std()
#
# HINT: the two bugs push the reported number in opposite directions, so neither is
#       visible from the printout alone. One factor is sqrt(n); the other is a split.'''))

    # ---------------------------------------------------------------- task 2 --
    c.append(md("""### Task 2 — three quantiles, split by time, de-crossed

Three time blocks, disjoint and in order:

| block | window | purpose |
|---|---|---|
| train | … through 2023-09-30 | fit the quantile models |
| calibration | October 2023 | estimate q̂ — never used for fitting |
| test | November–December 2023 | the only honest coverage estimate |

`QuantileLGBM` fits one model per (horizon, τ): 3 × 24 = 72 models. Nothing constrains the
three fits to be monotone, so q95 can land below q50 for some rows — an incoherent
distribution that would produce a negative-width interval. Sort each row."""))
    if sol:
        c.append(code('''from tayyar.models.quantile import QuantileLGBM

Xtr = X[:CUT_TRAIN].dropna(); ytr = yy[Xtr.index]
Xca, yca = X[CUT_TRAIN:CUT_CAL], yy[CUT_TRAIN:CUT_CAL]
Xte, yte = X[CUT_CAL:], yy[CUT_CAL:]
for nm, ix in (("train", Xtr.index), ("calib", Xca.index), ("test", Xte.index)):
    print(f"{nm:<6} {ix.min():%Y-%m-%d} -> {ix.max():%Y-%m-%d}  ({len(ix):,} rows)")

TAUS = (0.05, 0.50, 0.95)
qm = QuantileLGBM(quantiles=TAUS, horizon=24).fit(Xtr, ytr)   # 72 models — a few minutes
print(f"\\nfitted {len(qm.models_)} models = {len(TAUS)} quantiles x 24 horizons")'''))
        c.append(code('''def q_predict(Xs):
    """(3, n_origins, 24) — one plane per quantile, one row per origin."""
    return np.stack([np.column_stack([qm.models_[(h, t)].predict(Xs)
                                      for h in range(1, 25)]) for t in TAUS])

def day_blocks(Xs, ys, step=24):
    """One forecast origin per day; the 24 actual hours that follow each."""
    rows = list(range(0, len(Xs) - 24, step))
    Y = np.array([ys.iloc[i + 1: i + 25].to_numpy() for i in rows])
    return Y, rows, [Xs.index[i] for i in rows]

Yca, rows_ca, idx_ca = day_blocks(Xca, yca)
Pca = q_predict(Xca.iloc[rows_ca])
Yte, rows_te, idx_te = day_blocks(Xte, yte)
Pte = q_predict(Xte.iloc[rows_te])

for nm, P in (("calibration", Pca), ("test", Pte)):
    print(f"{nm:<12} {P.shape[1]} origins x 24 h = {P[0].size} cells")
    print(f"   q05 > q50 : {int((P[0] > P[1]).sum()):4d}")
    print(f"   q50 > q95 : {int((P[1] > P[2]).sum()):4d}")
    print(f"   q05 > q95 : {int((P[0] > P[2]).sum()):4d}   <- band inversions")

# The repair. Sorting the row is the blunt version and is what
# QuantileLGBM.predict_interval does. Here the band itself is never inverted
# (q05 <= q95 in every cell), so the only incoherence is the median falling
# outside its own interval — clip it back in and keep the model's endpoints.
Pca_raw, Pte_raw = Pca.copy(), Pte.copy()
for P in (Pca, Pte):
    assert (P[0] <= P[2]).all()
    P[1] = np.clip(P[1], P[0], P[2])
print(f"\\nmedians clipped back inside the band, largest move: "
      f"{np.abs(Pte - Pte_raw).max():,.1f} MW")
print("remaining incoherent cells:",
      int((Pte[0] > Pte[1]).sum() + (Pte[1] > Pte[2]).sum()))'''))
        c.append(md("""Eighty incoherent cells out of 1,464 on the test window: 17 where q05 came out above
q50, 63 where q50 came out above q95. Nothing constrains three separate fits to be monotone,
so this is expected rather than surprising — and "rare and small" is still not "acceptable".
A median sitting outside its own 90% interval is not a wide forecast or a noisy one; it is
not a distribution, and it is indefensible on a control-room screen.

Two repairs. `np.sort(P, axis=0)` takes the order statistics and is what
`QuantileLGBM.predict_interval` does — correct, and the right choice when the band endpoints
themselves invert. Here they never do (`q05 > q95` in zero cells), so the band the model
learned is coherent and only the median is misplaced; clipping the median back inside keeps
the endpoints the quantile models actually produced. The principled fix, ahead of both, is a
monotone constraint at fit time."""))
    else:
        c.append(code('''from tayyar.models.quantile import QuantileLGBM

# TODO (10 min)
#   1. Three disjoint blocks, in time order:
#        Xtr = X[:CUT_TRAIN].dropna();  ytr = yy[Xtr.index]
#        Xca, yca = X[CUT_TRAIN:CUT_CAL], yy[CUT_TRAIN:CUT_CAL]     # October
#        Xte, yte = X[CUT_CAL:],          yy[CUT_CAL:]              # Nov-Dec
#      Print each window and check they do not overlap.
#   2. qm = QuantileLGBM(quantiles=(0.05, 0.50, 0.95), horizon=24).fit(Xtr, ytr)
#      72 models. Start it and read the next paragraph while it runs.
#   3. Write two helpers:
#        q_predict(Xs) -> array (3, n_origins, 24), one plane per quantile
#        day_blocks(Xs, ys) -> the 24 actual hours after each daily origin
#   4. COUNT the quantile crossings before you repair them — separately for
#      (q05 > q50), (q50 > q95) and (q05 > q95). Then repair: np.sort(P, axis=0)
#      takes the order statistics; if the band itself is never inverted you can
#      instead clip the median into [q05, q95] and keep the model's endpoints.
#      Report the largest correction you applied.
#
# HINT: report the crossing count. "We sorted it" without a count is how a broken
#       quantile model gets shipped quietly.'''))

    # ---------------------------------------------------------------- task 3 --
    c.append(md("""### Task 3 — what the raw band actually covers"""))
    if sol:
        c.append(code('''from tayyar.eval.pinball import coverage

lo_raw, med, hi_raw = Pte[0], Pte[1], Pte[2]
print(f"nominal coverage        : 0.900")
print(f"empirical coverage      : {coverage(Yte.ravel(), lo_raw.ravel(), hi_raw.ravel()):.4f}")
print(f"mean width              : {np.mean(hi_raw - lo_raw):,.1f} MW")
print()
print(f"on the calibration month: "
      f"{coverage(Yca.ravel(), Pca[0].ravel(), Pca[2].ravel()):.4f}")'''))
        c.append(md("""**0.786 against a nominal 0.900.** One test hour in five falls outside a band advertised as
covering nineteen in twenty.

Nothing is broken. `QuantileLGBM` minimises pinball loss on the *training* window, and a
finite, regularised, boosted model does not reproduce its training quantiles out of sample —
gradient boosting shrinks towards the centre, the test window is a different season from most
of the training data, and the pinball optimum is only asymptotically the quantile. The
calibration month shows the same shortfall (0.823), which is what makes it usable as a
correction: the gap is a property of the model, not of November.

**This is where Day 2 ends.** Go home holding a 90% interval that covers 79%."""))
    else:
        c.append(code('''from tayyar.eval.pinball import coverage

# TODO (10 min)
#   lo_raw, med, hi_raw = Pte[0], Pte[1], Pte[2]
#   Report, on the TEST window:
#     - nominal coverage (0.90)
#     - empirical coverage of [lo_raw, hi_raw]
#     - mean width in MW
#   Then the same coverage on the CALIBRATION month.
#
#   Write the two numbers in INTERVALS.md before you go any further.
#
# HINT: it will come out BELOW 0.90, and that is not a bug in your code. Ask why a
#       model that minimised pinball loss in-sample misses its quantiles out of sample,
#       and whether the calibration month shows the same shortfall. If it does, the
#       shortfall is a property of the model and you can correct for it.'''))

    # ---------------------------------------------------------------- task 4 --
    c.append(md("""### Task 4 — conformal calibration (CQR)

The recipe, in four lines:

1. **Split.** Hold out a calibration window the model never saw — October here.
2. **Score.** For CQR the nonconformity score is `max(lo - y, y - hi)`: how far the truth fell
   *outside* the band. It is negative when the truth was comfortably inside, which is how the
   band can also be made *narrower* when the model is over-cautious.
3. **q̂.** Take the `ceil((n+1)(1-α))`-th smallest score. The `+1` is the finite-sample
   correction — it is what turns an asymptotic statement into a guarantee that holds at any n.
4. **Widen.** The calibrated interval is `[lo - q̂, hi + q̂]`.

CQR keeps the *shape* the quantile model learned — wide on volatile afternoons, narrow at
04:00 — and rescales it. A symmetric split-conformal band around the point forecast would hit
the same marginal coverage with a constant width, and be badly wrong in both directions at
different hours."""))
    if sol:
        c.append(code('''from tayyar.models.conformal import CQR, conformal_quantile

cqr = CQR(alpha=0.10).calibrate(Yca.ravel(), Pca[0].ravel(), Pca[2].ravel())
lo_cal, hi_cal = cqr.interval(lo_raw, hi_raw)

n = Yca.size
scores = np.maximum(Pca[0].ravel() - Yca.ravel(), Yca.ravel() - Pca[2].ravel())
k = int(np.ceil((n + 1) * 0.90))
print(f"calibration scores      : n = {n}")
print(f"rank taken, ceil((n+1)(1-a)) = {k}   ({k}/{n} = {k/n:.4f})")
print(f"q-hat                   : {cqr.qhat_:,.1f} MW")
print(f"  (identical to conformal_quantile: {conformal_quantile(scores, 0.10):,.1f})")
print()
print(f"coverage before         : {coverage(Yte.ravel(), lo_raw.ravel(), hi_raw.ravel()):.4f}"
      f"   mean width {np.mean(hi_raw - lo_raw):8,.1f} MW")
print(f"coverage after          : {coverage(Yte.ravel(), lo_cal.ravel(), hi_cal.ravel()):.4f}"
      f"   mean width {np.mean(hi_cal - lo_cal):8,.1f} MW")'''))
        c.append(md("""0.786 -> **0.902**, for 409 MW added to each side and a mean width of 3,235 MW instead of
2,418. That is the trade, stated honestly: coverage was bought with sharpness, and the price
is on the table rather than hidden in a footnote.

Note what was *not* required. No distributional assumption, no normality, no correctly
specified variance model — only that the calibration and test scores be exchangeable. The
guarantee is finite-sample and distribution-free."""))
    else:
        c.append(code('''from tayyar.models.conformal import CQR, conformal_quantile

# TODO (10 min)
#   1. cqr = CQR(alpha=0.10).calibrate(Yca.ravel(), Pca[0].ravel(), Pca[2].ravel())
#   2. lo_cal, hi_cal = cqr.interval(lo_raw, hi_raw)
#   3. Recompute q-hat BY HAND and check it matches cqr.qhat_:
#        scores = np.maximum(Pca[0].ravel() - Yca.ravel(), Yca.ravel() - Pca[2].ravel())
#        k = ceil((n + 1) * (1 - alpha));  q-hat = the k-th smallest score
#      Print n, k, k/n and q-hat. Explain the +1 to your pair.
#   4. Coverage and mean width, before and after, on the TEST window.
#
# HINT: coverage should snap to about 0.90 and the width should grow. If coverage
#       overshoots to 0.99 you calibrated on a window from a different regime — check
#       that the calibration month is adjacent to the test window, not a summer month.'''))

    # ---------------------------------------------------------------- task 5 --
    c.append(md("""### Task 5 — marginal is not conditional"""))
    if sol:
        c.append(code('''from tayyar.models.conformal import coverage_report
from tayyar.eval.pinball import pinball_loss, interval_score

h = np.tile(np.arange(1, 25), len(Yte))          # horizon 1..24 from a 23:00 origin
band = pd.Series(np.where(pd.Series(h).isin(range(12, 19)),
                          "12:00-18:00 (peak)", "other hours"))

print("AFTER calibration")
print(coverage_report(Yte.ravel(), lo_cal.ravel(), hi_cal.ravel(), band).to_string(index=False))
print("\\nBEFORE calibration")
print(coverage_report(Yte.ravel(), lo_raw.ravel(), hi_raw.ravel(), band).to_string(index=False))'''))
        c.append(code('''print(f"pinball q05 (calibrated lo) : {pinball_loss(Yte.ravel(), lo_cal.ravel(), 0.05):7.1f}")
print(f"pinball q50 (as fitted)     : {pinball_loss(Yte.ravel(), Pte_raw[1].ravel(), 0.50):7.1f}")
print(f"pinball q50 (de-crossed)    : {pinball_loss(Yte.ravel(), med.ravel(), 0.50):7.1f}")
print(f"pinball q95 (calibrated hi) : {pinball_loss(Yte.ravel(), hi_cal.ravel(), 0.95):7.1f}")
print(f"Winkler                     : "
      f"{interval_score(Yte.ravel(), lo_cal.ravel(), hi_cal.ravel(), 0.10):7.1f}")'''))
        c.append(code('''k = 3
tt = pd.date_range(idx_te[k] + pd.Timedelta(1, "h"), periods=24, freq="h")

fig, ax = plt.subplots(figsize=(11, 4.2))
ax.fill_between(tt, lo_cal[k], hi_cal[k], color="#8FAADC", alpha=.55,
                label="90% interval (CQR-calibrated)")
ax.plot(tt, lo_raw[k], color="#7F7F7F", lw=.9, ls=":")
ax.plot(tt, hi_raw[k], color="#7F7F7F", lw=.9, ls=":", label="raw quantile band")
ax.plot(tt, med[k], color="#C00000", lw=1.8, label="forecast (q50)")
ax.plot(tt, Yte[k], color="#1F3864", lw=1.8, ls="--", label="actual")
ax.set_title(f"Day-ahead forecast from {idx_te[k]:%Y-%m-%d %H:%M} "
             f"with a calibrated 90% prediction interval")
ax.set_ylabel("MW"); ax.legend(frameon=False, ncols=4, fontsize=8, loc="upper left")
plt.tight_layout()'''))
        c.append(md("""**The headline, and it must be said in exactly these words: marginal coverage of 0.90 hides
a conditional hole — only 0.845 on the summer and peak afternoons that reserve is actually
sized for.**

```
AFTER   ALL                 0.9016   width 3234.8
        12:00-18:00 (peak)  0.8454   width 3863.4
        other hours         0.9248   width 2975.9
```

The band is already 30% wider on the peak block, so the model *knows* those hours are harder —
it is simply not wide enough. Averaging across 24 hours lets the easy overnight hours
(0.925) pay for the hard afternoon ones, and the average clears 0.90. Every hour the average
buys is an hour that does not need reserve.

Before calibration the same shape is there and worse: 0.738 on peak against 0.806 elsewhere.
Conformal calibration lifted the whole curve; it did not close the gap, and it was never
going to. **Split conformal guarantees marginal coverage under exchangeability, not
conditional coverage.** If you need the guarantee to hold *per hour band*, you need a method
that adapts: **adaptive conformal inference (ACI)**, which updates q̂ online from the realised
miss rate, or **EnbPI**, which bootstraps ensemble residuals and re-estimates as the window
rolls. Both are the honest next step and both belong in the recommendation.

**The exchangeability warning.** Calibrate on peak summer and test in winter and the
assumption fails in the other direction: the summer scores are far larger than the winter
ones, q̂ is far too big, and the interval over-covers to roughly 0.99 while being much too
wide to size anything with. An interval that always contains the truth carries no
information. The calibration window must be **adjacent in regime**, not merely held out —
which is why October calibrates November, and why in production q̂ is re-estimated on a
rolling recent window rather than fixed once.

The pinball losses (95.2 / 368.4 / 120.9, and 366.3 for the de-crossed median) and the
Winkler score (4,323) are how you compare
two candidate intervals without arguing. Pinball scores each quantile as a quantile; Winkler
adds width and a miss penalty into the one number that trades coverage against sharpness.
Two methods that both cover 90% are separated by Winkler, and the sharper one ships."""))
    else:
        c.append(code('''from tayyar.models.conformal import coverage_report
from tayyar.eval.pinball import pinball_loss, interval_score

# TODO (10 min)
#   1. Build the conditioning variable: horizon 1..24 tiled across the origins,
#        h = np.tile(np.arange(1, 25), len(Yte))
#      and label h in 12..18 as "12:00-18:00 (peak)", everything else "other hours".
#   2. coverage_report(...) AFTER calibration, then BEFORE. Print both.
#   3. pinball_loss at 0.05 / 0.50 / 0.95, and interval_score (Winkler) at alpha=0.10.
#   4. Plot one day: the calibrated band, the raw band, q50, and the actual.
#
#   Then answer in INTERVALS.md: your marginal coverage is ~0.90. What is it on the
#   peak block? Which hours does the grid actually size reserve for?
#
# HINT: conformal calibration guarantees MARGINAL coverage under exchangeability.
#       Nothing in the recipe promises the peak hours anything. Expect the marginal
#       number to look fine and the peak number not to.'''))

    c.append(md(QUIZ5_A if sol else QUIZ5_Q))
    c.append(md(COMMIT5))

    if sol:
        c.append(md("""### Instructor notes

**The day boundary is deliberate.** Stop after Task 3, with the room holding a 90% interval
that covers 78.6%. Do not let a fast pair run ahead into CQR — send them to the extension
below instead. The overnight gap is what makes the calibration land on Day 3 morning; if you
teach the fix in the same breath as the failure, it registers as a formula rather than as a
relief.

- **Branch `sim-hetero`** inflates the summer variance. The starter's analytic interval then
  covers about 90% overall and about 78% in summer — the same lesson as the peak-hour hole,
  arriving from the variance side rather than the hour-of-day side. Use it if the room accepts
  the conditional argument too readily.
- **Branch `sim-train-coverage`** reports 0.94 and delivers 0.83. It is bug (b) alone, in a
  form that looks entirely healthy on the page. Good as a five-minute opener on Day 3.
- **The coverage courtroom** (10 minutes, after Task 5). One pair defends the claim "our
  day-ahead interval has 90% coverage" — they are not lying, the marginal number is 0.902.
  Another pair cross-examines using only the held-out conditional table. The defence usually
  concedes within three questions; when it does, ask the room what the *honest* sentence would
  have been. Write the winning formulation on the board and require it in `INTERVALS.md`.
- **The elicitation drill** (5 minutes). Three decisions on the board — reserve margin, SKU
  stocking, staff roster. Each pair names the quantile that decision consumes and why: reserve
  is a high quantile because the cost of under-supply is asymmetric and severe; stocking
  balances holding cost against stock-out, so the quantile is the critical ratio and is rarely
  0.5; a roster is nearer the median because both over- and under-staffing cost roughly
  linearly. The point: **nobody consumes a point forecast.** They all consume a quantile, and
  if you do not ask which one, you have chosen 0.5 on their behalf.

**Troubleshooting**

| symptom | cause |
|---|---|
| coverage lands at 0.99 | the calibration window is from a different regime. Exchangeability failed; use an adjacent month. |
| coverage after CQR still ≈ 0.79 | q̂ applied to the wrong band, or the calibration scores were computed against sorted quantiles and the band against unsorted ones. |
| negative interval widths | quantile crossing was not repaired. Sort each row. |
| the fit takes forever | 72 models. Say so before the room starts it, and use the wait to teach the conformal recipe. |
| coverage reported on train looks perfect | that is bug (b) returning. Only the test window counts. |

**Fast finishers.** Re-run the calibration on a *summer* month (July) instead of October and
measure the over-coverage on the November–December test window — this is the exchangeability
warning as a number rather than a caution. Or implement one step of adaptive conformal: after
each day, nudge α by `γ(α_target − 1{miss})`, re-derive q̂, and plot the realised coverage over
the 61 test days converging on 0.90."""))

    write(f"lab5_{tag}.ipynb", c)


for s in (False, True):
    lab4(s); lab5(s)
print("labs 4 and 5 written")
