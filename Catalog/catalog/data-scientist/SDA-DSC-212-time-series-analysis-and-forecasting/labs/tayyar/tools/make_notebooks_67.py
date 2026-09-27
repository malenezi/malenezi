"""Generate the Lab 6 and Lab 7 notebooks (start + solution).

Same house style as tools/make_notebooks.py — see notebooks/_SPEC.md.
Lab 6 ships ONE planted leak in the START notebook (a "backtest" that fits once
on the whole file and then scores hours the model was fitted on); Lab 7 ships ONE
planted fault (selection by argmin(MASE), which promotes a model that cannot be
served). Both are diagnosed and repaired in the solution.

Every printed number is the one produced by tools/run_reference.py and stored in
reference_results.json (block "m6"), or is reproduced by running these notebooks.
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

LOAD67 = '''from tayyar.data.load import load_demand, load_calendar, join_calendar
from tayyar.features.build import build_features

df = join_calendar(load_demand(f"{DATA}/ksa_grid_demand.csv"),
                   load_calendar(f"{DATA}/ksa_calendar.csv"))
feat = build_features(df[["demand_mw", "temp_c", "is_weekend",
                          "is_ramadan", "is_eid", "is_national_day"]])
Xcols = [c for c in feat.columns if c != "demand_mw"]
X, yy = feat[Xcols].astype(float), feat["demand_mw"]
y = df["demand_mw"].astype(float)

CUT_TRAIN, CUT_CAL = "2023-09-30 23:00", "2023-10-31 23:00"
print(f"{len(feat):,} hourly rows x {len(Xcols)} features "
      f"({df.index.min():%Y-%m-%d} -> {df.index.max():%Y-%m-%d})")'''

# ============================================================= LAB 6 ==========
L6_TASKS = """### Tasks

| min | task |
|---|---|
| 5 | Find the **fit-once leak** in the inherited backtest. Show that its MASE is absurd. Record it in `BACKTEST.md`. **Do not fix it yet.** |
| 12 | Configure a proper rolling origin: expanding window, one-year initial window, step 24 h, horizon 24 h, training data ending **at** each origin. At least 50 origins, at least three model families. |
| 10 | Aggregate the per-origin errors: the **mean and the spread** of MAE, MAPE and MASE per model, every model reported relative to the seasonal-naive baseline. |
| 8 | Probabilistic scoring for the interval model: mean pinball loss and empirical coverage across origins. |
| 10 | `diebold_mariano` on the top two point models. Record the significance. Decide the champion and **state the rule you applied**. |
| 5 | Write `BACKTEST.md`: the table, the DM verdict, the champion, and the conditions under which the champion loses. Commit. |

> This is the headline deliverable of the course. Everything before it produced a model;
> this lab produces the **evidence** that lets somebody decide whether to run it.
"""

STARTER6 = '''# ---------------------------------------------------------------------------
# The backtest you inherited
#
# The note attached to it read:
#   "60-origin rolling backtest, day-ahead. MASE 0.02. Ready for the report."
#
# It runs. It loops over sixty origins. It prints a MASE. One line in it makes
# every number it produces meaningless. Find that line before you write any code.
# ---------------------------------------------------------------------------
import lightgbm as lgb
from tayyar.eval.metrics import all_metrics

ok = X.notna().all(axis=1)
Xall, yall = X[ok], yy[ok]

# "train the model"
starter = lgb.LGBMRegressor(n_estimators=600, learning_rate=0.08, num_leaves=255,
                            min_child_samples=2, verbose=-1,
                            random_state=7).fit(Xall, yall)

# "roll the origin forward one day at a time and score the next 24 hours"
ORIGINS_STARTER = pd.date_range("2023-11-01 23:00", periods=60, freq="D",
                               tz="Asia/Riyadh")
rows = []
for o in ORIGINS_STARTER:
    pos = X.index.get_loc(o)
    block = X.iloc[pos + 1: pos + 25]              # the 24 hours being "forecast"
    actual = yy.iloc[pos + 1: pos + 25]
    hist = yy.iloc[pos - 24 * 365: pos]            # in-sample scale for MASE
    rows.append(all_metrics(actual, starter.predict(block), hist, 24))

starter_bt = pd.DataFrame(rows)
print(f"origins scored : {len(starter_bt)}")
print(starter_bt[["MAE", "RMSE", "MAPE_%", "MASE", "bias"]].mean().round(4).to_string())'''

L6_T2_INTRO = """### Task 2 — a rolling origin that is actually rolling

**Why one split is not evidence.** A single train/test split estimates skill from *one*
realisation of the future. It gives you a number with no standard error attached, and the
luck of which weeks landed in the test window is baked into it — a mild fortnight flatters
every model, a fortnight with two calendar shocks flatters the one that happens to lag.
Change the split date by two weeks and rankings flip. A backtest replaces that single number
with a **distribution of skill over many origins**: the mean tells you what to expect, the
spread tells you what to plan for, and the per-origin series tells you *when* you are exposed.

**Expanding vs sliding.**

| window | train set at origin t | use it when |
|---|---|---|
| **expanding** | everything from the start of history to t; grows at every origin | the regime is stable and more history is more signal |
| **sliding** | a fixed-length block ending at t; forgets the oldest data | the regime drifts — a new industrial load, a tariff change, a post-refurbishment plant |

Expanding is the default here: three years of Saudi grid demand is one regime plus growth.
A sliding window is the right answer the moment you can name the date the world changed.

**"Refit at each origin" is two different requirements, and only one is negotiable.**

1. **Correctness — not negotiable.** The training data must end **at or before the origin**.
   Nothing the model saw may come from after the hour you are pretending to stand at. Break
   this and you have the Task 1 leak.
2. **Cadence — a budget decision you must state.** How often you re-estimate between
   origins. Refitting the 24-model direct forecaster at all 60 origins is 1,440 LightGBM
   fits, roughly an hour of CPU on a laptop, and three families make it three hours.

So we do both, honestly. The 60-origin table below uses models estimated **once at the
30 September boundary** — a monthly retrain cadence, with training data ending a full month
before the first origin and never after any origin — and then we **measure the cadence
choice** by refitting at every origin for six of the sixty and comparing. Say which of the
two you ran, every time you publish a backtest. Most published "rolling backtests" are the
periodic-retrain kind and do not admit it."""

L6_T2_SOL_A = '''from tayyar.eval.backtest import BacktestConfig, origins

cfg = BacktestConfig(horizon=24, n_origins=60, step=24,
                     initial_train=24 * 365,      # one year before the first origin
                     window="expanding", m=24)

folds = list(origins(y.index, cfg))
ORIGINS = [y.index[tr.stop - 1] for tr, te in folds]   # the last hour we may observe

print(f"origins produced : {len(folds)}   (the report needs at least 50)")
print(f"first origin     : {ORIGINS[0]}")
print(f"last origin      : {ORIGINS[-1]}")
print(f"step             : {(ORIGINS[1] - ORIGINS[0])}   horizon: {cfg.horizon} h")
print()
for k in (0, 1, 59):
    tr, te = folds[k]
    print(f"fold {k:2d}  train {y.index[tr.start]:%Y-%m-%d %H:%M} -> "
          f"{y.index[tr.stop - 1]:%Y-%m-%d %H:%M}  ({tr.stop - tr.start:6,d} h)"
          f"   test {y.index[te.start]:%Y-%m-%d %H:%M} -> {y.index[te.stop - 1]:%Y-%m-%d %H:%M}")

sl = list(origins(y.index, BacktestConfig(horizon=24, n_origins=60, step=24,
                                          initial_train=24 * 365, window="sliding")))
print()
print("expanding: train start position at folds 0 and 59 ->",
      folds[0][0].start, folds[59][0].start, "(never moves — all history is kept)")
print("sliding  : train start position at folds 0 and 59 ->",
      sl[0][0].start, sl[59][0].start, "(moves with the origin — old data is forgotten)")'''

L6_T2_SOL_B = '''from tayyar.models.lgbm_forecaster import DirectLGBMForecaster
from tayyar.models.quantile import QuantileLGBM

Xtr = X[:CUT_TRAIN].dropna(); ytr = yy[Xtr.index]
print(f"training window ends {Xtr.index.max():%Y-%m-%d %H:%M}, "
      f"{(ORIGINS[0] - Xtr.index.max()).days} days before the first origin — "
      f"nothing after any origin enters any fit.")

lgbm = DirectLGBMForecaster(horizon=24).fit(Xtr, ytr)            # 24 models, ~1 min
qm = QuantileLGBM(quantiles=(0.05, 0.50, 0.95), horizon=24).fit(Xtr, ytr)  # 72 models, ~3 min
print(f"fitted {len(lgbm.models_)} direct models and {len(qm.models_)} quantile models")'''

L6_T2_SOL_C = '''def backtest(predict_fn, name, origs=None):
    """One row of metrics per origin, plus the raw actual/prediction pairs for DM."""
    rows, per = [], []
    for o in (origs or ORIGINS):
        pos = X.index.get_loc(o)
        Xo = X.iloc[[pos]]                              # the one feature row we may use
        actual = yy.iloc[pos + 1: pos + 25]             # the 24 hours that follow
        if len(actual) < cfg.horizon or Xo.isna().any().any():
            continue
        f = np.asarray(predict_fn(Xo, pos), dtype=float)
        hist = yy.iloc[pos - cfg.initial_train: pos]    # the one-year in-sample MASE scale
        rows.append({"origin": o, "model": name, **all_metrics(actual, f, hist, cfg.m)})
        per.append({"origin": o, "actual": actual.to_numpy(), "pred": f})
    return pd.DataFrame(rows), per


f_lgbm = lambda Xo, pos: [lgbm.models_[h].predict(Xo)[0] for h in range(1, 25)]
f_q50 = lambda Xo, pos: [qm.models_[(h, 0.50)].predict(Xo)[0] for h in range(1, 25)]

def f_naive(Xo, pos):                                   # tomorrow = the last 24 hours
    last = yy.iloc[pos - 23: pos + 1].to_numpy()
    return [last[h % 24] for h in range(24)]

bt_l, per_l = backtest(f_lgbm,  "LightGBM (direct)")
bt_q, per_q = backtest(f_q50,   "LightGBM (quantile q50)")
bt_s, per_s = backtest(f_naive, "Seasonal-naive")
bt = pd.concat([bt_l, bt_q, bt_s], ignore_index=True)

print(f"{bt.groupby('model').size().min()} origins x 3 model families, "
      f"{bt.groupby('model').size().min() * cfg.horizon:,} forecast hours each")
print(bt.head(3).to_string(index=False))'''

L6_T2_SOL_D = '''import time

def refit_at(origin):
    """The strict version: expanding window, training data ending AT the origin."""
    Xt = X[:origin].dropna()
    return DirectLGBMForecaster(horizon=24).fit(Xt, yy[Xt.index])
    # DirectLGBMForecaster targets y.shift(-h); truncating y at the origin makes the
    # last h rows NaN and they are dropped, so no target after the origin is ever used.

CADENCE_ORIGINS = ORIGINS[::10]                    # six of the sixty
rows = []
t0 = time.time()
for o in CADENCE_ORIGINS:
    pos = X.index.get_loc(o); Xo = X.iloc[[pos]]
    actual = yy.iloc[pos + 1: pos + 25]
    hist = yy.iloc[pos - cfg.initial_train: pos]
    fixed = np.array([lgbm.models_[h].predict(Xo)[0] for h in range(1, 25)])
    m = refit_at(o)
    refit = np.array([m.models_[h].predict(Xo)[0] for h in range(1, 25)])
    rows.append({"origin": o,
                 "days_stale": (o - Xtr.index.max()).days,
                 "MASE_monthly_refit": all_metrics(actual, fixed, hist, 24)["MASE"],
                 "MASE_refit_at_origin": all_metrics(actual, refit, hist, 24)["MASE"]})

cad = pd.DataFrame(rows)
print(cad.to_string(index=False))
print(f"\\nmean MASE, monthly cadence   : {cad.MASE_monthly_refit.mean():.4f}")
print(f"mean MASE, refit at origin   : {cad.MASE_refit_at_origin.mean():.4f}")
print(f"six refits cost {time.time() - t0:,.0f} s; sixty would cost "
      f"{(time.time() - t0) * 10 / 60:,.0f} min for this family alone.")'''

L6_T3_INTRO = """### Task 3 — the comparison table, and the failure mode of every column in it

| metric | what it is | what it is good for | how it fails |
|---|---|---|---|
| **MAE** | mean absolute error | same units as the series; robust to outliers; the number an engineer can act on | not comparable across series of different scale |
| **RMSE** | root mean squared error | penalises large misses, which is right when the cost is convex | dominated by a handful of outliers; a single bad hour rewrites the ranking |
| **MAPE** | mean absolute percentage error | scale-free and immediately intuitive | explodes as the denominator approaches zero, and is asymmetric — an over-forecast is capped at 100% while an under-forecast is unbounded, so it quietly prefers models that under-predict |
| **sMAPE** | symmetric MAPE | bounded, so it cannot explode to 4,000% | still unstable near zero, and "symmetric" is a misnomer — it is not symmetric in the errors |
| **MASE** | MAE / MAE of the **in-sample seasonal-naive** | scale-free, symmetric, defined at zero, comparable across series | needs a sensible seasonal period `m`, and the denominator is a modelling choice you must state |

**MASE < 1 means you beat the free baseline.** MASE > 1 means you should have shipped the
baseline and gone home. It is the only column in this table that is simultaneously scale-free
and safe near zero, which is why it is the column the champion is chosen on.

Report the **spread**, not only the mean. The mean is what the model does on an average day;
the maximum is what the control room lives through on the worst one."""

L6_T4_INTRO = """### Task 4 — scoring the interval, not just the point

A point forecast is scored by how far it lands from the truth. A **quantile** forecast has to
be scored by something that knows which quantile it claims to be — that is pinball loss,
asymmetric on purpose: at τ = 0.95 an under-prediction is penalised nineteen times more than
an over-prediction, and its minimiser is the 95th percentile.

Two numbers, and you need both:

- **mean pinball loss** — sharpness and calibration together, averaged over the quantile grid.
  Lower is better; it is a proper score, so it cannot be gamed by widening the band.
- **empirical coverage** — the fraction of hours the interval actually contained the truth.
  Coverage is the constraint; pinball is the objective. An interval that covers 100% by being
  20,000 MW wide scores badly on pinball and is useless in a control room."""

L6_T5_INTRO = """### Task 5 — Diebold-Mariano: is the gap real?

The two LightGBM variants differ by about 16 MW of MAE on a 30,000 MW system. Before anybody
ships the marginally better one, answer the only question that matters: **could that gap be
noise?**

Diebold-Mariano tests **H0: the two forecasts have equal expected loss**, using the
*loss-differential series* `d_t = |e1_t| - |e2_t|`. It is a test on a series, so it accounts
for the autocorrelation the 24-hour horizon induces (Newey-West, with the Harvey-Leybourne-
Newbold small-sample correction). A significant negative statistic says model 1 is genuinely
better; a non-significant one says **you cannot distinguish them, so ship the simpler or
cheaper model**.

That last sentence is the promotion rule. Statistical significance **gates** added complexity:
a sub-1% "win" that fails DM does not justify a second model in production, a second thing to
monitor, and a second thing to wake somebody at 02:00."""

QUIZ6_Q = """### Mini-quiz

Answer these in your pair before you look at the next cell.

1. Why is a single train/test split not decision-grade evidence?
2. Expanding or sliding — which one forgets old data?
3. What does MASE < 1 mean?
4. Why does MAPE fail near zero?
5. What does a non-significant Diebold-Mariano result tell you to do?
"""

QUIZ6_A = """### Mini-quiz — answers

1. **Why is a single split not evidence?** It is a sample of one. You get a point estimate of
   skill with no spread attached, and the ranking can flip on the luck of which weeks fell in
   the test window. A backtest gives you a distribution of skill instead of a single draw
   from it.
2. **Which forgets old data?** **Sliding.** Its training window is a fixed length ending at
   the origin, so the oldest hours fall out as the origin advances. Expanding keeps
   everything. Sliding is the right choice when the regime has drifted; expanding when it
   has not.
3. **What does MASE < 1 mean?** The model beats the seasonal-naive baseline — it makes less
   error than copying the last 24 hours forward. MASE > 1 means the free baseline was better
   and you should ship that.
4. **Why does MAPE fail near zero?** Its denominator is the actual value. As demand
   approaches zero the percentage explodes — a 40 MW miss on a 60 MW hour is 67%, and on an
   embedded-generation hour that nets to 5 MW it is 800%. It is also asymmetric: over-forecasts
   are capped at 100% and under-forecasts are unbounded, so it quietly prefers models that
   under-predict. Use MASE.
5. **What does a non-significant DM tell you to do?** Pick the **simpler or cheaper** model —
   the gap is noise, and you cannot buy accuracy you cannot demonstrate. Significance is the
   gate that added complexity has to pass.
"""

COMMIT6 = """### Task 6 — `BACKTEST.md` and commit

The report is the deliverable, not the notebook. Five short sections, in this order:

1. **The design.** Expanding window, one-year initial window, step 24 h, horizon 24 h, 60
   origins from 2023-11-01 to 2023-12-30, training data ending at the 30 September boundary
   (monthly retrain cadence — say so), MASE denominator = in-sample seasonal-naive over the
   preceding year.
2. **The table**, mean and spread, every model relative to the seasonal-naive baseline.

```
model                      MAE  MAPE_%   MASE   MASE sd   vs baseline
LightGBM (direct)        719.1   2.328  0.445     0.196      -42.2%
LightGBM (quantile q50)  735.4   2.381  0.455     0.203      -40.9%
Seasonal-naive          1244.0   4.117  0.770     0.474           --
```

3. **The DM verdict.** LightGBM vs seasonal-naive: dm = -6.75, p = 0.000, significant.
   LightGBM vs quantile q50: dm = -1.901, p = 0.0575, **not** significant at 5%.
4. **The champion and the rule.** The quantile q50 model, because it is statistically
   indistinguishable from the direct model on accuracy and it also produces the interval the
   reserve decision consumes. State the rule: *among models that are not
   DM-distinguishable, take the one that is simpler, cheaper, or more useful downstream.*
5. **The conditions under which the champion loses**, named as dates and regimes, plus the
   regimes this backtest window contains **no** evidence about.

```
git add -A && git commit -m "feat(eval): 60-origin rolling backtest, DM significance test and champion selection"
```"""


CADENCE_INTERP = """**Expected**

```
                   origin  days_stale  MASE_monthly_refit  MASE_refit_at_origin
2023-11-01 23:00:00+03:00          32              0.5159                0.3844
2023-11-11 23:00:00+03:00          42              0.5090                0.4206
2023-11-21 23:00:00+03:00          52              0.4951                0.5281
2023-12-01 23:00:00+03:00          62              0.3125                0.3360
2023-12-11 23:00:00+03:00          72              0.4015                0.4393
2023-12-21 23:00:00+03:00          82              0.3932                0.2884

mean MASE, monthly cadence   : 0.4379
mean MASE, refit at origin   : 0.3995
```

**Refitting at every origin is worth about 0.04 of MASE here — and it is not worth it on
three of the six origins.** It wins clearly at the start of the window, where the fixed model
is only a month stale, loses in the middle, and wins again at the end. That shape is what a
stable regime looks like: the value of a refit is real but small and noisy, because there is
no drift for the fresh data to correct.

Two conclusions, and they are different in kind.

**Correctness.** Nothing here is a leak. Every fit in both columns used training data ending
at or before its origin. Contrast Task 1, where the fit consumed the origins themselves: that
was not a cadence choice, it was a wrong answer.

**Cost.** Six refits took the time you just watched; sixty would take ten times that, for one
family. The published table below therefore uses the monthly cadence, which on this evidence
makes the champion look **slightly worse** than a refit-at-every-origin system would — an
error in the conservative direction, which is the only direction an error in a backtest is
allowed to point. State the cadence next to the table and the reader can judge it.

In production the cadence is a monitoring decision, not a research one, and it belongs in the
retrain clause of Lab 7's decision record: refit weekly, plus on any drift threshold breach."""


EID_INTERP = """**Expected**

```
the champion's six worst origins
       day weekday  t_max_C    MAE  MAPE_%   MASE  MASE_naive
2023-11-06     Mon     33.0 2014.6   5.406 1.2590      1.2525
2023-11-04     Sat     32.1 1458.1   4.239 0.9111      0.9274
2023-11-30     Thu     29.5 1469.8   4.330 0.9103      0.8613
2023-11-11     Sat     32.5 1332.8   4.071 0.8293      1.2754
2023-11-10     Fri     24.5 1305.2   4.145 0.8123      1.9256
2023-11-15     Wed     25.7 1236.3   4.065 0.7670      0.6596

origins with MASE > 1 (worse than the free baseline's own scale): 1 of 60
```

**Five of the six worst days fall in the first half of November, and the worst of them is
Monday 6 November at 33.0 °C** — an out-of-season warm spell that pushed the daily peak to
42,963 MW, well clear of the days on either side. The baseline scored 1.2525 on that same day,
so it was a hard day for every method that extrapolates from recent history: the level moved
and they all followed it late. Contrast 10 November, where the model scored 0.8123 against the
baseline's 1.9256 — that one was a genuine model win, on a day copying yesterday had no chance.

The pattern worth naming is temperature, not the calendar: in this window the hard days are the
warm ones. Which raises the question the table cannot answer at all.

```
forecast_day day_name  is_eid     MAE  MAPE_%   MASE
  2023-04-21      Fri    True  2093.0   7.601 1.3497
  2023-04-22      Sat    True  1070.9   3.544 0.6855
  2023-04-23      Sun    True   939.5   2.877 0.6017
  2023-04-24      Mon    True   938.9   2.965 0.6001
  2023-04-25      Tue   False  3319.5   8.957 2.1247
  2023-04-26      Wed   False  1408.8   4.093 0.8991
  2023-04-27      Thu   False  1109.2   3.122 0.7073
  2023-04-28      Fri   False   780.8   2.391 0.4979
  2023-04-29      Sat   False  1211.2   3.707 0.7710
```

**Across those nine days the champion's mean MASE is 0.92 — roughly double its 0.445 over the
November-December origins — and on two of the nine it is above 1, worse than the free
baseline.** Compare that with one origin in sixty in the backtest window.

Look at *which* two days fail. Not the middle of Eid, which the model handles at MASE 0.60:
it has seen two previous Eids and the calendar flag tells it one is happening. The failures are
the **transitions** — 21 April, the first day of the holiday, where consumption collapses out
of the Ramadan pattern, and 25 April, the first working day back, which is the single worst day
in the window at MASE 2.12. Regime *changes* are what break a model that learns levels from
recent lags; regime *states* it can be told about.

Two honest caveats, both of which belong in the report. This model is up to ten days stale by
the end of the probe, which flatters neither column. And the MASE denominators differ between
April and November because each origin divides by its own preceding year, so treat the factor
of two as an order of magnitude, not a measurement.

**The finding for `BACKTEST.md` is the one the main table cannot state:** the 60-origin window
runs from 1 November to 30 December 2023. It contains **no Eid** (`df["is_eid"]` sums to zero
across it), a maximum temperature of 33.8 °C against July's 49.5 °C, and no record peak. The
backtest is therefore silent about the three regimes most likely to hurt — calendar
transitions, extreme heat, and extrapolation beyond the training range — and silence is not
evidence of safety. Write that sentence into the report next to the table, not in a footnote,
and carry it into Lab 7 as the weakness clause of the brief and the trigger list of the
monitoring contract."""


STARTER7_STUB = '''# The backtest table Lab 6 produced, loaded from the committed reference run so that
# the inherited selection step below runs before you have finished rebuilding it.
# Replace it with YOUR pipeline\'s output as soon as Task 1 prints MATCH.
import json

MET = ["MAE", "RMSE", "MAPE_%", "WAPE_%", "MASE", "bias"]
bt = pd.DataFrame(json.load(open("../reference_results.json"))["m6"]["summary"])
summary = bt.set_index("model")[MET].sort_values("MASE")'''


def lab6(sol: bool):
    tag = "solution" if sol else "start"
    c = [md(HDR.format(n=6, title="The Rolling-Origin Backtest Report", dur=50, tag=tag)),
         md(L6_TASKS), code(SETUP), code(LOAD67)]

    # ---------------------------------------------------------------- task 1 --
    c.append(md("""### Task 1 — the backtest you inherited

Run the next cell. It loops over sixty origins, it forecasts twenty-four hours at each, and
it reports a MASE of 0.017 — the model makes under two per cent of the error of the free
seasonal-naive baseline.

Nobody in this industry has a day-ahead load model with a MASE of 0.017.

Five minutes: find the line, and write it into `BACKTEST.md`. Do not fix it yet."""))
    c.append(code(STARTER6))

    if sol:
        c.append(md("""**The leak: the model was fitted once, on the whole file, including the sixty days
it is then scored on.** `starter.fit(Xall, yall)` runs before the loop and consumes every row
in the dataset. The loop that follows looks like a rolling origin — it advances a day at a
time, it slices the next 24 hours, it computes honest metrics — but every one of those 1,440
hours was in the training set. It is measuring how well a 600-tree, 255-leaf model memorised
its own training data, and reporting the answer as forecast skill.

The tell is the number itself. **MASE 0.017 is not an excellent model, it is a broken
evaluation**, and the same is true of MAPE 0.096% on a grid. Any time a backtest reports skill
an order of magnitude better than the published state of the art for the problem, the
evaluation is wrong before the model is right — check the scoring before you celebrate.

Note what is *not* wrong here. The features are the leakage-safe Lab 4 matrix. The metrics
function is correct. The origin schedule is correct. A single line of ordering — fitting
before the loop rather than inside it, on all the data rather than on the past — is enough,
and it leaves no trace anywhere else in the code."""))
        c.append(code('''# Proof — every hour scored was an hour the model was fitted on.
scored = pd.DatetimeIndex(np.concatenate(
    [X.index[X.index.get_loc(o) + 1: X.index.get_loc(o) + 25] for o in ORIGINS_STARTER]))
inside = len(scored.intersection(Xall.index))
print(f"hours scored by the inherited backtest : {len(scored):,}")
print(f"of those, hours inside its training set: {inside:,}  ({inside / len(scored):.0%})")
print(f"last training hour                     : {Xall.index.max():%Y-%m-%d %H:%M}")
print(f"last hour it claims to forecast        : {scored.max():%Y-%m-%d %H:%M}")
print()

# The same model, scored on hours it genuinely never saw: refit on data ending
# 30 September and score the same sixty origins.
honest = lgb.LGBMRegressor(n_estimators=600, learning_rate=0.08, num_leaves=255,
                           min_child_samples=2, verbose=-1, random_state=7)
Xh = X[:CUT_TRAIN].dropna()
honest.fit(Xh, yy[Xh.index])
rows = []
for o in ORIGINS_STARTER:
    pos = X.index.get_loc(o)
    rows.append(all_metrics(yy.iloc[pos + 1: pos + 25],
                            honest.predict(X.iloc[pos + 1: pos + 25]),
                            yy.iloc[pos - 24 * 365: pos], 24))
h = pd.DataFrame(rows).mean()
print(f"{'':32s}{'MASE':>8s}{'MAPE_%':>9s}{'MAE':>10s}")
print(f"{'fitted on everything (in-sample)':32s}{starter_bt.MASE.mean():8.4f}"
      f"{starter_bt['MAPE_%'].mean():9.3f}{starter_bt.MAE.mean():10.1f}")
print(f"{'same model, unseen hours':32s}{h.MASE:8.4f}{h['MAPE_%']:9.3f}{h.MAE:10.1f}")
print()
print(f"A factor of {h.MASE / starter_bt.MASE.mean():.0f} in MASE, "
      f"from one line of ordering.")'''))
        c.append(md("""The honest version of the same model is still optimistic — it is reading the *actual*
lag-1, lag-2 and lag-3 demand of the hours it is forecasting, because the loop feeds it the
feature rows of the horizon window itself. That is a second, separate defect and Task 2 fixes
it by predicting all 24 hours from the single feature row available at the origin. The point
of this cell is narrower and worth keeping clean: **one line of ordering moved the reported
MASE by a factor of twenty, and nothing else in the code changed.**

**`BACKTEST.md`, section 1**

```
## The leak in the inherited backtest (labs/lab6)

Fit-once on the whole file. `starter.fit(Xall, yall)` runs BEFORE the origin loop
and includes every hour the loop then scores: 1,440 of 1,440 scored hours are
training rows. The reported MASE of 0.017 is in-sample memorisation, not skill.
The same model scored on hours it never saw reports MASE 0.224 — a factor of 13.

Fix: the training data must end at or before the origin. Fit inside the loop
(refit at each origin), or fit once on a window that ends before the FIRST origin
and say which of the two you did.

Tell: a MASE near zero. No day-ahead load model has one. When a backtest reports
skill an order of magnitude better than the published state of the art, the
evaluation is wrong before the model is right.
```"""))
    else:
        c.append(code('''# TODO (5 min) — do not change the cell above yet.
#
# The MASE is 0.017. Before you look for a bug, look for the reason it CANNOT be real:
# what does MASE = 0.017 claim, in words, about this model versus copying yesterday?
#
#   1. Collect every hour the loop scores:
#        X.index[pos+1 : pos+25] for every origin
#      How many are there? How many of them are in the index the model was fitted on?
#
#   2. Print the last hour of the training data and the last hour the backtest claims
#      to forecast. Which is later?
#
#   3. Refit the SAME model on data ending at CUT_TRAIN, score the same sixty origins,
#      and put the two MASE numbers side by side.
#
# Write it up in BACKTEST.md: the line, the mechanism, the two numbers. Do not fix it.
#
# HINT: a backtest is a claim about what you knew at a moment in time. Read the cell
#       above in that light and ask, at the line that fits the model, what time it is.'''))

    # ---------------------------------------------------------------- task 2 --
    c.append(md(L6_T2_INTRO))
    if sol:
        c.append(code(L6_T2_SOL_A))
        c.append(md("""Sixty origins, one per day, 2023-11-01 23:00 to 2023-12-30 23:00. Each fold's train
slice ends at the origin hour, and its test slice is the twenty-four hours that follow — the
day-ahead run issued at 23:00 for tomorrow, which is the operational shape of this forecast.

The expanding/sliding contrast is the last two lines: the expanding window's training block
always starts at position 0, so the fold at the end of the year carries every hour of history;
the sliding window's start position moves with the origin, so the same fold has forgotten the
oldest 1,416 hours. Nothing in the code changes except `window=`; everything about what the
model is allowed to remember does."""))
        c.append(code(L6_T2_SOL_B))
        c.append(code(L6_T2_SOL_C))
        c.append(md("""Three families, deliberately chosen to span the trade-off space rather than to fill a
table: the **seasonal-naive** baseline that costs nothing and must be beaten; the **Lab 4
direct LightGBM**, the accuracy candidate; and the **Lab 5 quantile model's median**, which
is a point forecast that arrives with an interval attached. Every one of them is scored at the
same sixty origins on the same 1,440 hours, which is what makes the Diebold-Mariano test in
Task 5 legitimate — the loss differentials are paired.

Now the cadence measurement: refit at the origin, properly, for six of the sixty."""))
        c.append(code(L6_T2_SOL_D))
        c.append(md(CADENCE_INTERP))
    else:
        c.append(code('''from tayyar.eval.backtest import BacktestConfig, origins
from tayyar.models.lgbm_forecaster import DirectLGBMForecaster
from tayyar.models.quantile import QuantileLGBM

# TODO (12 min)
#
#   1. cfg = BacktestConfig(horizon=24, n_origins=60, step=24,
#                           initial_train=24*365, window="expanding", m=24)
#      folds = list(origins(y.index, cfg))
#      ORIGINS = [y.index[tr.stop - 1] for tr, te in folds]
#      Print len(folds) — the report needs at least 50 — and the first/last origin.
#      Print fold 0 and fold 59 for window="expanding" and again for "sliding".
#      Which one moves its train START position, and what does that mean?
#
#   2. Fit the candidates on data ending at CUT_TRAIN (30 September), a month before
#      the first origin:
#        lgbm = DirectLGBMForecaster(horizon=24).fit(Xtr, ytr)          # ~1 min
#        qm   = QuantileLGBM((0.05, 0.50, 0.95), horizon=24).fit(...)   # ~3 min
#      Start them, then read the next markdown cell while they run.
#
#   3. backtest(predict_fn, name) -> one metrics row per origin. At each origin:
#        Xo     = X.iloc[[pos]]                  ONE feature row — the origin's
#        actual = yy.iloc[pos+1 : pos+25]
#        hist   = yy.iloc[pos - cfg.initial_train : pos]     the MASE scale
#      Run it for all three families: LightGBM direct, quantile q50, seasonal-naive.
#      Keep the raw (actual, pred) arrays per origin — Task 5 needs them.
#
#   4. Then measure the CADENCE choice: for six origins, refit the direct model with
#      training data ending AT the origin and compare its MASE with the fixed fit.
#      Time it, and report what sixty refits would have cost.
#
# HINT: the forecast for hour t+7 must come from the feature row at the ORIGIN, not
#       from the feature row at t+7 — that row contains the lag-1 demand of t+6, which
#       nobody has at 23:00. If your MAPE comes out near 1%, that is what happened.''')) 

    # ---------------------------------------------------------------- task 3 --
    c.append(md(L6_T3_INTRO))
    if sol:
        c.append(code('''MET = ["MAE", "RMSE", "MAPE_%", "WAPE_%", "MASE", "bias"]
summary = bt.groupby("model")[MET].mean().round(3).sort_values("MASE")
print("mean over the 60 origins")
print(summary.to_string())

spread = bt.groupby("model")[["MAE", "MAPE_%", "MASE"]].agg(["mean", "std", "min", "max"]).round(3)
print("\\nspread over the 60 origins")
print(spread.to_string())'''))
        c.append(code('''base = summary.loc["Seasonal-naive"]
rel = pd.DataFrame({
    "MAE": summary.MAE.round(1),
    "MASE": summary.MASE,
    "MASE sd": bt.groupby("model").MASE.std().round(3),
    "MASE worst origin": bt.groupby("model").MASE.max().round(3),
    "MAE vs baseline": (summary.MAE / base.MAE - 1).map("{:+.1%}".format),
    "origins worse than baseline":
        [int((bt_l.MASE.to_numpy() > bt_s.MASE.to_numpy()).sum()) if m == "LightGBM (direct)"
         else int((bt_q.MASE.to_numpy() > bt_s.MASE.to_numpy()).sum()) if m.endswith("q50)")
         else 0 for m in summary.index],
}).loc[summary.index]
print(rel.to_string())'''))
        c.append(code('''fig, ax = plt.subplots(1, 2, figsize=(11.5, 4), gridspec_kw={"width_ratios": [1.75, 1]})
for n, g in bt.groupby("model"):
    ax[0].plot(g.origin, g.MASE, marker="o", ms=2.6, lw=.9, label=n)
ax[0].axhline(1.0, color="#C00000", ls="--", lw=1)
ax[0].text(bt.origin.iloc[1], 1.04, "MASE = 1 — the free seasonal-naive baseline",
           color="#C00000", fontsize=7.5)
ax[0].set_ylabel("MASE"); ax[0].tick_params(axis="x", rotation=20)
ax[0].set_title(f"Per-origin MASE over {len(bt_l)} rolling origins")
ax[0].legend(frameon=False, fontsize=7.5)

ax[1].boxplot([bt_l.MASE, bt_q.MASE, bt_s.MASE], tick_labels=["LGBM", "q50", "naive"],
              widths=.55)
ax[1].axhline(1.0, color="#C00000", ls="--", lw=1)
ax[1].set_title("The distribution is the result"); ax[1].set_ylabel("MASE")
plt.tight_layout()'''))
        c.append(md("""**Expected**

```
mean over the 60 origins
                              MAE      RMSE  MAPE_%  WAPE_%   MASE    bias
LightGBM (direct)         719.075   904.303   2.328   2.385  0.445 -14.060
LightGBM (quantile q50)   735.373   920.578   2.381   2.440  0.455   5.340
Seasonal-naive           1244.025  1464.803   4.117   4.189  0.770  74.795
```

**Know your denominator.** The seasonal-naive baseline scores **MASE 0.770, not 1.000**, and
a room that does not stop here will misread the whole table. MASE divides by the MAE of the
seasonal-naive forecast computed **in-sample over the preceding year** — a year that contains
the Saudi summer, when the daily swing is three times the winter swing and hour-to-hour
changes are far larger. These origins fall in November and December. The baseline is therefore
being compared against a denominator built in a harder season than the one it is forecasting,
and it comes out below 1. Nothing is broken; the denominator is doing exactly what it is
defined to do. But **a MASE is only interpretable next to the denominator it used**, so state
it: *in-sample seasonal-naive, m = 24, over the 8,760 hours preceding each origin.*

Because of that, also report a **relative** measure that has no denominator to misread:
**the direct LightGBM's MAE is 42.2% below the seasonal-naive's** (719.1 MW against
1,244.0 MW), and the quantile median's is 40.9% below. Those two sentences travel to a
non-technical reader without a footnote.

**Now read the spread, which is the reason we ran sixty origins.** The champion's mean MASE
is 0.445 with a standard deviation of 0.196, a best origin of 0.235 and a worst of **1.259** —
one day in sixty on which the model was *worse than copying yesterday*, and twelve days in
sixty on which the seasonal-naive had the lower error of the two. That is what a p < 0.001 win
looks like at the level of individual days, and a single split reporting "MASE 0.445" hides it
entirely. The baseline's spread is worse again (sd 0.474,
worst 2.047), which is the real argument for the model: it is not only better on average, it
is far more predictable, and predictable error is what a reserve margin is sized against."""))
    else:
        c.append(code('''# TODO (10 min)
#
#   1. summary = bt.groupby("model")[MET].mean().round(3).sort_values("MASE")
#      with MET = ["MAE","RMSE","MAPE_%","WAPE_%","MASE","bias"]
#   2. The SPREAD is not optional: .agg(["mean","std","min","max"]) on MAE, MAPE_%, MASE.
#   3. Report every model RELATIVE to the seasonal-naive baseline:
#        - MAE as a percentage of the baseline's MAE
#        - how many of the 60 origins the model was worse than the baseline on
#   4. Plot per-origin MASE for all three families, with a line at MASE = 1, and a
#      boxplot of the three distributions beside it.
#
#   Then answer in BACKTEST.md, in one sentence each:
#     - the seasonal-naive baseline scores MASE 0.77, not 1.00. Why?
#     - what is the champion's WORST origin, and what would that day have cost?
#
# HINT: MASE divides by the in-sample seasonal-naive MAE over the preceding YEAR.
#       Which season dominates that year, and which season are these origins in?''')) 

    # ---------------------------------------------------------------- task 4 --
    c.append(md(L6_T4_INTRO))
    if sol:
        c.append(code('''from tayyar.eval.pinball import pinball_loss, coverage
from tayyar.models.conformal import CQR

TAUS = (0.05, 0.50, 0.95)
P = {t: np.array([[qm.models_[(h, t)].predict(X.iloc[[X.index.get_loc(o)]])[0]
                   for h in range(1, 25)] for o in ORIGINS]) for t in TAUS}
Y = np.array([yy.iloc[X.index.get_loc(o) + 1: X.index.get_loc(o) + 25].to_numpy()
              for o in ORIGINS])

# Calibrate on October — held out, adjacent in regime, disjoint from every origin.
Xca, yca = X[CUT_TRAIN:CUT_CAL], yy[CUT_TRAIN:CUT_CAL]
rows_ca = list(range(0, len(Xca) - 24, 24))
Yca = np.array([yca.iloc[i + 1: i + 25].to_numpy() for i in rows_ca])
Pca = {t: np.column_stack([qm.models_[(h, t)].predict(Xca.iloc[rows_ca])
                           for h in range(1, 25)]) for t in (0.05, 0.95)}
cqr = CQR(alpha=0.10).calibrate(Yca.ravel(), Pca[0.05].ravel(), Pca[0.95].ravel())
lo_c, hi_c = cqr.interval(P[0.05], P[0.95])

print(f"{'':28s}{'coverage':>10s}{'mean width':>13s}")
print(f"{'raw quantile band':28s}"
      f"{coverage(Y.ravel(), P[0.05].ravel(), P[0.95].ravel()):10.4f}"
      f"{np.mean(P[0.95] - P[0.05]):12,.1f} MW")
print(f"{'after CQR (q-hat ' + format(cqr.qhat_, ',.1f') + ')':28s}"
      f"{coverage(Y.ravel(), lo_c.ravel(), hi_c.ravel()):10.4f}"
      f"{np.mean(hi_c - lo_c):12,.1f} MW")
print(f"{'nominal':28s}{0.90:10.4f}")'''))
        c.append(code('''pin = {t: pinball_loss(Y.ravel(), P[t].ravel(), t) for t in TAUS}
print("pinball loss by quantile (MW)")
for t, v in pin.items():
    print(f"   tau = {t:.2f} : {v:7.1f}")
print(f"   mean over the grid : {np.mean(list(pin.values())):7.1f}")

per_pin = np.array([np.mean([pinball_loss(Y[i], P[t][i], t) for t in TAUS])
                    for i in range(len(Y))])
per_cov = np.array([coverage(Y[i], lo_c[i], hi_c[i]) for i in range(len(Y))])
print(f"\\nacross the {len(Y)} origins")
print(f"   mean pinball : mean {per_pin.mean():6.1f}   sd {per_pin.std():6.1f}"
      f"   min {per_pin.min():6.1f}   max {per_pin.max():6.1f}")
print(f"   coverage     : mean {per_cov.mean():6.3f}   min {per_cov.min():6.3f}"
      f"   max {per_cov.max():6.3f}")
print(f"   origins with coverage below 0.80 : {int((per_cov < 0.80).sum())} of {len(Y)}")

fig, ax = plt.subplots(1, 2, figsize=(11.5, 3.6))
ax[0].plot(ORIGINS, per_cov, marker="o", ms=3, lw=.9, color="#1F3864")
ax[0].axhline(0.90, color="#C00000", ls="--", lw=1)
ax[0].set_ylabel("coverage"); ax[0].set_title("Per-origin coverage of the calibrated 90% band")
ax[0].tick_params(axis="x", rotation=20)
ax[1].plot(ORIGINS, per_pin, marker="o", ms=3, lw=.9, color="#2E7D32")
ax[1].set_ylabel("mean pinball (MW)"); ax[1].set_title("Per-origin mean pinball loss")
ax[1].tick_params(axis="x", rotation=20)
plt.tight_layout()'''))
        c.append(md("""**Expected**

```
raw quantile band             0.7826      2,396.4 MW
after CQR (q-hat 408.5)       0.9000      3,213.5 MW
nominal                       0.9000

pinball  tau = 0.05 :    99.7      tau = 0.50 :   367.7      tau = 0.95 :   136.7
         mean over the grid : 201.4
```

The raw band under-covers at **0.783** against a nominal 0.900, exactly as it did in Lab 5;
conformal calibration on the held-out October window buys the missing 12 points of coverage
for 817 MW of extra width. That trade is the whole content of the interval: coverage is the
constraint, width is the price, and both go in the report.

The per-origin view is the part a single marginal number cannot give you. Mean coverage is
0.900 — nominal, and it would pass any audit — while **13 of the 60 origins covered less than
80% of their hours**, and the worst covered 45.8%. Marginal coverage is an average over days,
and an average over days is cold comfort on the day you are short. Mean pinball loss behaves
the same way: 201.4 MW on average, 630.4 MW on the worst origin, a factor of six between the
easy days and the hard one.

Pinball is the score that lets you compare two interval methods without arguing, because it
cannot be gamed: widening the band to force coverage up drives pinball up too."""))
    else:
        c.append(code('''from tayyar.eval.pinball import pinball_loss, coverage
from tayyar.models.conformal import CQR

# TODO (8 min)
#
#   1. Predict all three quantiles at each of the 60 origins:
#        P[tau] -> array (n_origins, 24);  Y -> the matching actuals
#   2. Calibrate CQR on OCTOBER (X[CUT_TRAIN:CUT_CAL]) — held out and adjacent in
#      regime, disjoint from every origin — and apply q-hat to the band.
#   3. Report coverage and mean width, raw and calibrated, against the nominal 0.90.
#   4. pinball_loss at each tau and the MEAN over the grid.
#   5. Then the same two quantities PER ORIGIN: mean, sd, min, max, and how many
#      origins covered less than 0.80. Plot both series against the origin date.
#
# HINT: the marginal coverage will land on 0.90 and look finished. Count the origins
#       below 0.80 before you write that number into the report — an average over
#       days is not a promise about any day.''')) 

    # ---------------------------------------------------------------- task 5 --
    c.append(md(L6_T5_INTRO))
    if sol:
        c.append(code('''from tayyar.eval.diebold_mariano import diebold_mariano

actual = np.concatenate([p["actual"] for p in per_l])
pred = {"LightGBM (direct)":       np.concatenate([p["pred"] for p in per_l]),
        "LightGBM (quantile q50)": np.concatenate([p["pred"] for p in per_q]),
        "Seasonal-naive":          np.concatenate([p["pred"] for p in per_s])}

dm_naive = diebold_mariano(actual, pred["LightGBM (direct)"],
                           pred["Seasonal-naive"], h=cfg.horizon)
dm_q50 = diebold_mariano(actual, pred["LightGBM (direct)"],
                         pred["LightGBM (quantile q50)"], h=cfg.horizon)

for title, r in (("LightGBM (direct)  vs  Seasonal-naive", dm_naive),
                 ("LightGBM (direct)  vs  LightGBM (quantile q50)", dm_q50)):
    print(title)
    print(f"   dm = {r['dm_stat']:>7.3f}   p = {r['p_value']:.4f}   "
          f"n = {r['n']:,}   mean loss diff = {r['mean_loss_diff']:+,.2f} MW")
    print(f"   {r['verdict']}")
    print()'''))
        c.append(code('''d = np.abs(actual - pred["LightGBM (direct)"]) - np.abs(actual - pred["Seasonal-naive"])
d2 = np.abs(actual - pred["LightGBM (direct)"]) - np.abs(actual - pred["LightGBM (quantile q50)"])

fig, ax = plt.subplots(1, 2, figsize=(11.5, 3.4), sharey=False)
for a, dd, t, r in ((ax[0], d, "vs seasonal-naive", dm_naive),
                    (ax[1], d2, "vs quantile q50", dm_q50)):
    per = dd.reshape(len(per_l), 24).mean(axis=1)
    a.bar(range(len(per)), per, color=["#2E7D32" if v < 0 else "#C00000" for v in per])
    a.axhline(0, color="#1F3864", lw=1)
    a.set_title(f"mean loss differential per origin, {t}\\n"
                f"dm = {r['dm_stat']:.2f}, p = {r['p_value']:.4f}", fontsize=9)
    a.set_xlabel("origin"); a.set_ylabel("|e1| - |e2|  (MW)")
plt.tight_layout()

print(f"origins where the direct model had the lower loss: "
      f"{int((d.reshape(len(per_l), 24).mean(axis=1) < 0).sum())} of {len(per_l)}  (vs naive)")
print(f"origins where the direct model had the lower loss: "
      f"{int((d2.reshape(len(per_l), 24).mean(axis=1) < 0).sum())} of {len(per_l)}  (vs q50)")'''))
        c.append(md("""**Expected**

```
LightGBM (direct)  vs  Seasonal-naive
   dm =  -6.750   p = 0.0000   n = 1,440   mean loss diff = -524.95 MW
   model 1 significantly better

LightGBM (direct)  vs  LightGBM (quantile q50)
   dm =  -1.901   p = 0.0575   n = 1,440   mean loss diff = -16.30 MW
   no significant difference — prefer the simpler model
```

**Against the baseline the result is not close.** 525 MW of mean absolute error per hour,
dm = -6.75, p < 0.001. The model earns its place; the complexity is bought and paid for.

**Between the two LightGBM variants there is no result at all.** The direct model is 16.3 MW
per hour better — a 2.2% relative improvement — and **p = 0.0575 says that gap is
indistinguishable from noise at the 5% level.** Look at the right-hand panel: the direct model
wins on most origins but loses on plenty, and the differential wanders around zero. That is
what "not significant" looks like, and it is why we plot it before we report it.

**The champion, and the rule that picked it.**

> *Among models whose accuracy is not distinguishable by a Diebold-Mariano test at the 5%
> level, take the one that is simpler, cheaper to run, or more useful to the decision. Only a
> DM-significant, decision-relevant gain buys added complexity.*

By that rule the champion is the **quantile q50 model**. It is statistically tied with the
direct model on accuracy, and it wins on grounds that have nothing to do with accuracy: the
same fit also produces the 5th and 95th percentiles, and the reserve decision downstream is a
quantile decision, not a point decision. Shipping the direct model would mean running a second
model to get the interval anyway.

Two things not to say. Do not say "p = 0.0575, so it is nearly significant" — 0.058 is a
number, not an argument, and had it landed at 0.049 the accuracy gain would still have been
2.2% and still not worth a second pipeline. And do not say "the models are equal" — the test
failed to distinguish them, which is a statement about the evidence, not about the models."""))
    else:
        c.append(code('''from tayyar.eval.diebold_mariano import diebold_mariano

# TODO (10 min)
#
#   1. Concatenate the per-origin actuals and predictions into 1,440-hour vectors
#      (they must be PAIRED — same origins, same hours, for every model).
#   2. diebold_mariano(actual, f1, f2, h=cfg.horizon) for
#        LightGBM (direct)  vs  Seasonal-naive
#        LightGBM (direct)  vs  LightGBM (quantile q50)
#      Report dm, p, n and the mean loss differential for both.
#   3. Plot the mean loss differential PER ORIGIN for each comparison. What does a
#      non-significant result look like on that plot?
#   4. Name the champion, and WRITE DOWN THE RULE you applied. A rule that only names
#      the winner is not a rule.
#
# HINT: h=24 matters. The loss differentials of a 24-hour-ahead forecast are
#       autocorrelated; the test uses a Newey-West long-run variance with h-1 lags,
#       and passing h=1 would understate the variance and manufacture significance.''')) 

    # ------------------------------------------------- when the champion loses --
    c.append(md("""### When does the champion lose?

The mean is what you report; the per-origin breakdown is what tells you **which weeks** the
champion fails on, and that is the section of the report an operator actually reads. Two
questions, and the second matters more:

1. Which origins in this window went worst, and what was happening on them?
2. **Which regimes does this window contain no evidence about at all?**"""))
    if sol:
        c.append(code('''worst = (bt_l.merge(bt_s[["origin", "MASE"]], on="origin", suffixes=("", "_naive"))
           .sort_values("MASE", ascending=False).head(6))
worst = worst.assign(day=lambda d: (d.origin + pd.Timedelta(1, "h")).dt.date)
tmax = df["temp_c"].resample("D").max()
worst["t_max_C"] = [round(float(tmax.loc[str(d)]), 1) for d in worst.day]
worst["weekday"] = [pd.Timestamp(d).day_name()[:3] for d in worst.day]
print("the champion's six worst origins")
print(worst[["day", "weekday", "t_max_C", "MAE", "MAPE_%", "MASE", "MASE_naive"]]
      .to_string(index=False))
print(f"\\norigins with MASE > 1 (worse than the free baseline's own scale): "
      f"{int((bt_l.MASE > 1).sum())} of {len(bt_l)}")'''))
        c.append(code('''# The regimes this window has no evidence about. Eid al-Fitr 2023 fell on 21-24 April,
# so we refit honestly at a cut before it and score the Eid days against the days after.
EID_CUT = "2023-04-18 23:00"
eid_model = refit_at(EID_CUT)                       # ~1 min, training data ends 18 April

rows = []
for d in pd.date_range("2023-04-20", "2023-04-28", freq="D"):
    o = pd.Timestamp(f"{d:%Y-%m-%d} 23:00", tz="Asia/Riyadh")
    pos = X.index.get_loc(o); Xo = X.iloc[[pos]]
    actual = yy.iloc[pos + 1: pos + 25]
    hist = yy.iloc[pos - cfg.initial_train: pos]
    f = np.array([eid_model.models_[h].predict(Xo)[0] for h in range(1, 25)])
    day = (o + pd.Timedelta(1, "h")).date()
    rows.append({"forecast_day": str(day),
                 "day_name": pd.Timestamp(day).day_name()[:3],
                 "is_eid": bool(df["is_eid"].loc[str(day)].max()),
                 **{k: all_metrics(actual, f, hist, 24)[k] for k in ("MAE", "MAPE_%", "MASE")}})
eid = pd.DataFrame(rows)
print(eid.to_string(index=False))
print()
print(eid.groupby("is_eid")[["MAE", "MAPE_%", "MASE"]].mean().round(3).to_string())'''))
        c.append(md(EID_INTERP))
    else:
        c.append(code('''# TODO (part of Tasks 5-6)
#
#   1. Sort the champion's per-origin table by MASE and take the worst six. For each,
#      print the forecast day, the weekday, the day's maximum temperature, and the
#      seasonal-naive's MASE on the same origin. Which of them are hard days for
#      everybody, and which are hard days for the MODEL?
#   2. How many origins did the champion score MASE > 1 on?
#   3. Now the question the table cannot answer: which regimes are NOT in this window?
#      Check df["is_eid"] and df["temp_c"] across 2023-11-01 .. 2023-12-30.
#      Then refit honestly at a cut before Eid al-Fitr (21-24 April 2023) and score
#      the Eid days against the ordinary days that follow them.
#
# HINT: "we have no evidence about X" is a finding, and it belongs in the report next
#       to the table — not omitted because the table looks good without it.''')) 

    c.append(md(QUIZ6_A if sol else QUIZ6_Q))
    c.append(md(COMMIT6))

    if sol:
        c.append(md("""### Instructor notes

**Protect the full 50 minutes.** With Lab 4 this is the second of the two most overrun-prone
slots in the course, and it is the one that produces the course's headline deliverable. If you
are behind, cut the Eid probe and the plots — never Task 1, never the DM.

- **Branch `sim-fit-once`** is the Task 1 leak on its own, with everything else correct: the
  reported MASE is ≈ 0 and the room's first instinct is always that the model is brilliant.
  Do not hint. Ask one question — *what time is it when that line runs?* — and wait.
- **Branch `sim-lucky-split`** evaluates the same two models on two different single test
  windows and the ranking **flips** between them. Run both in front of the room before Task 2,
  announce nothing, and let a pair notice that the "winner" changed. It is the fastest way to
  make "one split is a sample of one" stop being a slogan.
- **Baseline first** (10 minutes, before anyone touches a model). Every pair hand-computes the
  seasonal-naive forecast and its MAE for one specific day — on paper, from the previous 24
  hours. They then keep that number as their denominator for the rest of the lab. Pairs who
  have computed a baseline by hand never again ask what MASE is dividing by, and it inoculates
  the room against Task 3's 0.77.
- **The significance debate** (15 minutes, at Task 5). Put the per-origin loss-differential
  plot on the projector with the p-values hidden. Each pair writes down its verdict on both
  comparisons — significant or not — and commits to it out loud. Then reveal: p < 0.001 and
  p = 0.058. The room is nearly always right about the baseline and nearly always wrong about
  the two LightGBM variants, because 38 wins out of 60 origins *looks* decisive by eye. That
  gap between what the eye sees and what the test says is the entire lesson.
- **The shared leaderboard.** Put a table on the projector — pair, model, MASE, DM p-value
  against the seasonal-naive — and fill it in as pairs finish. Two rules, stated before you
  start: a row without a p-value does not go on the board, and any MASE below 0.2 gets audited
  in front of the room. Both rules will be needed.

**Troubleshooting**

| symptom | cause |
|---|---|
| every model reports MASE ≈ 0 | scored in-sample. The training data ends after the origins — fit inside the loop, or before the first origin. |
| MAPE = 4,000% on one origin | a near-zero demand hour in the denominator. Not a bug in the model; it is the failure mode of MAPE. Report MASE and keep the origin. |
| only three origins produced | `step` too large or `initial_train` too big for the series. `len(index) - horizon - initial_train` has to leave room for `n_origins * step`. |
| the backtest runs for minutes | expected — 24 models per direct fit. Cache the cheap families, fit the expensive ones once, and parallelise folds if you must; do not "fix" it by dropping to five origins. |
| the champion changes when you re-run | a seed is loose somewhere. Every LightGBM in `src/tayyar` is seeded at 212; if yours is not, fix that before you report anything. |
| MAPE ≈ 1% and MASE ≈ 0.2 | the loop is predicting each hour from that hour's own feature row instead of from the origin's. The lag-1 column is doing the work. |

**Fast finishers.** Re-run the whole backtest with `window="sliding"` and compare the two
tables — on this stable series the expanding window wins slightly, which is the *right* answer
for the wrong-sounding reason and is worth explaining. Or drop `n_origins` to 10 and show how
much the ranking moves; it is the sample-of-one lesson at a scale they can feel."""))

    write(f"lab6_{tag}.ipynb", c)


# ============================================================= LAB 7 ==========
L7_TASKS = """### Tasks

| min | task |
|---|---|
| 8 | Wire the pipeline end to end from a **committed config** and confirm a clean run reproduces the Lab 6 backtest table. Print `MATCH`. Then read the inherited selection step and find the **fault** in it. |
| 10 | Three constraint scenarios with explicit weights over accuracy / explainability / latency / maintenance. Build the candidate profile table and run `recommend.score` for each. |
| 10 | Observe that the champion **changes** across scenarios. Record which constraint flipped each decision, and use `flip_conditions` to state what would have to change for the runner-up to win. |
| 8 | Generate the reserve brief with `pipeline.brief.reserve_brief`, then critique it as a control-room engineer would. Rewrite the jargon version in decision language. |
| 9 | Write `DECISION_RECORD.md`: the decision and its cost function, the candidates, the constraints and weights, the recommendation with its DM evidence, the flip-conditions, and the monitoring contract. |
| 5 | Commit. |
"""

STARTER7 = '''# ---------------------------------------------------------------------------
# The selection step you inherited
#
#   "Backtest reproduces. Champion selected. Ready to promote."
#
# It runs, it uses the library function, and the model it names is genuinely the
# most accurate one in the table. It is still the wrong answer.
# ---------------------------------------------------------------------------
from tayyar.pipeline.select import champion

winner = champion(bt, metric="MASE")
print(summary.to_string())
print()
print(f"CHAMPION: {winner}")
print(f"MASE {summary.loc[winner, 'MASE']:.3f} — lowest in the table. Promoting to production.")'''

L7_T2_INTRO = """### Task 2 — three use cases, three weightings, one candidate set

**Selection is a function of the use case, not a position on a leaderboard.** The same three
models, ranked for three different customers, produce three different answers — and none of
the rankings is wrong.

The six constraints that legitimately override accuracy:

1. **Deadline and latency.** A forecast that misses the publication window has an error of
   infinity. A model that trains in four hours cannot serve a 15-minute re-run.
2. **Explainability.** A regulator, or an operator at 02:00, has to be able to interrogate the
   forecast. "Feature importance says lag-3" is not an answer to "why is it high tonight?".
3. **Cost asymmetry.** Under-forecasting load costs far more than over-forecasting it — the
   first buys emergency generation, the second buys idle spinning reserve. A symmetric MAE
   objective encodes a symmetry the business does not have. Optimise a quantile or an
   asymmetric loss and select on it.
4. **Maintenance and total cost of ownership.** One model per operating area, per horizon, per
   quantile is a pipeline somebody owns forever. Multiply by four areas before you choose.
5. **Serve-time data availability.** A feature you cannot compute at 23:00 is not a feature.
   No day-ahead temperature feed means no SARIMAX-with-temperature and no weather columns —
   whatever the backtest said.
6. **Adoption.** The winning model is the one people will actually use at 02:00 during an
   unusual event. A model the control room overrides every time it matters has zero skill in
   production regardless of its MASE.

The rule that follows: **the simplest model meeting the constraints wins, and complexity is
justified only by a DM-significant, decision-relevant gain.**"""

L7_PROFILES = '''from tayyar.pipeline.recommend import score, flip_conditions

# Scores are 0-1, higher is better, and every one of them is a judgement you must be
# able to defend in the decision record. maintenance = LOW burden scores HIGH.
profiles = pd.DataFrame(
    [
        # accuracy  explainability  latency  maintenance
        [0.10,      1.00,           1.00,    1.00],   # Seasonal-naive
        [0.50,      0.80,           0.95,    0.90],   # ETS
        [0.80,      0.95,           0.55,    0.60],   # SARIMAX + temperature
        [1.00,      0.45,           0.80,    0.35],   # LightGBM + CQR (per area)
        [0.90,      0.45,           0.80,    0.75],   # LightGBM + CQR (global)
    ],
    columns=["accuracy", "explainability", "latency", "maintenance"],
    index=["Seasonal-naive", "ETS", "SARIMAX + temperature",
           "LightGBM + CQR (per area)", "LightGBM + CQR (global)"])

# The hard facts that become FILTERS, not scores. A constraint you can score away is
# not a constraint.
facts = pd.DataFrame(
    {"interval": ["none", "analytic", "analytic (native)", "calibrated (CQR)",
                  "calibrated (CQR)"],
     "needs_feature_store": [False, False, False, True, True],
     "needs_temp_forecast": [False, False, True, True, True],
     "models_to_own_4_areas": [0, 4, 4, 4 * 24 * 3, 24 * 3]},
    index=profiles.index)

print(profiles.to_string())
print()
print(facts.to_string())'''

L7_SCENARIOS = '''SCENARIOS = {
    "A. Regulator (published day-ahead forecast)": {
        "weights": {"accuracy": 0.30, "explainability": 0.40,
                    "latency": 0.20, "maintenance": 0.10},
        "hard": {"needs_feature_store": False},
        "why": "published under a licence condition, must be explained on request, "
               "produced by a scheduled batch job with no online feature store",
    },
    "B. Internal dispatch (unit commitment)": {
        "weights": {"accuracy": 0.60, "explainability": 0.10,
                    "latency": 0.20, "maintenance": 0.10},
        "hard": {},
        "why": "every MW of error is money; the team owns a feature store already",
    },
    "C. Four operating areas, one analyst": {
        "weights": {"accuracy": 0.30, "explainability": 0.10,
                    "latency": 0.20, "maintenance": 0.40},
        "hard": {},
        "why": "the same person maintains all four; whatever is chosen is chosen four times",
    },
}

ranked = {}
for name, s in SCENARIOS.items():
    elig = profiles.copy()
    for col, required in s["hard"].items():
        elig = elig[facts.loc[elig.index, col] == required]
    r = score(elig, s["weights"])
    ranked[name] = r
    dropped = [m for m in profiles.index if m not in elig.index]
    print(f"{name}")
    print(f"   weights {s['weights']}")
    print(f"   why     {s['why']}")
    if dropped:
        print(f"   EXCLUDED by hard constraint: {', '.join(dropped)}")
    print(r[["accuracy", "explainability", "latency", "maintenance",
             "weighted_score"]].to_string())
    print(f"   -> champion: {r.index[0]}")
    print()'''

QUIZ7_Q = """### Mini-quiz

Answer these in your pair before you look at the next cell.

1. Is "lowest MASE" always the right selection?
2. Which family fits "covariates plus a regulator demanding explainability"?
3. What must a recommendation include besides the champion?
4. Why present a quantile rather than a point forecast for reserve sizing?
5. What makes selection evidence reproducible?
"""

QUIZ7_A = """### Mini-quiz — answers

1. **Is lowest MASE always right?** No. The deadline, explainability, the asymmetry between
   the cost of under- and over-forecasting, maintenance burden, serve-time data availability
   and adoption can each override it — and a gap that fails a Diebold-Mariano test is not a
   reason to override anything.
2. **Covariates plus a regulator demanding explainability?** **SARIMAX with exogenous
   regressors.** It has a component story you can narrate — trend, seasonality, the
   temperature coefficient with a sign and a magnitude — and it produces native analytic
   intervals. LightGBM offers feature importance, which is an association, not an explanation.
3. **What else must a recommendation include?** Its own **limits** — the flip-conditions that
   would change the answer, and the regimes the evidence does not cover — and a **monitoring
   plan** with thresholds and a fallback. A recommendation without limits is an advertisement.
4. **Why a quantile for reserve sizing?** Because the decision is a risk decision. Reserve is
   sized so that demand exceeds supply with acceptably small probability; that is a quantile,
   and the cost of being short is not the cost of being long. A point forecast forces the
   consumer to invent the quantile themselves, usually badly.
5. **What makes it reproducible?** Fixed splits and fixed seeds, pinned dependency versions,
   and a config-driven pipeline that runs end to end from a committed file — so the table in
   the report can be regenerated by somebody who was not in the room.
"""

COMMIT7 = """### Task 6 — commit

```
git add -A && git commit -m "feat(pipeline): constraint-weighted selection, reserve brief and decision record"
```

The two files that leave this course are `BACKTEST.md` (the evidence) and
`DECISION_RECORD.md` (the decision). The notebooks are the working; those two are the work."""


BRIEF_INTERP = """**Critique it the way the engineer will.**

The template gets the *order* right, and the order is most of the battle: the recommended
reserve appears before the model is mentioned, and the model is never mentioned at all. It
gets three more things right that are usually missing. It states the **coverage the interval
actually achieved** over 60 backtested days rather than the nominal figure it was designed for.
It names **where the forecast is weakest** in the same breath as the recommendation, not in an
appendix. And it names a **fallback**, with triggers, so the reader knows what to do at 02:00
when it is wrong — which is the question the third paragraph of every brief should answer and
almost none do.

What it still does not do, and what the engineer will ask for: it gives one reserve number for
the day when the uncertainty is not flat across the day, and it quotes marginal coverage when
the peak-hour coverage is the number that matters for a peak-hour decision. Both belong in the
next revision, and both are already measured in Lab 6.

One more thing to fix, and it is the kind of thing that gets a brief sent back: the word
**reserve** is used for two different quantities. The template calls the 1,199 MW *margin* the
"recommended spinning reserve"; a control room may equally read "reserve" as the level to cover
to, 33,323 MW. Both readings are defensible from the words alone, and the difference is 32,000
MW. Decision language has to be unambiguous about the unit and the datum — say "hold 1,199 MW
above the expected peak" or "cover to 33,323 MW", never the bare noun.

**The two versions, side by side.** Every number in the jargon line is correct and none of them
is a decision. "The p95 is 33,323 MW" is a fact about a distribution; "hold 1,199 MW above the
expected peak of 32,124 MW at 18:00" is an instruction somebody can execute. "MASE is 0.455"
answers a question nobody in the control room asked; "this covers all but about 5% of
afternoons" answers the one they did. The decision version carries no less information — it
carries the same information, addressed to the person who has to act on it, plus the one
sentence the jargon version omits entirely: **where it fails and what to do then.**

Note the size of that gap and why it is small. 31 December is a mild winter day, peaking at
32,124 MW; the interval is correspondingly narrow. Across the sixty backtested days the mean
band width was 3,213 MW, and on a July afternoon it is wider again. **That variation is the
interval working**, not noise in it — a constant-width band would be too wide tonight and far
too narrow in August. It is also why the brief says the uncertainty is widest on hot days
rather than quoting one number as if it held all year."""


def lab7(sol: bool):
    tag = "solution" if sol else "start"
    c = [md(HDR.format(n=7, title="End-to-End Selection and the Decision Record",
                       dur=50, tag=tag)),
         md(L7_TASKS), code(SETUP)]

    # ---------------------------------------------------------------- task 1 --
    c.append(md("""### Task 1 — the config, the clean run, and the selection step you inherited

**Reproducibility is what makes the Lab 6 report evidence rather than anecdote.** Three things
buy it, and all three are cheap: **fixed splits** (dates in a file, not in a head), **fixed
seeds** (every LightGBM in `src/tayyar` is seeded at 212), and **pinned dependencies** (a
LightGBM minor version can move the third decimal). A number nobody else can regenerate is not
a result; it is a claim.

The test is blunt: run the whole pipeline from the committed config in a clean kernel and
check that it reproduces `reference_results.json` exactly. If it prints `MATCH`, the report
can be defended. If it does not, nothing downstream of it means anything."""))
    c.append(code('''import json

CONFIG = {
    "data": {"demand": f"{DATA}/ksa_grid_demand.csv",
             "calendar": f"{DATA}/ksa_calendar.csv"},
    "features": {"source_columns": ["demand_mw", "temp_c", "is_weekend",
                                    "is_ramadan", "is_eid", "is_national_day"]},
    "split": {"cut_train": "2023-09-30 23:00", "cut_calibration": "2023-10-31 23:00"},
    "backtest": {"horizon": 24, "n_origins": 60, "step": 24,
                 "initial_train": 24 * 365, "window": "expanding", "m": 24},
    "models": {"point": "DirectLGBMForecaster(horizon=24)",
               "quantile": "QuantileLGBM(quantiles=(0.05, 0.50, 0.95), horizon=24)",
               "baseline": "seasonal_naive(m=24)"},
    "interval": {"method": "CQR", "alpha": 0.10, "calibration_window": "2023-10"},
    "seeds": {"lightgbm": 212, "numpy": 212},
    "refit": {"cadence": "monthly", "boundary": "2023-09-30 23:00"},
}
print(json.dumps(CONFIG, indent=2))'''))
    if sol:
        c.append(code('''import lightgbm, sklearn, statsmodels, scipy
from tayyar.data.load import load_demand, load_calendar, join_calendar
from tayyar.features.build import build_features
from tayyar.models.lgbm_forecaster import DirectLGBMForecaster
from tayyar.models.quantile import QuantileLGBM
from tayyar.models.conformal import CQR
from tayyar.eval.backtest import BacktestConfig, origins
from tayyar.eval.metrics import all_metrics

print("pinned at run time:",
      {"pandas": pd.__version__, "numpy": np.__version__,
       "lightgbm": lightgbm.__version__, "scikit-learn": sklearn.__version__,
       "statsmodels": statsmodels.__version__, "scipy": scipy.__version__})


def run_pipeline(conf):
    """Config in, backtest table out. No arguments hidden in the caller's scope."""
    np.random.seed(conf["seeds"]["numpy"])
    df = join_calendar(load_demand(conf["data"]["demand"]),
                       load_calendar(conf["data"]["calendar"]))
    feat = build_features(df[conf["features"]["source_columns"]])
    Xcols = [c for c in feat.columns if c != "demand_mw"]
    X, yy = feat[Xcols].astype(float), feat["demand_mw"]
    y = df["demand_mw"].astype(float)

    cfg = BacktestConfig(**conf["backtest"])
    ORIGINS = [y.index[tr.stop - 1] for tr, te in origins(y.index, cfg)]

    Xtr = X[:conf["split"]["cut_train"]].dropna(); ytr = yy[Xtr.index]
    lgbm = DirectLGBMForecaster(horizon=cfg.horizon).fit(Xtr, ytr)
    qm = QuantileLGBM(quantiles=(0.05, 0.50, 0.95), horizon=cfg.horizon).fit(Xtr, ytr)

    def one(fn, name):
        rows, per = [], []
        for o in ORIGINS:
            pos = X.index.get_loc(o); Xo = X.iloc[[pos]]
            actual = yy.iloc[pos + 1: pos + 25]
            hist = yy.iloc[pos - cfg.initial_train: pos]
            f = np.asarray(fn(Xo, pos), dtype=float)
            rows.append({"origin": o, "model": name,
                         **all_metrics(actual, f, hist, cfg.m)})
            per.append({"origin": o, "actual": actual.to_numpy(), "pred": f})
        return pd.DataFrame(rows), per

    def naive(Xo, pos):
        last = yy.iloc[pos - 23: pos + 1].to_numpy()
        return [last[h % 24] for h in range(24)]

    parts = {"LightGBM (direct)":
                 one(lambda Xo, pos: [lgbm.models_[h].predict(Xo)[0] for h in range(1, 25)],
                     "LightGBM (direct)"),
             "LightGBM (quantile q50)":
                 one(lambda Xo, pos: [qm.models_[(h, 0.50)].predict(Xo)[0]
                                      for h in range(1, 25)], "LightGBM (quantile q50)"),
             "Seasonal-naive": one(naive, "Seasonal-naive")}
    bt = pd.concat([p[0] for p in parts.values()], ignore_index=True)
    per = {k: v[1] for k, v in parts.items()}
    return dict(df=df, X=X, yy=yy, cfg=cfg, ORIGINS=ORIGINS, lgbm=lgbm, qm=qm,
                bt=bt, per=per)


art = run_pipeline(CONFIG)          # ~4 minutes: 24 + 72 LightGBM models
bt, per = art["bt"], art["per"]
MET = ["MAE", "RMSE", "MAPE_%", "WAPE_%", "MASE", "bias"]
summary = bt.groupby("model")[MET].mean().round(3).sort_values("MASE")
print()
print(summary.to_string())'''))
        c.append(code('''ref = json.load(open("../reference_results.json"))["m6"]
ref_tbl = pd.DataFrame(ref["summary"]).set_index("model")[MET].loc[summary.index]

delta = (summary - ref_tbl).abs().max().max()
print(f"largest absolute difference from reference_results.json: {delta:.6f}")
print(f"origins: run {int(bt.groupby('model').size().min())}, reference {ref['n_origins']}")

from tayyar.eval.diebold_mariano import diebold_mariano
actual = np.concatenate([p["actual"] for p in per["LightGBM (direct)"]])
P = {k: np.concatenate([p["pred"] for p in v]) for k, v in per.items()}
dm1 = diebold_mariano(actual, P["LightGBM (direct)"], P["Seasonal-naive"], h=24)
dm2 = diebold_mariano(actual, P["LightGBM (direct)"], P["LightGBM (quantile q50)"], h=24)
dm_ok = (abs(dm1["dm_stat"] - ref["dm_lgbm_vs_naive"]["dm_stat"]) < 5e-3 and
         abs(dm2["p_value"] - ref["dm_lgbm_vs_q50"]["p_value"]) < 5e-4)
print(f"DM vs naive: dm {dm1['dm_stat']} p {dm1['p_value']}   "
      f"DM vs q50: dm {dm2['dm_stat']} p {dm2['p_value']}")
print()
print("MATCH" if delta < 5e-4 and dm_ok else "MISMATCH — do not publish anything downstream")'''))
        c.append(md("""`MATCH`, from a clean kernel, from a committed config. That is the whole point of the
task: the table in `BACKTEST.md` is not a screenshot of a good afternoon, it is the output of
a program somebody else can run.

What actually buys the reproduction, in order of how often each one is missing in practice:
the **split dates are in the config**, not typed into a cell; the **seed is inside the model
class** (`random_state=212` in `lgbm_forecaster.py` and `quantile.py`), so nobody has to
remember to pass it; the **origin schedule is derived** from `BacktestConfig` rather than
hand-rolled per notebook; and the **library versions are printed with the result**, so a
future mismatch can be attributed instead of argued about.

Now the selection step that came with the pipeline."""))
        c.append(code(STARTER7))
        c.append(md("""**The fault: selection is not `argmin`.** `pipeline.select.champion` sorts the
summary table by MASE and returns the top row. That is a correct implementation of a narrow
question — *which model was most accurate on this window?* — and the model it names, the direct
LightGBM, genuinely was. It is the wrong answer to the question actually being asked, which is
*which model do we run in production, for whom, under what constraints?*

Three things the argmin cannot see, all of them fatal in at least one of the scenarios below:

1. **The gap it selects on is not significant.** Lab 6's Diebold-Mariano put the direct model
   and the quantile model at p = 0.058. The argmin ranked them anyway, because a sort has no
   concept of a confidence interval. Selecting on an insignificant difference is selecting on
   noise, and it will pick a different winner next quarter.
2. **It ships a model that cannot be served for one of the three customers.** The direct
   LightGBM needs 44 features at serve time, including 336-hour lags and a **day-ahead
   temperature forecast**, which means an online feature store and a live weather feed. The
   regulated publication runs as a scheduled batch job with neither.
3. **It throws away the interval.** The direct model emits a point forecast. The decision
   downstream — how much spinning reserve to hold — is a quantile decision. The argmin
   optimised a column that the consumer of the forecast does not consume."""))
    else:
        c.append(code('''# TODO (8 min)
#
#   1. Write run_pipeline(CONFIG): load -> build_features -> BacktestConfig ->
#      fit DirectLGBMForecaster and QuantileLGBM on data ending at the config's
#      cut_train -> backtest the three families at the config's origins.
#      NOTHING may come from the caller's scope. That is what "config-driven" means.
#   2. Print the installed versions of pandas, numpy, lightgbm, scikit-learn,
#      statsmodels and scipy alongside the result.
#   3. Compare your summary table with reference_results.json["m6"]["summary"] and
#      the two Diebold-Mariano results. Print MATCH or MISMATCH — and mean it: if it
#      mismatches, nothing downstream of it is worth writing down.
#   4. Then run the inherited selection cell below and find the fault in it.
#
# HINT: reproducibility is fixed splits + fixed seeds + pinned versions. If your
#       numbers move between runs, look for a split date typed into a cell, an
#       unseeded model, or a dropna() that silently depends on execution order.''')) 
        c.append(code(STARTER7_STUB))
        c.append(code(STARTER7))
        c.append(code('''# TODO (part of Task 1) — the selection step above is wrong. It is not wrong
# because it picked the wrong row; it is wrong because of the QUESTION it asks.
#
#   1. What is champion() actually optimising? Read pipeline/select.py.
#   2. Lab 6 put the top two models at p = 0.058 on a Diebold-Mariano test. What does
#      a sort do with that information?
#   3. List everything the winning model needs AT SERVE TIME, at 23:00, to produce
#      tomorrow's forecast. Which of those things does a regulated batch publication
#      job actually have?
#   4. What does the decision downstream consume — a number, or a distribution?
#
# Write the fault in one sentence at the top of DECISION_RECORD.md before you fix it.
#
# HINT: "the most accurate model" and "the model we should run" are different
#       questions, and only one of them can be answered by sorting a column.''')) 

    # ---------------------------------------------------------------- task 2 --
    c.append(md(L7_T2_INTRO))
    if sol:
        c.append(code(L7_PROFILES))
        c.append(code(L7_SCENARIOS))
        c.append(md("""**Expected**

```
A. Regulator                 EXCLUDED by hard constraint: LightGBM + CQR (per area, global)
   SARIMAX + temperature   0.790     ETS  0.750     Seasonal-naive  0.730
B. Internal dispatch
   LightGBM + CQR (per area) 0.840   LightGBM + CQR (global) 0.820   SARIMAX 0.745
C. Four areas, one analyst
   ETS 0.780   LightGBM + CQR (global) 0.775   Seasonal-naive 0.730   SARIMAX 0.685
```

Three customers, one candidate set, three different champions — and the accuracy column never
changed. Read each one:

**A. The regulator.** The two LightGBM variants never reach the scoring step: they are removed
by a **hard filter**, not by a low score, because they cannot be served by the publication job
at all. This is the distinction to insist on in the room — *a constraint you can trade away
with a weight is not a constraint*. Among what remains, explainability at 0.40 carries
SARIMAX: a component story (trend, seasonality, a temperature coefficient with a sign and a
magnitude a regulator can question) plus native analytic intervals.

**B. Internal dispatch.** Accuracy at 0.60 and a team that already owns a feature store, so
the filter does not fire and the most accurate model wins on the merits — and, crucially, its
margin over the baseline is DM-significant (p < 0.001). Complexity bought with evidence.

**C. Four operating areas, one analyst.** Maintenance at 0.40 changes everything. The per-area
LightGBM means 4 × 24 × 3 = 288 fitted models to own, monitor and retrain; ETS means four.
Note the top two are separated by **0.005**, which is not a decision — it is a tie, and the
same rule that settled Lab 6's DM result settles it here: when two options are
indistinguishable, take the simpler or the cheaper one. Either answer is defensible; what is
not defensible is presenting 0.780 and 0.775 as if the first had won something."""))
        c.append(code('''# Serve-time data availability is a filter too. Suppose the day-ahead temperature
# feed is down for a week — which candidates survive, and who is champion then?
elig = profiles[~facts["needs_temp_forecast"]]
r = score(elig, SCENARIOS["A. Regulator (published day-ahead forecast)"]["weights"])
print("no day-ahead temperature feed available:")
print(r[["accuracy", "explainability", "latency", "maintenance", "weighted_score"]]
      .to_string())
print(f"-> champion: {r.index[0]}  (SARIMAX + temperature is not a candidate without "
      f"a temperature forecast)")'''))
    else:
        c.append(code('''from tayyar.pipeline.recommend import score, flip_conditions

# TODO (10 min)
#
#   1. Build `profiles`: one row per candidate family, columns accuracy /
#      explainability / latency / maintenance, scored 0-1, higher is better.
#      Derive them from the trade-off space, not from taste:
#        seasonal-naive  accuracy low, explainability total, no interval,
#                        latency trivial, maintenance none
#        ETS             medium / high / analytic interval / very fast / low burden
#        SARIMAX + temp  medium-high / high, a component story / native analytic
#                        interval / moderate, slow at large m / medium burden
#        LightGBM + CQR  high / medium, importance only / calibrated and sharp /
#                        fast to train but needs a feature store / higher, a pipeline
#      Add a GLOBAL LightGBM row (one model across the four areas).
#   2. Build `facts`: the hard, non-negotiable columns — needs_feature_store,
#      needs_temp_forecast, models_to_own_4_areas, interval type. These become
#      FILTERS. A constraint you can score away is not a constraint.
#   3. Three scenarios, with the weights written down BEFORE you look at the result:
#        A Regulator          0.3 / 0.4 / 0.2 / 0.1  + hard: no feature store
#        B Internal dispatch  0.6 / 0.1 / 0.2 / 0.1
#        C Four areas         0.3 / 0.1 / 0.2 / 0.4
#      Apply the hard filter, then score(elig, weights), and print the champion.
#
# HINT: if the same model wins all three scenarios, either your weights are barely
#       different or your hard filters are not being applied. Check both.''')) 

    # ---------------------------------------------------------------- task 3 --
    c.append(md("""### Task 3 — the champion changes, and you must say what changed it

A recommendation that does not state its own flip-conditions is not a recommendation, it is a
preference. `flip_conditions` answers one question precisely: **how much would have to move,
and in which column, for the runner-up to win?** If the answer is "0.02 of explainability",
the decision is a coin toss dressed as analysis and you must say so."""))
    if sol:
        c.append(code('''rows = []
for name, s in SCENARIOS.items():
    r = ranked[name]
    rows.append({"scenario": name.split(".")[0],
                 "champion": r.index[0],
                 "score": r.weighted_score.iloc[0],
                 "runner-up": r.index[1],
                 "gap": round(float(r.weighted_score.iloc[0] - r.weighted_score.iloc[1]), 3),
                 "decisive constraint": {"A": "explainability + serve-time (hard filter)",
                                         "B": "accuracy, DM-significant",
                                         "C": "maintenance"}[name.split(".")[0]]})
print(pd.DataFrame(rows).to_string(index=False))
print()
for name, s in SCENARIOS.items():
    print(name)
    for line in flip_conditions(ranked[name], s["weights"]):
        print("   " + line)
    print()'''))
        c.append(md("""Read the gaps before you read the champions. Scenario A is decided by 0.040, and only
after two candidates were removed by a **hard filter** that no weighting could have overridden.
Scenario B picks a *family* decisively — the best LightGBM stands 0.095 clear of the best
non-LightGBM candidate, and that margin is backed by a Diebold-Mariano result — but the choice
*within* the family, per-area against global, is 0.020 and is not decided by this table at all.
Scenario C is decided by **0.005**, which is to say it is not decided: `flip_conditions` prints
a required move of 0.01 in maintenance, well inside the precision of the judgements that
produced the table.

That is the honest output of this task, and it belongs in the record verbatim:

- **A flipped on explainability plus serve-time availability.** The LightGBM candidates were
  never eligible; among those that were, weighting explainability at 0.40 chose SARIMAX.
- **B flipped on accuracy**, and the accuracy gap over the baseline is DM-significant.
- **C flipped on maintenance.** 288 models against 4. The two leaders are tied; report the tie.

The general rule this makes concrete: **the simplest model that meets the constraints wins.**
Complexity has to be bought with a DM-significant, decision-relevant gain, and in two of these
three scenarios it cannot be."""))
    else:
        c.append(code('''# TODO (10 min)
#
#   1. Tabulate, per scenario: champion, weighted score, runner-up, the GAP between
#      them, and the constraint you judge to have been decisive.
#   2. flip_conditions(ranked[name], weights) for each scenario. Print every line.
#   3. Then the question that matters: which of these three decisions is real, and
#      which is a tie you have dressed up as a decision? Look at the gaps.
#
# HINT: a 0.005 gap between two candidates is not a champion. Say so in the record,
#       and apply the same rule Lab 6 applied to p = 0.058 — take the simpler one.''')) 

    # ---------------------------------------------------------------- task 4 --
    c.append(md("""### Task 4 — the brief, and what a control-room engineer does with it

The forecast is finished. The **communication** is not, and it is where forecasts are most
often rejected. Lead with the decision, not the model."""))
    if sol:
        c.append(code('''from tayyar.pipeline.brief import reserve_brief

X_, yy_, qm_, ORIGINS_ = art["X"], art["yy"], art["qm"], art["ORIGINS"]
TAUS = (0.05, 0.50, 0.95)

# Calibrate on October, exactly as the config says, then issue the last origin's day.
Xca = X_[CONFIG["split"]["cut_train"]:CONFIG["split"]["cut_calibration"]]
yca = yy_[Xca.index]
rows_ca = list(range(0, len(Xca) - 24, 24))
Yca = np.array([yca.iloc[i + 1: i + 25].to_numpy() for i in rows_ca])
Pca = {t: np.column_stack([qm_.models_[(h, t)].predict(Xca.iloc[rows_ca])
                           for h in range(1, 25)]) for t in (0.05, 0.95)}
cqr = CQR(alpha=CONFIG["interval"]["alpha"]).calibrate(
    Yca.ravel(), Pca[0.05].ravel(), Pca[0.95].ravel())

o = ORIGINS_[-1]
pos = X_.index.get_loc(o); Xo = X_.iloc[[pos]]
q = {t: np.array([qm_.models_[(h, t)].predict(Xo)[0] for h in range(1, 25)]) for t in TAUS}
lo, hi = cqr.interval(q[0.05], q[0.95])
fc = pd.DataFrame({"q05": lo, "q50": np.clip(q[0.50], lo, hi), "q95": hi},
                  index=pd.date_range(o + pd.Timedelta(1, "h"), periods=24, freq="h"))

brief = reserve_brief(
    fc, coverage=0.90, n_origins=60,
    weakness=("Eid and public holidays. This backtest window (Nov-Dec) contains none, "
              "and at the 2023 Eid al-Fitr the same model's error roughly doubles. "
              "Also the hottest afternoons: marginal coverage is 0.90 but only ~0.85 "
              "on the 12:00-18:00 block."),
    fallback=("seasonal-naive plus the on-call analyst's uplift, with the interval taken "
              "from the last 30 days' empirical errors. Trigger it on any Eid day, on any "
              "day the temperature feed is missing, or when rolling 7-day MASE exceeds 0.60."),
    issued=f"{o:%Y-%m-%d %H:%M}")
print(brief)'''))
        c.append(code('''peak_i = fc.q50.idxmax()
peak, p95 = fc.q50.max(), fc.q95.max()

print("THE JARGON VERSION — every number in it is correct, and not one of them is a decision")
print(f"  The p95 is {p95:,.0f} MW, MASE is 0.455, marginal coverage is 0.90, and the "
      f"mean pinball loss is 201 MW.")
print()
print("THE DECISION VERSION — same numbers, addressed to the person who has to act")
print(f"  Cover demand up to {p95:,.0f} MW tomorrow: hold {p95 - peak:,.0f} MW above the "
      f"expected peak of")
print(f"  {peak:,.0f} MW at {peak_i:%H:%M}. That gap is the honest uncertainty, and it "
      f"widens on hot days;")
print(f"  it covers all but about 5% of afternoons. It is least reliable on Eid days, "
      f"which this")
print(f"  evidence does not cover at all — on those, fall back to the analyst uplift.")'''))
        c.append(md(BRIEF_INTERP))
    else:
        c.append(code('''from tayyar.pipeline.brief import reserve_brief

# TODO (8 min)
#
#   1. Calibrate CQR on the October window from CONFIG, then build a one-day forecast
#      frame for the last origin with columns q05 / q50 / q95 and a DatetimeIndex.
#   2. brief = reserve_brief(fc, coverage=..., n_origins=..., weakness=..., fallback=...)
#      The weakness and fallback arguments are not decoration. Write them as if the
#      person reading them will be woken at 02:00 by exactly the failure you name.
#   3. Print the brief. Then critique it as a control-room engineer:
#        - what is the FIRST sentence, and is it a decision or a description?
#        - which numbers would you act on, and which are for the modeller?
#        - what does it tell you to do when it is wrong?
#   4. Write the jargon version and the decision version side by side:
#        "the p95 is X MW, MASE is 0.455, marginal coverage is 0.90"
#        vs
#        "set spinning reserve to X MW; expected peak is Y at 15:00; the gap is the
#         honest uncertainty and it is widest on hot days"
#
# HINT: every number in the jargon version is correct. That is the problem — none of
#       them is a decision, and a correct sentence nobody can act on is a failed one.''')) 

    # ---------------------------------------------------------------- task 5 --
    c.append(md("""### Task 5 — `DECISION_RECORD.md`

Seven sections, in this order. The order is the argument.

**1. The decision and its cost function.** *How much spinning reserve to hold for each hour of
tomorrow.* Under-forecasting buys emergency generation at a large multiple of the marginal
cost, and in the tail buys load shedding; over-forecasting buys idle capacity at the marginal
cost of holding it. The costs are asymmetric, so the object being decided is a **quantile**,
not a mean, and the model is selected on that basis.

**2. The candidates.** Seasonal-naive, ETS, SARIMAX + temperature, LightGBM + CQR (per area),
LightGBM + CQR (global). With the profile table.

**3. The constraints applied**, hard filters separated from weighted criteria — publication
deadline, explainability to the regulator, cost asymmetry, maintenance across four areas,
serve-time data availability (feature store, day-ahead temperature feed), and adoption by the
control room.

**4. The stated weights**, per scenario, written down before the scores were computed.

**5. The recommendation and its evidence.** The champion per scenario, with the Lab 6
Diebold-Mariano results attached: significant against the baseline (dm = -6.75, p < 0.001),
**not** significant between the two LightGBM variants (p = 0.058) — which is why the quantile
model is preferred over the marginally more accurate direct model in scenario B, and why
scenario C's 0.005 gap is reported as a tie.

**6. The flip-conditions.** Verbatim from `flip_conditions`, per scenario, plus the operational
ones: no day-ahead temperature feed removes SARIMAX + temperature; a fifth operating area
moves scenario C further towards the global model; a regulator accepting a documented
importance analysis re-admits LightGBM to scenario A.

**7. The monitoring contract**, which is the part that makes the recommendation survive
contact with production:

| what | how often | threshold | action |
|---|---|---|---|
| rolling MASE, 7-day and 28-day | weekly | 28-day MASE > 0.60 | investigate; > 0.77 (the baseline's own score) means fall back |
| empirical coverage of the 90% band | weekly | outside 0.85-0.95 for two consecutive weeks | re-estimate q̂ on the last 30 days |
| conditional coverage on the 12:00-18:00 block | weekly | below 0.85 | widen the peak-hour band; consider adaptive conformal |
| feature drift (temperature, weekly mean level) | weekly | new maximum outside the training range | expect extrapolation failure; trees cannot forecast a record high |
| retrain | monthly, and on any threshold breach | — | full refit, then re-run this backtest before promotion |
| champion / challenger | continuous | challenger beats champion on a DM test at 5% over 60 origins | promote; otherwise keep the incumbent |

**Say what the recommendation cannot do.** This backtest window contains no Eid, no summer
heatwave and no record peak. That absence is a finding, and naming it is what earns adoption:
a report that names the Eid weeks and ships a fallback should outscore a silent, marginally
sharper submission, because the second one will be overridden the first time it is wrong and
then ignored forever after. Candour is not a weakness in a recommendation; it is the thing
that makes it usable at 02:00."""))

    c.append(md(QUIZ7_A if sol else QUIZ7_Q))
    c.append(md(COMMIT7))

    if sol:
        c.append(md("""### Instructor notes

This lab folds directly into the capstone assembly. Whatever the room writes here is the
skeleton of their submission, so do not let it become a discussion — make them type.

- **Branch `sim-leaderboard`** ships the Task 1 fault alone: the pipeline reproduces, the
  argmin selects the direct LightGBM, and the deployment note says "publication job, batch, no
  feature store". Nothing errors. The fix is the constraint filter and a re-run of
  `recommend.score`, and the room should reach it without being told which line is wrong.
- **The communication drill** (10 minutes, at Task 4). Each pair rewrites the jargon summary
  into exactly **two** sentences of decision language — a hard limit; three sentences is a
  hedge. Then a participant plays the control-room engineer and pushes back with the three
  questions that always come: *what do I do differently because of this?*, *how wrong has it
  been lately?*, and *what do I do when it is wrong tonight?* A brief that cannot answer the
  third one gets sent back.
- **The walkthrough to tell before Task 2.** A utility promoted a gradient-boosted model on
  MASE alone. It was, on the evidence, the most accurate model they had. During an unusual load
  event the control-room engineer could not interrogate why it was forecasting what it was
  forecasting, so he overrode it — and then kept overriding it, and the model's realised skill
  in production went to zero. **The failure was the selection, not the model.** Nobody had
  weighted explainability, and nobody had asked the person who would have to act on it at
  02:00. Ask the room whose fault that was; the useful answer is that it was the selection
  criterion's.
- **Let them argue about the weights.** The weights are the only genuinely subjective input in
  this lab, and the argument is the point: a decision record exists so that a future reader can
  see what was assumed and challenge it. Time-box it to five minutes and require the numbers to
  be written down *before* the scores are computed.

**Troubleshooting**

| symptom | cause |
|---|---|
| the same champion in every scenario | the weights are barely different, or the hard filters are not being applied. Print the eligible set per scenario. |
| pipeline numbers differ from Lab 6 | a split date typed into a cell instead of read from the config, an unseeded model, or an unpinned LightGBM. Print the versions with the result. |
| `recommend` returns no candidate | the hard constraints are collectively unsatisfiable. That is a real finding — report it as "no candidate meets these constraints" and negotiate one of them, rather than quietly relaxing it. |
| the brief reads as jargon | rewrite it in reserve-margin terms, with the weakness named in the same paragraph as the recommendation. |
| flip_conditions prints nothing useful | the gap exceeds any single criterion's weight, i.e. no one-column move flips it. Say that — it is a strong result. |

**If a cohort is behind**, reduce Task 2 to two scenarios and demo the third from the front.
**Never drop the decision record.** A model without one is not deliverable, and the record is
what the capstone is actually assessed on."""))

    write(f"lab7_{tag}.ipynb", c)


for s in (False, True):
    lab6(s); lab7(s)
print("labs 6 and 7 written")
