# Time Series Analysis and Forecasting
## تحليل السلاسل الزمنية والتنبؤ

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Time Series Analysis and Forecasting |
| **Arabic Title** | تحليل السلاسل الزمنية والتنبؤ |
| **Code** | SDA-DSC-212 |
| **Level** | Specialist |
| **Duration** | 3 days × 5 learning hours = **15 hours** |
| **Audience** | Data scientists and analysts working with temporal data |
| **Prerequisites** | SDA-DSC-111; SDA-DSC-211 recommended |
| **Assessment** | Forecasting project with backtest report |
| **Stackability** | Forecasting badge · Part of the Analytics & Experimentation specialisation · Next: SDA-DSC-311 |
| **Tools & Platforms** | statsmodels · Prophet · sktime · LightGBM (also: pandas, pmdarima, darts) |

## Course Description

A specialist module on modelling data that evolves over time. Participants decompose series into trend, seasonality, and remainder; build statistical and ML-based forecasting models; and evaluate them with time-aware backtesting. Applications include demand planning, workforce projections, and economic indicators relevant to national programmes. The emphasis throughout is on the one discipline that separates forecasting from ordinary machine learning: **respecting the arrow of time** so that every reported accuracy number would survive contact with the future.

The course is built around a single evolving artefact: **"Tayyar" (تيّار) — a National Load-Forecasting service** for the Saudi power grid. Participants work with three years of hourly electricity demand for the Central Operating Area (the Riyadh region), a series with textbook-rich structure — a growth trend from economic expansion, a daily air-conditioning cycle, a Thursday–Friday weekend rhythm, a fierce summer annual peak, and calendar shocks from Ramadan, the two Eids, and National Day. Every lab advances the same service: from decomposition, through classical and ML models, to probabilistic day-ahead forecasts validated by rolling-origin backtests. By the end of Day 3 each participant owns a working, backtested forecasting pipeline and a backtest report — exactly the deliverable a grid operator, a retail demand planner, or a workforce planner would commission.

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Analyze trend, seasonality, and autocorrelation structure in time series
2. **LO2** — Develop classical forecasting models including ARIMA and exponential smoothing
3. **LO3** — Implement ML and gradient-boosting approaches with engineered temporal features
4. **LO4** — Design backtesting frameworks with proper time-based validation
5. **LO5** — Evaluate forecasts using scale-appropriate accuracy and uncertainty metrics
6. **LO6** — Compare model families to select the right approach per use case

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Seeing the signal | M1: Time-Series Structure & Decomposition · M2: Stationarity & Autocorrelation | 50% | 50% | Clean hourly `Tayyar` series with decomposition plots + stationarity report (ADF/KPSS, ACF/PACF) |
| **Day 2** | Building forecasts | M3: ARIMA & Exponential Smoothing · M4: Feature-Based ML Forecasting | 45% | 55% | SARIMA + ETS baselines and a LightGBM feature-based forecaster, all producing 24h-ahead forecasts |
| **Day 3** | Trust and selection | M5: Probabilistic Forecasts & Intervals · M6: Backtesting & Evaluation · M7: Forecasting Case Study · Capstone | 35% | 65% | Rolling-origin backtest report with calibrated intervals + model-selection decision + capstone demo |

## Hour-by-Hour Breakdown

### Day 1 — Seeing the Signal

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why time series breaks ordinary ML** + course kickoff | Recognise autocorrelation and temporal leakage; frame the 7 topics; meet the `Tayyar` golden thread | Interactive lecture + forecast-failure story | 80/20 |
| 2 | **Decomposition: trend, seasonality, remainder** (M1) | Additive vs multiplicative; STL; multiple seasonalities; resampling and calendars | Lecture + live STL demo | 65/35 |
| 3 | **Lab 1 — Load, index, resample, decompose** | Build the `DatetimeIndex`, handle gaps/DST, STL-decompose the demand series | Guided lab (pairs) | 15/85 |
| 4 | **Stationarity and autocorrelation** (M2) | Stationarity intuition; ADF/KPSS; differencing; ACF/PACF reading | Lecture + ACF/PACF walkthrough | 65/35 |
| 5 | **Lab 2 — Stationarity report** | ADF/KPSS, seasonal & regular differencing, ACF/PACF interpretation | Guided lab (pairs) | 15/85 |

### Day 2 — Building Forecasts

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **ARIMA and SARIMA** (M3) | (p,d,q)(P,D,Q)m; order selection; exogenous regressors (SARIMAX) | Lecture + `pmdarima` demo | 65/35 |
| 2 | **Exponential smoothing / ETS** (M3) + **Lab 3** | SES, Holt, Holt-Winters; ETS taxonomy; when smoothing beats ARIMA | Micro-lecture + guided lab | 40/60 |
| 3 | **Feature-based ML forecasting** (M4) | Reduction to supervised learning; lags, windows, calendar, Fourier terms; leakage traps | Lecture + feature-build demo | 60/40 |
| 4 | **Lab 4 — LightGBM forecaster** | Engineer temporal features, train LightGBM, produce recursive/direct 24h forecast | Guided lab (pairs) | 10/90 |
| 5 | **Probabilistic forecasting** (M5) + **Lab 5 start** | Why point forecasts lie; quantile loss; LightGBM quantile models | Lecture + lab | 45/55 |

### Day 3 — Trust and Selection

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Intervals and calibration** (M5) + **Lab 5 finish** | Prediction intervals; conformal prediction; coverage vs sharpness | Micro-lecture + lab | 35/65 |
| 2 | **Backtesting and forecast evaluation** (M6) | Rolling-origin vs expanding window; MAE/RMSE/MAPE/sMAPE/MASE; pinball; Diebold-Mariano | Lecture + backtest dissection | 55/45 |
| 3 | **Lab 6 — Rolling-origin backtest** | Backtest all model families with `sktime`, build the comparison table | Guided lab (pairs) | 10/90 |
| 4 | **Case study + capstone assembly** (M7) | Model-family selection under constraints; integrate the pipeline; peer review | Case discussion + project work | 20/80 |
| 5 | **Capstone demos + assessment + wrap-up** | 5-minute demos; rubric scoring; path to SDA-DSC-311 | Presentations | 15/85 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module advances the same `Tayyar` load-forecasting service on the same hourly demand series. Never introduce a throwaway airline-passengers toy set beyond one warm-up plot — always evolve `Tayyar`. This is what makes the Day-3 backtest report and capstone achievable in the time available.
- **The one non-negotiable:** temporal leakage. Reinforce in every lab that the train/test split, every feature, and every scaler must be computable using only past data. Publish a "leakage smell" poster and point at it whenever a random `train_test_split` appears.
- **Pace control:** Labs 4 (feature engineering) and 6 (backtesting) are the most overrun-prone. Publish checkpoint tags (`lab1-start`, `lab1-solution`, … `lab6-start`) in the course repo so stragglers fast-forward: `git checkout lab4-start`.
- **Pairing:** rotate pairs each day; pair a strong-statistics participant with a strong-ML participant. The classical/ML bridge (M3→M4) is where the skill transfer pays off.
- **Environment strategy:** primary = local `conda`/`uv` env with Python 3.12; fallback = provided Colab notebooks (data pre-loaded to a mounted drive). `Prophet` and `pmdarima` are the fragile installs — verify both the week before delivery on Windows and macOS.
- **Language:** deliver in Arabic or English; keep all code, column names, and commit messages in English (production convention — mixed-language logs and identifiers break tooling in Saudi enterprise environments).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-3 afternoon is deliberately lighter on new theory so the backtest and capstone get uninterrupted build time.
- **Assessment logistics:** the backtest report is the spine of the grade. Collect notebook/repo URLs at the end of Day 3 Hour 4 so backtest results can be spot-checked before the Hour-5 demos begin.

---

# Module 1 — Time-Series Structure and Decomposition

## Module Overview

**Purpose.** Before anyone fits a model, they must *see* the series. This module teaches participants to load temporal data correctly, establish a clean time index, and decompose a series into the three ingredients every forecasting method reasons about: trend, seasonality, and remainder. Decomposition is both a diagnostic (what structure exists?) and a modelling strategy (forecast the parts, recombine). Get this wrong — a broken index, a hidden gap, the wrong additive/multiplicative choice — and every downstream model inherits the error.

**Business relevance.** National programmes run on temporal forecasts: grid operators size generation and avoid brownouts from load forecasts; Vision 2030 workforce plans project Saudisation trajectories; ministries forecast economic indicators for budgeting. A demand planner who cannot separate "sales are trending up" from "it is simply summer" will over-order every June and blame the model. Decomposition is the shared vocabulary between the data scientist and the decision-maker.

**Industry use cases.**
- A grid operator decomposes hourly load to quantify how much of the summer peak is structural annual seasonality versus a temperature anomaly, feeding both capacity planning and day-ahead dispatch.
- A national retailer decomposes weekly sales to strip out Ramadan and Eid effects before judging whether a marketing campaign moved the trend.
- A telecom decomposes daily active users to detect that a "growth plateau" is actually a masked weekly seasonality change after a product launch.

**Expected competencies.** After this module a participant can build a correct `DatetimeIndex` with an explicit frequency and timezone, resample and handle gaps, choose additive vs multiplicative decomposition on evidence, run and interpret STL, and read a decomposition plot to state what a model must capture.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Construct a correct, gap-free `DatetimeIndex` with explicit frequency and timezone | LO1 |
| 1.2 | Distinguish trend, seasonal, and remainder components and choose additive vs multiplicative | LO1 |
| 1.3 | Apply STL and classical decomposition, including multiple seasonalities | LO1 |
| 1.4 | Resample and aggregate series without introducing temporal artefacts | LO1 |
| 1.5 | Read a decomposition to specify what a downstream model must capture | LO1, LO6 |

## Technical Content

### 1. What makes a time series different

An ordinary supervised-learning row is exchangeable: shuffle the dataset and nothing is lost. A time series is the opposite — **order is the signal**. Three properties follow, and every one of them will bite a practitioner who treats a series like a normal table:

- **Autocorrelation.** Today's value is correlated with yesterday's. Observations are not independent, so ordinary error bars, cross-validation folds, and significance tests computed under an i.i.d. assumption are wrong.
- **Temporal leakage.** Any information from the future — a random-split test point, a global mean subtracted before splitting, a feature that peeks ahead — inflates measured accuracy and evaporates in production. This is *the* recurring failure of the whole field.
- **Non-stationarity.** The mean, variance, and seasonal pattern can drift. A model trained on last year's level may forecast a level that no longer exists.

**Instructor note:** open with a 5-minute failure story (the `Tayyar` postmortem in §6). Do not draw a single model yet. The message of Hour 1 is *"time is not a feature you can shuffle."*

### 2. The additive model of a series

The organising equation. A series `y_t` is modelled as a combination of unobserved components:

- **Additive:** `y_t = T_t + S_t + R_t` (trend + seasonality + remainder)
- **Multiplicative:** `y_t = T_t × S_t × R_t`

Choose **multiplicative** when the seasonal swing *grows with the level* — retail sales whose December spike is 20% of a rising baseline. Choose **additive** when the seasonal swing is roughly constant in absolute size regardless of level. A multiplicative series becomes additive under a log transform (`log y_t = log T_t + log S_t + log R_t`), which is why "take logs" is such common advice. For `Tayyar`, the daily air-conditioning swing scales with the summer level — so demand is closer to multiplicative, and we model `log(demand_mw)` or use a variance-stabilising transform.

`Tayyar` carries **three seasonal periods at once**: daily (period 24 hours), weekly (period 168 hours, with the Thursday–Friday weekend in KSA), and annual (period ≈ 8,766 hours, the summer peak). Classical single-period decomposition cannot represent this; §3 introduces the tools that can.

### 3. Decomposition methods

**Classical decomposition** (`seasonal_decompose`) estimates the trend with a centred moving average, then averages the detrended series by season position. It is fast and intuitive but assumes a single fixed seasonal period and a constant seasonal shape, and it loses points at both ends to the moving-average window.

**STL — Seasonal-Trend decomposition using Loess** is the workhorse. It estimates the seasonal component with local regression, allowing the seasonal shape to *evolve slowly* over time (a summer peak that deepens year over year), is robust to outliers with the `robust=True` option, and lets you control smoothness. STL handles one seasonal period per call; for multiple seasonalities you either run **MSTL** (multiple-STL, which peels off seasonalities in sequence) or supply Fourier terms to a regression (Module 4).

**Best practice.** Decompose to *understand and diagnose*, not usually to forecast directly. The insight — "80% of the summer peak is structural annual seasonality; the weekly effect is 6%; the remainder has volatility clusters" — is what tells you which model family to reach for and whether a temperature covariate is worth the trouble.

### 4. Time indexing, frequency, and calendars

Everything in the ecosystem keys off a correct index. The disciplines:

- **Set an explicit frequency.** `df.asfreq("h")` declares the series hourly and *materialises missing timestamps as NaN* — a gap you can see and impute beats a gap that silently shortens your series. Never let `statsmodels` guess the frequency.
- **Timezone and DST.** Store timestamps in a defined timezone (`Asia/Riyadh`, which fortunately has no daylight-saving shifts — say so explicitly, because a US or EU series would have duplicate/missing hours twice a year that must be handled before `asfreq`).
- **Calendars are features.** KSA's weekend is **Friday–Saturday** (officially Friday–Saturday since 2013); Ramadan shifts on the Hijri calendar each Gregorian year; the two Eids and National Day (23 September) are load shocks. These belong in a holiday/calendar table (Module 4), but you must *see* them in decomposition first.
- **Gaps and duplicates.** Sensor feeds drop and re-send. De-duplicate on timestamp, sort the index, then `asfreq`. Impute short gaps (≤ a few hours) with time interpolation; flag long gaps rather than fabricate them.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Plot before you model.* Every series gets four plots: the raw line, a seasonal subseries/heatmap, the decomposition panel, and the ACF (Module 2). Ninety percent of modelling decisions are visible in these four.
- *Resample deliberately.* Down-sampling (hourly → daily) uses an aggregation that matches the question: `mean` for average load, `max` for peak-capacity planning, `sum` for energy. The wrong aggregator answers the wrong question.
- *One transform, applied consistently.* If you log the series, everything downstream — model, intervals, metrics — must invert the log correctly (and remember the retransformation bias when back-transforming a mean).

**Common mistakes (each appears in the Lab 1 starter deliberately)**
1. Reading timestamps as strings, so the index sorts `"10:00"` before `"9:00"` lexically — silent chaos.
2. No explicit frequency, so a two-day sensor outage shortens the series with no warning and shifts every seasonal alignment.
3. Using multiplicative decomposition on a series that hits zero (division blows up).
4. Aggregating hourly to daily with `mean` when the operator needs the daily **peak** for capacity.
5. Treating the STL remainder as noise when its variance clusters — a sign of conditional heteroskedasticity worth modelling.
6. Forgetting that KSA weekends are Friday–Saturday and coding a Saturday–Sunday weekend feature.

**Production considerations.** Decomposition is recomputed as new data arrives; freeze the seasonal-window and robustness settings so the diagnostic is comparable across weeks. Persist the calendar table under version control — a wrong Eid date silently corrupts every model that consumes it.

### 6. Real-world example walkthrough

Narrate this (5 minutes): a regional operator's demand-planning team reported their forecast "suddenly got worse every June." The model was fine. The pipeline resampled hourly telemetry to daily using `mean`, but the planners cared about the daily **peak** for reserve margins. In summer, the gap between mean and peak widens (afternoon AC spikes), so the mean-based forecast under-called reserves exactly when the grid was most stressed. No model change fixed it — the fix was decomposition-level: forecast the daily-max series, and separately confirm that the annual seasonal component, not a trend break, drove the June behaviour. This module is that diagnostic discipline, generalised.

## Code Examples

### Loading and indexing the demand series

```python
# src/tayyar/data/load.py
"""Load and index the KSA grid demand series.

Rules for this file:
- timestamps are timezone-aware (Asia/Riyadh, no DST)
- the returned series has an EXPLICIT hourly frequency
- gaps are materialised as NaN, never silently dropped
"""
from pathlib import Path
import pandas as pd

RIYADH = "Asia/Riyadh"

def load_demand(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df = (df
          .drop_duplicates(subset="timestamp")      # sensor re-sends
          .sort_values("timestamp")
          .set_index("timestamp"))

    # Localise to Riyadh (naive -> aware). KSA has no DST, so this is safe.
    if df.index.tz is None:
        df.index = df.index.tz_localize(RIYADH)

    # Declare the frequency: missing hours become NaN rows we can SEE.
    df = df.asfreq("h")

    gaps = int(df["demand_mw"].isna().sum())
    print(f"Loaded {len(df):,} hourly rows | {gaps} missing hours materialised")
    return df

def impute_short_gaps(df: pd.DataFrame, limit: int = 3) -> pd.DataFrame:
    """Interpolate gaps up to `limit` hours; leave longer gaps flagged."""
    out = df.copy()
    out["demand_mw"] = out["demand_mw"].interpolate(method="time", limit=limit)
    out["was_imputed"] = df["demand_mw"].isna() & out["demand_mw"].notna()
    return out
```

### STL decomposition and reading the components

```python
# src/tayyar/analysis/decompose.py
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL, MSTL

def daily_stl(series: pd.Series) -> pd.DataFrame:
    """Single-seasonality STL on the DAILY-mean series (period=7, weekly)."""
    daily = series.resample("D").mean().dropna()
    stl = STL(np.log(daily), period=7, robust=True).fit()  # log => multiplicative
    return pd.DataFrame({
        "observed": daily,
        "trend": np.exp(stl.trend),
        "seasonal_weekly": np.exp(stl.seasonal),
        "remainder": stl.resid,
    })

def multi_seasonal(series: pd.Series) -> pd.DataFrame:
    """MSTL on the HOURLY series: daily (24) and weekly (168) at once."""
    s = series.dropna()
    res = MSTL(np.log(s), periods=(24, 168)).fit()
    seasonal = np.exp(res.seasonal)           # DataFrame: one column per period
    return pd.DataFrame({
        "trend": np.exp(res.trend),
        "seasonal_daily": seasonal["seasonal_24"],
        "seasonal_weekly": seasonal["seasonal_168"],
        "remainder": res.resid,
    })

def seasonal_strength(remainder: pd.Series, seasonal: pd.Series) -> float:
    """Hyndman's seasonal strength in [0,1]: how much structure the season carries."""
    var_r = np.var(remainder.dropna())
    var_rs = np.var((remainder + seasonal).dropna())
    return float(max(0.0, 1 - var_r / var_rs))
```

### Choosing additive vs multiplicative on evidence

```python
# src/tayyar/analysis/transform.py
import numpy as np
import pandas as pd

def additive_or_multiplicative(series: pd.Series, period: int = 24) -> str:
    """Heuristic: if the seasonal amplitude grows with the level, go multiplicative.

    We correlate the per-cycle MEAN with the per-cycle RANGE. A strong positive
    correlation means bigger levels have bigger swings => multiplicative.
    """
    s = series.dropna()
    cycles = s.groupby(np.arange(len(s)) // period)
    level = cycles.mean()
    swing = cycles.max() - cycles.min()
    corr = np.corrcoef(level, swing)[0, 1]
    return "multiplicative" if corr > 0.3 else "additive"
```

## Hands-on Lab 1 — Load, Index, and Decompose the Tayyar Series

| | |
|---|---|
| **Objective** | Turn raw `ksa_grid_demand.csv` into a clean, explicitly-indexed hourly series and produce a decomposition that states what downstream models must capture |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, `pip install pandas statsmodels matplotlib`, course repo cloned, `git checkout lab1-start` |

**Instructions & tasks**

1. *(5 min)* Load `data/ksa_grid_demand.csv`; confirm the raw file has duplicate and out-of-order timestamps (the starter data is deliberately messy). Note the row count *before* cleaning.
2. *(10 min)* Implement `load_demand`: de-duplicate, sort, localise to `Asia/Riyadh`, `asfreq("h")`. Report the number of materialised gap rows and the longest gap.
3. *(10 min)* Impute gaps ≤ 3 hours with time interpolation; flag longer gaps. Plot the raw hourly line for one representative summer week and one winter week — describe the difference in one sentence each.
4. *(10 min)* Decide additive vs multiplicative using `additive_or_multiplicative`; justify with the seasonal-amplitude plot. Log-transform if multiplicative.
5. *(10 min)* Run MSTL for daily + weekly seasonality; compute `seasonal_strength` for each. Produce the four-panel decomposition figure.
6. *(5 min)* Write three bullet points in `FINDINGS.md`: dominant seasonality, trend direction, and remainder behaviour. Commit: `feat(analysis): clean index + MSTL decomposition of Tayyar demand`.

**Expected output**
```
$ python -m tayyar.analysis.run_decompose
Loaded 26,304 hourly rows | 41 missing hours materialised (longest gap: 5h)
Imputed 33 short gaps; 1 long gap (5h) flagged
Transform decision: multiplicative (level/swing corr = 0.71) -> modelling log(demand)
Seasonal strength  daily=0.83  weekly=0.34  | trend: +2.9% YoY
Wrote decomposition_panel.png, FINDINGS.md
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Index not monotonic error in STL | Timestamps unsorted or duplicated | `drop_duplicates` + `sort_values` before `set_index` |
| `ValueError: freq not set` | Skipped `asfreq("h")` | Always declare frequency; it also reveals gaps |
| Multiplicative decomposition NaNs | Log of a zero/negative demand | Inspect the zeros (sensor dropouts); impute or flag before log |
| Seasonal component looks flat | Wrong `period` (used 12 not 24) | Period is in *observations per cycle*; hourly daily cycle = 24 |

**Instructor notes.** The messy-timestamp trap (task 1) is the highest-value teachable moment — let a pair discover the silent row loss when they skip `asfreq`. Fast finishers: overlay the annual seasonal shape for 2021 vs 2023 and observe the deepening summer peak — a perfect motivation for STL's evolving seasonality and for the trend-plus-growth story.

## Mini Exercises

**Quiz (5 questions)**
1. Additive or multiplicative for a series whose seasonal swing grows with its level? → **multiplicative** (or log then additive).
2. What does `asfreq("h")` do that `parse_dates` alone does not? → declares frequency and materialises missing timestamps as NaN.
3. `period` for the daily cycle of an hourly series? → **24**.
4. Why decompose before modelling if you won't forecast the components directly? → to diagnose which structure a model must capture and which covariates matter.
5. True/False: STL requires a single seasonal period per call. → **True** (use MSTL for several).

**Debugging exercise.** Give participants a branch where the series is resampled to daily with `.sum()` for what should be an average-load question; the trend looks 24× too large. Fix and explain aggregator choice.

**Feature-spotting exercise.** Show a decomposition of `Tayyar` with Ramadan month highlighted; ask participants to locate the shifted evening peak in the remainder and propose the calendar feature that would absorb it.

## Case Study — Demand Planning at a National Grid Operator

**Scenario.** "Shabakah", the operations-planning unit of a national grid operator, must publish a day-ahead load forecast every afternoon for the Central Operating Area. Reserve margins — how much spare generation to keep spinning — are sized off this forecast. Under-forecast and you risk load-shedding on a 47°C afternoon; over-forecast and you burn fuel and money keeping idle units hot.

**Business context.** A 1% day-ahead error on a ~55,000 MW peak is ~550 MW — roughly a mid-size gas turbine held in reserve for nothing, or missing when needed. Summer is where accuracy pays: the annual seasonal peak, the daily AC cycle, and temperature all compound.

**Technical challenge.** Before any model, the team must decompose to separate *structural* summer seasonality (plannable) from *weather-driven* anomalies (needs a temperature covariate) and from *calendar* shocks (Ramadan's shifted evening load, Eid troughs).

**Constraints.** Hourly telemetry with occasional sensor gaps; a strict afternoon publication deadline (the pipeline must run in minutes); the forecast must be explainable to control-room engineers who distrust black boxes; Friday–Saturday weekend and Hijri-calendar holidays must be handled correctly.

**Solution approach (facilitate, don't lecture).** (1) Clean index + gap policy; (2) MSTL to quantify daily/weekly/annual strength and expose the remainder's weather signature; (3) decide multiplicative modelling; (4) specify the calendar table (weekend, Ramadan, Eids, National Day) that later modules consume; (5) agree the target is the hourly series with a day-ahead horizon, aggregated to daily-max for the reserve-margin view.

**Discussion questions.**
1. Why might daily-max and daily-mean forecasts need different models?
2. Which structure should be a model component versus an exogenous covariate (temperature)?
3. How would you detect that this year's summer seasonality is deepening rather than a one-off heatwave?
4. What is the cost asymmetry of over- vs under-forecasting here, and how should it shape evaluation (Module 6)?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Materialised gaps identified | Data quality | 100% of missing hours surfaced | count of NaN after `asfreq` |
| Index correctness | Data quality | Monotonic, unique, tz-aware, freq set | `df.index.is_monotonic_increasing and df.index.freq` |
| Additive/multiplicative decision | Analysis | Justified by amplitude evidence | level/swing correlation reported |
| Seasonal strength (daily) | Analysis | Reported in [0,1] | Hyndman strength formula |
| Decomposition reproducibility | Rigor | Identical panel on re-run | fixed STL params committed |

**Example benchmark table (filled during lab):**

| Series form | Daily strength | Weekly strength | Trend YoY | Remainder note |
|---|---|---|---|---|
| Raw hourly (additive) | 0.79 | 0.31 | +2.9% | variance grows in summer |
| log(demand) hourly | 0.83 | 0.34 | +2.9% | variance stabilised |

## Required Visuals and Training Assets

### Diagrams
1. **The additive model of a series** — *Purpose:* anchor image for the course. *Elements:* one observed line splitting into three stacked panels (Trend, Seasonality, Remainder) with a "+/×" toggle showing additive vs multiplicative. *Style:* flat vector, 3-colour palette, English labels with Arabic subtitles.
2. **Three seasonalities of Tayyar** — *Purpose:* motivate MSTL. *Elements:* the same demand series annotated with the daily AC cycle, the Fri–Sat weekly dip, and the summer annual peak, each on its own timescale strip. *Style:* three-row timeline poster.
3. **Temporal leakage vs valid split** — *Purpose:* the course's thesis, introduced early. *Elements:* a timeline with a red random-shuffle split (crossed out) and a green past→future split. *Style:* before/after split panel, red forbidden marker.

### Images (screenshots)
1. **Decomposition panel in a notebook** — *why:* expected-output reference for Lab 1; *content:* four-panel MSTL figure with strengths annotated.
2. **`asfreq` before/after** — *why:* makes the silent-gap smell visible; *content:* row count and a NaN row highlighted.
3. **Summer vs winter week overlay** — *why:* shows amplitude growth motivating multiplicative choice.

### Simulations
1. **Silent gap** — *Setup:* branch `sim-gap` removes 48 hours of telemetry without a marker. *Expected behaviour:* skipping `asfreq` shortens the series and misaligns every seasonal index by two days; the STL seasonal shape smears. *Learning objective:* declare frequency or inherit silent corruption.
2. **Wrong aggregator** — *Setup:* branch `sim-agg` resamples with `sum` instead of `mean`. *Expected behaviour:* trend inflates 24×. *Learning objective:* aggregation encodes the question.

### Interactive Activities
- **Decomposition read-aloud (15 min):** pairs exchange decomposition panels and each states, in one sentence per component, what a model must capture.
- **"Component or covariate?" card sort (10 min):** cards (temperature, hour-of-day, Ramadan, economic growth, sensor noise) sorted into seasonal component / trend / exogenous covariate / remainder.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | Synthetic, generated by course tooling to mimic Central Operating Area hourly load (3 years, realistic daily/weekly/annual seasonality, temperature, Ramadan/Eid effects, injected sensor gaps) | CSV | ~26,300 rows × 3 cols (`timestamp`, `demand_mw`, `temp_c`) | The golden thread; reused in every module and the capstone |
| `ksa_calendar.csv` | Course-provided KSA calendar (Fri–Sat weekend, Hijri holidays 2021–2023, National Day) | CSV | ~1,100 rows | Calendar features (Modules 4–7) |
| `decomposition_reference.png` | Reference solution | PNG | — | Expected Lab 1 output |

### Demo Requirements
- **Instructor demo:** live clean-and-decompose of the raw file in under 8 minutes, deliberately skipping `asfreq` once to show the silent gap, then fixing it.
- **Student demo:** one pair presents their four-panel decomposition and reads the three findings aloud at end of Hour 3.
- **Expected outputs:** clean tz-aware hourly series, MSTL panel, `FINDINGS.md` with three bullets.

---

# Module 2 — Stationarity and Autocorrelation

## Module Overview

**Purpose.** Classical forecasting models assume the series is **stationary** — its statistical behaviour does not change over time. Real series rarely are, so the practitioner's job is to *diagnose* non-stationarity and *transform* the series into a stationary one, then read its autocorrelation to fingerprint the right model. This module gives participants the two instruments every forecaster reaches for first: stationarity tests (ADF, KPSS) and the autocorrelation/partial-autocorrelation functions (ACF/PACF).

**Business relevance.** A model fitted to a non-stationary series produces confidently wrong forecasts: it projects yesterday's level and variance into a future where both have moved. In demand and economic forecasting, mistaking a trend for a stationary mean is the single most expensive analytical error — it drives systematic over- or under-planning. Stationarity discipline is what makes a forecast's uncertainty band honest.

**Industry use cases.**
- A grid analyst differences load to remove the growth trend before ARIMA, so the model forecasts *changes* it can actually estimate rather than a level it will always lag.
- An economist confirms an inflation series is integrated of order one (needs one difference) before building a model, avoiding spurious regression against another trending series.
- A demand planner reads the ACF of weekly sales and instantly sees the 52-week seasonal spike, deciding a seasonal model is mandatory.

**Expected competencies.** After this module a participant can test stationarity with ADF and KPSS and reconcile their opposite null hypotheses, apply regular and seasonal differencing to the correct order, and read ACF/PACF plots to propose candidate ARIMA orders.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Define weak stationarity and identify sources of non-stationarity | LO1 |
| 2.2 | Apply and reconcile ADF and KPSS tests | LO1 |
| 2.3 | Apply regular and seasonal differencing to achieve stationarity | LO1, LO2 |
| 2.4 | Compute and interpret ACF and PACF | LO1 |
| 2.5 | Translate ACF/PACF signatures into candidate ARIMA orders | LO1, LO2 |

## Technical Content

### 1. Stationarity, precisely

A series is **weakly (covariance) stationary** if three things are constant over time: the mean, the variance, and the autocovariance at each lag (the relationship between `y_t` and `y_{t-k}` depends only on the gap `k`, not on where you are in the series). Stationarity matters because ARIMA-family models estimate *one* set of parameters assumed to hold throughout — if the mean drifts, that assumption is void.

Sources of non-stationarity, each with its own remedy:
- **Trend** (mean changes) → differencing, or detrend by modelling the trend.
- **Seasonality** (mean changes periodically) → seasonal differencing, or model the season.
- **Changing variance** (heteroskedasticity) → variance-stabilising transform (log, Box-Cox).

For `Tayyar`, all three are present: an upward growth trend, strong multi-period seasonality, and summer-amplified variance. We stabilise variance with the log from Module 1, then difference to remove trend and season.

### 2. Testing stationarity: ADF and KPSS

Two tests, **opposite nulls** — this trips up everyone, so teach it as a 2×2 table:

- **Augmented Dickey-Fuller (ADF):** null = "has a unit root" = **non-stationary**. A small p-value (< 0.05) lets you *reject non-stationarity* → evidence of stationarity.
- **KPSS:** null = "is stationary". A small p-value (< 0.05) lets you *reject stationarity* → evidence of non-stationarity.

| | KPSS says stationary | KPSS says non-stationary |
|---|---|---|
| **ADF says stationary** | Stationary — proceed | Difference-stationary; try differencing |
| **ADF says non-stationary** | Trend-stationary; detrend | Non-stationary — difference and re-test |

Using both is best practice precisely because they can disagree, and the disagreement is informative (trend-stationary vs difference-stationary). Never rely on a single test or on eyeballing alone.

### 3. Differencing: regular and seasonal

**Regular differencing** `∇y_t = y_t − y_{t−1}` removes a trend; the order of differencing needed is the `d` in ARIMA. **Seasonal differencing** `∇_m y_t = y_t − y_{t−m}` removes a seasonal pattern of period `m`; it is the `D` in SARIMA. 

Discipline:
- **Difference as little as possible.** Over-differencing injects artificial negative autocorrelation at lag 1 and inflates variance. Signs of over-differencing: the lag-1 ACF is strongly negative (< −0.5) and the differenced series looks noisier than needed.
- **Order of operations for seasonal data:** apply seasonal differencing first, re-test; then apply a regular difference only if still non-stationary. Most series need `d ≤ 2` and `D ≤ 1`.
- **Let a routine suggest, you decide.** `pmdarima.arima.ndiffs` and `nsdiffs` estimate `d` and `D` from the tests, but confirm with a plot and ACF; automation proposes, the analyst disposes.

### 4. ACF and PACF: the model fingerprint

The **autocorrelation function (ACF)** at lag `k` is the correlation between `y_t` and `y_{t−k}`. The **partial autocorrelation function (PACF)** is the correlation at lag `k` *after removing* the effect of the intervening lags. Together they fingerprint the process:

| Pattern | ACF | PACF | Suggests |
|---|---|---|---|
| AR(p) | tails off (decays) | cuts off after lag p | AR order p |
| MA(q) | cuts off after lag q | tails off | MA order q |
| ARMA(p,q) | tails off | tails off | mixed; use information criteria |
| Seasonal | spike at lag m, 2m, … | spike at m | seasonal terms |

"Cuts off" means drops inside the significance band (±1.96/√n). For `Tayyar`'s daily-differenced series, expect a spike at lag 24 and its multiples — the daily seasonality announcing itself. Reading these plots is a skill built by repetition; the lab provides six series to fingerprint.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Transform for variance, difference for mean.* Log/Box-Cox stabilise variance; differencing stabilises the mean. Do them in that order.
- *Stationarity is a means, not the goal.* You transform so a model's assumptions hold; you must invert every transform to forecast on the original scale.
- *Autocorrelation is structure, not noise.* Strong ACF is exactly the exploitable signal; a flat ACF near zero everywhere means the series is (already) white noise and nothing beats the naive forecast.

**Common mistakes (each appears in the Lab 2 starter deliberately)**
1. Interpreting ADF's null backwards ("p > 0.05 so it's stationary").
2. Over-differencing until the series is stationary but the model is worse.
3. Differencing before stabilising variance, so heteroskedasticity survives.
4. Reading the ACF of a non-stationary series (which decays slowly and linearly) and mistaking the slow decay for high AR order rather than a trend to be differenced.
5. Ignoring seasonal spikes at lag `m` because the plot's default `lags=20` doesn't reach 24.
6. Running tests on the log series but forecasting/evaluating on the raw series without back-transforming.

**Production considerations.** Re-run stationarity diagnostics on a schedule; a series that was I(1) can shift regime (a tariff change, a new industrial load). Persist the chosen `d`, `D`, and transform so refits are reproducible and drift in these choices is itself a monitored signal.

### 6. Real-world example walkthrough

Narrate this: an analyst regressed a rising electricity-demand series on a rising GDP series and reported an R² of 0.98 — "demand is explained by the economy." Both series were non-stationary (trending), so the regression was **spurious**: any two trending series correlate. After differencing both to stationarity, the relationship weakened dramatically and a seasonal structure the trend had masked emerged as the real driver. The lesson — establish stationarity *before* you trust any relationship — is why this module precedes all modelling.

## Code Examples

### Stationarity report (ADF + KPSS reconciled)

```python
# src/tayyar/analysis/stationarity.py
"""Stationarity diagnostics. ADF and KPSS have OPPOSITE nulls;
we report both and label the reconciled verdict."""
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

def stationarity_report(series: pd.Series) -> dict:
    s = series.dropna()
    adf_p = adfuller(s, autolag="AIC")[1]
    # KPSS around a constant ("c"); "ct" tests trend-stationarity
    kpss_p = kpss(s, regression="c", nlags="auto")[1]

    adf_stationary = adf_p < 0.05      # reject unit root
    kpss_stationary = kpss_p > 0.05    # fail to reject stationarity

    if adf_stationary and kpss_stationary:
        verdict = "stationary"
    elif not adf_stationary and not kpss_stationary:
        verdict = "non-stationary (difference)"
    elif adf_stationary and not kpss_stationary:
        verdict = "difference-stationary"
    else:
        verdict = "trend-stationary (detrend)"

    return {"adf_p": round(adf_p, 4), "kpss_p": round(kpss_p, 4),
            "verdict": verdict}
```

### Choosing differencing order and applying it

```python
# src/tayyar/analysis/differencing.py
import numpy as np
import pandas as pd
from pmdarima.arima.utils import ndiffs, nsdiffs

def suggest_orders(series: pd.Series, m: int = 24) -> dict:
    """Estimate regular (d) and seasonal (D) differencing orders."""
    s = series.dropna()
    d = ndiffs(s, test="adf")                 # regular differences suggested
    D = nsdiffs(s, m=m, test="ocsb")          # seasonal differences suggested
    return {"d": int(d), "D": int(D), "m": m}

def make_stationary(series: pd.Series, d: int, D: int, m: int) -> pd.Series:
    """Seasonal difference FIRST, then regular. Minimal differencing."""
    s = series.copy()
    for _ in range(D):
        s = s.diff(m)
    for _ in range(d):
        s = s.diff(1)
    return s.dropna()
```

### ACF/PACF for order identification

```python
# src/tayyar/analysis/correlograms.py
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def correlograms(series: pd.Series, lags: int = 60, path: str = "acf_pacf.png"):
    """Plot ACF and PACF far enough to SEE the seasonal spike (>= 2*m)."""
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))
    plot_acf(series.dropna(), lags=lags, ax=ax[0])   # MA(q): cuts off at q
    plot_pacf(series.dropna(), lags=lags, ax=ax[1],  # AR(p): cuts off at p
              method="ywm")
    ax[0].set_title("ACF — look for spikes at 24, 48 (daily seasonality)")
    ax[1].set_title("PACF")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    return path
```

## Hands-on Lab 2 — The Stationarity Report

| | |
|---|---|
| **Objective** | Produce a defensible stationarity report for the `Tayyar` series: test, difference to the right order, and propose candidate ARIMA orders from ACF/PACF |
| **Duration** | 50 minutes |
| **Setup** | Lab 1 solution (`git checkout lab2-start`), `pip install pmdarima` |

**Instructions & tasks**

1. *(8 min)* Run `stationarity_report` on the raw log-demand series; interpret ADF and KPSS *together* and record the verdict. Predict what differencing will be needed before running it.
2. *(10 min)* Use `suggest_orders` (m=24) to estimate `d` and `D`; apply `make_stationary` (seasonal first). Re-run the report on the differenced series to confirm stationarity.
3. *(10 min)* Plot the series before and after differencing; check the lag-1 ACF for the over-differencing signature (strong negative). Reduce `d` if you see it.
4. *(12 min)* Produce ACF/PACF with `lags=60`; annotate the seasonal spike at lag 24 and read off candidate `(p,q)` and seasonal `(P,Q)` orders.
5. *(5 min)* Write `STATIONARITY.md`: the verdict, the chosen `(d,D)`, and 2–3 candidate SARIMA orders with a one-line justification each.
6. *(5 min)* Commit: `feat(analysis): stationarity report + candidate SARIMA orders`.

**Expected output**
```
$ python -m tayyar.analysis.run_stationarity
Raw log-demand : ADF p=0.42  KPSS p=0.01  -> non-stationary (difference)
Suggested       : d=1, D=1, m=24
After D=1,d=1   : ADF p=0.00  KPSS p=0.10  -> stationary
ACF/PACF        : PACF cuts ~lag 2; ACF spike at 24 -> candidates:
                  SARIMA(2,1,1)(1,1,1)[24], (1,1,2)(0,1,1)[24], (2,1,0)(1,1,0)[24]
Wrote acf_pacf.png, STATIONARITY.md
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| ADF and KPSS both say "non-stationary" but you called it stationary | Null hypotheses read backwards | ADF small-p = stationary; KPSS small-p = non-stationary |
| Lag-1 ACF ≈ −0.6 after differencing | Over-differenced | Reduce `d` by one; re-test |
| No visible seasonal spike | `lags` too small (< 24) | Set `lags ≥ 2*m` to see lag 24, 48 |
| KPSS "p-value greater than 0.1" warning | Test statistic outside table | Expected; treat as p > 0.1 (stationary evidence) |

**Instructor notes.** The opposite-null reconciliation is the concept most worth 10 extra minutes; put the 2×2 table on the board and quiz cold. Fast finishers: difference the *non-logged* series and compare ACF — the surviving heteroskedasticity motivates the Module 1 variance transform retroactively.

## Mini Exercises

**Quiz (5 questions)**
1. ADF p-value = 0.01 — stationary or not? → evidence of **stationary** (reject unit root).
2. KPSS p-value = 0.01 — stationary or not? → evidence of **non-stationary** (reject stationarity).
3. Which comes first for seasonal data, seasonal or regular differencing? → **seasonal**, then re-test.
4. ACF tails off, PACF cuts off after lag 2 — which model and order? → **AR(2)**.
5. A slowly, linearly decaying ACF indicates what? → a **trend** (non-stationary); difference before reading further.

**Debugging exercise.** Branch `sim-overdiff` differences twice where once suffices; participants diagnose the negative lag-1 ACF and fix.

**Pattern-matching drill.** Six anonymised ACF/PACF pairs (AR, MA, ARMA, seasonal, white noise, non-stationary); pairs label each and name a candidate order. Compare to the solution key.

## Case Study — Forecasting a Non-Stationary Economic Indicator

**Scenario.** A planning ministry forecasts a monthly economic activity index to support quarterly budgeting. An analyst's first model regressed the index on a trending oil-price series and reported near-perfect fit — which collapsed out of sample.

**Business context.** Budget allocations move on these forecasts; a spurious relationship that inflates confidence leads to over-commitment. Decision-makers need honest uncertainty, not an impressive-looking R².

**Technical challenge.** Establish the integration order of both series, difference to stationarity, and only then assess whether any genuine relationship survives — separating real co-movement from shared trend.

**Constraints.** Short monthly history (10 years ≈ 120 points); strong annual seasonality; a structural break at a known policy change that must not be differenced away blindly.

**Solution approach (facilitate).** (1) ADF/KPSS on each series; (2) determine `d` for each; (3) seasonal differencing for the annual pattern; (4) re-test the relationship on the stationary, differenced series; (5) discuss the structural break — dummy variable versus split sample.

**Discussion questions.**
1. Why does regressing two trending series produce a spurious high R²?
2. How would you decide whether the structural break needs a dummy or a model reset?
3. With only 120 points, what constrains how much you can difference and still estimate parameters?
4. When is a slowly-decaying ACF a sign to difference versus a sign of genuine long memory?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Stationarity achieved | Analysis | ADF p < 0.05 **and** KPSS p > 0.05 on transformed series | `stationarity_report` verdict |
| Differencing minimality | Rigor | Lowest `(d,D)` that passes; no over-differencing | lag-1 ACF not strongly negative |
| Candidate orders proposed | Analysis | ≥ 3 justified SARIMA candidates | `STATIONARITY.md` |
| Seasonal spike identified | Analysis | Lag-24 spike documented | annotated ACF plot |
| Reproducibility | Rigor | Same verdict + orders on re-run | committed params |

**Example benchmark table (filled during lab):**

| Series | ADF p | KPSS p | Verdict | Chosen (d,D) |
|---|---|---|---|---|
| log(demand) raw | 0.42 | 0.01 | non-stationary | — |
| seasonal + regular diff | 0.00 | 0.10 | stationary | (1,1)[24] |

## Required Visuals and Training Assets

### Diagrams
1. **The ADF/KPSS 2×2** — *Purpose:* fix the opposite-null confusion. *Elements:* a 2×2 grid crossing ADF verdict with KPSS verdict, each cell labelled with the reconciled conclusion. *Style:* clean matrix, colour-coded green (stationary) to red.
2. **ACF/PACF fingerprint chart** — *Purpose:* order-identification reference poster. *Elements:* four mini correlogram pairs (AR, MA, ARMA, seasonal) with the "tails off / cuts off" rule annotated. *Style:* reference card, A4 printable.
3. **Differencing ladder** — *Purpose:* show minimal differencing. *Elements:* raw → seasonal-diff → +regular-diff, with ADF p-value falling at each step and an over-differenced 4th panel flagged red. *Style:* left-to-right ladder.

### Images (screenshots)
1. **Stationarity report output** — *why:* Lab 2 expected output; *content:* the ADF/KPSS/verdict block.
2. **ACF with seasonal spike** — *why:* teaches setting `lags ≥ 2m`; *content:* annotated lag-24 spike.
3. **Over-differencing signature** — *why:* recognisable negative lag-1 ACF; *content:* side-by-side correct vs over-differenced.

### Simulations
1. **Spurious regression** — *Setup:* branch `sim-spurious` regresses two independent random walks. *Expected behaviour:* R² ~ 0.9 despite no relationship; vanishes after differencing. *Learning objective:* stationarity before relationships.
2. **Over-differencing** — *Setup:* branch `sim-overdiff`. *Expected behaviour:* strong negative lag-1 ACF, worse forecasts. *Learning objective:* difference as little as possible.

### Interactive Activities
- **ACF/PACF speed round (15 min):** flash six correlograms; pairs call the model family within 30 seconds each.
- **Verdict reconciliation drill (10 min):** given ADF+KPSS p-value pairs, class states the reconciled verdict aloud.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | (as Module 1) | CSV | ~26,300 rows | Stationarity testing and differencing |
| `correlogram_gallery.npz` | Course-generated AR/MA/seasonal/white-noise series | NPZ | 6 series | Pattern-matching drill |

### Demo Requirements
- **Instructor demo:** live stationarity report + differencing + ACF read in under 8 minutes, reading ADF and KPSS aloud together.
- **Student demo:** one pair reads their ACF/PACF and defends two candidate SARIMA orders.
- **Expected outputs:** `STATIONARITY.md`, annotated `acf_pacf.png`, reconciled verdict.

---

# Module 3 — ARIMA and Exponential Smoothing

## Module Overview

**Purpose.** This module delivers the two classical forecasting workhorses: the **ARIMA/SARIMA** family (which models autocorrelation directly) and **exponential smoothing / ETS** (which models level, trend, and seasonality as weighted-recency updates). These are not legacy methods — a well-specified SARIMA or ETS is frequently the model to beat, is fast, interpretable, and ships trustworthy prediction intervals out of the box. Participants learn to specify, fit, diagnose, and forecast with both, and to know which fits which situation.

**Business relevance.** In regulated and safety-critical settings — grid dispatch, hospital staffing, treasury cash-flow — decision-makers demand models they can interrogate. "The forecast rose because the level term updated and the summer seasonal factor kicked in" is a sentence a control-room engineer accepts; "the gradient boosting said so" is not. Classical models also need little data and little compute, so they are the right default for the thousands of medium-importance series an organisation forecasts routinely.

**Industry use cases.**
- A grid operator runs SARIMAX with temperature as an exogenous regressor for day-ahead load, getting both a point forecast and a calibrated interval for reserve sizing.
- A retailer forecasts hundreds of SKU-store weekly series with automated ETS — fast, robust, no per-series tuning.
- A finance team forecasts monthly cash position with Holt's linear trend, because interpretability and a clean interval matter more than the last 2% of accuracy.

**Expected competencies.** Participants can specify a SARIMA(p,d,q)(P,D,Q)m model from ACF/PACF and information criteria, add exogenous regressors (SARIMAX), select an ETS specification from the taxonomy, run residual diagnostics, and produce forecasts with intervals — and articulate when to prefer each family.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Specify and fit ARIMA/SARIMA models with justified orders | LO2 |
| 3.2 | Incorporate exogenous regressors with SARIMAX | LO2, LO3 |
| 3.3 | Select an exponential-smoothing/ETS specification from the taxonomy | LO2 |
| 3.4 | Diagnose model adequacy from residuals | LO2, LO5 |
| 3.5 | Compare ARIMA and ETS and choose per situation | LO2, LO6 |

## Technical Content

### 1. The ARIMA family

**ARIMA(p,d,q)** combines three ideas on a differenced (stationary) series:
- **AR(p)** — autoregression: `y_t` depends linearly on its own `p` past values.
- **I(d)** — integration: `d` differences applied to reach stationarity (from Module 2).
- **MA(q)** — moving average: `y_t` depends on the last `q` forecast errors (shocks).

**SARIMA(p,d,q)(P,D,Q)m** adds a seasonal counterpart at period `m`: seasonal AR (`P`), seasonal differencing (`D`), seasonal MA (`Q`). For hourly `Tayyar` with a daily cycle, `m = 24`. Note a practical constraint: with `m = 24` (or worse, `168`) the state space grows and estimation slows sharply — a reason practitioners often model a *daily-aggregated* series with `m = 7` in SARIMA and leave sub-daily patterns to the ML approach in Module 4. Teach this trade-off explicitly; it is where classical methods strain.

### 2. Order selection

Two complementary routes, used together:
- **Read the correlograms** (Module 2): AR order from PACF cut-off, MA order from ACF cut-off, seasonal terms from spikes at `m`.
- **Minimise an information criterion** (AICc for small samples, BIC for parsimony) across a candidate grid. `pmdarima.auto_arima` automates a stepwise search, but the analyst constrains it (`max_p`, `seasonal=True`, `m=…`, `D=…`) and *confirms* the winner's residuals — automation without diagnostics is how bad models ship.

AIC/BIC compare models on the *same* data and difference order; never compare AIC across different `d`. Lower is better; differences under ~2 are not meaningful.

### 3. SARIMAX: exogenous regressors

Load is driven by **temperature** — a covariate available (as a forecast) at prediction time. **SARIMAX** adds exogenous regressors `X` to SARIMA: `y_t` is explained by its own dynamics *plus* a linear function of `X_t`. For `Tayyar` we add temperature, and calendar dummies (weekend, Ramadan, Eid). Two cautions: (1) at forecast time you need *future* values of the regressors — for temperature you use the weather forecast, and its error propagates into your load forecast; (2) regressors must be genuinely exogenous and available ahead of time, or you have built a leak.

### 4. Exponential smoothing and ETS

Exponential smoothing forecasts as a **weighted average of past observations with exponentially decaying weights** — recent points matter more. The ladder:
- **SES (simple):** level only; flat forecast. For series with no trend/season.
- **Holt (linear trend):** level + trend; the trend can be damped (`damped_trend=True`) so long-horizon forecasts don't extrapolate to implausible extremes — damping is almost always the safer production choice.
- **Holt-Winters (seasonal):** level + trend + seasonality, additive or multiplicative season.

The **ETS taxonomy** systematises this as (Error, Trend, Seasonal), each ∈ {None, Additive, Multiplicative}, e.g. ETS(A,Ad,M) = additive error, additive damped trend, multiplicative season. `statsmodels`' `ETSModel` (or the automated selection in `sktime`/`statsforecast`) picks the specification by AICc. ETS handles a single seasonal period cleanly; multiple seasonalities need TBATS or the ML route.

### 5. Residual diagnostics

A fitted model is only trustworthy if its **residuals are white noise** — no structure left to exploit. Check:
- **Residual ACF / Ljung-Box test:** null = "residuals are independent." A small p-value means autocorrelation remains → the model is missing structure (raise an order).
- **Residual mean ≈ 0** (no bias) and **roughly constant variance** (transform worked).
- **Approximate normality** (histogram / Q-Q) — matters for interval validity, less for the point forecast.

`statsmodels`' `plot_diagnostics()` produces all four panels at once. Teach diagnostics as *mandatory*, not optional: an un-diagnosed auto_arima result is a liability.

### 6. Common mistakes & production considerations

**Common mistakes**
1. Comparing AIC across models fitted with different differencing orders.
2. Trusting `auto_arima` without checking residual autocorrelation (Ljung-Box).
3. Forgetting exogenous regressors need future values at forecast time (temperature leak or unavailable).
4. Un-damped Holt trend producing absurd long-horizon forecasts.
5. Fitting multiplicative seasonality/ETS to a series containing zeros.
6. Reporting forecasts on the log scale, or back-transforming a log-mean without the bias correction.

**Production considerations.** Refit on a schedule (SARIMA parameters drift as the series evolves); persist orders and let re-selection be a monitored event. Classical models give analytic prediction intervals cheaply — use them as the honest baseline the fancier Module 5 methods must beat. For thousands of series, prefer automated ETS (`statsforecast` is vectorised and fast) over per-series ARIMA hand-tuning.

## Code Examples

### SARIMAX with temperature and calendar regressors

```python
# src/tayyar/models/sarimax.py
"""SARIMA + exogenous temperature/calendar for day-ahead load.
We model the DAILY-mean series with m=7 to keep estimation tractable;
sub-daily structure is handled by the ML model (Module 4)."""
import pandas as pd
import statsmodels.api as sm

def fit_sarimax(y: pd.Series, exog: pd.DataFrame,
                order=(2, 1, 1), seasonal_order=(1, 1, 1, 7)):
    model = sm.tsa.SARIMAX(
        y, exog=exog, order=order, seasonal_order=seasonal_order,
        enforce_stationarity=False, enforce_invertibility=False,
    )
    res = model.fit(disp=False)
    return res

def forecast_sarimax(res, exog_future: pd.DataFrame, steps: int):
    """Exog_future MUST be available at forecast time (weather forecast,
    known calendar). Returns mean + 90% interval on the original scale."""
    fc = res.get_forecast(steps=steps, exog=exog_future)
    mean = fc.predicted_mean
    ci = fc.conf_int(alpha=0.10)          # 90% interval
    return pd.DataFrame({"forecast": mean,
                         "lower": ci.iloc[:, 0],
                         "upper": ci.iloc[:, 1]})
```

### Automated order search with mandatory diagnostics

```python
# src/tayyar/models/auto_order.py
import pmdarima as pm
from statsmodels.stats.diagnostic import acorr_ljungbox

def select_arima(y, exog=None, m=7):
    model = pm.auto_arima(
        y, X=exog, seasonal=True, m=m,
        d=1, D=1,                      # from the Module 2 stationarity report
        max_p=3, max_q=3, max_P=2, max_Q=2,
        information_criterion="aicc", stepwise=True, suppress_warnings=True,
    )
    # MANDATORY: residuals must be white noise, else the model is under-specified
    lb = acorr_ljungbox(model.resid(), lags=[14], return_df=True)
    p = float(lb["lb_pvalue"].iloc[0])
    ok = p > 0.05
    print(f"Selected {model.order}x{model.seasonal_order} | "
          f"Ljung-Box p={p:.3f} -> {'white noise OK' if ok else 'STRUCTURE LEFT'}")
    return model, ok
```

### Automated ETS baseline

```python
# src/tayyar/models/ets.py
from statsmodels.tsa.exponential_smoothing.ets import ETSModel
import numpy as np, pandas as pd

def fit_ets(y: pd.Series, seasonal_periods=7):
    """Holt-Winters with DAMPED trend and multiplicative season.
    Damping keeps long-horizon forecasts sane."""
    model = ETSModel(y, error="add", trend="add", damped_trend=True,
                     seasonal="mul", seasonal_periods=seasonal_periods)
    res = model.fit(disp=False)
    return res

def forecast_ets(res, steps: int, alpha: float = 0.10) -> pd.DataFrame:
    pred = res.get_prediction(start=len(res.model.endog),
                              end=len(res.model.endog) + steps - 1)
    summary = pred.summary_frame(alpha=alpha)
    return summary.rename(columns={"mean": "forecast",
                                   "pi_lower": "lower", "pi_upper": "upper"})
```

## Hands-on Lab 3 — Classical Baselines: SARIMAX and ETS

| | |
|---|---|
| **Objective** | Fit SARIMAX (with temperature + calendar) and an automated ETS on the daily `Tayyar` series; diagnose both; produce 14-day-ahead forecasts with intervals |
| **Duration** | 50 minutes |
| **Setup** | Lab 2 solution (`git checkout lab3-start`), `pip install statsmodels pmdarima` |

**Instructions & tasks**

1. *(5 min)* Aggregate to a daily-mean series; build the exogenous frame: daily mean temperature, weekend flag, Ramadan flag, Eid flag (from `ksa_calendar.csv`). Hold out the last 14 days as a test window.
2. *(12 min)* Run `select_arima` (m=7, d/D from Lab 2); confirm the Ljung-Box p-value passes. If it fails, raise an order and re-fit. Record the selected orders.
3. *(10 min)* Fit `fit_ets` (damped trend, multiplicative season); inspect `res.summary()` for the chosen smoothing parameters.
4. *(10 min)* Forecast 14 days ahead with both models (SARIMAX needs the future exog — use the provided temperature forecast). Plot both against the held-out actuals with 90% intervals.
5. *(8 min)* Compute MAE and MAPE on the 14-day window for each; note which family wins and hypothesise why. Run `plot_diagnostics()` for SARIMAX.
6. *(5 min)* Commit: `feat(models): SARIMAX + ETS baselines with intervals and diagnostics`.

**Expected output**
```
$ python -m tayyar.models.run_classical
Selected (2,1,1)x(1,1,1)[7] | Ljung-Box p=0.214 -> white noise OK
ETS(A,Ad,M) chosen | alpha=0.41 beta=0.02 gamma=0.18 phi=0.98
14-day test  SARIMAX: MAE=612 MW  MAPE=1.9%   coverage(90%)=0.93
14-day test  ETS    : MAE=744 MW  MAPE=2.4%   coverage(90%)=0.86
Winner: SARIMAX (temperature regressor pays off in a heatwave week)
Wrote forecast_classical.png, diagnostics.png
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `auto_arima` runs for minutes | `m=24` on hourly series | Model the daily series with `m=7`; leave sub-daily to Module 4 |
| Ljung-Box p < 0.05 | Under-specified model | Raise `p`/`q` or seasonal order; re-diagnose |
| Forecast diverges to huge values | Un-damped trend | `damped_trend=True` |
| SARIMAX forecast errors on `get_forecast` | Missing future exog rows | Supply `exog_future` with exactly `steps` rows |

**Instructor notes.** The `m=24` slowdown (troubleshooting row 1) is a deliberate teachable wall — let a pair hit the multi-minute fit, then reframe to the daily series. This *motivates* Module 4: "if you want the hourly forecast, the ML route scales where SARIMA strains." Fast finishers: add a SARIMA *without* temperature and quantify how much the exogenous regressor buys.

## Mini Exercises

**Quiz (5 questions)**
1. What do the three letters in ARIMA(p,d,q) control? → AR order, differencing order, MA order.
2. In SARIMA(p,d,q)(P,D,Q)m, what is `m` for a daily cycle on hourly data? → **24**.
3. Why must exogenous regressors be known at forecast time? → you need their future values to forecast; otherwise it's a leak/unavailable.
4. What does a Ljung-Box p-value < 0.05 on residuals mean? → residual autocorrelation remains; model under-specified.
5. When is damped trend preferable? → almost always for multi-step horizons, to avoid implausible extrapolation.

**Debugging exercise.** Branch `sim-aic-trap` compares AIC across models with different `d`; participants explain why the comparison is invalid and fix it.

**Specification drill.** Given three series' ACF/PACF and descriptions, each pair writes the SARIMA order and an ETS(E,T,S) spec, then defends the choice.

## Case Study — Day-Ahead Load Forecasting for Reserve Margins

**Scenario.** The `Tayyar` team must deliver a day-ahead daily-peak load forecast with a *trustworthy interval*, because the reserve margin is set from the upper bound. Control-room engineers reject any model they cannot interrogate.

**Business context.** The interval, not just the point, drives money and reliability: too wide and reserves are wastefully high; too narrow and a hot afternoon risks shedding load. Interpretability is a hard requirement.

**Technical challenge.** Choose between SARIMAX (interpretable, interval-native, temperature-aware) and ETS (fast, robust, no exogenous) for a series with strong seasonality and a weather driver — and defend the choice to non-statisticians.

**Constraints.** Publication deadline (fit + forecast in minutes); temperature available only as a forecast (its error must be acknowledged); model must be explainable component-by-component.

**Solution approach (facilitate).** (1) ETS as the no-exog baseline; (2) SARIMAX adding temperature + calendar; (3) diagnose both; (4) compare on a held-out window with intervals *and coverage*; (5) recommend SARIMAX if temperature materially helps and coverage holds, else the simpler ETS — parsimony is a feature.

**Discussion questions.**
1. How does temperature-forecast error propagate into the load interval, and how would you widen the interval to account for it?
2. When would you ship the simpler ETS despite SARIMAX's lower point error?
3. How do you explain a SARIMAX forecast to a control-room engineer in one sentence?
4. What monitoring tells you the chosen orders have gone stale?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| Residual white noise | Adequacy | Ljung-Box p > 0.05 | `acorr_ljungbox` |
| Day-ahead MAPE (daily) | Accuracy | ≤ 2.5% on held-out window | MAPE on test |
| Interval coverage (90%) | Calibration | 0.88–0.93 | empirical coverage on test |
| Fit + forecast time | Performance | < 30 s for daily series | wall-clock |
| Exogenous value | Analysis | Quantified vs no-exog model | MAE delta |

**Example benchmark table (filled during lab):**

| Model | MAE (MW) | MAPE | 90% coverage | Fit time |
|---|---|---|---|---|
| ETS(A,Ad,M) | 744 | 2.4% | 0.86 | 3 s |
| SARIMAX + temp | 612 | 1.9% | 0.93 | 11 s |
| SARIMA (no exog) | 690 | 2.2% | 0.90 | 9 s |

## Required Visuals and Training Assets

### Diagrams
1. **ARIMA anatomy** — *Purpose:* demystify the acronym. *Elements:* three labelled blocks (AR feeds on past values, I differences, MA feeds on past errors) assembling into one forecast, with the seasonal counterpart mirrored below. *Style:* block-assembly diagram.
2. **ETS taxonomy tree** — *Purpose:* specification reference. *Elements:* branching (Error, Trend, Seasonal) × {N,A,M} with SES/Holt/Holt-Winters leaf labels. *Style:* decision tree, A4 poster.
3. **ARIMA vs ETS selection guide** — *Purpose:* per-situation choice. *Elements:* a flow of questions (exogenous drivers? many series? interpretability?) routing to a family. *Style:* flowchart.

### Images (screenshots)
1. **`plot_diagnostics` panel** — *why:* what "good residuals" look like; *content:* residual ACF flat, Q-Q near line.
2. **Forecast with interval vs actuals** — *why:* Lab 3 expected output; *content:* SARIMAX and ETS overlaid on held-out actuals.
3. **auto_arima + Ljung-Box console** — *why:* diagnostics-are-mandatory message.

### Simulations
1. **AIC-across-d trap** — *Setup:* `sim-aic-trap`. *Expected behaviour:* misleading "best" model from invalid comparison. *Learning objective:* compare like with like.
2. **Un-damped trend blow-up** — *Setup:* `sim-nodamp` forecasts 90 days with un-damped Holt. *Expected behaviour:* forecast runs to implausible values. *Learning objective:* damp long-horizon trends.

### Interactive Activities
- **Order-writing relay (15 min):** projected ACF/PACF; teams race to write SARIMA orders, then live-fit to check AICc.
- **"Explain it to the control room" (10 min):** each participant explains one fitted model's forecast in one plain sentence.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | (as Module 1) | CSV | ~26,300 rows | SARIMAX/ETS fitting |
| `ksa_calendar.csv` | (as Module 1) | CSV | ~1,100 rows | Exogenous calendar regressors |
| `temp_forecast_14d.csv` | Course-provided day-ahead temperature forecast | CSV | 14 rows | Future exog for SARIMAX |

### Demo Requirements
- **Instructor demo:** fit SARIMAX + ETS, diagnose, forecast with intervals in under 10 minutes; read the Ljung-Box aloud.
- **Student demo:** one pair defends SARIMAX vs ETS for the reserve-margin use case.
- **Expected outputs:** two forecasts with 90% intervals, diagnostics panel, MAE/MAPE/coverage table.

---

# Module 4 — Feature-Based ML Forecasting

## Module Overview

**Purpose.** This module reframes forecasting as **supervised learning**: turn a time series into a feature matrix (lags, rolling windows, calendar, Fourier terms, exogenous drivers) and let a gradient-boosting model learn the mapping. This "reduction" approach scales to the sub-hourly, multi-seasonal, covariate-rich problems where classical models strain, handles many related series in one model (global forecasting), and captures nonlinear interactions — the temperature-times-hour interaction that drives `Tayyar`'s summer afternoon peak. The catch, hammered throughout, is that every convenience of ML forecasting is also a fresh way to leak the future.

**Business relevance.** Most production forecasting at scale — retail demand across thousands of SKUs, ride-hailing demand per district per minute, energy load per feeder — runs on gradient-boosting reductions today. They win on accuracy when rich covariates exist, train in seconds on years of data, and let one model serve a whole portfolio. For Saudi programmes with abundant sensor and calendar data, this is the default modern approach.

**Industry use cases.**
- Grid load forecast per hour using lagged demand, temperature, hour-of-day, weekend, Ramadan, and their interactions in one LightGBM model.
- A national retailer forecasts daily sales for 5,000 SKU-store pairs with a single *global* LightGBM keyed by categorical IDs.
- A logistics firm forecasts parcel volume with weather and holiday features, updating hourly.

**Expected competencies.** Participants can build a leakage-safe temporal feature matrix, choose recursive versus direct multi-step strategies, train and tune LightGBM for forecasting, encode multiple seasonalities with Fourier terms, and read feature importance to explain the forecast.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Reduce a forecasting task to a supervised feature matrix without leakage | LO3, LO4 |
| 4.2 | Engineer lag, rolling-window, calendar, and Fourier features | LO3 |
| 4.3 | Train and tune gradient-boosting models (LightGBM) for forecasting | LO3 |
| 4.4 | Choose recursive vs direct multi-step forecasting strategies | LO3 |
| 4.5 | Interpret feature importance and compare against classical baselines | LO3, LO6 |

## Technical Content

### 1. Forecasting as supervised learning (reduction)

The core move: to forecast `y_t`, build a row of features known *strictly before* `t` — lagged values `y_{t-1}, y_{t-24}, y_{t-168}`, rolling statistics of the past, calendar attributes of `t`, and exogenous `X_t` (temperature, known at forecast time). Stack these rows into a matrix and it is an ordinary regression problem. This "reduction to tabular ML" is what `sktime`'s `make_reduction` and `skforecast`'s forecasters automate. The power: any tabular learner (LightGBM, XGBoost) now forecasts, with all its nonlinearity and covariate handling. The peril: the split, the features, and the validation must all respect time (Modules 2 and 6).

### 2. The feature families

- **Lag features:** `y` at 1, 2, 3, 24, 48, 168 hours ago — the model's memory. Choose lags from the ACF (Module 2): the significant lags *are* the useful features.
- **Rolling-window statistics:** mean/min/max/std over the past 24h, 168h — smoothed level and volatility. Critical: windows must end *before* the target (`.shift(1)` after rolling) or you leak the present into itself.
- **Calendar features:** hour-of-day, day-of-week, month, is-weekend (Fri–Sat), is-Ramadan, is-Eid, is-National-Day — encoded cyclically (`sin/cos`) or as categoricals.
- **Fourier terms:** pairs of `sin(2πkt/m), cos(2πkt/m)` compactly encode smooth seasonality of period `m` with few columns — the ML way to represent multiple seasonalities (daily *and* weekly *and* annual) simultaneously, which MSTL/SARIMA cannot do jointly.
- **Exogenous & interactions:** temperature, and explicit interactions (`temp × is_afternoon`) that capture the nonlinear AC-driven peak.

### 3. Multi-step strategies: recursive vs direct

Forecasting 24 hours ahead is not one prediction but 24. Two strategies:
- **Recursive:** train one model for one step; feed its prediction back as the lag to predict the next step, and so on. Compact, but errors compound and predicted lags differ in distribution from true lags.
- **Direct:** train a separate model per horizon (`h=1..24`), each predicting that horizon directly from features known at origin. No error compounding, but `H` models and no coherence guarantee across horizons.
- **Hybrid / multi-output** approaches (DirRec, or a single model taking horizon as a feature) trade off between them.

Teach the decision rule: short horizons with strong autocorrelation favour recursive; longer horizons or when error compounding bites favour direct. For `Tayyar`'s 24h day-ahead, direct-per-horizon (or `skforecast`'s `ForecasterDirect`) is a robust default.

### 4. Gradient boosting for forecasting

**LightGBM** is the workhorse: fast, handles categoricals natively, captures interactions, robust to feature scaling. Forecasting-specific guidance:
- Trees **cannot extrapolate** beyond the training range — a boosted model will never forecast a demand higher than any it has seen. Mitigate by (a) modelling on a differenced/detrended target so the level trend is handled outside the trees, or (b) including a trend feature (time index) with care.
- Tune with **time-series cross-validation** (Module 6), never random folds. Key knobs: `num_leaves`, `learning_rate` + `n_estimators`, `min_child_samples`, and regularisation.
- For many series, train **one global model** with the series ID as a categorical — it shares strength across series and often beats per-series models.

### 5. Design principles, best practices, common mistakes

**Principles**
- *Every feature must be computable at forecast time using only the past.* Write it on the board; it is the module's whole ethic.
- *Choose lags from the ACF, not from a guess.* The data already told you (Module 2).
- *Prefer differenced/relative targets* so trees operate in a stationary range they can interpolate.

**Common mistakes (each in the Lab 4 starter deliberately)**
1. `train_test_split(shuffle=True)` on time series — the cardinal leak; test rows precede train rows.
2. Rolling features that include the current row (forgot `.shift(1)`) — the target leaks into its own feature.
3. Scaling/encoding fit on the whole dataset before the split — the future's statistics contaminate the past.
4. Using a *future* value of an exogenous driver that won't be known at prediction time.
5. Ignoring that trees can't extrapolate, then being surprised the model under-forecasts a record heatwave.
6. Reporting feature importance as causal ("hour_of_day causes demand") rather than associational.

**Production considerations.** Feature pipelines must be identical in training and serving (a shared, versioned feature module — the training/serving-skew lesson). Recompute lags from a reliable recent-history store at serving time. Retrain on a cadence; monitor feature drift (temperature regime shifts, new industrial load). Log feature values with the prediction for debuggability.

### 6. Real-world example walkthrough

Narrate this: a demand team's LightGBM scored a stunning backtest — MAPE 0.6% — and then failed badly live. The culprit: a rolling-mean feature computed with a centred window (pandas default when you forget to shift), so each training row's "past 24h average" secretly included the target hour and its future neighbours. The backtest was measuring the model's ability to read the answer. One `.shift(1)` fixed the feature and the honest MAPE rose to 2.1% — worse on paper, real in production. This module exists to make that `.shift(1)` reflexive.

## Code Examples

### Leakage-safe feature engineering

```python
# src/tayyar/features/build.py
"""Temporal features. INVARIANT: every column is computable using only
information available strictly BEFORE the target timestamp."""
import numpy as np
import pandas as pd

def add_lags(df: pd.DataFrame, col="demand_mw",
             lags=(1, 2, 3, 24, 48, 168)) -> pd.DataFrame:
    out = df.copy()
    for L in lags:
        out[f"lag_{L}"] = out[col].shift(L)          # strictly past
    return out

def add_rolling(df: pd.DataFrame, col="demand_mw",
                windows=(24, 168)) -> pd.DataFrame:
    out = df.copy()
    for w in windows:
        # shift(1) FIRST so the window ends the hour BEFORE the target
        past = out[col].shift(1)
        out[f"roll_mean_{w}"] = past.rolling(w).mean()
        out[f"roll_std_{w}"]  = past.rolling(w).std()
        out[f"roll_max_{w}"]  = past.rolling(w).max()
    return out

def add_calendar(df: pd.DataFrame, calendar: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    idx = out.index
    out["hour"] = idx.hour
    out["dow"] = idx.dayofweek
    out["month"] = idx.month
    out["is_weekend"] = idx.dayofweek.isin([3, 4]).astype(int)  # Thu=3? -> Fri/Sat
    # KSA weekend is Friday(4)/Saturday(5) in pandas dayofweek (Mon=0)
    out["is_weekend"] = idx.dayofweek.isin([4, 5]).astype(int)
    out = out.join(calendar[["is_ramadan", "is_eid", "is_national_day"]],
                   how="left").fillna({"is_ramadan": 0, "is_eid": 0,
                                       "is_national_day": 0})
    return out

def add_fourier(df: pd.DataFrame, periods=(24, 168, 8766), k=3) -> pd.DataFrame:
    """Compact multi-seasonality encoding: k sin/cos pairs per period."""
    out = df.copy()
    t = np.arange(len(out))
    for m in periods:
        for i in range(1, k + 1):
            out[f"sin_{m}_{i}"] = np.sin(2 * np.pi * i * t / m)
            out[f"cos_{m}_{i}"] = np.cos(2 * np.pi * i * t / m)
    return out
```

### Direct multi-step LightGBM forecaster

```python
# src/tayyar/models/lgbm_forecaster.py
"""Direct strategy: one LightGBM per horizon h=1..H. No error compounding.
Target is the LOG-difference so trees interpolate in a stationary range."""
import lightgbm as lgb
import numpy as np, pandas as pd

FEATURES = None  # set after feature build; excludes the raw target

def make_direct_targets(y: pd.Series, H: int = 24) -> pd.DataFrame:
    """Target for horizon h is y shifted -h (the future we predict)."""
    return pd.DataFrame({f"y_h{h}": y.shift(-h) for h in range(1, H + 1)})

def train_direct(X: pd.DataFrame, Y: pd.DataFrame, params: dict) -> dict:
    models = {}
    for col in Y.columns:
        mask = Y[col].notna() & X.notna().all(axis=1)
        models[col] = lgb.LGBMRegressor(**params).fit(X[mask], Y[col][mask])
    return models

def forecast_direct(models: dict, x_origin: pd.DataFrame) -> pd.Series:
    """One feature row at the forecast origin -> H predictions."""
    preds = {int(c.split("h")[1]): m.predict(x_origin)[0]
             for c, m in models.items()}
    return pd.Series(dict(sorted(preds.items())))

DEFAULT_PARAMS = dict(n_estimators=400, learning_rate=0.05, num_leaves=63,
                      min_child_samples=50, subsample=0.8,
                      colsample_bytree=0.8, random_state=42)
```

### Feature importance for explanation

```python
# src/tayyar/models/explain.py
import pandas as pd

def importance_table(models: dict, feature_names, top: int = 15) -> pd.DataFrame:
    """Average gain importance across the per-horizon models."""
    import numpy as np
    gains = np.mean([m.booster_.feature_importance(importance_type="gain")
                     for m in models.values()], axis=0)
    return (pd.DataFrame({"feature": feature_names, "gain": gains})
            .sort_values("gain", ascending=False).head(top)
            .reset_index(drop=True))
```

## Hands-on Lab 4 — LightGBM Feature-Based Forecaster

| | |
|---|---|
| **Objective** | Build a leakage-safe feature matrix and a direct multi-step LightGBM that forecasts 24 hours ahead of hourly `Tayyar` demand, then explain it and beat the classical baseline |
| **Duration** | 50 minutes |
| **Setup** | Lab 3 solution (`git checkout lab4-start`), `pip install lightgbm skforecast` |

**Instructions & tasks**

1. *(5 min)* The starter has a deliberate `train_test_split(shuffle=True)` and a centred rolling feature. Find both leaks before writing new code — write them in `LEAKS.md`.
2. *(12 min)* Build features: lags from your Lab 2 ACF, rolling windows (with `.shift(1)`), calendar (Fri–Sat weekend, Ramadan/Eid), and Fourier terms for daily+weekly. Verify no feature uses future data with the provided `assert_no_leakage` helper.
3. *(12 min)* Create direct targets for H=24; split by *time* (last 28 days = test); train the per-horizon LightGBM.
4. *(8 min)* Forecast the test window day-by-day; compute MAE and MAPE; overlay against actuals and the SARIMAX baseline from Lab 3.
5. *(8 min)* Produce the feature-importance table; interpret the top five (expect `lag_24`, `lag_168`, temperature, hour, roll_mean_24).
6. *(5 min)* Commit: `feat(models): leakage-safe LightGBM direct forecaster + importance`.

**Expected output**
```
$ python -m tayyar.models.run_lgbm
Leak check: PASS (no feature references t or the future)
Direct H=24 trained (24 models) in 6.1s
Test (28d, hourly)  LightGBM: MAE=498 MW  MAPE=1.6%
Baseline compare    SARIMAX : MAE=612 MW  MAPE=1.9%   -> LightGBM wins on hourly
Top features: lag_24 (31%), temp_c (22%), lag_168 (14%), hour (9%), roll_mean_24 (7%)
Wrote forecast_lgbm.png, importance.png, LEAKS.md
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| MAPE suspiciously < 0.7% | Leak surviving (centred window / shuffle split) | Re-run `assert_no_leakage`; add `.shift(1)` to rolling |
| Model under-forecasts a heat spike | Trees can't extrapolate | Model log-difference target or add temperature interaction |
| NaN rows dropped, tiny train set | Long lags/windows create leading NaNs | Expected; ensure enough history before first target |
| Weekend feature wrong days | Coded Sat–Sun | KSA weekend = Fri(4)/Sat(5) in pandas dayofweek |

**Instructor notes.** Task 1 (find the two leaks) is the single most important 5 minutes of Day 2 — do not let anyone skip to modelling. When a pair reports MAPE 0.6%, celebrate publicly *then* reveal the leak; the emotional whiplash cements the lesson. Fast finishers: try a global model across two operating areas with an area-ID categorical.

## Mini Exercises

**Quiz (5 questions)**
1. Why is `train_test_split(shuffle=True)` fatal for time series? → test points can precede train points; leaks the future.
2. What does `.shift(1)` before a rolling window prevent? → the window including the target hour (self-leak).
3. Recursive vs direct multi-step — which compounds errors? → **recursive**.
4. Why can't a boosted-tree model forecast a record-high value? → trees interpolate; they can't extrapolate beyond training range.
5. What tells you which lags to include as features? → the **ACF** (significant lags).

**Debugging exercise.** Branch `sim-centred-roll` uses a centred rolling mean; participants locate the leak via the too-good backtest and fix with `.shift(1)`.

**Feature-design drill.** Given the `Tayyar` decomposition, each pair proposes five features and states, for each, exactly what past information it uses and why it is leak-free.

## Case Study — Scaling Load Forecasting Across Operating Areas

**Scenario.** `Tayyar` must expand from one operating area to all four (Central, Eastern, Western, Southern). Maintaining four hand-tuned SARIMA models per area is unsustainable; the team evaluates a single *global* LightGBM.

**Business context.** Four areas × hourly × day-ahead is a lot of forecasts; consistency, maintainability, and shared learning (a heatwave pattern in one area informs another) matter as much as raw accuracy.

**Technical challenge.** Build one feature matrix spanning all areas with an area-ID categorical, avoid leakage across areas, and confirm the global model matches or beats per-area classical baselines.

**Constraints.** Areas differ in level (Central is largest) and in weather regime; the model must not let a large area dominate the loss; features must be identical in training and serving.

**Solution approach (facilitate).** (1) Long-format panel with `area_id`; (2) per-area target scaling or a relative target so levels don't dominate; (3) global LightGBM with `area_id` categorical + Fourier + temperature; (4) backtest per area (Module 6); (5) compare to four SARIMAX baselines and to maintenance cost.

**Discussion questions.**
1. When does a global model beat per-series models, and when does it hurt a small, idiosyncratic series?
2. How do you prevent the largest area from dominating a global loss?
3. What leakage risks are unique to a multi-series panel (e.g., a global scaler)?
4. How do you weigh a 0.2% accuracy gain against four fewer models to maintain?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| Leakage check | Rigor | PASS (0 future-referencing features) | `assert_no_leakage` |
| Hourly day-ahead MAPE | Accuracy | ≤ 1.8% on held-out window | MAPE on test |
| Beats classical baseline | Accuracy | LightGBM MAE < SARIMAX MAE on hourly | side-by-side |
| Training time (24 models) | Performance | < 20 s on lab laptop | wall-clock |
| Feature interpretability | Explainability | Top-5 features named and justified | importance table |

**Example benchmark table (filled during lab):**

| Model | MAE (MW) | MAPE | Train time | Extrapolation-safe |
|---|---|---|---|---|
| SARIMAX (daily→hourly) | 612 | 1.9% | 11 s | yes |
| LightGBM raw target | 540 | 1.7% | 6 s | no (under heatwaves) |
| LightGBM log-diff target | 498 | 1.6% | 6 s | improved |

## Required Visuals and Training Assets

### Diagrams
1. **Reduction to supervised learning** — *Purpose:* the module's central idea. *Elements:* a series unrolling into a sliding window that becomes one feature-matrix row with a target; arrow to a tree model. *Style:* sliding-window animation still.
2. **Leakage smell poster** — *Purpose:* the course's ethic, made unavoidable. *Elements:* four red-flagged patterns (shuffle split, centred window, global scaler, future exog) each with the fix. *Style:* red-alert reference, A4.
3. **Recursive vs direct** — *Purpose:* strategy choice. *Elements:* recursive loop feeding predictions back vs H parallel models; error-compounding arrow on the recursive path. *Style:* side-by-side.

### Images (screenshots)
1. **Feature matrix head** — *why:* shows lags/rolling/calendar/Fourier columns; *content:* a few rows with NaN leading edge.
2. **Importance bar chart** — *why:* Lab 4 output; *content:* lag_24 and temp dominating.
3. **Too-good backtest reveal** — *why:* the leak lesson; *content:* MAPE 0.6% before vs 1.6% after fix.

### Simulations
1. **Centred-window leak** — *Setup:* `sim-centred-roll`. *Expected behaviour:* implausibly low backtest error. *Learning objective:* shift before rolling.
2. **Extrapolation failure** — *Setup:* `sim-heatwave` holds out a record-high week. *Expected behaviour:* raw-target model under-forecasts the peak. *Learning objective:* trees can't extrapolate; difference the target.

### Interactive Activities
- **Leak hunt (15 min):** pairs race to find planted leaks in a given feature script; first correct wins.
- **"What does this feature see?" (10 min):** for eight candidate features, class votes leak / safe and justifies.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | (as Module 1) | CSV | ~26,300 rows | Feature matrix + LightGBM |
| `ksa_grid_demand_4area.csv` | Course-generated 4-area panel | CSV | ~105,000 rows | Global-model case study |
| `ksa_calendar.csv` | (as Module 1) | CSV | ~1,100 rows | Calendar features |

### Demo Requirements
- **Instructor demo:** build features, reveal a planted leak, fix it, train LightGBM, show importance — under 10 minutes.
- **Student demo:** one pair presents their leak findings and the honest post-fix MAPE.
- **Expected outputs:** leak-free feature matrix, trained direct forecaster, importance table, comparison to SARIMAX.

---

# Module 5 — Probabilistic Forecasts and Intervals

## Module Overview

**Purpose.** A point forecast is a lie by omission: it states what *will* happen while hiding how sure the model is. Yet every decision built on a forecast is really a decision under uncertainty — how much reserve generation to keep spinning, how much stock to hold, how many staff to roster. This module teaches participants to produce and validate *probabilistic* forecasts: prediction intervals and full predictive quantiles that carry honest uncertainty. They learn quantile regression with the pinball loss, LightGBM quantile models, model-native intervals, and a distribution-free safety net — **conformal prediction** — then judge all of them on the only thing that matters for an interval: whether its stated coverage is the coverage it actually delivers.

**Business relevance.** For `Tayyar`, the reserve margin is sized off the *upper* bound of the day-ahead forecast, not the mean. An interval that is too narrow risks load-shedding on a 47 °C afternoon; one that is too wide burns fuel keeping idle turbines hot. The interval *is* the product. Across national programmes — treasury cash buffers, hospital surge capacity, strategic-reserve stocking — the decision is a quantile decision, and a well-calibrated interval is worth more than a point forecast that is 1% sharper but silent about risk.

**Industry use cases.**
- A grid operator sets the day-ahead reserve at the 95th percentile of predicted load, so the spinning reserve covers all but the worst 5% of afternoons.
- A retailer stocks each SKU to a service-level quantile (e.g. the 90th percentile of demand) rather than the mean, directly trading holding cost against stock-outs.
- A cloud-capacity team provisions to a high quantile of predicted traffic, accepting a known small probability of saturation instead of paying for the mean-plus-guesswork.

**Expected competencies.** After this module a participant can produce prediction intervals from a classical model, train LightGBM quantile models with the pinball loss, wrap any point forecaster with split-conformal prediction to guarantee marginal coverage, and evaluate intervals on coverage, sharpness, and pinball loss — choosing the method whose *empirical* coverage matches its *nominal* target.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain why point forecasts are insufficient and frame decisions as quantile problems | LO5 |
| 5.2 | Produce prediction intervals from classical (analytic) and ML (quantile) models | LO5 |
| 5.3 | Train quantile models with the pinball/quantile loss | LO3, LO5 |
| 5.4 | Apply split-conformal prediction for distribution-free coverage guarantees | LO4, LO5 |
| 5.5 | Evaluate intervals on coverage, sharpness, and pinball loss and diagnose miscalibration | LO5, LO6 |

## Technical Content

### 1. Why a point forecast is not enough

A point forecast collapses a whole predictive distribution to a single number, discarding exactly the information a risk-aware decision needs. Two forecasts can share a mean of 50,000 MW while one is near-certain and the other spans ±8,000 MW — and the reserve-margin decision is completely different. The reframing: **forecast the distribution, then let the decision pick the quantile it needs.** A cost-asymmetric decision (under-forecasting load is far more expensive than over-forecasting) does not want the mean at all — it wants the quantile whose position reflects that asymmetry. This module's ethic: *report uncertainty, and then prove it is honest.*

### 2. Prediction intervals vs confidence intervals

Sharpen a distinction learners routinely blur. A **confidence interval** quantifies uncertainty about a *parameter* (the mean level). A **prediction interval** quantifies uncertainty about a *future observation* — it must include both parameter uncertainty *and* the irreducible noise of a single realisation, so it is always wider. Forecasting is about future observations, so we almost always want **prediction intervals**. A classical model like SARIMAX or ETS produces these analytically (Module 3's `conf_int` / `summary_frame`), but the analytic interval trusts the model's distributional assumptions (usually Gaussian residuals with constant variance) — assumptions that summer heteroskedasticity in `Tayyar` violates, which is exactly why we cross-check with empirical methods.

### 3. Quantile regression and the pinball loss

To predict the τ-quantile directly, train a model to minimise the **pinball (quantile) loss**:

```
L_τ(y, ŷ) = max( τ·(y − ŷ),  (τ − 1)·(y − ŷ) )
```

It penalises under- and over-prediction *asymmetrically*: for τ = 0.9 an under-prediction costs 0.9 per unit while an over-prediction costs 0.1, so the minimiser sits where 90% of the mass falls below it — the 90th percentile. Fit one model per quantile (e.g. τ ∈ {0.05, 0.5, 0.95}) and the 0.05/0.95 pair *is* a 90% interval. LightGBM supports this natively with `objective="quantile", alpha=τ`. The pinball loss is also the *evaluation* metric for probabilistic forecasts (Module 6), so training and scoring speak the same language.

**Quantile crossing.** Independently-fit quantile models can cross (the predicted 0.95 dipping below the 0.50 on some rows) — an incoherent distribution. Detect it, and repair by sorting the predicted quantiles per row (isotonic post-processing) or by fitting a monotone-constrained model.

### 4. Conformal prediction: coverage you can guarantee

Quantile models give sharp intervals but *no guarantee* their coverage is correct — a miscalibrated model can claim 90% and deliver 78%. **Split (inductive) conformal prediction** fixes this with a model-agnostic wrapper that guarantees marginal coverage under one weak assumption (exchangeability of the calibration and test residuals):

1. Split the history into a training set and a held-out **calibration** set.
2. Fit the point model on the training set; on the calibration set compute nonconformity scores — typically the absolute residual `|y − ŷ|`.
3. Take the ⌈(n+1)(1−α)⌉/n empirical quantile `q̂` of those scores.
4. The interval for a new point is `ŷ ± q̂` — guaranteed ≈ (1−α) marginal coverage.

For time series the plain exchangeability assumption is strained (residuals are serially correlated and can drift), so we use time-series-aware variants — **EnbPI** or **adaptive conformal (ACI)**, which update `q̂` online as coverage errors accumulate. **Conformalised quantile regression (CQR)** is the best of both: it conformalises the quantile-model interval, keeping the sharpness of quantile regression *and* the coverage guarantee of conformal. Teach CQR as the default for `Tayyar`.

### 5. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Coverage first, sharpness second.* An interval that misses its coverage target is wrong at any width. Only among intervals that hit coverage do you prefer the sharpest (narrowest).
- *Calibrate on data the model never trained on.* Conformal and any coverage estimate must use a held-out calibration window that respects time — never the training set.
- *Decisions consume quantiles, not means.* Elicit the decision's cost asymmetry and report the quantile it needs, not a generic 95%.

**Common mistakes (each appears in the Lab 5 starter deliberately)**
1. Reporting a confidence interval where a prediction interval is required (far too narrow).
2. Trusting an analytic Gaussian interval on a heteroskedastic series — coverage collapses in summer.
3. Estimating coverage on the training set (optimistic) instead of a held-out window.
4. Letting quantile models cross and shipping an incoherent distribution.
5. Using vanilla i.i.d. conformal on a strongly autocorrelated series and over-trusting the guarantee.
6. Comparing two methods on sharpness alone while one silently under-covers.

**Production considerations.** Monitor *rolling empirical coverage* as a first-class metric — a drift from 90% to 80% signals the interval has gone stale before point error visibly degrades. Recalibrate conformal quantiles on a schedule; persist the calibration window and `q̂`. Expose the quantiles the downstream decision consumes (e.g. p50, p90, p95) as explicit service outputs, not a single number.

### 6. Real-world example walkthrough

Narrate this (5 minutes): a demand team shipped SARIMAX with its analytic 90% interval and reported it "covered 90% in the backtest — averaged over the year." Operations complained anyway: on the summer afternoons that actually mattered, coverage was ~78% — the constant-variance assumption under-widened exactly when demand variance spiked, so reserves were set too low on the hottest days. Averaged coverage hid a conditional failure. The fix was not a better point model but honest intervals: CQR widened the summer-afternoon interval where the data demanded it and tightened the calm winter nights, restoring conditional coverage without inflating the average width. This module is that discipline — an interval must be right *when it is consulted*, not merely on average.

## Code Examples

### LightGBM quantile models and a prediction interval

```python
# src/tayyar/models/quantile.py
"""Quantile forecasting with the pinball loss. Fit one LightGBM per quantile;
the (0.05, 0.95) pair is a 90% prediction interval. Guard against crossing."""
import numpy as np
import pandas as pd
import lightgbm as lgb

QUANTILES = (0.05, 0.50, 0.95)

def train_quantiles(X: pd.DataFrame, y: pd.Series,
                    quantiles=QUANTILES, params=None) -> dict:
    params = params or dict(n_estimators=400, learning_rate=0.05,
                            num_leaves=63, min_child_samples=50)
    models = {}
    for q in quantiles:
        models[q] = lgb.LGBMRegressor(objective="quantile", alpha=q,
                                      **params).fit(X, y)
    return models

def predict_interval(models: dict, X: pd.DataFrame) -> pd.DataFrame:
    preds = {q: m.predict(X) for q, m in models.items()}
    out = pd.DataFrame(preds, index=X.index)
    # Repair any quantile crossing by sorting each row's quantiles ascending.
    out.values.sort(axis=1)
    out.columns = [f"q{int(q*100):02d}" for q in sorted(models)]
    return out            # columns q05, q50, q95  ->  q05..q95 is the 90% PI
```

### The pinball loss (train and evaluate)

```python
# src/tayyar/eval/pinball.py
import numpy as np, pandas as pd

def pinball_loss(y_true: np.ndarray, y_pred: np.ndarray, q: float) -> float:
    """Average pinball loss at quantile q. Lower is better."""
    e = y_true - y_pred
    return float(np.mean(np.maximum(q * e, (q - 1.0) * e)))

def mean_pinball(y_true, q_preds: pd.DataFrame, quantiles) -> float:
    """Mean pinball across a set of quantile columns — a proper score for
    the whole predictive distribution."""
    losses = [pinball_loss(y_true, q_preds[f"q{int(q*100):02d}"], q)
              for q in quantiles]
    return float(np.mean(losses))
```

### Split-conformal / CQR wrapper for guaranteed coverage

```python
# src/tayyar/models/conformal.py
"""Conformalised Quantile Regression (CQR): keep quantile-model sharpness,
add a distribution-free coverage guarantee via a held-out calibration set."""
import numpy as np, pandas as pd

def cqr_calibrate(lo_cal: np.ndarray, hi_cal: np.ndarray,
                  y_cal: np.ndarray, alpha: float = 0.10) -> float:
    """Nonconformity = how far the truth fell OUTSIDE the [lo, hi] band.
    Returns the correction q_hat to widen the band to (1 - alpha) coverage."""
    scores = np.maximum(lo_cal - y_cal, y_cal - hi_cal)   # >0 when outside
    n = len(scores)
    k = int(np.ceil((n + 1) * (1 - alpha)))
    q_hat = np.sort(scores)[min(k, n) - 1]
    return float(q_hat)

def cqr_apply(lo: np.ndarray, hi: np.ndarray, q_hat: float):
    """Widen the raw quantile interval by the calibrated correction."""
    return lo - q_hat, hi + q_hat

def empirical_coverage(y: np.ndarray, lo: np.ndarray, hi: np.ndarray) -> float:
    return float(np.mean((y >= lo) & (y <= hi)))

def mean_width(lo: np.ndarray, hi: np.ndarray) -> float:
    return float(np.mean(hi - lo))
```

## Hands-on Lab 5 — Calibrated Day-Ahead Intervals

| | |
|---|---|
| **Objective** | Produce 90% day-ahead intervals for hourly `Tayyar` demand three ways — analytic SARIMAX, LightGBM quantile, and CQR — and pick the method whose empirical coverage matches 90% at the sharpest width |
| **Duration** | 50 minutes (Day 2 H5 start → Day 3 H1 finish) |
| **Setup** | Lab 4 solution (`git checkout lab5-start`), `pip install lightgbm statsmodels` |

**Instructions & tasks**

1. *(5 min)* The starter reports a *confidence* interval and estimates coverage on the *training* set — find both bugs and note them in `INTERVALS.md` before writing code.
2. *(10 min)* Reuse the Lab 4 feature matrix. Split the history into train / calibration / test by *time* (last 28 days = test; the 28 days before = calibration). Train LightGBM quantile models for τ ∈ {0.05, 0.50, 0.95}; repair any crossing.
3. *(10 min)* Compute empirical coverage and mean width of the raw 0.05–0.95 interval on the test window. Expect coverage below 90% (quantile models rarely hit nominal).
4. *(10 min)* Calibrate with `cqr_calibrate` on the calibration window; apply `cqr_apply` to the test interval; recompute coverage and width. Coverage should snap to ≈ 0.90.
5. *(10 min)* Add the analytic SARIMAX interval (Lab 3) on the same test window. Build the comparison table: method × {coverage, mean width, mean pinball}. Plot all three intervals over one hot week.
6. *(5 min)* Recommend one method with a one-paragraph justification in `INTERVALS.md`. Commit: `feat(models): calibrated day-ahead intervals via CQR + coverage report`.

**Expected output**
```
$ python -m tayyar.models.run_intervals
Test window: 28 days hourly (672 points)
SARIMAX analytic   : coverage=0.82  width=3100 MW  pinball=210   (under-covers in summer)
LGBM quantile raw  : coverage=0.86  width=2740 MW  pinball=188
LGBM quantile + CQR: coverage=0.91  width=3020 MW  pinball=181   <- hits nominal, sharpest at target
Recommendation: CQR (only method covering >= 0.90; 3% narrower than analytic at equal coverage)
Wrote intervals_hotweek.png, coverage_table.csv, INTERVALS.md
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Coverage ≈ 1.0, huge width | `alpha` mixed up (used 0.90 as tail not 0.10) | 90% interval → τ = 0.05 and 0.95; α = 0.10 |
| Predicted q95 below q50 on some rows | Quantile crossing | Sort per-row quantiles (isotonic) or monotone constraint |
| CQR barely changes the interval | Calibrated on the training set (residuals too small) | Calibrate on a held-out window that respects time |
| Coverage great, decision still fails on hot days | Marginal not conditional coverage | Report coverage *by hour band*; consider ACI/EnbPI |

**Instructor notes.** The moment that lands is task 3→4: a quantile interval claiming 90% actually covering 86%, then CQR snapping it to 91%. Put the coverage number on the board before and after. Fast finishers: bucket coverage by hour-of-day and expose the summer-afternoon conditional gap — the motivation for adaptive conformal.

## Mini Exercises

**Quiz (5 questions)**
1. Prediction interval or confidence interval for a future observation? → **prediction interval** (wider; includes noise).
2. What quantile does minimising pinball loss at τ = 0.9 recover? → the **90th percentile**.
3. What does split-conformal guarantee, and under what assumption? → marginal (1−α) coverage, under exchangeability of calibration/test scores.
4. Why can independently-fit quantile models be incoherent? → they can **cross** (q95 < q50); fix by sorting/monotone constraint.
5. Two intervals both cover 90% — which do you ship? → the **sharper** (narrower) one.

**Debugging exercise.** Branch `sim-train-coverage` estimates coverage on the training set (reports 0.94, delivers 0.83 on test). Participants relocate the estimate to a held-out window and explain the optimism.

**Elicitation drill.** Given three decisions (reserve margin, SKU stocking, staff roster) with stated cost asymmetries, each pair names the quantile the decision should consume and justifies it.

## Case Study — Sizing the Reserve Margin with Honest Uncertainty

**Scenario.** `Tayyar` must publish not just a day-ahead load point forecast but the **90th- and 95th-percentile** load, because the control room sets spinning reserve to the upper bound. Last summer the analytic interval under-covered on the hottest afternoons and reserves were set too low twice.

**Business context.** Reserve set to the 95th percentile means accepting a ~5% chance of dipping into emergency reserve on any afternoon — an explicit, defensible risk posture. Getting the quantile wrong is asymmetric: an under-covered upper bound risks load-shedding (headline-grade), while over-coverage wastes fuel (merely expensive).

**Technical challenge.** Deliver intervals whose coverage holds *conditionally* on the high-demand summer afternoons, not just on average across the year — the analytic Gaussian interval fails exactly here.

**Constraints.** Afternoon publication deadline (calibration must be cheap); the upper quantile must be explainable to control-room engineers; temperature-forecast error inflates true uncertainty and must be reflected in the width.

**Solution approach (facilitate).** (1) LightGBM quantile models at 0.5/0.9/0.95; (2) CQR calibration on a rolling recent window; (3) report coverage bucketed by hour-of-day and by temperature band to expose conditional gaps; (4) if the summer-afternoon bucket under-covers, switch to adaptive conformal (ACI) that widens online; (5) hand operations the p95 as the reserve-sizing input with its measured conditional coverage.

**Discussion questions.**
1. Why does an analytic Gaussian interval under-cover on high-variance summer afternoons?
2. Marginal vs conditional coverage — why can a model be perfect on one and dangerous on the other?
3. How should temperature-forecast uncertainty widen the load interval?
4. What rolling metric warns you the interval has gone stale before point error degrades?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| Empirical coverage (90%) | Calibration | 0.88–0.92 on held-out test | `empirical_coverage` |
| Conditional coverage (summer PM) | Calibration | ≥ 0.88 in the high-demand bucket | coverage by hour/temp band |
| Interval sharpness | Efficiency | Narrowest width at target coverage | `mean_width` |
| Mean pinball loss | Proper score | Lower than point-only baseline | `mean_pinball` |
| Quantile coherence | Rigor | 0 crossing rows | per-row monotonicity check |

**Example benchmark table (filled during lab):**

| Method | Coverage | Mean width (MW) | Mean pinball | Conditional (summer PM) |
|---|---|---|---|---|
| SARIMAX analytic | 0.82 | 3,100 | 210 | 0.76 |
| LGBM quantile (raw) | 0.86 | 2,740 | 188 | 0.80 |
| LGBM quantile + CQR | 0.91 | 3,020 | 181 | 0.89 |

## Required Visuals and Training Assets

### Diagrams
1. **Point forecast vs predictive distribution** — *Purpose:* the module's thesis. *Elements:* one point-forecast line vs a fan chart of quantiles, with a decision threshold cutting the fan at p95. *Style:* fan-chart poster, English labels + Arabic subtitles.
2. **The pinball loss** — *Purpose:* explain asymmetric penalty. *Elements:* a V-shaped loss with unequal arms for τ = 0.9, annotated with under-/over-prediction costs. *Style:* single annotated plot.
3. **Conformal calibration flow** — *Purpose:* demystify CQR. *Elements:* train → fit quantiles → calibration residuals → q̂ → widened interval, four boxes left to right. *Style:* pipeline flow.

### Images (screenshots)
1. **Coverage-vs-width table** — *why:* Lab 5 output; *content:* three methods with coverage snapping to 0.90 after CQR.
2. **Fan chart over a hot week** — *why:* shows intervals widening on summer afternoons; *content:* actuals inside the calibrated band.
3. **Coverage by hour-of-day** — *why:* marginal vs conditional lesson; *content:* the summer-afternoon dip before/after ACI.

### Simulations
1. **Heteroskedastic under-coverage** — *Setup:* branch `sim-hetero` inflates summer variance. *Expected behaviour:* analytic interval covers ~90% overall but ~78% in summer. *Learning objective:* conditional coverage matters.
2. **Train-set coverage optimism** — *Setup:* `sim-train-coverage`. *Expected behaviour:* reported 0.94, delivered 0.83. *Learning objective:* calibrate on held-out data.

### Interactive Activities
- **Quantile-decision match (10 min):** cards pair a decision with its cost asymmetry; class picks the serving quantile.
- **Coverage courtroom (15 min):** one pair "defends" an interval's 90% claim; another cross-examines with the held-out coverage number.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | (as Module 1) | CSV | ~26,300 rows | Quantile models + calibration |
| `ksa_calendar.csv` | (as Module 1) | CSV | ~1,100 rows | Calendar features for quantile models |
| `temp_forecast_28d.csv` | Course-provided day-ahead temperature forecast | CSV | 28×24 rows | Future exog for the test window |

### Demo Requirements
- **Instructor demo:** train quantile models, show raw under-coverage, apply CQR, watch coverage snap to 0.90 — under 10 minutes.
- **Student demo:** one pair reads their coverage/width/pinball table and defends the recommended method.
- **Expected outputs:** three intervals, coverage/width/pinball table, `INTERVALS.md` recommendation.

---

# Module 6 — Backtesting and Forecast Evaluation

## Module Overview

**Purpose.** Every number reported so far — MAE, MAPE, coverage — was measured on a single held-out window. That is a *sample of one* and it can flatter or slander a model by luck of which weeks landed in the test set. This module delivers the discipline that turns a forecasting demo into a trustworthy claim: **time-aware backtesting**. Participants learn rolling-origin and expanding-window evaluation, the family of accuracy metrics and *when each lies*, the scaled and probabilistic metrics that survive real data, and a statistical test — **Diebold-Mariano** — for whether one model is genuinely better than another or merely luckier. This is where the course's thesis, *respect the arrow of time*, becomes a measurement protocol.

**Business relevance.** A model chosen on a single fortunate split will disappoint in production and erode trust in the whole forecasting function. Grid operators, ministries, and retailers commission a **backtest report** precisely because a single accuracy number is not decision-grade evidence. Backtesting answers the questions a decision-maker actually asks: *how does this model do across many origins, including the hard weeks? is it reliably better than the cheap baseline? is the improvement worth the added complexity?* The `Tayyar` deliverable — the artefact this whole course builds toward — is a rolling-origin backtest report a grid operator would accept.

**Industry use cases.**
- A grid operator backtests every candidate day-ahead model over 90 rolling origins, reporting MASE against a seasonal-naive baseline and the fraction of origins where the champion beats it.
- A retailer runs expanding-window backtests across a year to confirm a new demand model beats the incumbent on the promotional weeks that actually cost money, not just on average.
- A forecasting platform gates model promotion on a Diebold-Mariano test: a new model ships only if its accuracy gain over the incumbent is statistically significant, not noise.

**Expected competencies.** After this module a participant can design a rolling-origin or expanding-window backtest that never leaks the future, choose scale-appropriate metrics (and explain why MAPE fails near zero and MASE does not), evaluate probabilistic forecasts with pinball loss and coverage, run a Diebold-Mariano test to compare two models, and assemble a defensible model-comparison table with `sktime`.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Design rolling-origin and expanding-window backtests without temporal leakage | LO4 |
| 6.2 | Select scale-appropriate point metrics and explain each one's failure mode | LO5 |
| 6.3 | Evaluate probabilistic forecasts with pinball loss and empirical coverage | LO5 |
| 6.4 | Compare models statistically with the Diebold-Mariano test | LO5, LO6 |
| 6.5 | Assemble a reproducible backtest report driving a model-selection decision | LO4, LO6 |

## Technical Content

### 1. Why a single split is not evidence

A single train/test split estimates a model's skill from one realisation of the future. If the test weeks happened to be calm, every model looks good; if they held a heatwave and an Eid, the ranking can flip. **Backtesting** repeats the evaluation over many *origins* — many points in time from which the model forecasts forward — and aggregates the errors. The result is a distribution of skill, not a point estimate, and distributions are what let you say "model A beats model B *reliably*" rather than "on the one week I tried." The non-negotiable throughout: at every origin the model may use only data available *at that origin*. This is Module 4's leakage ethic, elevated to the evaluation loop itself.

### 2. Backtesting schemes: rolling vs expanding origin

Two canonical schemes, both moving an evaluation origin forward through time:

- **Expanding window (anchored):** the training set grows — always starts at the beginning, ends at the current origin. Uses all history; mimics a system that never forgets. Preferred when more data always helps and the process is stable.
- **Rolling window (sliding):** the training set is a fixed-length window that slides forward, dropping the oldest data. Mimics a system that adapts to recent regime and forgets stale history. Preferred when the process drifts (a new industrial load, a tariff change).

Both are parameterised by the **forecast horizon** (`h`, e.g. 24 hours) and the **step** between origins (how far the origin jumps each fold). A crucial refinement is the **gap**: if the target uses features built from the recent past, leave a gap between train and test so no feature straddles the boundary. `sktime`'s `ExpandingWindowSplitter` / `SlidingWindowSplitter` and `evaluate` implement this correctly; hand-rolled loops are where leaks creep back in.

### 3. Point-accuracy metrics and their failure modes

No single metric is right for every series — teach each one's blind spot:

| Metric | Formula (sketch) | Strength | Fails when |
|---|---|---|---|
| **MAE** | mean \|y − ŷ\| | same units, robust | not comparable across series of different scale |
| **RMSE** | √mean (y − ŷ)² | penalises large misses | dominated by outliers; scale-bound |
| **MAPE** | mean \|y − ŷ\|/\|y\| | scale-free %, intuitive | explodes near zero; asymmetric (over-forecasts capped at 100%) |
| **sMAPE** | symmetric % | bounded | still unstable near zero; awkward interpretation |
| **MASE** | MAE / MAE of seasonal-naive | scale-free, symmetric, defined at zero | needs a sensible baseline period `m` |

**MASE** is the workhorse for cross-series comparison: it divides your model's MAE by the MAE of the **seasonal-naive** forecast (predict the value from one season ago). MASE < 1 means you beat the naive baseline; MASE = 1 means you tied it; MASE > 1 means the naive forecast — free — was better. Always report MASE alongside a % metric so "1.9% MAPE" is anchored to "and that is 0.6× the naive baseline."

### 4. Evaluating probabilistic forecasts

Point metrics ignore the intervals from Module 5. Evaluate the *distribution* with:
- **Pinball / quantile loss** aggregated across quantiles — a **proper scoring rule** (minimised by the true distribution), so it rewards honest calibration, not just a good median.
- **Empirical coverage** vs nominal — does the 90% interval contain the truth 90% of the time, across all origins?
- **Interval width / sharpness** — among calibrated models, narrower wins.
- **CRPS** (continuous ranked probability score) when a full predictive distribution is available — the integral of pinball over all quantiles, the gold-standard single number for probabilistic skill.

Report point and probabilistic metrics together; a model can have the best MAE and the worst coverage.

### 5. Comparing models: is the difference real?

Two models' backtest MAEs differ — but is the gap signal or noise? The **Diebold-Mariano (DM) test** compares the *loss differential* series (per-origin loss of A minus loss of B) and tests the null that its mean is zero. A significant result (small p-value) says one model is genuinely more accurate on this series and horizon; a non-significant result says *pick the simpler/cheaper one*, because you cannot distinguish them. Cautions: DM compares *two* models (use corrections or a Model Confidence Set for many), assumes the loss-differential is covariance-stationary, and needs enough origins to have power. Teach the decision rule: **statistical significance gates model promotion**, so a 0.1% MAE "win" that fails DM does not justify shipping added complexity.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Always beat a named baseline.* Report seasonal-naive first; a model that cannot beat it is not a model.
- *The backtest is the product.* Its reproducibility (fixed splits, seeds, pinned versions) is what makes the report evidence rather than an anecdote.
- *Refit inside the loop.* For an honest estimate of production behaviour, refit (or at least re-select) at each origin the same way you would in production — a fitted-once model flatters itself.

**Common mistakes (each appears in the Lab 6 starter deliberately)**
1. Random k-fold cross-validation on a time series — the cardinal leak, again.
2. Fitting the model once on all data then "backtesting" by predicting past points it already saw.
3. Reporting MAPE on a series with near-zero values (spikes to thousands of percent).
4. Comparing models on different test windows and declaring a winner.
5. No baseline, so a mediocre model looks impressive in isolation.
6. Declaring a winner on a fraction-of-a-percent MAE gap without a significance test.

**Production considerations.** Automate the backtest as a scheduled job; a rising rolling MASE is an early drift alarm. Version the backtest config with the model so a reported number is always reproducible. Store per-origin errors, not just the aggregate, so you can diagnose *which* conditions (heatwaves, Eids) a model handles poorly and target the next improvement there.

### 7. Real-world example walkthrough

Narrate this (5 minutes): a team replaced their seasonal-naive baseline with a shiny gradient-boosting model reporting 1.6% MAPE on a held-out fortnight and celebrated a "0.3-point win." A rolling-origin backtest over 90 origins told a different story: the ML model's MASE was 0.98 — it barely beat the free seasonal-naive forecast — and a Diebold-Mariano test returned p = 0.41, so the "win" was noise. Worse, the per-origin breakdown showed the ML model *lost* on every Eid week, where the naive forecast's copy-last-season behaviour accidentally handled the holiday. The team kept the naive baseline for holidays and used the ML model only where the backtest proved it won. No new model was built — the backtest changed the decision. This module is that protocol.

## Code Examples

### Rolling-origin backtest with sktime

```python
# src/tayyar/eval/backtest.py
"""Rolling-origin backtest that CANNOT leak: sktime moves the origin forward
and only ever trains on data before each origin. Refit at every origin."""
import numpy as np, pandas as pd
from sktime.forecasting.model_evaluation import evaluate
from sktime.forecasting.model_selection import (
    ExpandingWindowSplitter, SlidingWindowSplitter)
from sktime.performance_metrics.forecasting import (
    MeanAbsoluteError, MeanAbsolutePercentageError,
    MeanAbsoluteScaledError)

def rolling_backtest(y: pd.Series, forecaster, fh=range(1, 25),
                     initial_window=24*365, step=24*7, sliding=False):
    """fh = 24h horizon; step = advance the origin one week each fold."""
    Splitter = SlidingWindowSplitter if sliding else ExpandingWindowSplitter
    cv = Splitter(fh=list(fh),
                  initial_window=initial_window,
                  step_length=step,
                  window_length=initial_window if sliding else None)
    metrics = [MeanAbsoluteError(),
               MeanAbsolutePercentageError(symmetric=False),
               MeanAbsoluteScaledError(sp=24)]     # MASE vs seasonal-naive(24)
    results = evaluate(forecaster=forecaster, y=y, cv=cv,
                       scoring=metrics, strategy="refit", return_data=True)
    return results   # one row per origin: per-fold errors + fitted preds
```

### Metrics that survive real data (MASE + seasonal-naive baseline)

```python
# src/tayyar/eval/metrics.py
import numpy as np, pandas as pd

def seasonal_naive(y_train: pd.Series, h: int, m: int = 24) -> np.ndarray:
    """Baseline: forecast = value m steps ago. The number MASE divides by."""
    last_season = y_train.iloc[-m:].to_numpy()
    return np.resize(last_season, h)

def mase(y_true, y_pred, y_train, m: int = 24) -> float:
    """MAE(model) / MAE(seasonal-naive on the training set). <1 beats naive."""
    num = np.mean(np.abs(np.asarray(y_true) - np.asarray(y_pred)))
    diffs = np.abs(y_train[m:].to_numpy() - y_train[:-m].to_numpy())
    denom = np.mean(diffs)
    return float(num / denom) if denom > 0 else np.inf

def mape_safe(y_true, y_pred, floor: float = 1.0) -> float:
    """MAPE with a floor so near-zero targets don't explode the metric."""
    y_true = np.maximum(np.abs(np.asarray(y_true)), floor)
    return float(np.mean(np.abs((y_true - np.asarray(y_pred)) / y_true)))
```

### Diebold-Mariano: is model A really better than B?

```python
# src/tayyar/eval/diebold_mariano.py
"""Test whether two models' accuracy difference is statistically significant.
Null: equal expected loss. Small p-value -> a genuine winner."""
import numpy as np
from scipy import stats

def diebold_mariano(y_true, pred_a, pred_b, h: int = 1, power: int = 2):
    y_true, pred_a, pred_b = map(np.asarray, (y_true, pred_a, pred_b))
    e_a = np.abs(y_true - pred_a) ** power
    e_b = np.abs(y_true - pred_b) ** power
    d = e_a - e_b                      # loss differential
    n = len(d)
    d_bar = d.mean()
    # Newey-West style long-run variance for h-step-ahead autocorrelation
    gamma0 = np.var(d, ddof=0)
    gamma = [np.cov(d[k:], d[:-k])[0, 1] for k in range(1, h)]
    var_d = (gamma0 + 2 * sum(gamma)) / n
    dm_stat = d_bar / np.sqrt(var_d) if var_d > 0 else 0.0
    p_value = 2 * (1 - stats.norm.cdf(abs(dm_stat)))
    winner = "A" if d_bar < 0 else "B"
    return {"dm_stat": round(dm_stat, 3), "p_value": round(p_value, 4),
            "winner": winner if p_value < 0.05 else "tie (not significant)"}
```

## Hands-on Lab 6 — The Rolling-Origin Backtest Report

| | |
|---|---|
| **Objective** | Backtest all four `Tayyar` model families over many rolling origins, build the model-comparison table (MAE/MAPE/MASE + coverage/pinball), and decide the champion with a Diebold-Mariano test — producing the course's headline deliverable |
| **Duration** | 50 minutes |
| **Setup** | Lab 5 solution (`git checkout lab6-start`), `pip install sktime` |

**Instructions & tasks**

1. *(5 min)* The starter "backtests" by fitting once on all data then scoring past points — find the leak (the model already saw those points) and note it in `BACKTEST.md`.
2. *(12 min)* Configure an `ExpandingWindowSplitter` (initial_window = 1 year, step = 1 week, fh = 24h). Run `rolling_backtest` for the seasonal-naive baseline, SARIMAX, ETS, and the LightGBM forecaster. Confirm ≥ 50 origins.
3. *(10 min)* Aggregate per-origin errors into a table: mean and spread of MAE, MAPE (floored), and MASE for each model. Every model must be reported *relative to seasonal-naive* (MASE).
4. *(8 min)* Add probabilistic scoring for the two interval models: mean pinball and empirical coverage across origins.
5. *(10 min)* Run `diebold_mariano` on the top two point models. Record whether the gap is significant. Decide the champion and state the rule you applied.
6. *(5 min)* Write `BACKTEST.md`: the comparison table, the DM verdict, the champion + one-line justification, and note any conditions (Eid/heatwave) where the champion loses. Commit: `feat(eval): rolling-origin backtest report + DM model selection`.

**Expected output**
```
$ python -m tayyar.eval.run_backtest
Backtest: expanding window, 78 origins, fh=24h, refit each origin
Model            MASE   MAE(MW)  MAPE   coverage  pinball
seasonal-naive   1.00    980     3.1%     -         -
ETS(A,Ad,M)      0.79    770     2.4%    0.87      201
SARIMAX+temp     0.64    628     1.9%    0.90      181
LightGBM+CQR     0.54    528     1.6%    0.91      168   <- champion
Diebold-Mariano (LightGBM vs SARIMAX): dm=-3.41 p=0.0006 -> winner A (LightGBM), significant
Champion: LightGBM+CQR (lowest MASE, DM-significant over SARIMAX; loses only on 2 Eid origins)
Wrote backtest_table.csv, error_by_origin.png, BACKTEST.md
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Every model has MASE ≈ 0 | Scored on points the model trained on | Use `strategy="refit"`; never score in-sample |
| MAPE = 4000% on one origin | Near-zero demand in that window | Use floored/safe MAPE; prefer MASE |
| Only 3 origins produced | `step_length` too large / `initial_window` too big | Shrink step to one week; check series length |
| DM p-value unstable | Too few origins / h not accounted | Increase origins; pass the true horizon `h` |
| Backtest runs for many minutes | Refitting SARIMAX at every origin | Expected; cache the naive/ETS, parallelise folds |

**Instructor notes.** Task 1 (the fit-once leak) and task 5 (DM) are the two anchors — do not let a pair declare a champion on a raw MAE gap without running DM. When a strong ML model turns out to *lose* on Eid origins, dwell on it: this is why per-origin breakdowns beat a single aggregate. Fast finishers: swap to a sliding window and observe whether forgetting old data helps or hurts.

## Mini Exercises

**Quiz (5 questions)**
1. Why is a single train/test split not decision-grade evidence? → it's a sample of one; the ranking can flip on the luck of the test weeks.
2. Expanding vs sliding window — which forgets old data? → **sliding** (fixed-length window).
3. What does MASE < 1 mean? → the model **beats** the seasonal-naive baseline.
4. Why does MAPE fail near zero? → the denominator → 0, so the percentage explodes; use MASE.
5. What does a non-significant Diebold-Mariano test tell you to do? → pick the **simpler/cheaper** model; the accuracy gap is noise.

**Debugging exercise.** Branch `sim-fit-once` fits on all data then "backtests" past points; participants explain why MASE ≈ 0 is a leak and switch to `strategy="refit"`.

**Metric-choice drill.** Given four series (steady load, intermittent spare-parts demand with zeros, fast-growing new region, promotional retail), each pair picks the right primary metric and justifies why the others mislead.

## Case Study — Choosing the Champion Day-Ahead Model

**Scenario.** `Tayyar` has four candidate day-ahead models (seasonal-naive, ETS, SARIMAX+temp, LightGBM+CQR). Management wants *one* promoted to production and a report that survives audit — not a slide claiming "our model gets 1.6%."

**Business context.** The chosen model runs every afternoon for a year; a wrong choice made on a lucky split costs money and credibility daily. The report is the governance artefact: it must show the model beats the free baseline, reliably, including on the hard calendar weeks.

**Technical challenge.** Design a leakage-free rolling-origin backtest, pick metrics that are fair across the seasonal calendar, and prove the champion's lead over the runner-up is statistically real — while surfacing the conditions where it is not.

**Constraints.** Refitting SARIMAX at every origin is slow (compute budget); near-zero demand never occurs here but the metric choice must generalise to sister series that do have zeros; the report must be reproducible by an auditor from the committed config.

**Solution approach (facilitate).** (1) Expanding-window backtest, weekly step, 24h horizon, refit each origin; (2) MASE as the headline metric with MAPE and coverage alongside; (3) per-origin error breakdown to expose Eid/heatwave weaknesses; (4) Diebold-Mariano on the top two; (5) recommend the champion *with* the caveat conditions and a fallback (seasonal-naive on Eid weeks) where the backtest justifies it.

**Discussion questions.**
1. Why report MASE rather than only MAPE to a mixed audience of engineers and planners?
2. When would you promote the *simpler* model despite a lower-MASE rival?
3. How does the per-origin breakdown change the decision versus the aggregate?
4. What in the committed backtest config makes the report reproducible a year later?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Backtest validity | Rigor | 0 in-sample scores; refit each origin | `strategy="refit"`; audit split boundaries |
| Origins evaluated | Coverage | ≥ 50 rolling origins | fold count |
| Champion MASE | Accuracy | < 0.7 (beats naive by ≥ 30%) | mean MASE across origins |
| Significance of win | Rigor | DM p < 0.05 over runner-up | `diebold_mariano` |
| Report reproducibility | Rigor | Identical table on re-run | fixed splits + pinned versions committed |

**Example benchmark table (filled during lab):**

| Model | MASE | MAE (MW) | MAPE | Coverage (90%) | Pinball | DM vs runner-up |
|---|---|---|---|---|---|---|
| seasonal-naive | 1.00 | 980 | 3.1% | — | — | baseline |
| ETS(A,Ad,M) | 0.79 | 770 | 2.4% | 0.87 | 201 | — |
| SARIMAX + temp | 0.64 | 628 | 1.9% | 0.90 | 181 | runner-up |
| LightGBM + CQR | 0.54 | 528 | 1.6% | 0.91 | 168 | p=0.0006 (wins) |

## Required Visuals and Training Assets

### Diagrams
1. **Rolling vs expanding origin** — *Purpose:* the module's core mechanic. *Elements:* two stacked timelines, origin marching forward, train/test blocks (growing vs sliding) with a gap band. *Style:* animated-still timeline poster.
2. **Metric decision tree** — *Purpose:* pick the right metric. *Elements:* questions (zeros in the series? compare across scales? probabilistic?) routing to MAE/MASE/pinball/CRPS. *Style:* A4 decision tree.
3. **Diebold-Mariano intuition** — *Purpose:* signal vs noise. *Elements:* a loss-differential series with its mean and a significance band, "is the mean far enough from zero?" *Style:* single annotated plot.

### Images (screenshots)
1. **Backtest comparison table** — *why:* the course deliverable; *content:* four models × MASE/MAPE/coverage/pinball.
2. **Error-by-origin plot** — *why:* exposes the Eid/heatwave weakness; *content:* per-origin MAE with holiday origins flagged.
3. **DM console output** — *why:* significance gating; *content:* dm-stat, p-value, verdict.

### Simulations
1. **Fit-once leak** — *Setup:* branch `sim-fit-once`. *Expected behaviour:* absurdly low MASE from in-sample scoring. *Learning objective:* refit each origin; never score in-sample.
2. **Lucky-split flip** — *Setup:* `sim-lucky-split` picks two different single test windows. *Expected behaviour:* the model ranking flips between them. *Learning objective:* one split is not evidence; backtest.

### Interactive Activities
- **Baseline first (10 min):** before any model, each pair computes the seasonal-naive error by hand for one day — the number everything else must beat.
- **Significance debate (15 min):** given two models' per-origin errors, class predicts the DM verdict, then runs it.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | (as Module 1) | CSV | ~26,300 rows | The backtested series |
| `ksa_calendar.csv` | (as Module 1) | CSV | ~1,100 rows | Flags Eid/Ramadan origins in the breakdown |
| `backtest_reference.csv` | Reference solution comparison table | CSV | 4 rows | Expected Lab 6 output |

### Demo Requirements
- **Instructor demo:** run a rolling-origin backtest of three models, build the table, run DM — under 10 minutes; read the champion decision aloud with its caveat.
- **Student demo:** one pair presents their backtest table and defends the champion with the DM verdict.
- **Expected outputs:** reproducible backtest table, per-origin breakdown, DM verdict, `BACKTEST.md`.

---

# Module 7 — Forecasting Case Study

## Module Overview

**Purpose.** The first six modules built techniques in isolation, each in its own lab. This module is where they become a **decision**. Participants take the full `Tayyar` toolkit — decomposition, stationarity diagnostics, classical baselines, ML forecasters, calibrated intervals, and the rolling-origin backtest — and drive a single end-to-end model-selection under real constraints: a publication deadline, a compute budget, an explainability requirement, and cost-asymmetric errors. The output is not a model but a *recommendation with evidence*: which model family to run in production for day-ahead load, why, where it is weak, and what to monitor. This is the deliverable a grid operator, a demand planner, or a workforce planner actually commissions, and it is the direct on-ramp to the capstone.

**Business relevance.** In practice, the hard part of forecasting is rarely fitting a model — it is choosing *which* model to trust for *which* decision, and defending that choice to people who will act on it. Every constraint pulls a different way: accuracy wants the LightGBM; explainability wants the SARIMAX; the deadline and compute budget want the ETS; the seasonal calendar wants a naive fallback on Eid. The value a data scientist adds is navigating those trade-offs with evidence rather than preference. This module rehearses exactly that judgement on the golden-thread service.

**Industry use cases.**
- A grid operator selects a production day-ahead model per operating area, running the interpretable SARIMAX where regulators demand transparency and the LightGBM where accuracy pays, each justified by a backtest.
- A retailer chooses a global ML model for the long tail of SKUs and a per-series classical model for the top 50 revenue drivers, on cost-of-error grounds.
- A workforce-planning unit forecasts Saudisation headcount trajectories, choosing a damped-trend ETS for interpretability to policy stakeholders over a marginally sharper black box.

**Expected competencies.** After this module a participant can integrate the full pipeline into one reproducible workflow, weigh accuracy against explainability, latency, compute, and maintenance under stated constraints, defend a model-family recommendation from backtest evidence, and communicate the decision — including its limits — to a non-technical decision-maker.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Integrate decomposition, models, intervals, and backtesting into one reproducible pipeline | LO1–LO5 |
| 7.2 | Select a model family under multi-dimensional real-world constraints | LO6 |
| 7.3 | Weigh accuracy against explainability, latency, compute, and maintenance cost | LO6 |
| 7.4 | Defend a recommendation from backtest and significance evidence | LO5, LO6 |
| 7.5 | Communicate a forecast and its uncertainty to non-technical decision-makers | LO5, LO6 |

## Technical Content

### 1. From techniques to a decision

A model-selection decision is a function of the *use case*, not of a leaderboard. The same series can warrant different models for different decisions: the daily-mean forecast for energy planning, the daily-max for reserve margins, the hourly probabilistic forecast for dispatch. This module frames selection as: (a) state the decision and its cost function; (b) enumerate candidate model families; (c) evaluate them on a backtest aligned to the decision; (d) weigh non-accuracy constraints; (e) recommend, with the conditions under which the recommendation flips. The technique modules were means; this is the end.

### 2. The model-family trade-off space

Lay the four families on a common set of axes so the trade-off is explicit:

| Family | Accuracy | Explainability | Interval quality | Compute/latency | Maintenance | Best when |
|---|---|---|---|---|---|---|
| Seasonal-naive | low | total | none (add conformal) | trivial | none | baseline / stable calendar-driven series |
| ETS | medium | high | analytic, decent | very fast | low (auto) | many series, no covariates, interpretability |
| SARIMAX | medium-high | high (component story) | analytic, native | moderate (slow at large m) | medium | covariates + explainability required |
| LightGBM (+CQR) | high | medium (importance) | calibrated, sharp | fast train, needs feature store | higher (pipeline) | rich covariates, scale, nonlinear interactions |

The lesson: there is no dominant row. Every cell that matters is a negotiation with a constraint.

### 3. Constraint-driven selection

Real constraints, each mapping to an axis:
- **Deadline / latency:** the afternoon publication window caps fit+forecast time — rules out refitting a large-`m` SARIMA per origin at serve time.
- **Explainability:** control-room and regulatory acceptance can *require* a component story, promoting SARIMAX/ETS even at an accuracy cost.
- **Cost asymmetry:** under-forecasting load is far costlier than over-forecasting — selection should optimise a quantile / asymmetric loss, not symmetric MAE.
- **Maintenance:** a feature pipeline is a standing liability; if the accuracy gain is thin, the simpler model wins on total cost of ownership.
- **Data availability at serve time:** covariate models need *future* covariates (temperature forecast) — no forecast, no SARIMAX-with-temp.

Teach a written **decision record**: constraints listed, candidates scored, weights stated, recommendation and its flip-conditions. This is what makes a choice defensible rather than a preference.

### 4. Integrating the pipeline

The end-to-end `Tayyar` pipeline chains the module artefacts into one reproducible run: load+index (M1) → transform+stationarity (M1–M2) → feature build (M4) → fit candidate models (M3–M5) → rolling-origin backtest (M6) → select + report. The engineering disciplines that make it trustworthy: a single versioned feature module shared by train and serve (no training/serving skew), pinned dependencies, fixed splits and seeds, and every stage idempotent and re-runnable from the committed config. The pipeline *is* the reproducibility guarantee behind the recommendation.

### 5. Communicating forecasts to decision-makers

A forecast unheeded is worthless. Translation skills:
- Lead with the decision, not the model: "reserve to 52,400 MW covers all but ~5% of afternoons," not "the p95 is 52,400."
- Show the interval as risk, not as hedging — the width *is* the honest uncertainty, and narrowing it dishonestly costs load-shedding.
- Name the model's known weaknesses (Eid weeks) and the fallback, so trust survives the first miss.
- Use one plain sentence per component for interpretable models; use feature importance as a *story*, not a causal claim, for the ML model.

### 6. Design principles, best practices, common mistakes

**Principles to teach explicitly**
- *Select for the decision, not the leaderboard.* The metric must match the cost function the decision faces.
- *The simplest model that meets the constraints wins.* Complexity is justified only by a DM-significant, decision-relevant gain.
- *A recommendation includes its own limits.* State where the model loses and what you monitor — that candour is what earns adoption.

**Common mistakes**
1. Picking the lowest-MAE model regardless of deadline, explainability, or cost asymmetry.
2. Optimising symmetric error when the decision's costs are asymmetric.
3. Shipping an accurate model with no fallback for the calendar weeks it demonstrably fails.
4. Presenting a point forecast to a decision that is inherently a quantile decision.
5. A pipeline that runs only on the author's laptop — irreproducible evidence is no evidence.
6. Communicating in model jargon ("MASE 0.54") instead of decision terms ("beats the free forecast by 46%").

**Production considerations.** The selected model needs a monitoring contract: rolling MASE and coverage tracked per week, drift alarms, a documented retrain cadence, and a champion/challenger setup so the next candidate is always being backtested against the incumbent. The decision record is a living document, revisited when a monitored metric breaches threshold.

### 7. Real-world example walkthrough

Narrate this (5 minutes): a planning unit ran a bake-off and the LightGBM won on MASE, so it was promoted — full stop. Two months later a control-room engineer refused to act on a forecast he could not interrogate during an unusual load event, and the team fell back to spreadsheets on exactly the night that mattered. The failure was not the model; it was the *selection*, which had weighted accuracy at 100% and explainability at 0%. The redo kept the LightGBM as the default but ran the interpretable SARIMAX in parallel as the "explain the number" model, with a documented rule for when the operator consults which. Adoption followed. The lesson this module teaches: selection is a multi-constraint decision, and the winning model is the one people will actually use.

## Code Examples

### The end-to-end selection pipeline

```python
# src/tayyar/pipeline/select.py
"""End-to-end: build features, backtest every candidate, score against the
decision's constraints, emit a defensible recommendation. Reproducible from
a single committed config."""
from dataclasses import dataclass
import pandas as pd
from tayyar.data.load import load_demand, impute_short_gaps
from tayyar.features.build import add_lags, add_rolling, add_calendar, add_fourier
from tayyar.eval.backtest import rolling_backtest

@dataclass
class Constraints:
    max_fit_seconds: float          # publication-deadline budget
    require_explainable: bool       # control-room / regulator
    cost_asymmetry: float           # under:over error cost ratio (e.g. 3.0)

def run_selection(cfg) -> pd.DataFrame:
    df = impute_short_gaps(load_demand(cfg.data_path))
    feats = add_fourier(add_calendar(add_rolling(add_lags(df)), cfg.calendar))
    rows = []
    for name, forecaster in cfg.candidates.items():
        res = rolling_backtest(feats["demand_mw"], forecaster,
                               initial_window=cfg.initial_window, step=cfg.step)
        rows.append({"model": name,
                     "mase": res["test_MeanAbsoluteScaledError"].mean(),
                     "fit_s": res["fit_time"].mean()})
    return pd.DataFrame(rows).sort_values("mase")
```

### Constraint-weighted scoring and recommendation

```python
# src/tayyar/pipeline/recommend.py
"""Turn a backtest table + constraints into a scored recommendation.
Selection is NOT argmin(MASE); it is a weighted, constraint-filtered decision."""
import pandas as pd

def recommend(table: pd.DataFrame, c, weights: dict) -> dict:
    df = table.copy()
    # Hard filters: a model that breaks a constraint is disqualified.
    df = df[df["fit_s"] <= c.max_fit_seconds]
    if c.require_explainable:
        df = df[df["explainable"]]
    if df.empty:
        raise ValueError("No candidate satisfies the hard constraints")
    # Soft score: normalise each axis to [0,1], higher is better, then weight.
    for col, better in [("mase", "low"), ("fit_s", "low"),
                        ("coverage_gap", "low"), ("explain_score", "high")]:
        v = df[col]
        norm = (v.max() - v) / (v.max() - v.min() + 1e-9) if better == "low" \
               else (v - v.min()) / (v.max() - v.min() + 1e-9)
        df[f"s_{col}"] = norm
    df["score"] = sum(weights[k] * df[f"s_{k}"] for k in weights)
    best = df.sort_values("score", ascending=False).iloc[0]
    return {"champion": best["model"], "score": round(float(best["score"]), 3),
            "runner_up": df.sort_values("score", ascending=False).iloc[1]["model"]}
```

### A decision-maker-facing forecast summary

```python
# src/tayyar/pipeline/brief.py
"""Translate a probabilistic forecast into decision language, not model jargon."""
import pandas as pd

def reserve_brief(interval: pd.DataFrame, target_q: str = "q95") -> str:
    peak_p95 = interval[target_q].max()
    peak_p50 = interval["q50"].max()
    hour = interval[target_q].idxmax()
    return (f"Set spinning reserve to {peak_p95:,.0f} MW "
            f"(expected peak {peak_p50:,.0f} MW at {hour:%H:%M}). "
            f"This covers all but ~5% of afternoons; the gap of "
            f"{peak_p95 - peak_p50:,.0f} MW is the honest uncertainty, "
            f"widest on hot days. Known weak spot: Eid weeks — fall back to "
            f"the seasonal-naive forecast, which handles the holiday shift.")
```

## Hands-on Lab 7 — End-to-End Selection and the Decision Record

| | |
|---|---|
| **Objective** | Integrate the full `Tayyar` pipeline, run the constraint-weighted selection across all model families, and produce a one-page decision record recommending a production model with evidence and limits |
| **Duration** | 50 minutes (Day 3 H4, folds into capstone assembly) |
| **Setup** | Lab 6 solution (`git checkout lab7-start`); no new installs |

**Instructions & tasks**

1. *(8 min)* Wire `run_selection` end-to-end from the committed config; confirm it reproduces your Lab 6 backtest table from a clean run (same numbers = reproducible).
2. *(10 min)* Define three `Constraints` scenarios: (A) deadline-tight + explainability-required (regulator), (B) accuracy-first (internal dispatch), (C) many-areas maintenance-sensitive. Run `recommend` for each with stated weights.
3. *(10 min)* Observe that the champion *changes* across scenarios (SARIMAX for A, LightGBM for B, ETS/global for C). Record which constraint flipped each decision.
4. *(8 min)* For the accuracy-first champion, generate a `reserve_brief` and critique it as a control-room engineer would — is it decision-language, does it name its weakness?
5. *(9 min)* Write `DECISION_RECORD.md`: the decision, candidates, constraint weights, recommendation per scenario, flip-conditions, and monitoring plan.
6. *(5 min)* Commit: `feat(pipeline): end-to-end selection + decision record`.

**Expected output**
```
$ python -m tayyar.pipeline.run_select
Reproduced backtest table from clean config: MATCH
Scenario A (deadline+explainable): champion=SARIMAX+temp  (LightGBM disqualified: needs feature store at serve)
Scenario B (accuracy-first)      : champion=LightGBM+CQR   (MASE 0.54, DM-significant)
Scenario C (many-areas, low-maint): champion=global-LightGBM / ETS  (maintenance weight decisive)
Brief (Scenario B): "Set spinning reserve to 52,400 MW (expected peak 49,900 MW at 15:00)..."
Wrote decision_record.md, selection_scores.csv
```

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Same champion in all scenarios | Weights identical / hard filters not applied | Differentiate weights; enforce the constraint filters |
| Pipeline numbers differ from Lab 6 | Non-fixed splits or unpinned versions | Commit splits/seeds; pin the environment |
| `recommend` raises "no candidate" | Constraints too strict | Relax one hard filter or add a compliant candidate |
| Brief reads as jargon | Reported quantiles not decisions | Rewrite in reserve-margin terms with the weakness named |

**Instructor notes.** The payoff is task 3: the champion *changing* with the constraints proves selection is a decision, not a leaderboard lookup. Push back on any pair that reports one universal "best model." Fast finishers: add a fourth scenario with an explicit asymmetric loss and show the optimal serving quantile shifts.

## Mini Exercises

**Quiz (5 questions)**
1. Is "lowest MASE" always the right selection? → **No** — deadline, explainability, cost asymmetry, and maintenance can override.
2. Which family fits "covariates + regulator demands explainability"? → **SARIMAX** (component story + native intervals).
3. What must a recommendation include besides the champion? → its **limits/flip-conditions** and a monitoring plan.
4. Why present a quantile, not a point, for reserve sizing? → the decision is inherently a **risk/quantile** decision.
5. What makes selection evidence reproducible? → fixed splits/seeds, pinned versions, config-driven pipeline.

**Debugging exercise.** Branch `sim-leaderboard` selects purely by MASE and ships a model that misses the deadline; participants add the constraint filter and re-recommend.

**Communication drill.** Each pair rewrites a jargon-heavy forecast summary ("p95 = 52.4k, MASE 0.54") into two decision-language sentences for a non-technical planner.

## Case Study — Selecting the Production Day-Ahead Model for Tayyar

**Scenario.** `Tayyar` is going live. Management must approve one day-ahead model for the Central Operating Area now, with a documented plan to extend to all four areas. They have the Lab 6 backtest; they need a decision they can defend to the regulator and the control room.

**Business context.** The chosen model runs daily for at least a year; the decision is high-stakes and public. The regulator wants explainability; the control room wants to interrogate the number; dispatch wants accuracy; the platform team wants low maintenance across four areas. No single model maximises all four.

**Technical challenge.** Produce a defensible, reproducible recommendation that names the champion *and* the conditions under which a different model is used — reconciling conflicting constraints with evidence rather than assertion.

**Constraints.** Afternoon deadline; regulatory explainability for the published number; asymmetric cost (under-forecast far worse); four-area maintenance budget; temperature available only as a forecast.

**Solution approach (facilitate).** (1) Reproduce the backtest from config; (2) define constraint scenarios with stated weights; (3) run constraint-weighted selection; (4) recommend a *primary* model (LightGBM+CQR for accuracy) with the interpretable SARIMAX run in parallel as the "explain the number" model and seasonal-naive as the Eid fallback; (5) write the decision record and the monitoring contract (rolling MASE + coverage, drift alarms, retrain cadence, champion/challenger).

**Discussion questions.**
1. How do you reconcile the regulator's explainability demand with dispatch's accuracy demand — one model or two?
2. What monitored metric would trigger revisiting this decision?
3. How does the asymmetric cost of load-shedding change which quantile you publish?
4. When extending to four areas, does the global-ML case (Module 4) change the recommendation?

## Benchmarks and Evaluation

| Metric | Category | Target after M7 | How measured |
|---|---|---|---|
| Pipeline reproducibility | Rigor | Clean-run numbers match Lab 6 exactly | config-driven re-run |
| Constraint sensitivity | Decision quality | Champion changes across ≥ 2 scenarios | scenario table |
| Recommendation completeness | Decision quality | Champion + limits + monitoring named | `DECISION_RECORD.md` review |
| Communication clarity | Stakeholder fit | Brief is decision-language, weakness named | peer/instructor rubric |
| Evidence sufficiency | Rigor | Backtest + DM cited for the choice | decision record |

**Example benchmark table (filled during lab):**

| Scenario | Weights (acc/explain/latency/maint) | Champion | Decisive constraint |
|---|---|---|---|
| A — regulator | 0.3 / 0.4 / 0.2 / 0.1 | SARIMAX+temp | explainability + deadline |
| B — dispatch | 0.6 / 0.1 / 0.2 / 0.1 | LightGBM+CQR | accuracy (DM-significant) |
| C — four areas | 0.3 / 0.1 / 0.2 / 0.4 | global-LightGBM / ETS | maintenance |

## Required Visuals and Training Assets

### Diagrams
1. **Model-family trade-off radar** — *Purpose:* make the trade-offs visible. *Elements:* a radar/spider chart with axes accuracy, explainability, interval quality, latency, maintenance; one polygon per family. *Style:* radar poster, English + Arabic labels.
2. **Constraint-to-decision map** — *Purpose:* selection is constraint-driven. *Elements:* constraints on the left routing through weights to a champion on the right; the same series → different champions. *Style:* Sankey-style flow.
3. **End-to-end pipeline** — *Purpose:* integration overview. *Elements:* M1 load → M2 stationarity → M4 features → M3–M5 models → M6 backtest → M7 select, one lane. *Style:* pipeline poster, capstone reference.

### Images (screenshots)
1. **Scenario selection table** — *why:* champion changes with constraints; *content:* three scenarios, three champions.
2. **Decision record** — *why:* the deliverable shape; *content:* recommendation + flip-conditions + monitoring.
3. **Reserve brief** — *why:* decision-language communication; *content:* the plain-sentence forecast summary.

### Simulations
1. **Leaderboard trap** — *Setup:* branch `sim-leaderboard` selects by MASE only. *Expected behaviour:* the chosen model misses the deadline in production. *Learning objective:* selection is multi-constraint.
2. **Asymmetric cost shift** — *Setup:* `sim-asymmetric` sets under:over cost = 4:1. *Expected behaviour:* the optimal serving quantile shifts above the median. *Learning objective:* match the metric to the cost function.

### Interactive Activities
- **Constraint auction (15 min):** each group is dealt a stakeholder (regulator, dispatch, platform) and argues its constraint weights; class negotiates a shared weighting.
- **Explain-the-number relay (10 min):** each participant delivers the reserve brief in one breath; peers flag any jargon.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `ksa_grid_demand.csv` | (as Module 1) | CSV | ~26,300 rows | End-to-end pipeline input |
| `ksa_grid_demand_4area.csv` | (as Module 4) | CSV | ~105,000 rows | Four-area extension scenario |
| `ksa_calendar.csv` | (as Module 1) | CSV | ~1,100 rows | Calendar features + Eid fallback logic |
| `temp_forecast_28d.csv` | (as Module 5) | CSV | 28×24 rows | Future exog for serving |

### Demo Requirements
- **Instructor demo:** run the selection pipeline across two constraint scenarios and show the champion flip — under 10 minutes.
- **Student demo:** one pair presents their decision record and defends the primary + fallback choice.
- **Expected outputs:** reproducible selection table, `DECISION_RECORD.md`, a decision-language reserve brief.

---

# Final Capstone Project

## Title: Tayyar — A Backtested Day-Ahead Load-Forecasting Service

## Project Scenario

You are the forecasting lead for **"Tayyar" (تيّار)**, the national load-forecasting service introduced on Day 1. The operations-planning unit of the grid operator has asked for a production-ready day-ahead forecasting pipeline for the Central Operating Area, plus a **backtest report** it can put in front of the regulator and the control room. Everything you built in Labs 1–7 is a component; the capstone is the integration plus your own extension. The service must forecast the next 24 hours of hourly demand, deliver a calibrated interval for reserve sizing, and — crucially — prove its own accuracy through a rolling-origin backtest that respects the arrow of time. The repository *is* the evidence: a stranger should clone it, run one command, and reproduce every number in your report.

## Requirements

**Mandatory (maps to grading rubric):**

1. **Clean, reproducible pipeline (LO1):** a `src/tayyar` package that runs end-to-end from a committed config: load → clean/index → decompose → feature-build → fit candidates → backtest → select → report. Fixed splits and seeds; pinned dependencies; a single `make run` (or `python -m tayyar.pipeline.run`) reproduces every reported number.
2. **Decomposition & diagnostics (LO1):** correct tz-aware hourly `DatetimeIndex` with explicit frequency and gap policy; MSTL decomposition with reported daily/weekly seasonal strengths; a stationarity report (ADF+KPSS reconciled) with the chosen `(d, D)` justified.
3. **At least three model families (LO2, LO3):** a seasonal-naive baseline, one classical model (SARIMAX with temperature/calendar **or** ETS), and one feature-based ML model (LightGBM). Every model must be leakage-safe and reproducible.
4. **Calibrated probabilistic forecast (LO5):** a 90% day-ahead prediction interval with **empirical coverage in 0.88–0.92** on the held-out test window, produced by quantile regression + conformal calibration (CQR) or an equivalently justified method; coverage reported marginally *and* by hour-of-day.
5. **Rolling-origin backtest (LO4):** ≥ 50 origins, expanding or sliding window, refit each origin, 24h horizon, no temporal leakage. Report MASE (vs seasonal-naive), a % metric, coverage, and pinball per model; include a per-origin breakdown flagging Eid/heatwave weeks.
6. **Model-selection decision (LO6):** a `DECISION_RECORD.md` recommending one production model with evidence — a Diebold-Mariano test over the runner-up, stated constraints and weights, flip-conditions, a fallback for the weeks the champion loses, and a monitoring contract (metrics + thresholds + retrain cadence).
7. **Report & communication (LO5, LO6):** a `BACKTEST_REPORT.md` an operator would accept — the comparison table, the decision, the known limits — plus a decision-language reserve brief (no unexplained jargon). `BENCHMARKS.md` filled with *your* measured numbers.

**One extension (choose at least one):**
- **Multi-area global model:** extend to all four operating areas with a global LightGBM (`area_id` categorical) and backtest per area against per-area baselines.
- **Adaptive conformal (ACI/EnbPI):** replace static CQR with an online-updating interval and show improved *conditional* (summer-afternoon) coverage.
- **Weather-uncertainty propagation:** widen the interval to reflect temperature-forecast error and show the coverage impact.
- **Automated retraining trigger:** a monitor that fires when rolling MASE or coverage breaches threshold, with a test that the trigger fires on injected drift.
- **Champion/challenger harness:** a scheduled backtest that continuously re-evaluates a challenger against the incumbent and reports promotion eligibility.

## Architecture (target state)

```
config.yaml ──► tayyar.pipeline.run
   │
   ├─ data.load ─► clean tz-aware hourly series (gaps materialised)
   ├─ analysis  ─► MSTL decomposition + ADF/KPSS stationarity report
   ├─ features  ─► lags · rolling(.shift(1)) · calendar(Fri–Sat, Ramadan/Eid) · Fourier
   ├─ models    ─► seasonal-naive · SARIMAX+temp/ETS · LightGBM · quantile+CQR
   ├─ eval      ─► ExpandingWindowSplitter → rolling backtest → MASE/MAPE/coverage/pinball
   └─ pipeline  ─► constraint-weighted select → DECISION_RECORD + BACKTEST_REPORT + reserve brief
Serving view:  origin features → champion → {p50, p90, p95} → reserve brief (with Eid fallback)
```

## Deliverables

1. Git repository URL (public or instructor-shared) with full history and checkpoint commits.
2. One-command reproducible run that regenerates every reported number from the committed config.
3. `BACKTEST_REPORT.md`: the model-comparison table, per-origin breakdown, calibrated-interval coverage, and the model-selection decision.
4. `DECISION_RECORD.md`: recommendation, constraints/weights, DM evidence, flip-conditions, fallback, monitoring contract.
5. `BENCHMARKS.md`: the module benchmark tables filled from *your* runs (decomposition strengths, stationarity verdict, per-model MASE/coverage/pinball).
6. 5-minute demo: clone-to-running, one day-ahead forecast with its interval, the backtest table, and the decision defended — including where the model loses.

## Milestones

| Milestone | Due | Gate |
|---|---|---|
| M-A: clean series + decomposition + stationarity report | End Day 1 | instructor spot-check of index/gaps/strengths |
| M-B: classical + ML models producing 24h forecasts | End Day 2 | leak check PASS; forecasts vs actuals plotted |
| M-C: calibrated 90% interval (coverage in band) | Day 3 H1 | coverage 0.88–0.92 on held-out window |
| M-D: rolling-origin backtest + DM selection | Day 3 H3 | ≥ 50 origins, no leak, champion chosen |
| M-E: decision record + extension + demo | Day 3 H5 | rubric scoring |

## Grading Rubric (100 points)

| Criterion | Weight | 90–100% band | 70–89% band | < 70% band |
|---|---|---|---|---|
| Data, index & decomposition | 12 | Correct tz-aware freq, gap policy, MSTL with justified strengths and transform | Minor gaps (implicit freq, unjustified additive/multiplicative) | Broken index, silent gaps, wrong `period` |
| Stationarity & modelling rigour | 15 | ADF+KPSS reconciled, minimal differencing, ≥ 3 families all leak-safe & diagnosed | One family thin or residuals undiagnosed | Leakage present, no baseline, or invalid AIC comparisons |
| Feature engineering (leakage-safe) | 15 | `assert_no_leakage` PASS; lags from ACF; `.shift(1)` rolling; Fri–Sat + Hijri calendar correct | One subtle leak caught late or weekend miscoded | Shuffle split / centred window survives; future exog used |
| Probabilistic calibration | 15 | Coverage 0.88–0.92 marginal **and** conditional; CQR justified; sharpest at target | Marginal coverage in band but conditional gap unaddressed | Confidence not prediction interval; coverage off target |
| Backtesting validity | 18 | ≥ 50 origins, refit each, no leak, MASE + coverage + pinball + per-origin breakdown | Fewer origins or missing probabilistic metrics | Fit-once/in-sample scoring; single split; no baseline |
| Model selection & evidence | 15 | DM-significant choice, constraints/weights stated, flip-conditions + fallback + monitoring | Choice reasonable but evidence or limits thin | Lowest-MAE pick with no significance test or limits |
| Report, brief & reproducibility | 10 | One-command reproduction; decision-language brief; auditor-ready report | Runs with fiddling; brief partly jargon | Irreproducible; jargon-only; numbers not regenerable |

**Pass ≥ 70. Distinction ≥ 90.** The chosen extension adds up to +5 bonus (capped at 100) only if mandatory scope is ≥ 80.

## Assessment Criteria Notes for Instructors

- Grade *from the repository and its reproducibility first* — clone it, run the one command, and check the numbers regenerate — then the demo. The course's thesis is that a forecast's accuracy claim must survive contact with the future; the backtest is that survival, made auditable.
- Anti-pattern flags that cap a criterion at 70%: any `train_test_split(shuffle=True)` or centred rolling feature; a "backtest" that scores in-sample; MAPE reported without MASE/baseline; a champion declared on a sub-1% gap with no Diebold-Mariano test; a confidence interval where a prediction interval is required.
- Verify one calibration claim live: ask the participant to show empirical coverage on the held-out window matches the nominal 90%, and to break it by hour-of-day.
- Reward candour: a report that names *where* the model loses (Eid weeks) and ships a fallback should score above a silent, marginally sharper submission.

## Bonus Tasks (for early finishers / distinction seekers)

1. TBATS or Prophet as a fourth family with multiple seasonalities, backtested head-to-head.
2. A Model Confidence Set (MCS) over all candidates instead of pairwise Diebold-Mariano.
3. Cost-sensitive selection: optimise an explicit asymmetric (under:over) loss and show the serving quantile shift.
4. A `sim-drift` reproduction: inject a regime change, show which monitored metric catches it first, write a 10-line postmortem.

---

# Assessment Package

## Quiz Bank (20 questions — use 10 per cohort, 15 min, closed book)

**Q1.** Why can't you shuffle a time series before splitting? → order is the signal; shuffling leaks the future into the past.
**Q2.** `asfreq("h")` does what that `parse_dates` alone does not? → declares frequency and materialises missing timestamps as NaN.
**Q3.** Additive vs multiplicative — which for a seasonal swing that grows with the level? → multiplicative (or log then additive).
**Q4.** ADF p = 0.01 and KPSS p = 0.01 — reconciled verdict? → difference-stationary (ADF says stationary, KPSS disagrees → difference).
**Q5.** For seasonal data, seasonal or regular differencing first? → seasonal, then re-test.
**Q6.** ACF tails off, PACF cuts off after lag 2 — model and order? → AR(2).
**Q7.** What is `m` in SARIMA(p,d,q)(P,D,Q)m for a daily cycle on hourly data? → 24.
**Q8.** Why must SARIMAX exogenous regressors be known at forecast time? → you need their future values; otherwise it is a leak/unavailable.
**Q9.** A Ljung-Box p-value < 0.05 on residuals means? → residual autocorrelation remains; the model is under-specified.
**Q10.** Why can a gradient-boosted tree never forecast a record-high demand? → trees interpolate; they cannot extrapolate beyond the training range.
**Q11.** What does `.shift(1)` before a rolling feature prevent? → the window including the target hour (self-leak).
**Q12.** Prediction interval or confidence interval for a future observation? → prediction interval (wider; includes noise).
**Q13.** Minimising pinball loss at τ = 0.9 recovers what? → the 90th percentile.
**Q14.** What does split-conformal guarantee and under what assumption? → marginal (1−α) coverage under exchangeability of calibration/test scores.
**Q15.** Two intervals both cover 90% — which ships? → the sharper (narrower) one.
**Q16.** Expanding vs sliding window — which forgets old data? → sliding (fixed-length window).
**Q17.** MASE < 1 means what? → the model beats the seasonal-naive baseline.
**Q18.** Why does MAPE fail near zero and MASE not? → MAPE's denominator → 0 and explodes; MASE divides by a fixed baseline MAE.
**Q19.** A non-significant Diebold-Mariano test tells you to do what? → pick the simpler/cheaper model; the gap is noise.
**Q20.** Marginal vs conditional coverage — why can a model be safe on one, dangerous on the other? → 90% on average can hide ~78% on the high-demand afternoons that matter.

## Practical Assessments

**PA-1 (30 min, Day 1):** Given a messy `ksa_grid_demand.csv` (duplicate/unsorted timestamps, silent gaps) and a broken decompose script (implicit frequency, wrong `period`), produce a clean tz-aware hourly series and a correct MSTL panel with reported strengths. Scored on: index correctness (40%), gap policy (30%), decomposition + strengths (30%).

**PA-2 (30 min, Day 2):** Given a LightGBM notebook reporting a suspiciously low 0.6% MAPE, find and fix both planted leaks (shuffle split + centred rolling window), then report the honest post-fix accuracy. Scored on: leak diagnosis notes (40%), correct fixes (40%), honest re-measurement (20%).

**PA-3 (Day 3):** Capstone (rubric above) — 40% of the course grade. Lab completion + PA-1/PA-2 + quiz — 60%.

## Evaluation Criteria Summary

| Component | Weight | Evidence |
|---|---|---|
| Lab completion (7 labs) | 30% | checkpoint commits + expected outputs |
| PA-1 + PA-2 | 20% | artefacts + diagnosis notes |
| Quiz | 10% | 10-question selection |
| Capstone | 40% | rubric, repo-first + backtest report |

Badge issuance (Forecasting badge) requires ≥ 70 overall **and** capstone ≥ 70 **and** zero academic-integrity flags (identical backtest tables or decision records across repos are checked; the backtest must reproduce from each repo's own config).

---

# Instructor Guide

## Preparation Checklist (T-minus 1 week)

- [ ] Fork/clone the course repo; push checkpoint tags (`lab1-start` … `lab7-start`) and all `sim-*` branches (`sim-gap`, `sim-agg`, `sim-spurious`, `sim-overdiff`, `sim-aic-trap`, `sim-nodamp`, `sim-centred-roll`, `sim-heatwave`, `sim-hetero`, `sim-train-coverage`, `sim-fit-once`, `sim-lucky-split`, `sim-leaderboard`, `sim-asymmetric`).
- [ ] Regenerate the synthetic `ksa_grid_demand.csv`, `ksa_grid_demand_4area.csv`, `ksa_calendar.csv`, `temp_forecast_14d.csv`, and `temp_forecast_28d.csv`; verify the reference decomposition, stationarity, and backtest solutions run clean.
- [ ] Dry-run all 7 labs end-to-end on a clean machine **and** on the Colab fallback (data pre-loaded to a mounted drive).
- [ ] Verify the two fragile installs — `pmdarima` and `Prophet` — on both Windows and macOS; pin working versions in the lock file.
- [ ] Time-box the two overrun-prone labs (Lab 4 feature engineering, Lab 6 backtesting); confirm the `git checkout labN-start` fast-forward works.
- [ ] Print A4 posters: the additive-model anchor, the leakage-smell poster, the ADF/KPSS 2×2, the ACF/PACF fingerprint card, and the model-family trade-off radar.
- [ ] Load the `correlogram_gallery.npz` and reference PNGs onto the shared drive.
- [ ] Prepare the shared leaderboard (MASE, coverage, pinball) for the Day-3 backtest bake-off.

## Software Installation Checklist (participants, T-minus 2 days email)

- [ ] Python 3.12 + git + a GitHub account.
- [ ] `conda`/`uv` environment; `pip install pandas numpy matplotlib statsmodels pmdarima sktime lightgbm scipy` (Prophet optional — provided via Colab if the local install fails).
- [ ] Verify `pmdarima` and `Prophet` import cleanly; if not, plan to use the Colab fallback (no penalty).
- [ ] VS Code (or preferred IDE) with the Python extension.
- [ ] Clone the course repo; run `make doctor` (validates the environment and prints ✓/✗ per package).
- [ ] Confirm classroom network allows github.com and pypi (or a mirror is configured); pre-download the datasets to the shared drive for offline rooms.

## Common Student Issues & Troubleshooting

| Issue | Frequency | Resolution |
|---|---|---|
| `pmdarima` / `Prophet` install fails (Windows/macOS wheels) | High | Pin known-good versions; fall back to provided Colab notebooks — no penalty |
| `auto_arima`/SARIMAX with `m=24` runs for minutes | High | Model the daily series with `m=7`; leave sub-daily to the ML route — a deliberate teachable wall |
| ADF/KPSS null hypotheses read backwards | High | The 2×2 poster; quiz cold; ADF small-p = stationary, KPSS small-p = non-stationary |
| Suspiciously low MAPE (leak surviving) | High | Re-run `assert_no_leakage`; check `.shift(1)` on rolling and no shuffle split |
| KSA weekend coded Sat–Sun | Medium | Fri(4)/Sat(5) in pandas `dayofweek` (Mon=0); check the calendar join |
| Backtest scores in-sample (MASE ≈ 0) | Medium | Use `sktime` `strategy="refit"`; never predict points the model trained on |
| Confidence vs prediction interval confusion | Medium | Prediction interval includes noise → wider; forecasting always wants it |
| Slow rolling backtest with SARIMAX refit | Medium | Expected; cache naive/ETS, parallelise folds, shrink the candidate grid |
| Quantile crossing (q95 < q50) | Low | Sort per-row quantiles or use a monotone constraint |
| Coverage good marginally, fails on hot afternoons | Low | Report coverage by hour band; switch to adaptive conformal (ACI/EnbPI) |

## Timing Recommendations

- Protect Lab 4 (feature engineering, the leakage lesson) and Lab 6 (backtesting) at full length; compress the M6 theory if behind — it lands through the lab.
- Day-3 afternoon is deliberately light on new theory so the backtest and capstone get uninterrupted build time; guard that.
- If a cohort is strong: pull the multi-area global model (Module 4 case study) into the capstone main scope and add a fourth model family (TBATS/Prophet).
- If a cohort is weak: reduce Lab 7 to two constraint scenarios and demo the third; never drop the *backtest report* — it is the course's deliverable and thesis made visible.
- Hard rule: capstone assembly (Day 3 H4) must start on time; cut discussion, not build time. Collect repo URLs at the end of H4 so backtest results can be spot-checked before the H5 demos.

## Discussion Prompts (use during transitions)

1. "What is the most expensive forecasting error you've seen reach a decision — and would a backtest have caught it?"
2. "Your model's MAPE is 1.6%. Your interval covers 90% on average but 78% on the hottest afternoons. Which number does the control room feel?"
3. "When is the free seasonal-naive forecast the *right* answer, and how would your report prove it?"
4. "Who owns the reserve-margin quantile — forecasting, operations, or risk? What does your answer imply about which number you publish?"
5. "If the repository is the audit evidence for an accuracy claim, what does *your* current backtest testify?"

## Wrap-up (Day 3 final 15 minutes)

- Map each capstone requirement to the module that taught it (one slide): decomposition→M1, stationarity→M2, classical→M3, features→M4, intervals→M5, backtest→M6, selection→M7.
- Reinforce the single thesis one last time: *respect the arrow of time so every reported accuracy number would survive contact with the future.* The leakage-safe features, the time-aware backtest, and the calibrated intervals are three faces of that one discipline.
- Forward pointer: SDA-DSC-311 builds on this pipeline; SDA-DSC-213 (Experimentation & Causal Inference) is the sibling "what actually works" skill for decisions forecasting alone cannot answer.
- Collect: repo URLs, `BACKTEST_REPORT.md`, `DECISION_RECORD.md`, `BENCHMARKS.md`; issue Forecasting-badge recommendations within 5 working days.

---

*End of instructor package. All code samples target Python 3.12 with statsmodels ≥ 0.14, pmdarima ≥ 2.0, sktime ≥ 0.30, and LightGBM ≥ 4.0. Verify pinned versions in the course lock file before each delivery. The golden thread — the `Tayyar` national load-forecasting service on the `ksa_grid_demand` hourly series — runs unbroken from decomposition (Module 1) to the backtested, calibrated, defensibly-selected production pipeline of the capstone.*
