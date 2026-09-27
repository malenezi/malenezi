"""Generate the 7 lab notebooks (start + solution) and the leakage failure exercise."""
import json, pathlib
NB = pathlib.Path("notebooks"); NB.mkdir(exist_ok=True)


def _lines(t):
    """Notebook source is a list of lines that must keep their newline terminators."""
    ls = t.rstrip().split(chr(10))
    return [l + chr(10) for l in ls[:-1]] + [ls[-1]]

def md(t): return {"cell_type":"markdown","metadata":{},"source":_lines(t)}
def code(t): return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],
                     "source":_lines(t)}
def write(name, cells):
    # nbformat >= 4.5 requires a cell id; a stable per-notebook slug keeps the
    # regenerated JSON diff-clean and nbformat.validate silent.
    cells = [{**c, "id": f"c{i:02d}"} for i, c in enumerate(cells, 1)]
    nb={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python",
        "name":"python3"},"language_info":{"name":"python","version":"3.12"}},
        "nbformat":4,"nbformat_minor":5}
    (NB/name).write_text(json.dumps(nb, indent=1))

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

# =========================================================== LAB 1 ==========
L1_TASKS = """### Tasks

| min | task |
|---|---|
| 5 | Load the raw CSV. Confirm the duplicate and out-of-order timestamps. **Note the row count before cleaning.** |
| 10 | Implement / call `load_demand`: de-duplicate, sort, localise to `Asia/Riyadh`, `asfreq("h")`. Report gap rows and the longest gap. |
| 10 | Impute gaps ≤ 3 h by time interpolation; flag longer gaps. Plot one summer week and one winter week. |
| 10 | Decide additive vs multiplicative with `additive_or_multiplicative`. Justify from the amplitude evidence. |
| 10 | Run MSTL for daily + weekly seasonality. Compute `seasonal_strength` for each. Four-panel figure. |
| 5 | Write three bullets in `FINDINGS.md`. Commit. |
"""
for tag, sol in (("start", False), ("solution", True)):
    c=[md(HDR.format(n=1, title="Load, Index and Decompose the Tayyar Series", dur=50, tag=tag)),
       md(L1_TASKS), code(SETUP)]
    c.append(md("### Task 1 — how messy is the raw file?"))
    c.append(code('''raw = pd.read_csv(f"{DATA}/ksa_grid_demand.csv", parse_dates=["timestamp"])
print("raw rows          :", f"{len(raw):,}")
print("duplicate stamps  :", int(raw.timestamp.duplicated().sum()))
print("monotonic         :", raw.timestamp.is_monotonic_increasing)
print("zero demand rows  :", int((raw.demand_mw == 0).sum()))
raw.head()'''))
    c.append(md("> **Stop and predict.** How many rows do you expect after cleaning — more, fewer, or the same? Write your answer down before running the next cell."))
    c.append(md("### Task 2 — the clean, explicitly-indexed series"))
    if sol:
        c.append(code('''from tayyar.data.load import load_demand, load_calendar, join_calendar

df = load_demand(f"{DATA}/ksa_grid_demand.csv")
cal = load_calendar(f"{DATA}/ksa_calendar.csv")
df = join_calendar(df, cal)

print(f"rows in the raw file        : {df.attrs['n_raw_rows']:,}")
print(f"rows after asfreq('h')      : {len(df):,}")
print(f"missing hours materialised  : {df.attrs['n_missing']}")
print(f"longest single gap          : {df.attrs['longest_gap_h']} hours")
print(f"short gaps interpolated     : {int(df.is_imputed.sum())}")
print()
print("index is monotonic :", df.index.is_monotonic_increasing)
print("index is unique    :", df.index.is_unique)
print("index freq         :", df.index.freq)
print("index tz           :", df.index.tz)'''))
        c.append(md("The clean series has **more** rows than the raw file. The missing hours were never *in* the file — they were absent, not null. `asfreq` is the line that makes them visible."))
    else:
        c.append(code('''from tayyar.data.load import load_demand, load_calendar, join_calendar

# TODO: load the messy CSV into a clean, tz-aware hourly frame.
# Do it in this order — any other order loses data silently:
#   1. parse timestamps      2. drop duplicate timestamps (keep last)
#   3. sort                  4. set_index + tz_localize("Asia/Riyadh")
#   5. asfreq("h")   <-- the line that materialises the gaps
#   6. treat demand_mw == 0 as missing (sensor dropouts)
#
# df = ...

# Then report:
#   rows before / rows after / number of missing hours / longest gap'''))
    c.append(md("### Task 3 — a summer week and a winter week"))
    c.append(code('''y = df["demand_mw"].astype(float)

fig, ax = plt.subplots(2, 1, figsize=(11, 5), sharey=True)
y["2023-07-09":"2023-07-16"].plot(ax=ax[0], color="#C00000")
ax[0].set_title("A summer week"); ax[0].set_ylabel("MW")
y["2023-01-08":"2023-01-15"].plot(ax=ax[1], color="#1F3864")
ax[1].set_title("A winter week"); ax[1].set_ylabel("MW")
plt.tight_layout()

# One sentence each, in FINDINGS.md: what is the same, and what is different?'''))
    c.append(md("### Task 4 — additive or multiplicative? Decide on evidence."))
    if sol:
        c.append(code('''from tayyar.analysis.transform import additive_or_multiplicative, apply_transform

decision = additive_or_multiplicative(y, period=24*7)
print(decision)
# level/swing correlation is high -> the seasonal swing grows with the level
# -> multiplicative -> model log(demand) additively

ylog = apply_transform(y, decision["transform"])'''))
    else:
        c.append(code('''from tayyar.analysis.transform import additive_or_multiplicative, apply_transform

# TODO: run additive_or_multiplicative on y and read the level/swing correlation.
# If it says multiplicative, apply the log transform.
# Careful: the series contains sensor zeros. What happens to log(0)?'''))
    c.append(md("### Task 5 — MSTL and the seasonal strengths"))
    if sol:
        c.append(code('''from tayyar.analysis.decompose import mstl_decompose

dec = mstl_decompose(ylog, periods=(24, 24*7))
for k, v in dec["strength"].items():
    print(f"{k:<14} {v:.3f}")

idx = ylog.index
trend = pd.Series(np.asarray(dec["trend"]), index=idx)
rem   = pd.Series(np.asarray(dec["remainder"]), index=idx)
sd    = pd.Series(np.asarray(dec["seasonal"].iloc[:, 0]), index=idx)
sw    = pd.Series(np.asarray(dec["seasonal"].iloc[:, 1]), index=idx)

sl = slice("2023-06-01", "2023-08-31")
fig, ax = plt.subplots(5, 1, figsize=(11, 8), sharex=True)
np.exp(ylog[sl]).plot(ax=ax[0], lw=.6); ax[0].set_ylabel("Observed")
np.exp(trend[sl]).plot(ax=ax[1], lw=1.6, color="#C00000"); ax[1].set_ylabel("Trend")
sd[sl].plot(ax=ax[2], lw=.5, color="#2E7D32"); ax[2].set_ylabel("Daily")
sw[sl].plot(ax=ax[3], lw=.7, color="#7030A0"); ax[3].set_ylabel("Weekly")
rem[sl].plot(ax=ax[4], lw=.4, color="#7F7F7F"); ax[4].set_ylabel("Remainder")
plt.tight_layout()'''))
        c.append(md("""**Expected**

```
seasonal_24    0.972
seasonal_168   0.610
trend          0.969
```

Read it aloud: the daily air-conditioning cycle is the dominant structure a model must
capture; the Friday–Saturday weekly rhythm is real but secondary; the trend is strong
and includes a step change when a large industrial customer connected in October 2022."""))
    else:
        c.append(code('''from tayyar.analysis.decompose import mstl_decompose

# TODO: MSTL with periods (24, 24*7). Report both seasonal strengths and the trend strength.
# Then build the panel figure.
# HINT: MSTL drops the DatetimeIndex from its components — reattach it before plotting,
#       or every panel will come out blank.'''))
    c.append(md("""### Task 6 — `FINDINGS.md`

Three bullets, no more:
1. the dominant seasonality and its strength,
2. the trend direction and rough magnitude,
3. what the remainder is telling you (look at Ramadan and at a heatwave week).

```
git add -A && git commit -m "feat(analysis): clean index + MSTL decomposition of Tayyar demand"
```"""))
    if sol:
        c.append(md("""### Instructor notes

- The messy-timestamp trap in Task 1 is the highest-value teachable moment on Day 1.
  Let a pair discover the silent row loss when they skip `asfreq` — do not pre-warn them.
- Branch `sim-gap` removes 48 hours of telemetry without a marker: skipping `asfreq`
  shortens the series and misaligns every seasonal index by two days.
- Branch `sim-agg` resamples with `.sum()` where the question needs `.mean()` — the trend
  inflates 24×. Aggregation encodes the question.
- Fast finishers: overlay the annual seasonal shape for 2021 against 2023 and observe the
  deepening summer peak."""))
    write(f"lab1_{tag}.ipynb", c)

print("lab 1 written")
