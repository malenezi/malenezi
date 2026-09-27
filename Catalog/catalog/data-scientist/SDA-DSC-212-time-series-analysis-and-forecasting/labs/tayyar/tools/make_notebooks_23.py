"""Generate the Lab 2 and Lab 3 notebooks (start + solution).

Same house style as tools/make_notebooks.py — see notebooks/_SPEC.md.
Every printed number is the one produced by tools/run_reference.py and stored
in reference_results.json.
"""
import json, pathlib

NB = pathlib.Path("notebooks"); NB.mkdir(exist_ok=True)


def _lines(t):
    """Notebook source is a list of lines that must keep their newline terminators."""
    ls = t.rstrip().split(chr(10))
    return [l + chr(10) for l in ls[:-1]] + [ls[-1]]


def md(t): return {"cell_type": "markdown", "metadata": {}, "source": _lines(t)}


def code(t): return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
                     "source": _lines(t)}


def write(name, cells):
    # nbformat >= 4.5 requires a cell id; a stable per-notebook slug keeps the
    # regenerated JSON diff-clean and nbformat.validate silent.
    cells = [{**c, "id": f"c{i:02d}"} for i, c in enumerate(cells, 1)]
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python",
          "name": "python3"}, "language_info": {"name": "python", "version": "3.12"}},
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

# =========================================================== LAB 2 ==========
L2_TASKS = """### Tasks

| min | task |
|---|---|
| 8 | Run `stationarity_report` on the raw log-demand for 2023. Interpret ADF and KPSS **together**. Record the verdict and predict the differencing you will need. |
| 10 | `choose_differencing` with `m=24` — seasonal difference first, then regular. Print the trace and re-run the report to confirm stationarity was reached. |
| 10 | Plot before / after differencing. Check the lag-1 ACF for the over-differencing signature. Reduce `d` if you see it. |
| 12 | ACF / PACF with `lags >= 60`. Annotate the seasonal spike at lag 24. Read candidate `(p,q)` and seasonal `(P,Q)` off the fingerprint rules. |
| 10 | Write `STATIONARITY.md`: the verdict, the chosen `(d, D)`, and 2–3 candidate SARIMA orders with justification. Commit. |
"""

L2_RECAP = """from tayyar.data.load import load_demand, load_calendar, join_calendar

df = load_demand(f"{DATA}/ksa_grid_demand.csv")
df = join_calendar(df, load_calendar(f"{DATA}/ksa_calendar.csv"))

y = df["demand_mw"].astype(float)
ylog = np.log(y)          # variance first (Lab 1), mean second (this lab)
sub = ylog["2023"]        # one clean year — the tests stay fast and the plots stay readable

print(f"log-demand, 2023: {len(sub):,} hourly observations")
print(f"from {sub.index[0]} to {sub.index[-1]}")
"""

L2_NULLS = """### The two tests have opposite nulls

This is the single most common error in the room, so read it slowly.

| test | H0 (the null) | small p (< 0.05) means | large p means |
|---|---|---|---|
| **ADF** | there **is** a unit root — *non-stationary* | reject H0 → **evidence of stationarity** | cannot reject a unit root |
| **KPSS** | the series **is** stationary | reject H0 → **evidence of non-stationarity** | cannot reject stationarity |

A small p-value is good news from ADF and bad news from KPSS. Reconciling them:

| | KPSS says stationary | KPSS says non-stationary |
|---|---|---|
| **ADF says stationary** | `stationary` — proceed | `difference-stationary` — difference once and re-test |
| **ADF says non-stationary** | `trend-stationary` — detrend, or add a trend regressor | `non-stationary` — difference and re-test |

The disagreement cells are not a failure of the method. They are the reason we run both:
they separate a series that needs differencing from one that needs detrending.
"""

L2_T1_SOL = """from tayyar.analysis.stationarity import stationarity_report, format_report

r0 = stationarity_report(sub)
print(format_report(r0))
print()
print(f"ADF  p = {r0['adf_p']}  ->  reject 'unit root'      ->  evidence of STATIONARITY")
print(f"KPSS p = {r0['kpss_p']}  ->  reject 'is stationary'  ->  evidence of NON-STATIONARITY")
"""

L2_T1_START = """from tayyar.analysis.stationarity import stationarity_report, format_report

# TODO: run stationarity_report on `sub` and print it with format_report.
# Then write down, one sentence each:
#   1. what the ADF p-value ALONE would have you conclude,
#   2. what the KPSS p-value ALONE would have you conclude,
#   3. the reconciled verdict from the 2x2 table above,
#   4. your PREDICTION of (d, D) before Task 2 runs — commit to a number now.
#
# r0 = ...

# HINT: the nulls are opposite. Nearly every wrong answer in this room comes from
#       reading one test's p-value with the other test's null in mind.
"""

L2_T1_INTERP = """**Expected**

```
ADF  stat=  -3.103  p=0.0263  -> stationary
KPSS stat=   5.258  p=0.01    -> non-stationary
VERDICT: difference-stationary
ACTION : ADF stationary, KPSS not: a deterministic/level shift remains — difference once and re-test.
```

The tests disagree, and the disagreement is the finding. ADF can reject a unit root because
the daily cycle keeps pulling the series back towards its mean; KPSS still sees a level that
does not sit still across the year — summer runs far above winter. That combination is
`difference-stationary`: the remedy is a difference, not a detrend.

Note `kpss_p = 0.01`. KPSS p-values come from a lookup table and are clipped at the ends of
that table, so `0.01` means "at most 0.01" and `0.10` means "at least 0.10". statsmodels warns
about this in words; the warning is expected and is not an error.
"""

L2_PREDICT = """> **Stop and predict.** You have a strongly seasonal hourly series with an annual swing.
> Write down the `(d, D)` you expect `choose_differencing` to return before you run the next
> cell. Most pairs write `d=1, D=1`. Keep your prediction — you will need it in a minute.
"""

L2_T2_SOL = """from tayyar.analysis.differencing import choose_differencing, difference

diffs = choose_differencing(sub, m=24)      # seasonal difference FIRST, then regular

cols = ["d", "D", "adf_stat", "adf_p", "kpss_stat", "kpss_p", "verdict"]
print(diffs["trace"][cols].to_string(index=False))
print()
print(f"chosen: d={diffs['d']}, D={diffs['D']}, m={diffs['m']}  ->  {diffs['final_verdict']}")
print()

ds = difference(sub, diffs["d"], diffs["D"], m=24)
print(format_report(stationarity_report(ds)))
"""

L2_T2_START = """from tayyar.analysis.differencing import choose_differencing, difference

# TODO:
#   1. call choose_differencing(sub, m=24)
#   2. print the trace DataFrame — one row per differencing step, both p-values on each row
#   3. rebuild the differenced series with difference(sub, d, D, m=24)
#   4. re-run stationarity_report on it and confirm the verdict is "stationary"
#
# diffs = ...

# HINT: the routine takes the SEASONAL difference first and stops at the first
#       "stationary" verdict. Both of those are deliberate. Difference in the other
#       order, or keep going after the verdict flips, and you will spend a difference
#       you did not need — see Task 3 for what that costs.
"""

L2_T2_INTERP = """**Expected**

```
 d  D  adf_stat  adf_p  kpss_stat  kpss_p               verdict
 0  0    -3.103 0.0263      5.258    0.01 difference-stationary
 0  1   -15.823 0.0000      0.092    0.10            stationary

chosen: d=0, D=1, m=24  ->  stationary
```

**`d = 0`, `D = 1`.** One seasonal difference was enough; no regular difference was needed.

This surprises almost everyone, including people who have fitted ARIMA models for years —
the reflex is `d=1, D=1`. Read the trace and see why the reflex is wrong: `y_t - y_{t-24}`
removes both the daily cycle *and* the slow level movement, because consecutive days sit at
almost the same level. Having removed both, there is nothing left for a regular difference
to remove — only structure the AR terms should be estimating.

The rule the routine encodes: **stop at the first stationary verdict.** Not "difference until
it looks nice", not "difference the standard amount".
"""

L2_T3_SOL = """from statsmodels.tsa.stattools import acf

sl = slice("2023-06-01", "2023-06-30")
fig, ax = plt.subplots(2, 1, figsize=(11, 5))
sub[sl].plot(ax=ax[0], color="#1F3864", lw=.9)
ax[0].set_title("log-demand — level, June 2023 (mean drifts, variance drifts)")
ax[0].set_ylabel("log MW")
ds[sl].plot(ax=ax[1], color="#2E7D32", lw=.6)
ax[1].axhline(0, color="#C00000", lw=1)
ax[1].set_title(f"after D={diffs['D']}, d={diffs['d']} at m=24 — flat mean, stable spread")
ax[1].set_ylabel("seasonal difference")
plt.tight_layout()

# The over-differencing ladder: what each EXTRA regular difference would cost.
rows = []
for extra_d in (0, 1, 2):
    s = difference(sub, extra_d, 1, m=24)
    rows.append({"d": extra_d, "D": 1, "n": len(s),
                 "sd": round(float(s.std()), 5),
                 "variance": round(float(s.var()), 6),
                 "lag1_acf": round(float(acf(s, nlags=1, fft=True)[1]), 3)})
print(pd.DataFrame(rows).to_string(index=False))
print()
print("over-differencing signature: lag-1 ACF strongly negative (< -0.5) and variance rising")
"""

L2_T3_START = """from statsmodels.tsa.stattools import acf

# TODO:
#   1. two stacked panels for June 2023: the level series, then the differenced series.
#      Add a zero line to the second panel — a stationary series should sit on it.
#   2. build the over-differencing ladder: for extra_d in (0, 1, 2), difference the series
#      with that many regular differences ON TOP of D=1, and report n, sd, variance and
#      the lag-1 ACF of each.
#   3. decide from the table whether the chosen (d, D) is the minimal one.
#
# HINT: the over-differencing signature is a lag-1 ACF strongly negative (below -0.5)
#       together with a variance that has gone UP, not down. A difference that lowers the
#       variance is not automatically a difference worth taking — the stationarity verdict
#       decides, not the variance.
"""

L2_T3_INTERP = """**Expected**

```
 d  D    n      sd  variance  lag1_acf
 0  1 8736 0.05946  0.003535     0.898
 1  1 8735 0.02680  0.000718    -0.065
 2  1 8734 0.03910  0.001529    -0.508
```

Read the ladder honestly, because it does not say quite what the textbook slogan says.

- At `d=0` (our choice) the lag-1 ACF is **+0.898**. That is a lot of structure — and it is
  structure an AR term should *estimate*, not structure a difference should destroy. The
  tests already say stationary; we stop.
- At `d=1` the variance actually falls. This is the trap: the extra difference looks
  harmless, even flattering, so people take it. It is still a difference spent on nothing,
  and it converts an AR(1)-shaped series into one that needs an MA term to describe the
  same information.
- At `d=2` the damage is unmistakable: lag-1 ACF **−0.508** and the variance more than
  doubles, from 0.000718 to 0.001529. That is over-differencing in its textbook form —
  artificial negative autocorrelation injected at lag 1, and a noisier series than we
  started with. The `sim-overdiff` branch sits here, at roughly −0.6.

Every difference costs you an observation and adds an MA root you then have to model.
Difference as little as the tests allow.
"""

L2_T4_SOL = """from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from tayyar.analysis.correlograms import correlogram_table, suggest_orders, FINGERPRINT

fig, ax = plt.subplots(2, 2, figsize=(11, 6))
plot_acf(sub.dropna(), lags=72, ax=ax[0, 0])
ax[0, 0].set_title("ACF — level: slow, near-linear decay = non-stationary")
plot_pacf(sub.dropna(), lags=72, ax=ax[0, 1])
ax[0, 1].set_title("PACF — level: one huge spike at lag 1")
plot_acf(ds, lags=72, ax=ax[1, 0])
ax[1, 0].set_title(f"ACF — after D={diffs['D']}, d={diffs['d']}, m=24")
plot_pacf(ds, lags=72, ax=ax[1, 1])
ax[1, 1].set_title("PACF — after differencing")
for a in ax.ravel():
    a.axvline(24, color="#C00000", ls="--", lw=1)
    a.axvline(48, color="#C00000", ls=":", lw=.8)
    a.set_xlabel("lag (hours)")
ax[1, 0].annotate("m = 24", xy=(24, ax[1, 0].get_ylim()[1] * 0.7),
                  color="#C00000", fontsize=9)
plt.tight_layout()

tbl = correlogram_table(ds, nlags=72)
show = tbl[tbl.lag.isin([1, 2, 3, 4, 5, 23, 24, 25, 48, 72])]
print(show.round(3).to_string(index=False))
print()
print("suggest_orders:", suggest_orders(tbl, m=24))
print()
print(FINGERPRINT.to_string(index=False))
"""

L2_T4_START = """from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from tayyar.analysis.correlograms import correlogram_table, suggest_orders, FINGERPRINT

# TODO:
#   1. a 2x2 correlogram figure with lags=72 — ACF and PACF of the LEVEL series (top row)
#      and of the differenced series (bottom row). Mark lag 24 on every panel.
#   2. correlogram_table(ds, nlags=72); print the rows at lags 1-5, 23, 24, 25, 48, 72.
#   3. suggest_orders(tbl, m=24), then read the fingerprint table and decide whether you
#      agree with what it returned.
#
# HINT: the default in every plotting API is lags=20, which NEVER REACHES LAG 24. Ask for
#       at least 2*m or the seasonal structure you came here to find is off the right-hand
#       edge of the plot. And treat suggest_orders as a candidate generator, never a verdict:
#       with n=8736 the significance band is +/-0.021, so almost everything is "significant".
"""

L2_T4_INTERP = """**Expected**

```
 lag    acf   pacf  acf_significant  pacf_significant
   1  0.898  0.899             True              True
   2  0.810  0.015             True             False
   3  0.732  0.006             True             False
   4  0.661 -0.001             True             False
   5  0.602  0.029             True              True
  23 -0.146 -0.089             True              True
  24 -0.208 -0.099             True              True
  25 -0.179  0.402             True              True
  48 -0.264 -0.072             True              True
  72  0.002 -0.023            False              True

suggest_orders: {'p': 5, 'q': 5, 'P': 1, 'Q': 1, 'm': 24}
```

**Reading the regular part.** The ACF decays geometrically (0.898, 0.810, 0.732, 0.661, …)
while the PACF collapses from 0.899 to 0.015 at lag 2. ACF tails off, PACF cuts off after
lag 1: that is the AR fingerprint, `p = 1`, possibly `p = 2` if you want a little slack.

**Reading the seasonal part.** After a seasonal difference the ACF is negative around
lag 24 (−0.208) and at 48 (−0.264), with a sharp PACF spike at lag 25 (0.402). A negative
ACF at the seasonal lag after seasonal differencing is the classic seasonal MA signature:
`Q = 1`, `P = 0` or 1.

**Why `suggest_orders` said `p=5, q=5`.** It returns the largest *significant* lag inside
1–5, and with 8,736 observations the significance band is ±0.021 — a PACF value of 0.029 at
lag 5 clears it while being of no practical interest. This is exactly why the function's
docstring calls it "a first candidate, never a verdict". Automation proposes; the analyst
disposes, and then confirms with residual diagnostics.

**Candidate orders**, to be settled by AIC/BIC and Ljung-Box in Lab 3:

| candidate | why |
|---|---|
| `SARIMA(1,0,1)(0,1,1)[24]` | AR(1) from the PACF cut-off, seasonal MA(1) for the ACF trough at 24 — the default first fit |
| `SARIMA(2,0,0)(1,1,0)[24]` | the pure-AR reading, if you take the marginal PACF spike at lag 5 seriously |
| `SARIMA(1,0,0)(1,1,1)[24]` | the parsimonious one; if it is within ~2 AIC of the others, ship it |

All three keep `d=0` and `D=1`. Never compare their AIC against a model with a different
`d` — the likelihoods are computed on different data.
"""

L2_QUIZ_Q = """### Mini-quiz — answer before you open the solution notebook

1. ADF returns p = 0.01. Stationary or not?
2. KPSS returns p = 0.01. Stationary or not?
3. For a seasonal series, which differencing comes first — seasonal or regular?
4. The ACF tails off and the PACF cuts off after lag 2. What model and order?
5. A slowly, almost linearly decaying ACF indicates what?
"""

L2_QUIZ_A = """### Mini-quiz

1. **ADF p = 0.01 — stationary or not?** Evidence of *stationary*: reject the unit-root null.
2. **KPSS p = 0.01 — stationary or not?** Evidence of *non-stationary*: reject the stationarity null.
3. **Seasonal or regular differencing first?** Seasonal, then re-test — it often removes the
   trend as well, as it did here.
4. **ACF tails off, PACF cuts off after lag 2?** AR(2).
5. **A slowly, linearly decaying ACF?** A trend — the series is non-stationary. Difference it
   before reading the correlogram any further; that shape is not a high AR order.
"""

L2_DELIV_START = """### Task 5 — `STATIONARITY.md`

Write the file. Four sections, no more:

1. **Verdict on the level series** — both p-values, and the reconciled verdict in words.
2. **Chosen `(d, D)` and `m`**, with the trace that justifies stopping there.
3. **Evidence that you did not over-difference** — the lag-1 ACF and the variance ladder.
4. **Two or three candidate SARIMA orders**, each with the correlogram feature that
   suggested it.

```
git add -A && git commit -m "feat(analysis): stationarity report + candidate SARIMA orders"
```
"""

L2_DELIV_SOL = """### Task 5 — `STATIONARITY.md`

```markdown
# Stationarity report — Tayyar log-demand, 2023

## 1. Verdict on the level series
ADF  stat = -3.103, p = 0.0263  -> reject unit root, evidence of stationarity
KPSS stat =  5.258, p = 0.01    -> reject stationarity, evidence of non-stationarity
VERDICT: difference-stationary. The level moves across the year even though the daily
cycle keeps pulling the series back to a local mean. Remedy is a difference, not a detrend.

## 2. Chosen differencing
d = 0, D = 1, m = 24.
Trace: (d=0, D=0) ADF 0.0263 / KPSS 0.01 -> difference-stationary
       (d=0, D=1) ADF 0.0000 / KPSS 0.10 -> stationary  <- stop here
One seasonal difference removed both the daily cycle and the slow level movement.
No regular difference is required; the reflexive d=1 would be a difference spent on nothing.

## 3. Evidence against over-differencing
d=0: sd 0.05946, var 0.003535, lag-1 ACF +0.898
d=1: sd 0.02680, var 0.000718, lag-1 ACF -0.065
d=2: sd 0.03910, var 0.001529, lag-1 ACF -0.508   <- variance rising, ACF turning negative
The +0.898 at d=0 is AR structure for the model to estimate, not a reason to difference again.

## 4. Candidate SARIMA orders
SARIMA(1,0,1)(0,1,1)[24] - ACF tails off geometrically, PACF cuts off after lag 1 (AR(1));
                           ACF negative at lags 24 and 48 after seasonal differencing (seasonal MA(1)).
SARIMA(2,0,0)(1,1,0)[24] - pure-AR reading, taking the marginal PACF spike at lag 5.
SARIMA(1,0,0)(1,1,1)[24] - parsimonious; prefer it if within ~2 AIC of the others.
All three share d=0, D=1 so their AIC values are comparable with each other and with nothing else.
Confirm the winner with Ljung-Box on the residuals, not with AIC alone.
```

```
git add -A && git commit -m "feat(analysis): stationarity report + candidate SARIMA orders"
```
"""

L2_INSTR = """### Instructor notes

- The `(d=0, D=1)` result is the lesson of this lab. Ask for the prediction in writing before
  Task 2 runs; most of the room writes `d=1, D=1` and the gap between the prediction and the
  trace is what makes the "difference as little as possible" rule stick.
- Branch `sim-overdiff` differences twice where once suffices. Do not announce it — give the
  pair the series and let them diagnose it from the lag-1 ACF near −0.6 and the inflated
  variance. The fix is to drop back one `d`, not to add an MA term to compensate.
- The statsmodels KPSS warning "p-value is greater than the indicated p-value" is **expected**
  and means p > 0.1. It is not an error, and the `0.01` at the other end means p < 0.01.
  Every cohort loses a few minutes to this warning unless you call it out first.
- `lags=20` is the default in every plotting API in the stack and **never reaches lag 24**.
  A pair that reports "no seasonal structure" has almost certainly left the default in place.
- Run the ACF/PACF speed round after Task 4: six anonymised correlogram pairs (AR, MA, ARMA,
  seasonal, white noise, non-stationary), 30 seconds each, called out loud. It is the fastest
  way to turn the fingerprint table from something read into something recognised.
- Fast finishers: run `choose_differencing` on the raw (un-logged) series and on 2021 alone,
  and explain why the verdict can change with the window. Regime shifts are why this report is
  re-run on a schedule in production, not written once.
"""


def lab2():
    for tag, sol in (("start", False), ("solution", True)):
        c = [md(HDR.format(n=2, title="The Stationarity Report", dur=50, tag=tag)),
             md(L2_TASKS), code(SETUP),
             md("Lab 1's output, reloaded — the labs are independent notebooks."),
             code(L2_RECAP),
             md("### Task 1 — ADF and KPSS, read together"),
             md(L2_NULLS)]
        c.append(code(L2_T1_SOL if sol else L2_T1_START))
        if sol:
            c.append(md(L2_T1_INTERP))
        c.append(md(L2_PREDICT))
        c.append(md("### Task 2 — the minimum differencing, seasonal first"))
        c.append(code(L2_T2_SOL if sol else L2_T2_START))
        if sol:
            c.append(md(L2_T2_INTERP))
        c.append(md("### Task 3 — before / after, and the over-differencing check"))
        c.append(code(L2_T3_SOL if sol else L2_T3_START))
        if sol:
            c.append(md(L2_T3_INTERP))
        c.append(md("### Task 4 — ACF and PACF: the model fingerprint"))
        c.append(code(L2_T4_SOL if sol else L2_T4_START))
        if sol:
            c.append(md(L2_T4_INTERP))
        c.append(md(L2_QUIZ_A if sol else L2_QUIZ_Q))
        c.append(md(L2_DELIV_SOL if sol else L2_DELIV_START))
        if sol:
            c.append(md(L2_INSTR))
        write(f"lab2_{tag}.ipynb", c)


# =========================================================== LAB 3 ==========
L3_TASKS = """### Tasks

| min | task |
|---|---|
| 5 | Aggregate the hourly series to **daily max** — the reserve-margin question is about the peak. Restrict to 2022 onward, build the exogenous frame (`cdd`, `hdd`, `is_weekend`, `is_ramadan`, `is_eid`), hold out the last 28 days. |
| 12 | Fit SARIMAX `(2,1,1)(1,1,1)[7]`. Explain why `m=7` on a daily series rather than `m=24` on the hourly one. Run `residual_diagnostics` and report Ljung-Box honestly. |
| 10 | Fit ETS with `fit_ets` (damped trend, `seasonal_periods=7`). Sweep the taxonomy with `ets_grid` by AIC. State when AIC comparisons are valid. |
| 10 | Forecast 28 days from both with 90% intervals. SARIMAX needs the **future** exogenous rows. Plot both forecasts against the held-out actuals. |
| 8 | MAE / MAPE / MASE and 90% coverage for each. Fit a no-exogenous SARIMA to price what temperature is worth. Compute the seasonal-naive baseline. |
| 5 | Commit. |
"""

L3_RECAP = """from tayyar.data.load import load_demand, load_calendar, join_calendar

df = load_demand(f"{DATA}/ksa_grid_demand.csv")
df = join_calendar(df, load_calendar(f"{DATA}/ksa_calendar.csv"))
y = df["demand_mw"].astype(float)

print(f"hourly rows: {len(y):,}   from {y.index[0]} to {y.index[-1]}")
"""

L3_WHY_DAILY = """### Task 1 — the daily-max series, the exogenous frame, and the hold-out

Two decisions here, both of which encode the question rather than the data.

**Daily *max*, not daily mean.** The deliverable is a reserve margin. A control room sizes
reserve against the peak the system must carry, not against the average it happens to run at.
Aggregating with `.mean()` would answer a question nobody asked, and would answer it about
5,000 MW too low.

**`m = 7` on a daily series, not `m = 24` on the hourly one.** This is a wall you should walk
into deliberately. SARIMA's state space grows with the seasonal period: at `m=24` the
state vector is large enough that estimation slows from seconds to many minutes, and
`auto_arima` with `m=24` may simply never converge on this series. The classical route
therefore models the *daily* series with a weekly cycle, `m=7`, and leaves the sub-daily
structure to the feature-based ML route in Module 4. That hand-off is not an admission of
defeat; it is the honest boundary of the classical toolkit, and knowing where it sits is
part of the learning outcome.
"""

L3_T1_SOL = """d_daily = y.resample("D").max()          # the PEAK, because the question is reserve margin
d_daily = d_daily["2022":]                # two years is plenty for a daily model

exog = pd.DataFrame({
    "cdd":        np.clip(df["temp_c"].resample("D").max() - 21.0, 0, None),
    "hdd":        np.clip(14.0 - df["temp_c"].resample("D").min(), 0, None),
    "is_weekend": df["is_weekend"].resample("D").max().astype(int),
    "is_ramadan": df["is_ramadan"].resample("D").max().astype(int),
    "is_eid":     df["is_eid"].resample("D").max().astype(int),
})

H = 28
tr, te = d_daily[:-H], d_daily[-H:]
Xtr, Xte = exog.loc[tr.index], exog.loc[te.index]

print(f"daily-max series : {len(d_daily)} days, {d_daily.index[0].date()} to {d_daily.index[-1].date()}")
print(f"train            : {len(tr)} days  (to {tr.index[-1].date()})")
print(f"hold-out         : {len(te)} days  (from {te.index[0].date()})")
print(f"exog columns     : {list(Xtr.columns)}")
print()
print(Xtr.tail(3).round(2).to_string())
"""

L3_T1_START = """# TODO:
#   1. aggregate y to a DAILY series. Which aggregation answers a reserve-margin question?
#   2. restrict to 2022 onward.
#   3. build the exogenous frame with exactly these columns:
#        cdd        = max(daily max temp - 21, 0)     cooling-degree signal
#        hdd        = max(14 - daily min temp, 0)     heating-degree signal
#        is_weekend, is_ramadan, is_eid               daily flags, as int
#   4. hold out the last 28 days as `te`; everything before is `tr`. Slice the exog to match.
#
# HINT: aggregation encodes the question. `.mean()` and `.max()` are not two ways of saying
#       the same thing — the reserve margin is sized against the peak. Note also that cdd
#       uses the daily MAX temperature and hdd the daily MIN: each degree-day should be
#       built from the extreme that actually drives the load.
"""

L3_T1_INTERP = """**Expected**

```
daily-max series : 730 days, 2022-01-01 to 2023-12-31
train            : 702 days  (to 2023-12-03)
hold-out         : 28 days  (from 2023-12-04)
exog columns     : ['cdd', 'hdd', 'is_weekend', 'is_ramadan', 'is_eid']
```
"""

L3_T2_SOL = """from tayyar.models.sarimax import fit_sarimax, forecast_sarimax, residual_diagnostics

sar = fit_sarimax(tr, Xtr, order=(2, 1, 1), seasonal_order=(1, 1, 1, 7))

print("exogenous coefficients (MW per unit):")
print(sar.params[list(Xtr.columns)].round(1).to_string())
print()

diag = residual_diagnostics(sar, lags=14)
for k, v in diag.items():
    print(f"{k:<26} {v}")
"""

L3_T2_START = """from tayyar.models.sarimax import fit_sarimax, forecast_sarimax, residual_diagnostics

# TODO:
#   1. fit SARIMAX on `tr` with `Xtr`, order=(2,1,1), seasonal_order=(1,1,1,7).
#   2. print the exogenous coefficients — each is MW per unit of that regressor, so they
#      are readable out loud to an engineer. Sanity-check the sign of every one.
#   3. run residual_diagnostics(sar, lags=14) and print it in full.
#   4. report the Ljung-Box result HONESTLY, whatever it says. Do not quietly move on.
#
# HINT: do not be tempted to raise m to 24 and fit the hourly series. The state space grows
#       with m; the fit goes from seconds to many minutes and may not converge at all. The
#       daily series with m=7 is the classical route; sub-daily structure is Module 4's job.
"""

L3_T2_INTERP = """**Expected**

```
exogenous coefficients (MW per unit):
cdd            653.6
hdd             52.7
is_weekend       0.8
is_ramadan    1129.9
is_eid       -4139.4

ljung_box_p                0.0
residual_autocorrelation   True
verdict                    UNDER-SPECIFIED: structure remains in residuals
jarque_bera_p              0.0
aic                        11443.8
bic                        11493.6
```

The coefficients read out loud without translation: every cooling-degree-day above 21 °C adds
about **654 MW** to the daily peak; Ramadan adds about **1,130 MW**; Eid takes about
**4,139 MW** off. That sentence is the reason classical models survive in control rooms.

Now the uncomfortable part, and we are going to state it plainly rather than bury it.
**Ljung-Box p = 0.00.** The null is "the residuals are independent", and we reject it. Our own
model, fitted with the orders this course taught you to read off a correlogram, leaves
autocorrelation in its residuals. By the standard this course set in Module 3, the model is
**under-specified**. Jarque-Bera also rejects normality, which means the 90% interval is an
approximation resting on an assumption the residuals do not honour.

We are not going to pretend otherwise, and we are not going to grind through order after order
to chase the p-value above 0.05. The honest reading is that a daily SARIMAX with five
regressors cannot capture everything driving this series — the sub-daily shape, the nonlinear
temperature response, the interaction between the two. That is precisely the gap the
feature-based ML route in Module 4 exists to fill. A model that fails its own diagnostic and
says so is worth more than one that passes because nobody ran the test.
"""

L3_DIAG_PLOT = """fig = sar.plot_diagnostics(figsize=(11, 6), lags=28)
plt.tight_layout()
"""

L3_T3_SOL = """from tayyar.models.ets import fit_ets, forecast_ets, ets_grid

ets = fit_ets(tr, seasonal_periods=7)      # trend="add", damped=True, seasonal="add"

par = {k: v for k, v in ets.params.items() if np.isscalar(v)}
for k in ("smoothing_level", "smoothing_trend", "smoothing_seasonal", "damping_trend"):
    print(f"{k:<20} {par[k]:.4f}")
print(f"{'aic':<20} {ets.aic:.1f}")
print()

print(ets_grid(tr, seasonal_periods=7).to_string(index=False))
"""

L3_T3_START = """from tayyar.models.ets import fit_ets, forecast_ets, ets_grid

# TODO:
#   1. fit_ets(tr, seasonal_periods=7). The defaults are trend="add", damped=True,
#      seasonal="add" — an ETS(A,Ad,A). Print alpha, beta, gamma, phi and the AIC.
#   2. run ets_grid(tr, seasonal_periods=7) and read the AIC ranking.
#   3. write one sentence on when those AIC values may be compared and when they may not.
#
# HINT: AIC is comparable ONLY across models fitted to the same target — same
#       transformation, same length, same differencing. Comparing the AIC of a model fitted
#       to log(y) against one fitted to y, or a d=0 model against a d=1 model, is comparing
#       likelihoods computed on different data. The number will still print. It will still
#       be meaningless.
"""

L3_T3_INTERP = """**Expected**

```
smoothing_level      0.2638
smoothing_trend      0.0260
smoothing_seasonal   0.0000
damping_trend        0.9912
aic                  10532.0

trend seasonal  damped     aic
  add      mul    True 10511.6
  add      mul   False 10511.7
  NaN      mul   False 10518.3
  add      add    True 10532.0
  NaN      add   False 10538.6
  add      add   False 10540.9
  add      NaN   False 10898.3
  add      NaN    True 10898.3
  NaN      NaN   False 10914.6
```

`phi = 0.991` — the damping is mild but present, and it is what stops a 28-day horizon from
running off. `gamma = 0.000` says the weekly seasonal factors, once initialised, barely need
updating: the weekly shape of the peak is stable.

The sweep prefers **ETS(A,Ad,M)**, multiplicative seasonality, by about 20 AIC over the
additive fit we are carrying forward. That is a real gap, not noise, and on a series whose
swing grows with its level it is the expected answer. Note what makes the multiplicative fit
*available* at all: the daily-max series contains no zeros. Try the same sweep on the raw
hourly series with its sensor dropouts and every multiplicative row fails.

**When may these AICs be compared?** Only down this column, because every row was fitted to
the same untransformed 702-day target. Never against the SARIMAX AIC above (different model
class, different likelihood), never against a model fitted to `log(y)`, and never across
different `d`.
"""

L3_EXOG_POINT = """### Task 4 — 28-day forecasts with 90% intervals

`get_forecast(steps=28, exog=...)` needs **exactly 28 rows of future exogenous values**. That
requirement is not an API inconvenience, it is the definition of an exogenous regressor:
temperature qualifies only because a day-ahead weather forecast exists. If you have to wait
for the realised value, the variable cannot be used, and using the realised value anyway is a
leak that looks like skill — the model gets tomorrow's temperature for free and reports a MAE
no production system could reproduce.

For reproducibility in this lab we pass the realised temperatures, so the numbers here are a
mild optimistic bound: they price what temperature is worth *given a perfect forecast of it*.
`data/temp_forecast_28d.csv` holds the actual day-ahead forecast series; substituting it is
the fast-finisher extension, and the MAE gap you measure is the cost of the weather
forecast's own error propagating into yours.
"""

L3_T4_SOL = """f_sar = forecast_sarimax(sar, H, Xte, alpha=0.10)     # 90% interval
f_ets = forecast_ets(ets, H)

fig, ax = plt.subplots(figsize=(11, 4.6))
tr[-60:].plot(ax=ax, color="#7F7F7F", lw=1, label="train (last 60 d)")
te.plot(ax=ax, color="#1F3864", lw=2, label="actual (held out)")
ax.fill_between(f_sar.index, f_sar["lo"], f_sar["hi"], color="#8FAADC", alpha=.45,
                label="SARIMAX 90% interval")
f_sar["yhat"].plot(ax=ax, color="#C00000", lw=1.8, label="SARIMAX + temp + calendar")
f_ets.plot(ax=ax, color="#2E7D32", lw=1.8, ls="--", label="ETS(A,Ad,A)")
ax.set_ylabel("daily peak MW")
ax.set_title("28-day daily-peak forecast against the held-out actuals")
ax.legend(frameon=False, ncols=3, fontsize=8)
plt.tight_layout()

print(pd.DataFrame({"actual": te, "sarimax": f_sar["yhat"].round(0),
                    "ets": f_ets.round(0)}).head(7).to_string())
"""

L3_T4_START = """# TODO:
#   1. forecast_sarimax(sar, H, Xte, alpha=0.10)  -> yhat, lo, hi at 90%
#   2. forecast_ets(ets, H)
#   3. one figure: the last 60 training days, the 28 held-out actuals, both forecasts,
#      and the SARIMAX 90% band shaded.
#
# HINT: get_forecast needs EXACTLY `steps` rows of future exog. If it raises, count the rows
#       in your Xte. And read the paragraph above before you reach for the realised
#       temperatures in production code.
"""

L3_T4_INTERP = """The SARIMAX track sits on the actuals through the whole window and the band is narrow
enough to be useful. The ETS track runs visibly high — hold that thought until the bias
column in Task 5.
"""

L3_T5_SOL = """from tayyar.eval.metrics import all_metrics

# What is temperature worth? Fit the same model with no exogenous regressors at all.
sar_noex = fit_sarimax(tr, None, order=(2, 1, 1), seasonal_order=(1, 1, 1, 7))
f_noex = forecast_sarimax(sar_noex, H, None, alpha=0.10)

# And the free baseline everything must beat.
sn = pd.Series([tr.iloc[-7:].to_numpy()[i % 7] for i in range(H)], index=te.index)

rows = {
    "SARIMAX + temp + calendar": f_sar["yhat"],
    "SARIMA (no exog)":          f_noex["yhat"],
    "ETS(A,Ad,A) damped":        f_ets,
    "Seasonal-naive (m=7)":      sn,
}
tbl = pd.DataFrame({k: all_metrics(te, v, tr, 7) for k, v in rows.items()}).T
print(tbl[["MAE", "RMSE", "MAPE_%", "MASE", "bias"]].to_string())
print()

def coverage(f):
    inside = (te.to_numpy() >= f["lo"].to_numpy()) & (te.to_numpy() <= f["hi"].to_numpy())
    return round(float(inside.mean()), 3), round(float((f["hi"] - f["lo"]).mean()), 1)

for name, f in (("SARIMAX + temp + calendar", f_sar), ("SARIMA (no exog)", f_noex)):
    cov, width = coverage(f)
    print(f"{name:<26} 90% coverage {cov:<6} mean interval width {width:>8.1f} MW")
print(f"{'ETS(A,Ad,A) damped':<26} 90% coverage    n/a   "
      f"— the Holt-Winters API returns no analytic interval")
"""

L3_T5_START = """from tayyar.eval.metrics import all_metrics

# TODO:
#   1. fit the SAME SARIMAX with exog=None — this prices what temperature is worth.
#   2. build the seasonal-naive forecast at m=7 (last week repeated four times).
#   3. one table: MAE, RMSE, MAPE_%, MASE and bias for all four forecasts.
#      all_metrics(te, forecast, tr, 7) gives you the row; MASE needs the training series.
#   4. 90% coverage AND mean interval width for every model that produces an interval.
#
# HINT: coverage on its own is not a quality measure. An interval 10,000 MW wide will cover
#       100% of anything and be worth nothing. Report coverage and width together — Module 5
#       makes this precise with the interval score.
"""

L3_T5_INTERP = """**Expected**

```
                             MAE    RMSE  MAPE_%    MASE   bias
SARIMAX + temp + calendar  666.2   826.4    2.05  0.3325   36.7
SARIMA (no exog)           686.0   843.6    2.14  0.3424  142.3
ETS(A,Ad,A) damped         868.5  1036.5   2.682  0.4335  782.4
Seasonal-naive (m=7)      2609.0  3040.1   8.115  1.3021 2534.0

SARIMAX + temp + calendar  90% coverage 0.964  mean interval width   3875.3 MW
SARIMA (no exog)           90% coverage 1.0    mean interval width   8896.1 MW
ETS(A,Ad,A) damped         90% coverage    n/a — the Holt-Winters API returns no analytic interval
```

**MASE first.** Every model beats the free seasonal-naive baseline (MASE 1.302), and beats it
by a wide margin. That is the only sentence in this table that establishes the models are
worth running at all.

**Now look at the bias column, not the MAE column.** The no-exogenous model runs **+142 MW
high** on average; adding temperature and the calendar pulls that to **+37 MW**. A biased
forecast is not an occasional error, it is the same error every single day: a reserve margin
sized on a forecast that is systematically 142 MW high is 142 MW of capacity held, paid for
and never used, every day of the year. The MAE improvement from temperature is a modest 20 MW;
the bias improvement is 105 MW and matters more to the operator.

**What temperature is actually worth is in the intervals.** Coverage 0.964 versus 1.000 looks
like the no-exog model winning until you read the width beside it: 3,875 MW against
8,896 MW. Both intervals cover; one of them is **2.3 times wider**, and the reserve margin is
set from the upper bound. Knowing tomorrow's temperature halves the width of the band the
control room must hold capacity against. That, not the MAE, is the business case.

**ETS runs +782 MW high** across the window — a damped additive trend fitted to two years that
end in a rising December simply carries that rise forward. It is the fastest model here and it
needs no exogenous data at all, which is exactly why it is the right choice for a thousand
series and the wrong choice for this one.
"""

L3_QUIZ_Q = """### Mini-quiz — answer before you open the solution notebook

1. What do `p`, `d` and `q` control in an ARIMA model?
2. What is `m` for a daily cycle on hourly data?
3. Why must exogenous regressors be known at forecast time?
4. What does Ljung-Box `p < 0.05` on the residuals mean?
5. When is a damped trend preferable to an undamped one?
"""

L3_QUIZ_A = """### Mini-quiz

1. **What do p, d, q control?** The AR order, the differencing order, and the MA order.
2. **`m` for a daily cycle on hourly data?** 24. (And on this lab's *daily* series, the weekly
   cycle gives `m = 7`.)
3. **Why must exogenous regressors be known at forecast time?** Because forecasting `steps`
   ahead requires their future values. If you cannot obtain them ahead of time the regressor is
   simply unavailable; if you substitute the realised value you have built a leak that will
   report skill you cannot reproduce in production.
4. **Ljung-Box p < 0.05?** Residual autocorrelation remains — there is structure the model has
   not captured. The model is under-specified; raise an order, or accept and document the
   limitation as we did above.
5. **When is a damped trend preferable?** Almost always, and especially for multi-step
   horizons. An undamped linear trend extrapolated far enough produces a confidently absurd
   number.
"""

L3_DELIV = """### Task 6 — commit

The deliverable is the comparison table with the bias and interval-width columns intact, plus
one honest paragraph on the Ljung-Box result. Do not drop the failing diagnostic from the
write-up.

```
git add -A && git commit -m "feat(models): SARIMAX + ETS baselines with intervals and diagnostics"
```
"""

L3_INSTR = """### Instructor notes

- The Ljung-Box failure is the centrepiece of this lab, not an embarrassment to manage. Say it
  out loud: the course's own model fails a test the course taught, and the participants found
  it by running the diagnostic they were told to run. Then draw the line straight to Module 4 —
  the ML route exists because this wall is real. A cohort that watches an instructor report a
  failed diagnostic honestly will report their own.
- Branch `sim-aic-trap` compares AIC across models with different `d` and declares the wrong
  winner. Let a pair defend the winner before you intervene. The fix is not a better search;
  it is understanding that likelihoods computed on differently-differenced data are not
  commensurable, so the comparison never had meaning to begin with.
- Branch `sim-nodamp` forecasts 90 days with an undamped Holt trend and arrives at a peak
  demand the Central Operating Area could not physically carry. Ask what the operator would do
  with that number before you show the fix (`damped_trend=True`).
- Run "explain it to the control room" after Task 5, 10 minutes: each pair writes ONE sentence
  explaining the SARIMAX forecast to a shift engineer. Then strike out every sentence
  containing the word "parameter". What survives is usually the coefficient sentence — 654 MW
  per cooling-degree-day, 1,130 MW for Ramadan, −4,139 MW for Eid — which is the point.
- Troubleshooting:

  | symptom | cause | fix |
  |---|---|---|
  | `auto_arima` runs for minutes and never finishes | `m=24` on the hourly series | model the daily series with `m=7`; leave sub-daily to Module 4 |
  | Ljung-Box p < 0.05 | model under-specified | raise an order — and if it still fails, document it rather than hide it |
  | forecast diverges to implausible values | undamped trend | `damped_trend=True` |
  | `ConvergenceWarning: Maximum Likelihood optimization failed to converge` | the (2,1,1)(1,1,1)[7] likelihood is flat in places | expected on this series; the fit is usable, but it is a second hint the specification is not ideal |
  | `get_forecast` raises on the exog | wrong number of future rows | supply exactly `steps` rows of future exog, indexed to the forecast dates |
  | multiplicative ETS fails to fit | the series contains a zero | multiplicative seasonality needs strictly positive data — the hourly series has sensor zeros, the daily max does not |

- Fast finishers: rebuild `Xte` from `data/temp_forecast_28d.csv` instead of the realised
  temperatures and re-measure. The MAE gap between the two runs is the cost of the weather
  forecast's own error propagating into the load forecast — the number the case study asks
  them to widen the interval for.
"""


def lab3():
    for tag, sol in (("start", False), ("solution", True)):
        c = [md(HDR.format(n=3, title="Classical Baselines: SARIMAX and ETS", dur=50, tag=tag)),
             md(L3_TASKS), code(SETUP),
             md("Lab 1's output, reloaded — the labs are independent notebooks."),
             code(L3_RECAP),
             md(L3_WHY_DAILY)]
        c.append(code(L3_T1_SOL if sol else L3_T1_START))
        if sol:
            c.append(md(L3_T1_INTERP))
        c.append(md("### Task 2 — SARIMAX (2,1,1)(1,1,1)[7], and an honest residual check"))
        c.append(code(L3_T2_SOL if sol else L3_T2_START))
        if sol:
            c.append(md(L3_T2_INTERP))
            c.append(code(L3_DIAG_PLOT))
        c.append(md("### Task 3 — ETS, and the rules for reading an AIC"))
        c.append(code(L3_T3_SOL if sol else L3_T3_START))
        if sol:
            c.append(md(L3_T3_INTERP))
        c.append(md(L3_EXOG_POINT))
        c.append(code(L3_T4_SOL if sol else L3_T4_START))
        if sol:
            c.append(md(L3_T4_INTERP))
        c.append(md("### Task 5 — the scoreboard: accuracy, bias and interval width"))
        c.append(code(L3_T5_SOL if sol else L3_T5_START))
        if sol:
            c.append(md(L3_T5_INTERP))
        c.append(md(L3_QUIZ_A if sol else L3_QUIZ_Q))
        c.append(md(L3_DELIV))
        if sol:
            c.append(md(L3_INSTR))
        write(f"lab3_{tag}.ipynb", c)


lab2()
lab3()
print("labs 2 and 3 written")
