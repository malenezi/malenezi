# Advanced Machine Learning Methods
## أساليب تعلم الآلة المتقدمة

**Instructor-Ready Training Package — SDAIA Academy**

---

# Cover Page

| Field | Details |
|---|---|
| **Course Title** | Advanced Machine Learning Methods |
| **Arabic Title** | أساليب تعلم الآلة المتقدمة |
| **Code** | SDA-DSC-211 |
| **Level** | Specialist / متخصص |
| **Duration** | 4 days × 5 learning hours = **20 hours** |
| **Audience** | Data scientists progressing to specialist modelling roles |
| **Prerequisites** | SDA-AIE-111 (cross-listed); SDA-DSC-111 |
| **Assessment** | Modelling challenge; interpretability report |
| **Stackability** | Advanced ML badge · Core of the Data Scientist Specialist certificate · Next: SDA-DSC-212 / SDA-DSC-213 |
| **Tools & Platforms** | XGBoost · LightGBM · SHAP · scikit-learn · Optuna |

## Course Description

A specialist module that deepens modelling skill beyond the foundations. Participants master gradient-boosting frameworks, imbalanced and cost-sensitive learning, model interpretability with SHAP, and rigorous validation design. The emphasis is on winning reliable performance on messy, real-world tabular problems — the kind that dominate Saudi banking, telecom, health, and government analytics.

The course is built around a single evolving artefact: **"Tamweel" (تمويل)**, a consumer-financing default-risk model for a Saudi lender supervised under SAMA rules. Participants receive a realistic, imbalanced applications dataset and build the model up across every module — first a strong gradient-boosted baseline, then a leakage-proof validation scheme, cost-sensitive thresholds, SHAP explanations fit for a regulator, calibrated probabilities that price expected loss, and a stacked ensemble. By Day 4 each participant owns a documented, calibrated, explainable model and defends it in an applied modelling challenge — the same shape of deliverable expected in SDA-DSC-390 (the Data Science Capstone).

## Learning Outcomes

By the end of this course, participants will be able to:

1. **LO1** — Develop high-performance models with XGBoost and LightGBM
2. **LO2** — Design validation schemes that respect leakage, grouping, and time order
3. **LO3** — Apply techniques for imbalanced, noisy, and cost-sensitive problems
4. **LO4** — Analyze model behaviour using SHAP and permutation importance
5. **LO5** — Optimize feature pipelines and model ensembles for tabular data
6. **LO6** — Evaluate models for stability, calibration, and business impact

---

# Course Delivery Plan

## Day-by-Day Schedule

| Day | Theme | Modules | Theory % | Lab % | Deliverable at End of Day |
|---|---|---|---|---|---|
| **Day 1** | Strong baselines, honest validation | M1: Gradient Boosting Deep Dive · M2: Validation Design & Leakage Prevention | 45% | 55% | Tuned LightGBM baseline + leakage-audited, time-aware CV harness |
| **Day 2** | Hard data, real decisions | M3: Imbalanced & Cost-Sensitive Learning · M4: Model Interpretability with SHAP | 40% | 60% | Cost-optimal threshold + SHAP interpretability report v1 |
| **Day 3** | Trust the numbers | M5: Calibration & Uncertainty · M6: Ensembling & Stacking Strategies | 40% | 60% | Calibrated probabilities (reliability curve) + stacked ensemble |
| **Day 4** | Win it and defend it | M7: Applied Modelling Challenge · Capstone assembly & defence | 25% | 75% | Final Tamweel model, model card, leaderboard entry, panel defence |

## Hour-by-Hour Breakdown

### Day 1 — Strong Baselines, Honest Validation

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Why advanced ML is a data problem, not an algorithm problem** + course kickoff; meet the Tamweel dataset | Frame the module; recognise where AUC gains actually come from on tabular data; tour the golden-thread dataset | Interactive lecture + data exploration | 70/30 |
| 2 | **Gradient boosting deep dive** (M1) | How GBMs fit residuals; histogram algorithm; leaf-wise vs level-wise; the key hyperparameters and what they trade | Lecture + live training demo | 70/30 |
| 3 | **Lab 1 — Baseline that beats the benchmark** | Train, tune (Optuna), and early-stop a LightGBM/XGBoost default-risk model | Guided lab (pairs) | 15/85 |
| 4 | **Validation design & leakage prevention** (M2) | Leakage taxonomy; group/time splits; pipeline-inside-CV; nested CV; target encoding done safely | Lecture + leakage-hunt demo | 65/35 |
| 5 | **Lab 2 — Build the validation harness** | Replace naive CV with grouped, time-aware CV; find and fix two planted leaks | Guided lab (pairs) | 10/90 |

### Day 2 — Hard Data, Real Decisions

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Imbalanced & cost-sensitive learning** (M3) | Why resampling is overrated; class weights, `scale_pos_weight`, focal loss; the cost matrix; threshold as a business lever | Lecture + cost-curve demo | 65/35 |
| 2 | **Lab 3 — Cost-optimal decisions** | Add class weighting, sweep thresholds against a SAR cost matrix, choose the operating point | Guided lab | 10/90 |
| 3 | **Model interpretability: SHAP and beyond** (M4) | Global vs local; permutation importance vs SHAP; TreeSHAP; interaction values; reading beeswarm/dependence plots | Lecture + SHAP walkthrough | 65/35 |
| 4 | **Lab 4 — Interpretability report** | Generate global + local SHAP explanations; produce reason codes for adverse-action letters | Guided lab | 15/85 |
| 5 | **Lab 4 (cont.) + interpretation clinic** | Diagnose a leak found via SHAP; write plain-language findings for a risk committee | Lab + facilitated critique | 20/80 |

### Day 3 — Trust the Numbers

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **Calibration & uncertainty** (M5) | Why boosted scores aren't probabilities; reliability diagrams; Platt vs isotonic; ECE; prediction intervals & conformal basics | Lecture + reliability-curve demo | 70/30 |
| 2 | **Lab 5 — Calibrate for expected loss** | Calibrate the model, measure ECE before/after, convert scores to expected-loss SAR | Guided lab | 15/85 |
| 3 | **Ensembling & stacking strategies** (M6) | Bagging/boosting/blending; diversity; out-of-fold stacking; when ensembling helps vs hurts | Lecture + stacking demo | 65/35 |
| 4 | **Lab 6 — Stacked ensemble** | Build an OOF stack (LightGBM + XGBoost + linear) and compare to the best single model | Guided lab | 10/90 |
| 5 | **Stability & robustness clinic** | Seed variance, feature stability (PSI), slice metrics, adversarial "what breaks this model?" | Lab + discussion | 30/70 |

### Day 4 — Win It and Defend It

| Hour | Session | Learning Objectives | Delivery Mode | Theory/Lab |
|---|---|---|---|---|
| 1 | **The applied modelling challenge** (M7) briefing + strategy | Read the brief; plan experiments; set up the private leaderboard and submission format | Briefing + planning | 40/60 |
| 2 | **Challenge sprint 1** | Feature engineering + model selection against the held-out ledger | Project work | 0/100 |
| 3 | **Challenge sprint 2** | Calibration, thresholding, ensembling; finalise the operating point | Project work | 0/100 |
| 4 | **Model card + interpretability defence assembly** | Complete the model card; assemble SHAP + calibration + cost evidence | Project work | 10/90 |
| 5 | **Final leaderboard reveal + panel defence + wrap-up** | Present business-metric result; defend validation & fairness; path to SDA-DSC-212/213 | Presentations | 20/80 |

## Instructor Guidance Notes (Delivery Plan Level)

- **Golden thread:** every module operates on the same **Tamweel** default-risk dataset. Never introduce a throwaway toy dataset (no `load_breast_cancer`) — always evolve the Tamweel model. This is what makes the Day-4 challenge achievable and the interpretability report coherent.
- **Pace control:** Labs 1 and 4 overrun most often (Optuna tuning and SHAP rendering are time sinks). Publish checkpoint notebooks/commits (`lab1-start`, `lab1-solution`, `lab2-start`, …) so stragglers can fast-forward: `git checkout lab4-start`. Cap Optuna trials in-class (e.g. 40) and hand out a pre-computed `study.pkl`.
- **Pairing:** rotate pairs each day. Pair a strong-statistics participant (from SDA-DSC-111) with a strong-engineering participant; the validation-rigour ↔ tooling transfer is the point.
- **Environment strategy:** primary = local Python 3.12 venv with the pinned `requirements.txt`; fallback = Google Colab (GPU not required — CPU LightGBM is fast on this dataset). Verify both the week before delivery; SHAP + recent NumPy versions are the usual break point.
- **Language:** deliver in English or Arabic; keep all code, identifiers, column names, and commit messages in English (production convention in Saudi enterprise/banking environments — mixed-language columns break downstream pipelines and SAMA reporting).
- **Prayer and break scheduling:** each "hour" is 50 minutes of instruction + 10 minutes buffer; schedule the long break around Dhuhr. Day-4 sprints are deliberately continuous — protect them from theory creep.
- **Determinism discipline:** set and log every random seed from Hour 1. Much of Day 3's stability clinic depends on participants having seeded their earlier work; make it a habit early.
- **Assessment logistics:** the private leaderboard scores on a **held-out ledger** the participants never see, using a **business cost metric** (SAR), not raw AUC — collect submission files at the end of Day-4 Hour 3 so scoring completes before the Hour-5 reveal.

---

# Module 1 — Gradient Boosting Deep Dive

## Module Overview

**Purpose.** Gradient-boosted decision trees (GBDTs) are the workhorse of applied tabular ML and win the majority of real-world structured-data problems. Yet most practitioners treat XGBoost and LightGBM as black boxes with magic hyperparameters. This module opens the box: participants learn *how* boosting fits residuals stage by stage, why the histogram algorithm made GBDTs fast, what leaf-wise growth trades against level-wise growth, and — most usefully — which hyperparameters actually move the needle and in which direction.

**Business relevance.** For Saudi banks, telecoms, and government analytics teams, the dominant modelling substrate is tabular: applications, transactions, subscriber records, service tickets. On these, a well-tuned GBDT typically beats both logistic regression and deep learning while training in seconds on a laptop. Knowing how to extract that last few points of performance — and knowing when you have hit the ceiling — is directly what separates a specialist data scientist from a practitioner who runs `fit()` with defaults.

**Industry use cases.**
- A consumer lender scores default risk at application time to set approval and pricing (our Tamweel golden thread).
- A telecom predicts churn from usage and billing features to target retention offers within budget.
- A utility forecasts non-technical loss (meter tampering) from consumption patterns, a highly imbalanced tabular problem.

**Expected competencies.** After this module a participant can train and early-stop an XGBoost/LightGBM model, read a learning curve, tune the high-leverage hyperparameters deliberately (not by superstition), run an Optuna study with pruning, and explain to a colleague why leaf-wise growth needs `num_leaves` controlled rather than `max_depth` alone.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 1.1 | Explain how gradient boosting fits an additive model of trees on the loss gradient | LO1 |
| 1.2 | Contrast XGBoost (level-wise) and LightGBM (leaf-wise) growth and their implications | LO1 |
| 1.3 | Train a GBDT with early stopping and read the resulting learning curve | LO1, LO6 |
| 1.4 | Tune high-leverage hyperparameters deliberately with a validation-driven search | LO1, LO5 |
| 1.5 | Run an Optuna study with pruning and interpret the importance of each parameter | LO1, LO5 |

## Technical Content

### 1. From a single tree to an additive ensemble

A single decision tree is high-variance: it memorises. Boosting turns many *weak*, shallow trees into one strong model by adding them sequentially, each correcting the errors of those before it. Formally, boosting builds an additive model

```
F_0(x) = base score (e.g. log-odds of the prior)
F_m(x) = F_{m-1}(x) + η · h_m(x)
```

where each new tree `h_m` is fit to the **negative gradient** of the loss at the current predictions (for squared error, that gradient *is* the residual; for log-loss it is `y − p`). The learning rate `η` shrinks each tree's contribution so no single tree dominates — smaller `η` needs more trees but generalises better. This is *gradient descent in function space*: instead of nudging parameters, each step adds a function that points down the loss surface.

**Teach this with a picture, then a number.** Show residuals shrinking over 5 boosting rounds on a 1-D toy, then immediately return to Tamweel — the same mechanism, 40,000 rows and 34 features.

### 2. Second-order boosting: why XGBoost was a leap

XGBoost popularised using the **second-order** Taylor expansion of the loss — both the gradient `g_i` and the Hessian `h_i`. The optimal leaf weight and the split gain then have closed forms:

```
optimal leaf weight  w* = − (Σ g_i) / (Σ h_i + λ)
split gain           = ½ [ G_L²/(H_L+λ) + G_R²/(H_R+λ) − (G_L+G_R)²/(H_L+H_R+λ) ] − γ
```

Two regularisation knobs fall directly out of this maths and are worth naming in class: **λ** (`reg_lambda`, L2 on leaf weights) shrinks weights toward zero; **γ** (`min_split_loss`) is a minimum gain a split must clear to be kept — it is pruning expressed as a threshold. Understanding that these come from the objective, not from folklore, is what lets participants tune them with intent.

### 3. The histogram algorithm and why LightGBM is fast

Naive split-finding sorts every feature at every node — expensive. The **histogram algorithm** buckets each feature into a fixed number of bins (default 255) once, then evaluates splits on bin boundaries. This is the single biggest speed idea in modern GBDTs and both libraries use it (`tree_method="hist"` in XGBoost; native in LightGBM). LightGBM adds two tricks: **GOSS** (keep high-gradient rows, subsample low-gradient ones) and **EFB** (bundle mutually-exclusive sparse features). Practical consequence: on Tamweel-scale data LightGBM trains in a few seconds on CPU, which is why we use it as the default lab engine and keep XGBoost for cross-checking.

### 4. Leaf-wise vs level-wise growth — the hyperparameter that confuses everyone

- **XGBoost (level-wise / depth-wise):** grows the tree one full level at a time; `max_depth` is the natural control.
- **LightGBM (leaf-wise / best-first):** always splits the leaf with the highest gain, producing deep, asymmetric trees. This is more accurate per split but overfits fast if uncontrolled. Here `num_leaves` is the primary complexity control, **not** `max_depth`.

The classic mistake: setting `max_depth=6` in LightGBM and expecting XGBoost-like behaviour. A leaf-wise tree of depth 6 can have up to `2^6 = 64` leaves; if you leave `num_leaves=31` (the default), depth is the binding constraint and the model is smaller than you think — or if you raise `num_leaves` without a depth cap, it explodes. Rule of thumb: keep `num_leaves < 2^max_depth`, tune `num_leaves` as the real dial.

### 5. The hyperparameters that actually matter (and their direction)

Participants leave with this mental table, ordered by leverage:

| Parameter (LGBM / XGB) | What it controls | Increase → | Typical range |
|---|---|---|---|
| `n_estimators` + `learning_rate` | model capacity / step size | more trees + smaller LR = better, slower | LR 0.01–0.1; trees via early stopping |
| `num_leaves` / `max_depth` | tree complexity | more complex, more overfit | leaves 15–255; depth 3–10 |
| `min_child_samples` / `min_child_weight` | leaf minimum evidence | more = smoother, less overfit | 20–200 |
| `subsample` (bagging) | row sampling per tree | <1 adds regularisation + speed | 0.6–1.0 |
| `colsample_bytree` / `feature_fraction` | column sampling per tree | <1 adds regularisation + decorrelation | 0.6–1.0 |
| `reg_lambda`, `reg_alpha` | L2 / L1 on weights | more = simpler | 0–10 |
| `min_split_gain` / `gamma` | minimum split gain | more = more pruning | 0–1 |

**Golden pattern:** fix a low learning rate, let **early stopping** choose `n_estimators`, then tune complexity and regularisation with a search. Never grid-search `n_estimators` — early stopping does it for free and correctly per configuration.

### 6. Common mistakes & production considerations

1. **No early stopping**, or early stopping on the *training* set — you must pass a genuine held-out validation set (leak-free, per Module 2).
2. **Tuning learning rate and n_estimators independently** — they trade off; fix LR, early-stop the count.
3. **Ignoring categorical handling** — LightGBM handles categoricals natively (`categorical_feature=`); one-hot exploding a 400-city column is slower and often worse.
4. **Reading the training-set feature importance as truth** — split/gain importance is biased toward high-cardinality features; this motivates Module 4's permutation importance and SHAP.
5. **Chasing 0.001 AUC with 500 Optuna trials** while ignoring leakage (Module 2) and calibration (Module 5) — misallocated effort; the business metric rarely moves.
6. **Production drift blindness** — the boosted model that wins today degrades as the population shifts; log inputs and monitor (foreshadows Module 5 stability + SDA-DSC-212).

## Code Examples

### A clean, early-stopped LightGBM baseline

```python
# src/tamweel/models/baseline_lgbm.py
"""Tamweel default-risk baseline. One honest validation split here;
Module 2 replaces this with a leakage-proof, time-aware CV harness."""
from __future__ import annotations
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
TARGET = "default_90dpd"

def load_xy(path: str) -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_parquet(path)
    y = df[TARGET].astype(int)
    X = df.drop(columns=[TARGET, "application_id", "decision_date"])
    # LightGBM reads pandas 'category' dtype natively — no one-hot needed
    for col in X.select_dtypes("object"):
        X[col] = X[col].astype("category")
    return X, y

def train_baseline(X: pd.DataFrame, y: pd.Series) -> lgb.LGBMClassifier:
    X_tr, X_val, y_tr, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

    model = lgb.LGBMClassifier(
        objective="binary",
        learning_rate=0.03,        # low LR; count chosen by early stopping
        n_estimators=5000,         # upper bound — early stopping cuts it down
        num_leaves=63,             # leaf-wise complexity dial (NOT max_depth)
        min_child_samples=80,      # leaf must see >=80 rows -> smoother
        subsample=0.8, subsample_freq=1,
        colsample_bytree=0.8,
        reg_lambda=2.0,
        random_state=RANDOM_STATE, n_jobs=-1, verbose=-1,
    )
    model.fit(
        X_tr, y_tr,
        eval_set=[(X_val, y_val)],
        eval_metric="auc",
        callbacks=[lgb.early_stopping(200), lgb.log_evaluation(100)],
    )
    p = model.predict_proba(X_val)[:, 1]
    print(f"best_iteration={model.best_iteration_}  "
          f"AUC={roc_auc_score(y_val, p):.4f}  "
          f"PR-AUC={average_precision_score(y_val, p):.4f}")
    return model
```

### Optuna tuning with pruning

```python
# src/tamweel/models/tune_lgbm.py
"""Deliberate, validation-driven search. Fix LR low, early-stop the tree
count, and let Optuna prune unpromising trials to save time in class."""
import optuna
import lightgbm as lgb
from optuna.integration import LightGBMPruningCallback
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import numpy as np

def objective(trial, X, y):
    params = {
        "objective": "binary", "metric": "auc", "verbosity": -1,
        "learning_rate": 0.03,
        "num_leaves": trial.suggest_int("num_leaves", 15, 255, log=True),
        "min_child_samples": trial.suggest_int("min_child_samples", 20, 300),
        "subsample": trial.suggest_float("subsample", 0.6, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
        "reg_lambda": trial.suggest_float("reg_lambda", 1e-3, 10.0, log=True),
        "reg_alpha": trial.suggest_float("reg_alpha", 1e-3, 10.0, log=True),
    }
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = []
    for fold, (tr, va) in enumerate(cv.split(X, y)):
        dtr = lgb.Dataset(X.iloc[tr], y.iloc[tr])
        dva = lgb.Dataset(X.iloc[va], y.iloc[va])
        pruning = LightGBMPruningCallback(trial, "auc", valid_name="valid_0")
        booster = lgb.train(
            params, dtr, num_boost_round=5000, valid_sets=[dva],
            callbacks=[lgb.early_stopping(150), pruning])
        p = booster.predict(X.iloc[va], num_iteration=booster.best_iteration)
        scores.append(roc_auc_score(y.iloc[va], p))
    return float(np.mean(scores))

def run_study(X, y, n_trials: int = 40) -> optuna.Study:
    study = optuna.create_study(direction="maximize",
                                pruner=optuna.pruners.MedianPruner())
    study.optimize(lambda t: objective(t, X, y), n_trials=n_trials)
    print("best AUC:", round(study.best_value, 4))
    print("best params:", study.best_params)
    return study
```

### XGBoost cross-check (same interface, level-wise growth)

```python
# src/tamweel/models/baseline_xgb.py
import xgboost as xgb
from sklearn.metrics import roc_auc_score

def train_xgb(X_tr, y_tr, X_val, y_val):
    model = xgb.XGBClassifier(
        tree_method="hist",           # histogram algorithm, like LightGBM
        learning_rate=0.03, n_estimators=5000,
        max_depth=6,                  # level-wise: depth is the natural dial
        min_child_weight=5.0,         # Hessian-weighted leaf minimum
        subsample=0.8, colsample_bytree=0.8,
        reg_lambda=2.0, gamma=0.0,
        eval_metric="auc", early_stopping_rounds=200,
        enable_categorical=True, random_state=42, n_jobs=-1,
    )
    model.fit(X_tr, y_tr, eval_set=[(X_val, y_val)], verbose=100)
    p = model.predict_proba(X_val)[:, 1]
    print(f"XGB best_iteration={model.best_iteration}  "
          f"AUC={roc_auc_score(y_val, p):.4f}")
    return model
```

## Hands-on Lab 1 — A Baseline That Beats the Benchmark

| | |
|---|---|
| **Objective** | Train, early-stop, and tune a LightGBM (and cross-check XGBoost) default-risk model on Tamweel; beat the provided logistic-regression benchmark (AUC 0.741) by a documented margin |
| **Duration** | 50 minutes |
| **Setup** | Python 3.12, `pip install lightgbm xgboost optuna scikit-learn pandas pyarrow`, course repo, `git checkout lab1-start`; dataset `data/tamweel_train.parquet` |

**Instructions & tasks**

1. *(5 min)* Load `tamweel_train.parquet`; confirm the shape (≈40,000 × 35), the base default rate (≈7.4%), and cast object columns to `category`.
2. *(10 min)* Run `train_baseline`; record `best_iteration_`, validation AUC and PR-AUC. Note how many trees early stopping actually kept.
3. *(10 min)* Deliberately break it to learn: set `learning_rate=0.3`, re-run, observe worse validation AUC and a much smaller `best_iteration_`. Restore `0.03`. Discuss the LR/tree-count trade-off with your pair.
4. *(15 min)* Run `run_study(X, y, n_trials=40)` (a pre-computed `study.pkl` is provided as fallback). Retrain with `study.best_params`; record the new AUC.
5. *(5 min)* Cross-check with `train_xgb`; compare AUC and training time to LightGBM.
6. *(5 min)* Write one paragraph in `RESULTS.md`: your best AUC, the margin over the 0.741 benchmark, and which hyperparameter mattered most (read `optuna.importance.get_param_importances(study)`).

**Expected output**
```
$ python -m tamweel.models.baseline_lgbm
best_iteration=612  AUC=0.7863  PR-AUC=0.3120
$ python -m tamweel.models.tune_lgbm      # 40 trials, ~90s on a laptop
best AUC: 0.7911
best params: {'num_leaves': 41, 'min_child_samples': 140, ...}
param importance (top): num_leaves 0.38, min_child_samples 0.27, reg_lambda 0.14
```

**Acceptance criteria:** tuned validation AUC ≥ 0.785 and strictly greater than the baseline; early stopping used (no hand-set `n_estimators`); `RESULTS.md` names the top parameter.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `LightGBMError: Do not support special JSON characters in feature name` | Arabic/space column names | Rename columns to English snake_case on load (course loader does this) |
| Categorical columns treated as numeric | Left as `object`/`int` codes | Cast to pandas `category`; pass `categorical_feature="auto"` |
| AUC suspiciously high (>0.95) | A leaked feature (e.g. `days_past_due`) slipped in | Preview Module 2 — drop post-outcome columns; the loader excludes them, custom code may not |
| Optuna very slow in class | Too many trials / no pruning | Cap `n_trials=40`; ensure `MedianPruner` active; use provided `study.pkl` |

**Instructor notes.** The deliberate `learning_rate=0.3` step in task 3 is the highest-value 5 minutes — participants *see* early stopping cut the tree count and AUC drop, internalising the LR/count trade-off far better than a slide. Fast finishers: have them set `num_leaves=511` with no `min_child_samples` and watch train-AUC → 0.99 while val-AUC falls (overfitting made visible), a perfect bridge to Module 2.

## Mini Exercises

**Quiz (5 questions)**
1. In LightGBM, which parameter is the primary complexity control? (a) `max_depth` (b) `num_leaves` (c) `n_estimators` (d) `learning_rate` → **b**
2. You lower `learning_rate` from 0.1 to 0.03. What should happen to the early-stopped `best_iteration_`? → it increases (more, smaller steps).
3. Why never grid-search `n_estimators`? → early stopping selects it optimally per configuration for free.
4. Which importance type is biased toward high-cardinality features? → split/gain importance (motivates permutation/SHAP in M4).
5. True/False: `max_depth=6` fully controls a LightGBM tree's size. → **False** (leaf-wise growth; `num_leaves` binds).

**Coding exercise.** Given a fixed dataset, produce a learning curve: plot train vs validation AUC against boosting round using `evals_result`. Identify the round where validation plateaus and training keeps rising — mark the overfitting onset.

**Debugging exercise.** A participant's model shows validation AUC *below* train AUC by 0.15 with `num_leaves=255, min_child_samples=5`. Diagnose and prescribe two parameter changes; predict their effect on the gap.

**Discussion questions.**
- Your model gains 0.004 AUC from 300 more Optuna trials. Where else could that hour go for more business value?
- When would you *not* reach for a GBDT on tabular data? (tiny n, need for a monotone/linear audit story, hard extrapolation beyond training range).

## Case Study — The Overfit Champion at a Riyadh Consumer Lender

**Scenario.** A data scientist at a Riyadh consumer-finance company reports an internal-validation AUC of 0.94 on default prediction — far above the team's usual 0.79 — and requests deployment. Risk is thrilled; the model lead is suspicious.

**Business context.** A 0.94-AUC default model would be worth tens of millions of SAR in avoided losses if real. It is not: the model was tuned with `num_leaves=511`, no `min_child_samples`, and — the real culprit — a feature `current_dpd` (current days-past-due) that only exists *after* the loan has started performing.

**Technical challenge.** Separate genuine boosting skill from overfitting and leakage. Retrain with disciplined complexity control and an application-time-only feature set.

**Constraints.** SAMA model-risk governance requires a defensible validation story; the model must be explainable (Module 4); the team has one week before a model-risk committee review.

**Solution approach (facilitate, don't lecture).** (1) Re-run with strong regularisation and early stopping — AUC falls to 0.80, the honest number. (2) Audit features for outcome leakage (full treatment is Module 2) — remove `current_dpd` and two siblings. (3) Show the learning curve before/after to the committee as evidence of discipline. (4) Frame the 0.80 as *trustworthy* vs the 0.94 as *fictional*.

**Discussion questions.**
1. Which of the two problems (overfitting vs leakage) inflated the score more, and how would you quantify each?
2. How do you present "the number went down and that's good news" to a risk committee?
3. What repository/process control would have caught `current_dpd` before it reached tuning?
4. Is 0.80 good enough to ship? What other evidence (calibration, cost, fairness) does the committee need?

## Benchmarks and Evaluation

| Metric | Category | Target after M1 | How measured |
|---|---|---|---|
| Validation AUC (tuned) | Performance | ≥ 0.785, > baseline 0.741 | `roc_auc_score` on honest split |
| PR-AUC (default = positive) | Performance | ≥ 0.30 | `average_precision_score` |
| Train − Val AUC gap | Overfitting | ≤ 0.05 | difference of the two |
| Training time (LightGBM, CPU) | Efficiency | ≤ 10 s per fit | wall-clock |
| Optuna study (40 trials) | Efficiency | ≤ 3 min in class | wall-clock |
| Reproducibility (fixed seed) | Rigour | AUC identical across runs | two runs, same seed |

**Example benchmark table (filled during lab):**

| Model | Val AUC | PR-AUC | Trees kept | Train−Val gap |
|---|---|---|---|---|
| Logistic benchmark | 0.741 | 0.24 | — | 0.01 |
| LightGBM default | 0.779 | 0.29 | 480 | 0.06 |
| LightGBM + Optuna | 0.791 | 0.31 | 612 | 0.03 |
| XGBoost cross-check | 0.789 | 0.31 | 540 | 0.03 |

## Required Visuals and Training Assets

### Diagrams
1. **Boosting as additive correction** — *Purpose:* build intuition for the core mechanism. *Elements:* five stacked panels showing predictions converging on a 1-D target as residual trees are added; a running `F_m = F_{m-1} + η·h_m` caption. *Style:* flat vector, sequential panels, English labels with Arabic subtitles.
2. **Level-wise vs leaf-wise growth** — *Purpose:* fix the `num_leaves` confusion. *Elements:* two trees side by side — XGBoost balanced by level, LightGBM deep and asymmetric best-first — with the split order numbered. *Style:* side-by-side tree diagram.
3. **Histogram split-finding** — *Purpose:* explain the speed idea. *Elements:* a feature's values binned into 255 buckets; split gain evaluated at bin edges. *Style:* histogram with candidate-split markers.
4. **Hyperparameter leverage map** — *Purpose:* memorable tuning reference. *Elements:* the leverage table rendered as a labelled dial panel (capacity, complexity, regularisation, sampling). *Style:* printable A4 poster.

### Images (screenshots)
1. **Learning curve (train vs val AUC)**: *why:* the anchor image for early stopping; *content:* two curves diverging, early-stop line marked.
2. **Optuna optimisation history + param-importance bar**: *why:* shows deliberate search paying off; *content:* value-vs-trial plot and the importance ranking.
3. **Terminal — early stopping log**: *why:* expected-output reference; *content:* the `best_iteration` line exactly as in the lab.

### Simulations
1. **Overfit-on-demand** — *Setup:* a slider notebook exposing `num_leaves` and `min_child_samples`; participants watch the train/val gap open and close live. *Learning objective:* complexity control is visible, not mystical.
2. **Learning-rate trade-off** — *Setup:* re-run at LR ∈ {0.3, 0.1, 0.03, 0.01}, plot best-iteration and AUC. *Learning objective:* smaller LR + more trees generalises better, up to a point.

### Interactive Activities
- **Hyperparameter prediction game (10 min):** instructor names a change ("double `min_child_samples`"); pairs predict train-AUC and val-AUC direction before it is run.
- **"Guess the leak" cold open (10 min):** show a 0.99-AUC model; pairs list candidate leaked features before the reveal — seeds Module 2.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tamweel_train.parquet` | Synthetic, generated by course tooling (realistic Saudi consumer-finance schema, injected default patterns, SAR amounts) | Parquet | 40,000 rows × 35 cols | Baseline training; reused across all modules |
| `tamweel_holdout_ledger.parquet` | Held-out vintage, instructor-only | Parquet | 12,000 rows | Day-4 challenge scoring; never shown |
| `study.pkl` | Pre-computed Optuna study | pickle | small | Fallback if in-class tuning is slow |

### Demo Requirements
- **Instructor demo:** live train-early-stop-tune loop in under 8 minutes, narrating the early-stopping log line by line.
- **Student demo:** one pair presents their learning curve and names the parameter that helped most.
- **Expected outputs:** tuned AUC ≥ 0.785, reproducible under a fixed seed, `RESULTS.md` written.

---

# Module 2 — Validation Design and Leakage Prevention

## Module Overview

**Purpose.** The single most expensive error in applied ML is not a weak model — it is a validation scheme that lies. A validation number you cannot trust is worse than no number, because it manufactures false confidence that survives all the way to production. This module teaches participants to design validation that tells the truth: naming every way data leaks, choosing splits that respect grouping and time order, and putting the *entire* preprocessing pipeline inside cross-validation so that fit statistics never see the validation fold.

**Business relevance.** In Saudi banking and government analytics, models pass through model-risk governance (SAMA MRM, internal audit) that scrutinises validation methodology specifically. A model that scored 0.86 in a leaky offline test and 0.72 in production is not just embarrassing — it is a governance finding, a written incident, and often a moratorium on the team's deployments. Leakage-proof validation is the difference between a model that ships once and a team that is trusted to ship repeatedly.

**Industry use cases.**
- Credit default: features must reflect only what is knowable at *application time* — no future repayment behaviour (our Tamweel leak).
- Churn: customers must not appear in both train and validation (group leakage by `customer_id`); a household's multiple SIMs likewise.
- Demand forecasting: strictly time-ordered validation — you may never train on the future to predict the past.

**Expected competencies.** After this module a participant can enumerate the leakage taxonomy, choose between `StratifiedKFold`, `StratifiedGroupKFold`, and `TimeSeriesSplit` for a given problem, build an sklearn `Pipeline` so preprocessing is refit per fold, apply target encoding without leakage, and audit a feature set for outcome and temporal leakage.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 2.1 | Enumerate the forms of data leakage and detect them in a feature set | LO2 |
| 2.2 | Select a cross-validation scheme that respects grouping and time order | LO2 |
| 2.3 | Encapsulate preprocessing inside CV so no statistic leaks across folds | LO2, LO5 |
| 2.4 | Apply target/mean encoding safely with out-of-fold or smoothing schemes | LO2, LO5 |
| 2.5 | Design a hold-out and (optionally) nested-CV protocol for honest model selection | LO2, LO6 |

## Technical Content

### 1. The leakage taxonomy — name the enemy

Leakage is any information in your training features that will not be legitimately available at prediction time (or that carries the answer). Teach these categories explicitly:

- **Target leakage:** a feature is a proxy or consequence of the label. In Tamweel, `current_dpd`, `days_since_last_missed_payment`, `collections_flag` all only exist *because* the loan already defaulted or performed. AUC 0.94 — and useless.
- **Train/test contamination (preprocessing leakage):** fitting a scaler, imputer, target encoder, or feature selector on the *whole* dataset before splitting. The validation fold's statistics have bled into training.
- **Temporal leakage:** using future data to predict the past — training on 2024 loans to score 2023, or including a feature computed over a window that extends past the decision date.
- **Group leakage:** the same entity (customer, household, device) in both train and validation, letting the model memorise the entity rather than learn the pattern.
- **Duplicate/near-duplicate leakage:** copies or resampled rows straddling the split (a specific risk once we do imbalanced resampling in Module 3 — always resample *inside* the training fold only).

**Instructor note:** the taxonomy is the module. If participants can *name* which kind of leak they face, the fix is usually obvious. Print it as a poster.

### 2. Choosing the right split

The split must mirror how the model will be used in production:

| Situation | Split | Why |
|---|---|---|
| i.i.d. rows, class imbalance | `StratifiedKFold` | preserves class ratio per fold |
| repeated entities (customer, household) | `StratifiedGroupKFold` | keeps a group entirely on one side |
| time-ordered decisions | `TimeSeriesSplit` / forward-chaining | never train on the future |
| both grouping and time | time split + group check | the hardest, most realistic case |

For Tamweel, applications arrive over time and a customer can apply more than once. The honest scheme is **time-ordered** (train on earlier vintages, validate on later) with a **group guard** so a repeat customer does not straddle the boundary. This mirrors deployment: tomorrow's applicants are in the future and may be returning customers.

### 3. Put the pipeline *inside* cross-validation

The rule: **every step that learns from data must be refit on the training fold only.** That includes imputation means, scaler statistics, target-encoding tables, and feature selection. The mechanism is an sklearn `Pipeline` (or `ColumnTransformer`) passed to `cross_val_score`/`cross_validate` — sklearn refits it per fold automatically. The anti-pattern is `X = imputer.fit_transform(X)` *before* the CV loop; it silently leaks the validation folds' statistics into every training fit and inflates the score by a small, deceptive, consistent amount.

### 4. Target encoding without shooting yourself

High-cardinality categoricals (merchant, employer, city) are tempting to encode by their mean target. Done naively — `df.groupby(col)[target].mean()` on the whole set — this is textbook target leakage: each row's encoding contains its own label. Two safe schemes:

- **Out-of-fold (OOF) encoding:** compute each row's encoding from *other* folds only.
- **Smoothed / regularised encoding:** blend the category mean toward the global mean, weighted by how many rows the category has (`(n·cat_mean + m·global_mean)/(n+m)`), which also stabilises rare categories.

scikit-learn's `TargetEncoder` (1.3+) does internal cross-fitting; use it *inside* the pipeline so even its cross-fitting respects the outer fold boundaries. For Tamweel, `employer_id` and `merchant_category` are the encoding candidates — and the classic place a subtle leak sneaks back in.

### 5. Hold-out, nested CV, and honest model selection

Two distinct jobs need two distinct data budgets:

- **Model selection / tuning** uses cross-validation on the *development* set.
- **Final performance estimate** uses a **hold-out** that was never touched during any tuning — the closest offline analogue to production.

When you both tune hyperparameters *and* report a performance number from the same CV, you optimistically bias the estimate (you selected the config that got luckiest on those folds). **Nested CV** removes this bias: an inner loop tunes, an outer loop estimates — at the cost of `k_outer × k_inner` fits. Teach the trade-off honestly: nested CV is the gold standard for *comparing methods*; a single well-guarded hold-out is the pragmatic production choice for *estimating the chosen model*. For Tamweel we keep a final time-based hold-out (the latest vintage) and use time-series CV for tuning.

### 6. Common mistakes & production considerations

1. **`fit_transform` on the whole dataset** before splitting — the most common leak; the pipeline pattern eliminates it structurally.
2. **Random `KFold` on grouped or time data** — inflates the score and hides the drop that appears in production.
3. **Tuning and reporting from the same folds** — optimistic bias; separate selection from estimation.
4. **Leaky features that "make sense"** — `account_age_at_default`, `total_payments_made` — anything measured over the outcome window.
5. **Resampling before splitting** (SMOTE the whole set) — near-duplicates straddle folds; always resample inside the training fold (Module 3).
6. **Production parity:** the offline pipeline must be the same code path that runs at serving time. Feature computation windows, join keys, and as-of timestamps must match, or you rebuild the leak in production. Log an `as_of` timestamp on every feature.

## Code Examples

### Time-aware, group-guarded CV with the pipeline inside

```python
# src/tamweel/validation/cv.py
"""Honest CV for Tamweel: time order + a group guard, preprocessing
refit per fold. This harness replaces the naive split from Module 1."""
from __future__ import annotations
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import roc_auc_score

def time_group_folds(df: pd.DataFrame, n_splits: int = 5,
                     date_col: str = "decision_date",
                     group_col: str = "customer_id") -> list[tuple]:
    """Forward-chaining folds by calendar order; any customer that would
    straddle the boundary is pushed entirely into the training side."""
    order = df.sort_values(date_col).index.to_numpy()
    fold_edges = np.array_split(order, n_splits + 1)
    folds = []
    for k in range(1, n_splits + 1):
        train_idx = np.concatenate(fold_edges[:k])
        valid_idx = fold_edges[k]
        # group guard: no customer in both sides
        train_groups = set(df.loc[train_idx, group_col])
        valid_idx = np.array([i for i in valid_idx
                              if df.loc[i, group_col] not in train_groups])
        folds.append((train_idx, valid_idx))
    return folds

def cross_validate_lgbm(X, y, df, params) -> float:
    aucs = []
    for tr, va in time_group_folds(df):
        model = lgb.LGBMClassifier(**params)
        model.fit(X.loc[tr], y.loc[tr],
                  eval_set=[(X.loc[va], y.loc[va])], eval_metric="auc",
                  callbacks=[lgb.early_stopping(150, verbose=False)])
        p = model.predict_proba(X.loc[va])[:, 1]
        aucs.append(roc_auc_score(y.loc[va], p))
    print(f"time-group CV AUC: {np.mean(aucs):.4f} +/- {np.std(aucs):.4f}")
    return float(np.mean(aucs))
```

### Safe preprocessing pipeline with target encoding inside CV

```python
# src/tamweel/validation/pipeline.py
"""Every learned statistic (impute, target-encode) is refit per fold.
Nothing is fit on the full dataset before the split."""
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import TargetEncoder
from sklearn.model_selection import cross_val_score, StratifiedGroupKFold
from lightgbm import LGBMClassifier

HIGH_CARD = ["employer_id", "merchant_category", "city"]
NUMERIC   = ["amount_sar", "tenor_months", "income_sar", "dti", "bureau_score"]

def build_pipeline() -> Pipeline:
    pre = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), NUMERIC),
        # TargetEncoder cross-fits internally AND is refit per outer fold
        ("cat", TargetEncoder(smooth="auto", random_state=42), HIGH_CARD),
    ], remainder="passthrough")
    return Pipeline([
        ("pre", pre),
        ("clf", LGBMClassifier(learning_rate=0.05, n_estimators=400,
                               num_leaves=41, random_state=42, verbose=-1)),
    ])

def evaluate(X, y, groups) -> float:
    pipe = build_pipeline()
    cv = StratifiedGroupKFold(n_splits=5)          # group-safe folds
    scores = cross_val_score(pipe, X, y, groups=groups,
                             cv=cv, scoring="roc_auc")   # pipe refit per fold
    print(f"group-CV AUC: {scores.mean():.4f} +/- {scores.std():.4f}")
    return scores.mean()
```

### A leakage audit you can run on any feature set

```python
# src/tamweel/validation/leakage_audit.py
"""Two cheap, high-value checks: (1) single-feature AUC screen for
too-good-to-be-true predictors; (2) train-only vs full-fit score gap."""
import pandas as pd
from sklearn.metrics import roc_auc_score

POST_OUTCOME_DENYLIST = {              # features that only exist AFTER outcome
    "current_dpd", "days_since_last_missed_payment", "collections_flag",
    "total_payments_made", "account_age_at_default", "recovery_amount",
}

def screen_single_feature_auc(X: pd.DataFrame, y) -> pd.Series:
    """Any single feature with AUC > ~0.85 is a leakage suspect."""
    scores = {}
    for col in X.select_dtypes("number"):
        s = X[col]
        if s.notna().sum() < len(s) * 0.5:
            continue
        auc = roc_auc_score(y, s.fillna(s.median()))
        scores[col] = max(auc, 1 - auc)      # direction-agnostic
    return pd.Series(scores).sort_values(ascending=False)

def audit(X: pd.DataFrame, y) -> None:
    hits = POST_OUTCOME_DENYLIST & set(X.columns)
    if hits:
        print(f"[FAIL] post-outcome features present: {sorted(hits)}")
    suspects = screen_single_feature_auc(X, y).head(5)
    print("[INFO] top single-feature AUCs (investigate > 0.85):")
    print(suspects.to_string())
```

## Hands-on Lab 2 — Build the Validation Harness

| | |
|---|---|
| **Objective** | Replace the naive random split with a time-aware, group-guarded CV harness; run the leakage audit; find and remove two planted leaks; re-measure the honest AUC |
| **Duration** | 50 minutes |
| **Setup** | Lab 1 solution, `git checkout lab2-start`; dataset now includes a "dirty" feature view `tamweel_train_dirty.parquet` with planted leaks |

**Instructions & tasks**
1. *(5 min)* Load the dirty view. Run `audit(X, y)` — read the two flagged post-outcome features and the single-feature AUC screen.
2. *(10 min)* Confirm the leak's impact: train the Module-1 model on the dirty features, note the inflated AUC (~0.93). This is the "champion" from the case study.
3. *(10 min)* Remove the leaked columns; retrain; watch AUC fall to the honest ~0.79. Write both numbers to `RESULTS.md`.
4. *(10 min)* Swap random CV for `time_group_folds`; run `cross_validate_lgbm`. Compare its mean/variance to a plain `StratifiedKFold` on the same clean data — note the (usually lower, more honest) time-CV number.
5. *(10 min)* Add `TargetEncoder` for `employer_id` inside the pipeline; prove it is leak-safe by comparing pipeline-inside-CV AUC vs a deliberately-wrong "encode-then-CV" version.
6. *(5 min)* Commit: `feat(validation): time-group CV harness + leakage audit`.

**Expected output**
```
[FAIL] post-outcome features present: ['collections_flag', 'current_dpd']
[INFO] top single-feature AUCs (investigate > 0.85):
current_dpd           0.971
collections_flag      0.933
bureau_score          0.712
...
dirty AUC (leaked):   0.931
clean AUC (honest):   0.792
time-group CV AUC:    0.781 +/- 0.009
leaky encode AUC:     0.804   <- inflated; pipeline-inside-CV: 0.786
```

**Acceptance criteria:** both leaks identified and removed; honest CV AUC reported with its fold standard deviation; the leaky-vs-safe target-encoding gap demonstrated and explained in `RESULTS.md`.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Time-CV AUC *higher* than random-CV | Group guard dropped too few rows / dates unsorted | Confirm `decision_date` parsed as datetime; verify group guard executed |
| `TargetEncoder` import error | scikit-learn < 1.3 | Upgrade sklearn; or use provided smoothed-encoder fallback |
| Valid fold empty after group guard | One customer dominates a fold | Increase `n_splits` or coarsen groups to household |
| Audit flags a legitimate feature | Genuinely strong predictor (bureau_score) | AUC < 0.85 and available at application time → keep; judgement, not automation |

**Instructor notes.** Task 4's comparison is the payoff — participants often *dislike* that the honest number is lower. Name that discomfort: the goal is a number that survives production, not a number that wins a demo. Fast finishers: implement nested CV on a 2-parameter grid and compare its estimate to the single-hold-out estimate.

## Mini Exercises

**Quiz (5 questions)**
1. Which leak type does putting the pipeline inside CV eliminate? → preprocessing/contamination leakage.
2. You have repeat customers. Which splitter? → `StratifiedGroupKFold` (or time + group guard).
3. Why is `groupby(col)[target].mean()` on the full set unsafe? → each row's encoding contains its own label (target leakage).
4. Nested CV removes which bias? → optimistic bias from tuning and estimating on the same folds.
5. True/False: it is fine to run SMOTE before the train/test split. → **False** (near-duplicates straddle folds; resample inside the training fold only).

**Coding exercise.** Write a `check_temporal_leak(df, feature, date_col)` that flags any feature whose values are only populated for rows past a certain date (a sign it was computed over the outcome window).

**Debugging exercise.** A pipeline scores 0.81 in CV but 0.74 in a fresh hold-out. List three candidate causes ranked by likelihood and the check for each.

**Discussion questions.**
- Your stakeholder wants the higher (leaky) number "because the model can see those fields in the warehouse." How do you respond?
- Where in the Tamweel serving path could production reintroduce a leak that offline CV cannot catch?

## Case Study — The Vintage That Broke in Production at a National Bank

**Scenario.** A national bank's SME-lending default model validated at 0.83 AUC on random 5-fold CV, passed committee, and shipped. Three months live, realised discrimination dropped to 0.71 and approvals skewed badly toward a segment.

**Business context.** The model was trained and validated with random `KFold` on a snapshot spanning three years — including a COVID-era stimulus window where default behaviour was atypical. Random folds let the model train on post-stimulus rows to predict stimulus-era rows and vice versa. In production, facing only *future* applicants, the temporal structure it had implicitly exploited was gone.

**Technical challenge.** Rebuild validation to be strictly forward-chaining by loan vintage, and quantify how much of the 0.83 was borrowed from the future.

**Constraints.** SAMA model-risk review is now watching; the fix must be a documented methodology change, not a quiet retrain; the population has genuinely shifted, so some performance loss is real and must be distinguished from the validation artefact.

**Solution approach (facilitate, don't lecture).** (1) Reproduce with `TimeSeriesSplit` by vintage — CV AUC falls to 0.74, matching production. (2) Attribute the gap: ~0.09 was temporal leakage, not model decay. (3) Add a rolling-origin backtest as the standing validation protocol. (4) Introduce population-stability monitoring (previews Module 5 stability + SDA-DSC-212).

**Discussion questions.**
1. Why did random CV specifically hide this failure, while time-series CV exposed it?
2. How do you separate "validation was wrong" from "the world changed"?
3. What monitoring would have caught the drift before three months of bad approvals?
4. Should the model have shipped at 0.74 with honest validation? What guardrails would you attach?

## Benchmarks and Evaluation

| Metric | Category | Target after M2 | How measured |
|---|---|---|---|
| Honest time-group CV AUC | Validity | reported with fold std (≈0.78) | `cross_validate_lgbm` |
| Leaked features remaining | Integrity | 0 | `audit()` denylist + single-feature screen |
| Pipeline-inside-CV enforced | Integrity | yes (no pre-split `fit_transform`) | code review / import-of-fitter check |
| Random-CV vs time-CV gap | Diagnostic | measured and explained | difference of the two |
| Hold-out AUC vs CV AUC | Honesty | within ≈0.02 | latest-vintage hold-out |
| Fold-to-fold AUC std | Stability | ≤ 0.02 | std across folds |

**Example benchmark table (filled during lab):**

| Scheme | Reported AUC | Fold std | Honest? |
|---|---|---|---|
| Random KFold, leaked features | 0.931 | 0.004 | No (leak + contamination) |
| Random KFold, clean features | 0.804 | 0.006 | No (temporal optimism) |
| Time-group CV, clean features | 0.781 | 0.009 | Yes |
| Latest-vintage hold-out | 0.777 | — | Yes (production analogue) |

## Required Visuals and Training Assets

### Diagrams
1. **Leakage taxonomy tree** — *Purpose:* the anchor poster for the module. *Elements:* five branches (target, preprocessing, temporal, group, duplicate) each with a Tamweel example and its fix. *Style:* flat vector tree, English with Arabic subtitles.
2. **Pipeline-inside-CV vs outside-CV** — *Purpose:* make contamination visible. *Elements:* two flows — one fits the scaler/encoder on the whole set then splits (red), one refits per fold (green). *Style:* before/after split panel.
3. **Forward-chaining time-series CV** — *Purpose:* show honest temporal splits. *Elements:* expanding-window train blocks and the next-vintage validation block across a timeline. *Style:* timeline strip.
4. **Group leakage illustration** — *Purpose:* motivate grouped splits. *Elements:* one `customer_id` with rows on both sides of a naive split, crossed out; the grouped fix beside it. *Style:* two-panel.

### Images (screenshots)
1. **Leakage audit terminal output**: *why:* expected-output reference; *content:* the `[FAIL]` line and single-feature AUC ranking.
2. **Random-CV vs time-CV AUC side by side**: *why:* the honesty lesson made numeric; *content:* two boxplots of fold AUCs.
3. **`TargetEncoder` inside a `ColumnTransformer` in an IDE**: *why:* participants mirror it; *content:* the pipeline definition with the encoder highlighted.

### Simulations
1. **Contamination amplifier** — *Setup:* a branch that fits a scaler on the whole dataset; participants measure the small, consistent inflation vs the pipeline version. *Learning objective:* leakage is often *subtle* (a few AUC points), which is exactly why it survives review.
2. **Vintage-shift replay** — *Setup:* replay the case-study data by vintage; random CV vs time CV diverge live. *Learning objective:* the split must mirror deployment.

### Interactive Activities
- **Leak hunt (15 min):** pairs receive 20 candidate Tamweel features and sort each into "safe at application time" vs "post-outcome leak", then defend three borderline calls.
- **Split-choice cards (10 min):** ten problem descriptions; pairs pick the correct splitter and justify in one sentence.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tamweel_train_dirty.parquet` | Clean set + planted post-outcome leaks | Parquet | 40,000 × 38 | Leakage detection lab |
| `tamweel_vintages.parquet` | Same applications tagged by month | Parquet | 40,000 × 36 | Time-series CV & hold-out |
| `feature_dictionary.csv` | Column, description, `available_at_application` flag | CSV | 38 rows | Leak-hunt reference |

### Demo Requirements
- **Instructor demo:** take the 0.93 champion, run the audit, remove the leak, show 0.79 — in under 6 minutes; the drop *is* the lesson.
- **Student demo:** one pair presents their random-CV vs time-CV comparison and explains which number they would report to a committee.
- **Expected outputs:** zero leaked features, honest CV AUC with fold std, documented encoding-safety check.

---

# Module 3 — Imbalanced and Cost-Sensitive Learning

## Module Overview

**Purpose.** Real-world classification is rarely balanced: defaults, fraud, churn, disease, meter tampering — the interesting class is the rare one. This module dismantles the reflex to "just SMOTE it" and replaces it with a decision-theoretic frame: imbalance is a *threshold and cost* problem far more than a *resampling* problem. Participants learn class weighting inside the boosting objective, the true role (and risks) of resampling, why the default 0.5 threshold is almost always wrong, and how to choose an operating point from a business cost matrix denominated in real Saudi Riyals.

**Business relevance.** For a Saudi lender, a missed default (false negative) costs the outstanding balance minus recovery — often tens of thousands of SAR — while a wrongly-declined good customer (false positive) costs foregone margin and goodwill. These costs are wildly asymmetric, and the default classifier threshold assumes they are equal. The money in an imbalanced problem is made not in the last 0.005 of AUC but in choosing the threshold that minimises expected cost. This is the module where data science visibly becomes decision science.

**Industry use cases.**
- Consumer-finance default (Tamweel): ≈7% positive, asymmetric SAR costs, regulator watching the false-decline rate for fairness.
- Payment fraud: <1% positive, per-transaction cost matrix, hard latency budget.
- Predictive maintenance: rare failures where a missed failure dwarfs an unnecessary inspection.

**Expected competencies.** After this module a participant can apply `scale_pos_weight`/class weights, evaluate PR-AUC and cost curves instead of accuracy, run threshold-moving against a cost matrix, judge when resampling helps versus harms, and articulate the operating point as a business decision.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 3.1 | Explain why accuracy and a 0.5 threshold mislead on imbalanced data | LO3, LO6 |
| 3.2 | Apply class weighting / `scale_pos_weight` in gradient boosting | LO1, LO3 |
| 3.3 | Judge when resampling (SMOTE, undersampling) helps versus harms | LO3 |
| 3.4 | Choose an operating threshold from a business cost matrix | LO3, LO6 |
| 3.5 | Evaluate imbalanced models with PR-AUC, recall@budget, and expected cost | LO6 |

## Technical Content

### 1. Why the default recipe fails on rare classes

On a 7%-positive problem, a model that predicts "never default" scores 93% accuracy and is worthless. Accuracy, and the implicit 0.5 threshold behind `predict()`, both assume balanced classes and symmetric costs — neither holds. Two consequences: (1) **use ranking metrics** that focus on the positive class — **PR-AUC / average precision** is far more informative than ROC-AUC when positives are rare, because ROC-AUC is unmoved by the huge true-negative mass; (2) **stop calling `predict()`** — call `predict_proba()` and choose the threshold yourself. Almost every "the model doesn't catch fraud/defaults" complaint is really "nobody moved the threshold off 0.5."

### 2. Cost-sensitivity is the real problem

Frame it decision-theoretically. With a cost matrix:

| | Predicted good | Predicted default |
|---|---|---|
| **Actually good** | 0 (TN) | C_FP = lost margin (~SAR 400) |
| **Actually default** | C_FN = exposure − recovery (~SAR 18,000) | 0 (TP, declined) |

The expected cost at threshold `t` is `Σ [FP(t)·C_FP + FN(t)·C_FN]`. The optimal threshold is where the marginal cost of one more decline equals its marginal benefit — for a hugely asymmetric matrix this can be as low as 0.05–0.15, nowhere near 0.5. Everything else in the module serves this calculation. The Bayes-optimal threshold for a *well-calibrated* probability is `t* = C_FP / (C_FP + C_FN)` — which is exactly why Module 5's calibration matters: a threshold on an uncalibrated score is a threshold on a number that isn't a probability.

### 3. Class weighting — the boosting-native fix

Before reaching for resampling, use the objective. Both libraries reweight the positive class inside the loss:

- **LightGBM:** `class_weight="balanced"` or `scale_pos_weight = n_neg/n_pos`; also `is_unbalance=True`.
- **XGBoost:** `scale_pos_weight = n_neg/n_pos`.

This tells the gradient to care more about positives *without duplicating rows or fabricating neighbours*, so it does not distort the feature distribution and cannot leak across folds. It shifts the score distribution (and therefore where you set the threshold) but preserves ranking. **Teach the ordering:** try class weights first; reach for resampling only if weights are insufficient and you understand the risks.

### 4. Resampling — overrated, occasionally useful, always risky

- **Random undersampling** the majority is cheap and fast, sometimes competitive, but throws away data (and information).
- **Random oversampling** duplicates minority rows — combined with a GBDT this mostly just re-weights and risks overfitting exact copies.
- **SMOTE / ADASYN** synthesise interpolated minority points. They can help linear models on genuinely sparse minority regions, but on tabular GBDTs they frequently *underperform* class weighting, distort calibration (Module 5), and create three hazards: they invent points in categorical/mixed feature space that are not real applicants; they can bridge across the decision boundary; and if run before splitting they leak (Module 2). **Iron rule:** resample **inside the training fold only**, never before CV, never touching validation.

Honest guidance to give the room: on modern GBDTs, `scale_pos_weight` + threshold-moving beats SMOTE the large majority of the time. Resampling is a tool, not a ritual.

### 5. Threshold moving and operating-point selection

The deliverable of this module is a chosen threshold with a business justification. The procedure:

1. Get honest out-of-fold predicted probabilities (from the Module 2 harness).
2. Sweep thresholds; at each, compute the confusion matrix and total expected cost from the SAR matrix.
3. Pick `t*` = argmin expected cost. Report the confusion matrix, recall, precision, and the SAR cost there.
4. Add operational overlays: a **capacity constraint** (the manual-review team can only handle N cases/day → recall@budget), and a **fairness guardrail** (false-decline rate parity across segments — previews governance).

Present the result as an **expected-cost-vs-threshold curve** — a single figure a risk committee can read and sign.

### 6. Common mistakes & production considerations

1. **Optimising accuracy or F1 blindly** — F1 assumes equal FP/FN weight; your costs are not equal. Optimise *expected cost*.
2. **SMOTE before the split** — reintroduces the Module-2 leak with near-duplicates.
3. **Thresholding an uncalibrated score** — the Bayes threshold formula only holds for calibrated probabilities (Module 5 fixes this).
4. **A single global threshold** when segments have different base rates or costs — sometimes segment-specific thresholds are warranted (but watch fairness/legal constraints).
5. **Reporting the threshold's performance on the data used to pick it** — choose the threshold on validation OOF predictions, confirm it on the hold-out.
6. **Production drift of the base rate** — the default rate moves with the economy; the cost-optimal threshold moves with it. Re-derive on a schedule and monitor the realised cost, not just AUC.

## Code Examples

### Class weighting and the metrics that matter

```python
# src/tamweel/imbalance/weighted_model.py
"""Boosting-native class weighting + imbalance-appropriate metrics.
scale_pos_weight shifts the objective, not the data distribution."""
import numpy as np
import lightgbm as lgb
from sklearn.metrics import average_precision_score, roc_auc_score

def train_weighted(X_tr, y_tr, X_val, y_val) -> lgb.LGBMClassifier:
    n_pos = int(y_tr.sum()); n_neg = int(len(y_tr) - n_pos)
    spw = n_neg / n_pos                      # ~12.5 for a 7.4% positive rate
    model = lgb.LGBMClassifier(
        objective="binary", learning_rate=0.03, n_estimators=3000,
        num_leaves=41, min_child_samples=120,
        scale_pos_weight=spw,                # care more about the rare class
        random_state=42, n_jobs=-1, verbose=-1)
    model.fit(X_tr, y_tr, eval_set=[(X_val, y_val)],
              eval_metric="average_precision",
              callbacks=[lgb.early_stopping(200, verbose=False)])
    p = model.predict_proba(X_val)[:, 1]
    print(f"scale_pos_weight={spw:.1f}  "
          f"ROC-AUC={roc_auc_score(y_val, p):.4f}  "
          f"PR-AUC={average_precision_score(y_val, p):.4f}")
    return model
```

### Cost-matrix threshold optimisation

```python
# src/tamweel/imbalance/cost_threshold.py
"""Choose the operating point that minimises expected SAR cost.
Uses honest OOF probabilities from the Module 2 CV harness."""
import numpy as np
import pandas as pd

# Business cost matrix (SAR), signed off by Risk:
C_FP = 400.0        # decline a good customer -> lost margin + goodwill
C_FN = 18_000.0     # approve a defaulter    -> exposure minus recovery

def expected_cost_curve(y_true, proba, review_capacity=None):
    thresholds = np.linspace(0.01, 0.60, 120)
    rows = []
    for t in thresholds:
        pred = (proba >= t).astype(int)
        fp = int(((pred == 1) & (y_true == 0)).sum())
        fn = int(((pred == 0) & (y_true == 1)).sum())
        tp = int(((pred == 1) & (y_true == 1)).sum())
        flagged = int(pred.sum())
        cost = fp * C_FP + fn * C_FN
        recall = tp / max(int(y_true.sum()), 1)
        precision = tp / max(flagged, 1)
        feasible = review_capacity is None or flagged <= review_capacity
        rows.append(dict(threshold=t, cost_sar=cost, recall=recall,
                         precision=precision, flagged=flagged,
                         feasible=feasible))
    df = pd.DataFrame(rows)
    best = df[df.feasible].sort_values("cost_sar").iloc[0]
    print(f"optimal t*={best.threshold:.3f}  cost=SAR {best.cost_sar:,.0f}  "
          f"recall={best.recall:.2%}  precision={best.precision:.2%}  "
          f"flagged={int(best.flagged)}")
    return df, best
```

### SMOTE done correctly — inside the training fold only

```python
# src/tamweel/imbalance/resample_pipeline.py
"""If you must resample, it goes INSIDE the CV pipeline so validation
folds are never touched. imblearn's Pipeline enforces fit-time-only."""
from imblearn.over_sampling import SMOTENC
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.model_selection import cross_val_score, StratifiedGroupKFold
from lightgbm import LGBMClassifier

def build_resampled_pipeline(categorical_idx):
    return ImbPipeline([
        # SMOTENC handles mixed categorical+numeric; applied to TRAIN fold only
        ("smote", SMOTENC(categorical_features=categorical_idx,
                          sampling_strategy=0.3, random_state=42)),
        ("clf", LGBMClassifier(learning_rate=0.03, n_estimators=800,
                              num_leaves=41, random_state=42, verbose=-1)),
    ])

def compare_to_weighting(X, y, groups, categorical_idx):
    pipe = build_resampled_pipeline(categorical_idx)
    cv = StratifiedGroupKFold(n_splits=5)
    ap = cross_val_score(pipe, X, y, groups=groups, cv=cv,
                         scoring="average_precision")
    print(f"SMOTE-in-fold PR-AUC: {ap.mean():.4f} "
          f"(compare against class-weighting; often lower on GBDTs)")
    return ap.mean()
```

## Hands-on Lab 3 — Cost-Optimal Decisions

| | |
|---|---|
| **Objective** | Add class weighting to the Tamweel model, evaluate with PR-AUC, sweep thresholds against the SAR cost matrix, choose the operating point, and prove SMOTE does not beat weighting here |
| **Duration** | 50 minutes |
| **Setup** | Lab 2 harness, `git checkout lab3-start`, `pip install imbalanced-learn`; cost matrix in `configs/cost_matrix.yaml` |

**Instructions & tasks**
1. *(5 min)* Compute the imbalance ratio and set `scale_pos_weight`. Train the weighted model; record ROC-AUC and PR-AUC. Compare PR-AUC to the unweighted Module-1 model.
2. *(10 min)* Generate honest OOF probabilities via the Module 2 harness (provided helper). Never threshold on data the model trained on.
3. *(15 min)* Run `expected_cost_curve` with `C_FP=400`, `C_FN=18000`; find `t*`; record the SAR cost, recall, precision, and number flagged at `t*` vs at the naive 0.5.
4. *(10 min)* Add the review-capacity constraint (`review_capacity=600`); re-find the feasible optimum; discuss the recall you sacrifice to fit the team's throughput.
5. *(5 min)* Run `compare_to_weighting` (SMOTE-in-fold) and record its PR-AUC vs the weighted model. Note which wins.
6. *(5 min)* Write `DECISION.md`: the chosen threshold, its SAR cost, and one sentence justifying it to Risk. Commit.

**Expected output**
```
scale_pos_weight=12.5  ROC-AUC=0.7901  PR-AUC=0.3402   # PR-AUC up vs 0.31
optimal t*=0.086  cost=SAR 2,412,000  recall=71.4%  precision=18.9%  flagged=812
  vs naive t=0.5: cost=SAR 5,980,000  recall=22.1%   (money left on the table)
with review_capacity=600: t*=0.121  cost=SAR 2,740,000  recall=63.0%  flagged=598
SMOTE-in-fold PR-AUC: 0.3288   (class-weighting wins: 0.3402)
```

**Acceptance criteria:** cost-optimal threshold chosen from OOF predictions; SAR cost at `t*` strictly below the cost at 0.5; SMOTE-vs-weighting comparison reported; `DECISION.md` states the operating point in business terms.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `t*` at the extreme edge of the sweep | Cost ratio extreme / sweep range too narrow | Widen/refine `np.linspace`; confirm cost values |
| SMOTE beats weighting by a lot | Applied before split (leak) or wrong metric | Confirm `ImbPipeline` + in-fold; compare PR-AUC not accuracy |
| Cost curve is flat | Probabilities poorly spread (uncalibrated) | Preview Module 5; still pick argmin, but note calibration need |
| `SMOTENC` errors on category dtype | Needs integer-coded categorical indices | Pass positional `categorical_features` indices, not names |

**Instructor notes.** The single most memorable number of Day 2 is the SAR gap between `t*` and 0.5 — write both on the board. The point lands hardest when a participant realises the default classifier was quietly costing millions. Fast finishers: derive `t* = C_FP/(C_FP+C_FN)` analytically, compare to the swept optimum, and explain the (calibration-driven) discrepancy — a clean bridge to Module 5.

## Mini Exercises

**Quiz (5 questions)**
1. Why prefer PR-AUC over ROC-AUC at 1% positives? → ROC-AUC is dominated by the true-negative mass; PR focuses on the rare positive.
2. `scale_pos_weight` for a 4% positive rate? → ≈ 24 (n_neg/n_pos = 96/4).
3. Where must SMOTE run relative to the CV split? → strictly inside the training fold.
4. The analytic Bayes threshold for C_FP=400, C_FN=18000? → 400/18400 ≈ 0.0217 (valid only if calibrated).
5. True/False: F1 is the right objective for asymmetric business costs. → **False** (F1 weights FP and FN equally; optimise expected cost).

**Coding exercise.** Extend `expected_cost_curve` to add a segment-specific cost (e.g. SME loans have higher exposure) and compute a per-segment optimal threshold; discuss the fairness implications of segment thresholds.

**Debugging exercise.** A participant reports 99% recall at `t*=0.01` and calls it a win. Show why (precision ~7%, everyone flagged) and connect it to the review-capacity constraint.

**Discussion questions.**
- Risk asks for "the threshold that catches 90% of defaults." What do you need to tell them about the cost and workload of that choice?
- When would segment-specific thresholds be indefensible even if they lower total cost?

## Case Study — The 0.5 Threshold That Cost a Lender Millions

**Scenario.** A Saudi "buy-now-pay-later" provider deployed a strong default model (AUC 0.80) but wired it to `predict()` — the implicit 0.5 threshold. It flagged only the most extreme 2% of applicants, catching 22% of defaults. Losses stayed high; the team blamed the model.

**Business context.** With C_FN ≈ 20× C_FP, the cost-optimal threshold was near 0.09, not 0.5. The model was fine; the *decision* was the defect. Moving the threshold lifted default capture from 22% to ~70% and cut realised loss by roughly 40% — with zero change to the model.

**Technical challenge.** Retrofit threshold optimisation and an operating-point governance process without retraining, and size the manual-review team to the chosen recall.

**Constraints.** The manual-review team can process ~600 cases/day; a fairness review requires false-decline parity across regions; the operating point must be re-derivable as the portfolio's base rate shifts.

**Solution approach (facilitate, don't lecture).** (1) Compute honest OOF probabilities; (2) build the expected-cost curve, choose `t*` under the capacity constraint; (3) check false-decline parity across regions and adjust; (4) institute a monthly re-derivation tied to the realised base rate; (5) monitor realised SAR cost, not just AUC.

**Discussion questions.**
1. How much of the improvement came from the model versus the threshold? What does that say about where effort should go?
2. How do capacity and fairness constraints reshape the "pure" cost-optimal point?
3. What monitoring signals that `t*` needs re-derivation?
4. Who owns the threshold — data science, risk, or operations — and what does that imply for change control?

## Benchmarks and Evaluation

| Metric | Category | Target after M3 | How measured |
|---|---|---|---|
| PR-AUC (weighted model) | Performance | ≥ 0.33, > unweighted | `average_precision_score` on OOF |
| Expected SAR cost at `t*` | Business impact | < cost at t=0.5 by a large margin | cost curve |
| Recall at `t*` | Business impact | reported with precision | confusion matrix at `t*` |
| Recall @ review capacity | Operability | reported under the 600/day cap | feasible-optimum row |
| SMOTE vs weighting | Method choice | weighting ≥ SMOTE (documented) | in-fold comparison |
| False-decline parity across segments | Fairness | reported; gap within tolerance | per-segment FP rate |

**Example benchmark table (filled during lab):**

| Operating point | Threshold | Recall | Precision | Flagged | Cost (SAR) |
|---|---|---|---|---|---|
| Naive `predict()` | 0.500 | 22.1% | 46% | 178 | 5,980,000 |
| Cost-optimal | 0.086 | 71.4% | 18.9% | 812 | 2,412,000 |
| Capacity-constrained | 0.121 | 63.0% | 21% | 598 | 2,740,000 |

## Required Visuals and Training Assets

### Diagrams
1. **Cost matrix and the asymmetry** — *Purpose:* anchor the decision frame. *Elements:* 2×2 matrix with SAR values, C_FN dwarfing C_FP visually. *Style:* flat vector, English with Arabic subtitles.
2. **Expected-cost-vs-threshold curve** — *Purpose:* the committee-ready figure. *Elements:* U-shaped cost curve, `t*` marked, 0.5 marked far up the right arm, capacity line overlaid. *Style:* annotated line chart.
3. **ROC vs PR under imbalance** — *Purpose:* justify PR-AUC. *Elements:* the same model's flattering ROC and sobering PR curve side by side at 7% positives. *Style:* two-panel.
4. **Resampling in the pipeline** — *Purpose:* show the in-fold rule. *Elements:* CV fold with SMOTE applied only to the train block, validation block untouched and highlighted. *Style:* fold diagram.

### Images (screenshots)
1. **Cost-curve terminal output**: *why:* expected-output reference; *content:* the `t*` line with SAR cost and recall.
2. **Confusion matrices at 0.5 vs `t*`**: *why:* makes the trade-off concrete; *content:* two heatmaps side by side.
3. **PR curves: weighted vs unweighted**: *why:* shows weighting's effect; *content:* two precision-recall curves with AP annotated.

### Simulations
1. **Cost-ratio slider** — *Setup:* a notebook slider on C_FN/C_FP; `t*` slides live along the cost curve. *Learning objective:* the optimal threshold is a business input, not a model property.
2. **SMOTE-before-split leak** — *Setup:* branch that resamples before CV; PR-AUC inflates then collapses on the hold-out. *Learning objective:* resampling leakage is real and quiet.

### Interactive Activities
- **Set-the-threshold role play (15 min):** groups take Risk, Operations, and Fairness roles and negotiate the operating point from the cost curve; each must cite a number.
- **Metric-matching (10 min):** eight scenarios; pick accuracy / F1 / PR-AUC / expected cost and justify — most answers are "expected cost."

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `cost_matrix.yaml` | Risk-signed SAR costs (C_FP, C_FN, per-segment) | YAML | small | Threshold optimisation |
| `tamweel_oof_proba.parquet` | Honest OOF probabilities from M2 harness | Parquet | 40,000 rows | Threshold sweeping without leakage |
| `segment_map.csv` | Application → region/product segment | CSV | 40,000 rows | Fairness parity checks |

### Demo Requirements
- **Instructor demo:** build the cost curve live, drag the threshold, show the SAR gap between 0.5 and `t*` in under 6 minutes.
- **Student demo:** one group presents its negotiated operating point and defends it to a mock risk committee.
- **Expected outputs:** cost-optimal threshold chosen from OOF, SAR cost documented, SMOTE-vs-weighting comparison recorded.

---

# Module 4 — Model Interpretability: SHAP and Beyond

## Module Overview

**Purpose.** A gradient-boosted model that no one can explain is unshippable in Saudi banking. This module turns the Tamweel model from a black box into an auditable decision system. Participants learn the difference between *global* explanation (what drives the model overall) and *local* explanation (why this applicant was declined), master permutation importance and SHAP (TreeSHAP specifically), read beeswarm, dependence, and waterfall plots fluently, and — most consequentially — turn a local SHAP explanation into a compliant **adverse-action reason code** that a customer and a regulator both accept.

**Business relevance.** SAMA's model-risk governance and consumer-protection rules require that a declined applicant be given the principal reasons for the decision. "The gradient boosting said no" is not a reason. TreeSHAP gives an additive, per-applicant attribution that sums exactly to the score, which is precisely the property a reason-code engine needs. Interpretability is also the fastest leak detector in practice: the feature that dominates a SHAP beeswarm is often the leak that Module 2's audit missed. This module is where the model earns the committee's trust.

**Industry use cases.**
- Credit decisions (Tamweel): reason codes for adverse-action letters; feature-level fairness review.
- Fraud: analyst-facing local explanations so a human can adjudicate a flagged transaction.
- Clinical risk scores: clinician trust depends on local explanations that agree with domain knowledge.

**Expected competencies.** After this module a participant can compute and interpret permutation importance and TreeSHAP values, distinguish correlation-driven artefacts from genuine effects, read every standard SHAP plot, generate ranked local reason codes, and write a plain-language interpretability section for a model-risk committee.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 4.1 | Distinguish global vs local interpretability and choose the right tool for a question | LO4 |
| 4.2 | Compute and correctly interpret permutation importance, including its correlation caveats | LO4, LO6 |
| 4.3 | Explain the additive game-theoretic basis of SHAP and why TreeSHAP is exact and fast | LO4 |
| 4.4 | Read beeswarm, dependence, waterfall, and force plots and extract the right conclusion | LO4 |
| 4.5 | Convert local SHAP values into ranked, compliant adverse-action reason codes | LO4, LO6 |

## Technical Content

### 1. Global vs local — two different questions

"What does the model rely on?" is a **global** question; "Why was applicant #48213 declined?" is a **local** one. They need different tools and confusing them is the most common interpretability mistake. Global tools (gain importance, permutation importance, SHAP summary/beeswarm) describe average behaviour across the population; local tools (a single SHAP explanation, a force/waterfall plot) decompose one prediction. A model can have `bureau_score` as its top global driver yet decline a specific applicant primarily because of `dti` — both statements are true and non-contradictory. Teach participants to always state which question they are answering before they pick a plot.

### 2. Why split/gain importance lies, and permutation importance

Recall Module 1's warning: LightGBM's built-in `feature_importances_` (split or gain) is biased toward high-cardinality and continuous features, because they simply offer more places to split. It is fine for a rough triage and terrible for a committee slide. **Permutation importance** is model-agnostic and honest about *predictive* value: shuffle one feature's column, measure how much the validation metric drops, repeat. A feature whose permutation drops PR-AUC by 0.04 genuinely carries that much signal. Its one trap: with **correlated features**, permuting one lets the model recover the information from its correlated twin, so both look unimportant (the effect is shared, not absent). Always compute permutation importance on **held-out** data, never training data, and report it with its standard deviation across repeats.

### 3. SHAP: additive attributions with a fairness guarantee

SHAP (SHapley Additive exPlanations) borrows the Shapley value from cooperative game theory: distribute the "payout" (the prediction minus a baseline) among the "players" (the features) so that the attribution is *fair* in a precise axiomatic sense — efficiency (attributions sum to the prediction), symmetry, dummy, and additivity. The core equation participants should internalise:

```
f(x) = φ_0 + Σ_j φ_j        # baseline expected value + each feature's contribution
```

`φ_0` is the average model output over the background data (the base rate in log-odds space for Tamweel); each `φ_j` is how much feature `j` pushed this particular prediction above or below that baseline. Because the φ's *sum exactly to the score*, SHAP is the natural engine for reason codes: the most positive φ's are literally the reasons the applicant scored as risky.

### 4. TreeSHAP — exact and fast for GBDTs

General Shapley values are exponential to compute (all feature subsets). **TreeSHAP** exploits tree structure to compute exact SHAP values for tree ensembles in polynomial time — which is why SHAP is practical on XGBoost/LightGBM at Tamweel scale. Two things to flag in class: (a) use `shap.TreeExplainer` (not the slow `KernelExplainer`) for GBDTs; (b) understand the `feature_perturbation` choice — `"tree_path_dependent"` needs no background data and respects the tree's own handling of correlations, while `"interventional"` uses a background set and gives cleaner causal-flavoured attributions but costs more. For Tamweel we use interventional SHAP with a 1,000-row background sample for the committee report, and path-dependent for fast in-lab iteration. TreeSHAP also yields **interaction values** (`shap_interaction_values`) that split each φ into main and pairwise-interaction effects — useful for spotting, e.g., a `dti × tenor_months` interaction.

### 5. Reading the plots without fooling yourself

- **Beeswarm (summary):** one row per feature (ranked by mean |φ|), one dot per applicant, coloured by feature value. Reveals direction *and* spread: high `dti` (red) sitting on the positive-SHAP side means high debt-to-income raises risk. This is the single most information-dense interpretability plot.
- **Dependence plot:** φ for one feature vs that feature's value, coloured by an interacting feature — shows non-linearities and interactions the beeswarm compresses.
- **Waterfall / force:** a single applicant's φ's stacked from `φ_0` to `f(x)` — the exact picture behind a reason code.
- **Trap:** SHAP explains **the model, not the world.** A large φ on a leaked feature explains the model's (wrong) reliance on it — SHAP will faithfully explain a leak. High SHAP importance is not evidence of a causal effect; say "the model uses X," never "X causes default."

### 6. Common mistakes & production considerations

1. **Reporting gain importance to a regulator** — use permutation importance and SHAP; gain is high-cardinality-biased.
2. **KernelExplainer on a GBDT** — needlessly slow and approximate; TreeSHAP is exact.
3. **Reading SHAP causally** — it attributes the model's behaviour, not real-world causation.
4. **Explaining on training data** — global explanations must be computed on held-out rows to reflect generalisation.
5. **Baseline confusion** — SHAP values are relative to `φ_0` (the background expectation); changing the background changes every φ. Fix and document the background set.
6. **Production cost & drift** — computing interventional SHAP per request adds latency; cache background, precompute for batch, and monitor whether the top global drivers shift over time (a drift signal that foreshadows Module 5 stability and SDA-DSC-212).

## Code Examples

### Permutation importance on held-out data

```python
# src/tamweel/interpret/permutation.py
"""Honest, model-agnostic importance on the VALIDATION set.
Contrast this with LightGBM's biased split/gain importance."""
from __future__ import annotations
import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.metrics import average_precision_score, make_scorer

def permutation_report(model, X_val, y_val, n_repeats: int = 10) -> pd.DataFrame:
    scorer = make_scorer(average_precision_score, needs_proba=True)
    r = permutation_importance(
        model, X_val, y_val, scoring=scorer,
        n_repeats=n_repeats, random_state=42, n_jobs=-1)
    out = (pd.DataFrame({
        "feature": X_val.columns,
        "pr_auc_drop": r.importances_mean,
        "std": r.importances_std,
    }).sort_values("pr_auc_drop", ascending=False).reset_index(drop=True))
    print(out.head(12).to_string(index=False))
    return out
```

### TreeSHAP: global beeswarm and per-applicant reason codes

```python
# src/tamweel/interpret/shap_explain.py
"""Exact SHAP for the Tamweel LightGBM model via TreeExplainer.
Global beeswarm for the committee; local waterfall + reason codes
for the adverse-action letter."""
from __future__ import annotations
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt

def build_explainer(model, X_background: pd.DataFrame) -> shap.TreeExplainer:
    # interventional attributions against a fixed 1k-row background
    bg = X_background.sample(1000, random_state=42)
    return shap.TreeExplainer(
        model, data=bg, feature_perturbation="interventional",
        model_output="probability")

def global_beeswarm(explainer, X_sample: pd.DataFrame, out_png: str) -> None:
    sv = explainer(X_sample)                 # SHAP Explanation object
    shap.plots.beeswarm(sv, max_display=15, show=False)
    plt.tight_layout(); plt.savefig(out_png, dpi=150); plt.close()

def reason_codes(explainer, x_row: pd.DataFrame, top_k: int = 4) -> list[str]:
    """Turn one applicant's positive SHAP contributions into ranked,
    plain-language adverse-action reasons. φ's sum to the score exactly."""
    sv = explainer(x_row)
    phi = pd.Series(sv.values[0], index=x_row.columns)
    drivers = phi[phi > 0].sort_values(ascending=False).head(top_k)
    templates = {
        "dti": "Debt-to-income ratio is high relative to approved applicants",
        "bureau_score": "Credit bureau score is below the typical approved range",
        "amount_sar": "Requested financing amount is high for the stated income",
        "tenor_months": "Requested tenor lengthens exposure beyond comfort",
        "months_employed": "Employment tenure is short",
        "num_recent_inquiries": "Several recent credit inquiries indicate stacking",
    }
    return [templates.get(f, f"{f} contributed to the risk score")
            for f in drivers.index]

def additivity_check(explainer, x_row: pd.DataFrame, model) -> None:
    sv = explainer(x_row)
    recon = sv.base_values[0] + sv.values[0].sum()
    actual = model.predict_proba(x_row)[0, 1]
    assert abs(recon - actual) < 1e-3, "SHAP must sum to the prediction"
    print(f"phi_0={sv.base_values[0]:.4f}  sum(phi)={sv.values[0].sum():+.4f}  "
          f"-> {recon:.4f} (model={actual:.4f}) OK")
```

### SHAP as a leak detector

```python
# src/tamweel/interpret/shap_leak_hunt.py
"""If one feature dominates mean|SHAP| far above the rest, suspect a leak
Module 2's audit missed. Interpretability is a debugging tool."""
import numpy as np
import shap

def dominant_feature_scan(explainer, X_sample, ratio: float = 3.0):
    sv = explainer(X_sample)
    mean_abs = np.abs(sv.values).mean(axis=0)
    order = mean_abs.argsort()[::-1]
    top, second = mean_abs[order[0]], mean_abs[order[1]]
    name = X_sample.columns[order[0]]
    if top > ratio * second:
        print(f"[WARN] '{name}' dominates SHAP ({top:.3f} vs {second:.3f}); "
              f"verify it is available at application time (leak suspect).")
    return name, top / max(second, 1e-9)
```

## Hands-on Lab 4 — The Interpretability Report

| | |
|---|---|
| **Objective** | Produce a committee-ready interpretability report for the Tamweel model: permutation importance, a global SHAP beeswarm, three local explanations with reason codes, and a SHAP-driven leak check |
| **Duration** | 50 minutes (spills into the Day-2 interpretation clinic) |
| **Setup** | Lab 3 model, `git checkout lab4-start`, `pip install shap matplotlib`; provided `study.pkl` model and `X_background` sample |

**Instructions & tasks**
1. *(5 min)* Load the tuned, class-weighted model from Lab 3. Compute `permutation_report` on the validation set; contrast the top 5 with LightGBM's `feature_importances_` (note the high-cardinality bias).
2. *(10 min)* Build the `TreeExplainer` (interventional, 1k background). Run `additivity_check` on one row to prove φ's sum to the score.
3. *(10 min)* Generate the global beeswarm (`global_beeswarm`). Write two sentences: the top three drivers and their directions.
4. *(10 min)* Pick three applicants (one clear approve, one clear decline, one borderline). For each, produce a waterfall plot and `reason_codes(...)`. Confirm the reasons match the waterfall.
5. *(5 min)* Run `dominant_feature_scan`. If it warns, trace the feature back to the feature dictionary — is it a leak? (One planted subtle leak is present in the `lab4-start` feature view.)
6. *(10 min)* Assemble `INTERPRETABILITY_REPORT.md`: beeswarm image, the three reason-code sets, the permutation table, and one paragraph a risk committee could read. Commit.

**Expected output**
```
$ python -m tamweel.interpret.permutation
feature              pr_auc_drop     std
bureau_score            0.0421     0.0033
dti                     0.0288     0.0026
num_recent_inquiries    0.0173     0.0019
amount_sar              0.0121     0.0015
...
phi_0=0.0740  sum(phi)=+0.2114  -> 0.2854 (model=0.2854) OK
[WARN] 'utilisation_next_month' dominates SHAP (0.191 vs 0.052); verify ... (leak suspect)
reason codes (applicant 48213, declined):
  1. Credit bureau score is below the typical approved range
  2. Debt-to-income ratio is high relative to approved applicants
  3. Several recent credit inquiries indicate stacking
```

**Acceptance criteria:** additivity check passes; global beeswarm saved; three local reason-code sets produced and consistent with their waterfalls; the SHAP-flagged leak identified and removed, with the honest AUC re-reported.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| `shap` import/JIT error with recent NumPy | Version skew (the classic SHAP break) | Pin `shap`/`numpy` per `requirements.txt`; restart kernel |
| Beeswarm empty or all-grey | Passed raw array, not the `Explanation` object | Call `explainer(X)` (callable API), not the legacy `.shap_values` |
| Additivity check fails | `model_output` mismatch (log-odds vs probability) | Keep `model_output="probability"` consistent with the check |
| SHAP extremely slow | Used `KernelExplainer` | Switch to `TreeExplainer`; sample background to 1k |

**Instructor notes.** The highest-value moment is task 5: SHAP visibly *catches a leak the Module-2 audit missed* because the leak is a legitimate-looking engineered feature (`utilisation_next_month`) rather than an obvious post-outcome column. Let the room feel that interpretability is not decoration — it is debugging. Fast finishers: compute `shap_interaction_values` and find the strongest pairwise interaction (usually `dti × amount_sar`), then confirm it in a dependence plot.

## Mini Exercises

**Quiz (5 questions)**
1. Which importance type is safe to show a regulator? → permutation importance or SHAP (not gain/split).
2. What does the SHAP efficiency axiom guarantee? → the φ's plus the baseline sum exactly to the prediction.
3. Why TreeSHAP over KernelSHAP for LightGBM? → exact and polynomial-time on trees vs slow approximation.
4. A leaked feature has the largest mean |SHAP|. What does that tell you? → the model relies heavily on it — SHAP faithfully explains the leak; investigate availability at application time.
5. True/False: a large positive SHAP value for `dti` proves high debt-to-income *causes* default. → **False** (explains the model, not causation).

**Coding exercise.** Write `top_reason_coverage(explainer, X, k=3)` that reports, across all declined applicants, how often the same feature appears in the top-k reasons — a monitoring metric for reason-code stability.

**Debugging exercise.** Two applicants have identical scores (0.31) but completely different reason codes. Explain how that is possible and why it is desirable, using the additivity property.

**Discussion questions.**
- A committee asks "can we remove the top feature to be safe?" What do you tell them about the difference between removing a *leak* and removing a *legitimate strong predictor*?
- When is a global beeswarm misleading, and when must you fall back to dependence plots?

## Case Study — The Reason Code That Failed a SAMA Review

**Scenario.** A Riyadh lender's default model passed performance review but failed its consumer-protection audit: declined applicants received the reason "low model score," which SAMA rejected as non-specific. The team had never built local explanations.

**Business context.** Regulation requires *principal reasons* a customer can act on. Without per-applicant attribution the lender faced a remediation order and a freeze on new declines pending fix — a direct revenue impact.

**Technical challenge.** Retrofit TreeSHAP reason codes onto an already-deployed model, map raw feature contributions to human-readable, non-discriminatory reason templates, and prove the codes are faithful (sum to the score) and stable across similar applicants.

**Constraints.** Reason templates must avoid protected attributes and proxies; the explanation must be reproducible and auditable; latency budget allows only cached/batch SHAP, not per-request KernelSHAP.

**Solution approach (facilitate, don't lecture).** (1) Add a `TreeExplainer` with a fixed, documented background set; (2) build the reason-template map and a review to strip proxy features; (3) prove additivity per decision as the audit trail; (4) precompute SHAP in the batch scoring job to meet latency; (5) add reason-code stability monitoring.

**Discussion questions.**
1. Why is "low model score" both true and unacceptable as a reason?
2. How do you keep reason templates free of protected-attribute proxies without gutting the model?
3. What audit artefact proves a reason code is faithful to the actual decision?
4. Who signs off on the reason-template wording — data science, legal, or compliance?

## Benchmarks and Evaluation

| Metric | Category | Target after M4 | How measured |
|---|---|---|---|
| SHAP additivity error | Correctness | < 1e-3 per row | `additivity_check` |
| Permutation importance computed on held-out | Rigour | yes (not training data) | code review |
| Global beeswarm produced | Deliverable | yes, top-15 features | saved PNG |
| Local reason codes per decision | Deliverable | 3–5 ranked, plain-language | report |
| SHAP-flagged leak resolved | Integrity | 0 dominant leak features | `dominant_feature_scan` |
| Reason-code stability (top-3 coverage) | Monitoring | reported | `top_reason_coverage` |

**Example benchmark table (filled during lab):**

| Interpretability artefact | Result | Note |
|---|---|---|
| Top global driver (permutation) | `bureau_score` (−0.042 PR-AUC) | matches domain expectation |
| Top gain-importance feature | `employer_id` (high cardinality) | biased — do not report |
| SHAP leak flagged | `utilisation_next_month` | removed; AUC 0.79 → honest |
| Additivity error (worst row) | 4e-4 | within tolerance |

## Required Visuals and Training Assets

### Diagrams
1. **Global vs local map** — *Purpose:* fix the two-questions distinction. *Elements:* left panel a beeswarm (population), right panel a waterfall (one applicant), with the guiding question over each. *Style:* two-panel, English with Arabic subtitles.
2. **SHAP additivity ladder** — *Purpose:* make `f(x)=φ_0+Σφ_j` tangible. *Elements:* a waterfall from baseline to score with each φ labelled and the running sum. *Style:* annotated waterfall.
3. **Permutation vs gain importance** — *Purpose:* show the high-cardinality bias. *Elements:* side-by-side bar charts where gain ranks `employer_id` top and permutation ranks `bureau_score` top. *Style:* paired bar chart.
4. **Reason-code pipeline** — *Purpose:* the compliance flow. *Elements:* model → TreeSHAP φ's → positive-φ ranking → template map → adverse-action letter. *Style:* left-to-right flow.

### Images (screenshots)
1. **Beeswarm summary plot**: *why:* the anchor global figure; *content:* 15 features, coloured dots, direction visible.
2. **Waterfall for a declined applicant**: *why:* the exact picture behind a reason code; *content:* φ_0 to f(x) with top contributors labelled.
3. **Permutation-importance terminal output**: *why:* expected-output reference; *content:* the ranked PR-AUC-drop table.

### Simulations
1. **Explain-the-decision** — *Setup:* a notebook where participants change one feature of an applicant and watch its φ and the reason codes update live. *Learning objective:* local attribution is per-applicant and responsive.
2. **Leak-under-the-beeswarm** — *Setup:* toggle a planted engineered leak in/out; the beeswarm's top row appears/disappears. *Learning objective:* SHAP is a leak detector.

### Interactive Activities
- **Reason-code writing clinic (15 min):** pairs receive three waterfall plots and draft compliant, non-proxy reason codes; the room critiques wording.
- **Beeswarm read-off (10 min):** show a beeswarm with feature names hidden; pairs infer which feature and direction from the colour/position pattern.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `X_background_1k.parquet` | 1,000-row background sample for interventional SHAP | Parquet | 1,000 rows | Stable SHAP baseline |
| `reason_templates.yaml` | Feature → compliant reason-code text (legal-reviewed) | YAML | ~40 entries | Adverse-action letters |
| `tamweel_train_engineered.parquet` | Clean set + engineered features incl. one subtle leak | Parquet | 40,000 × 42 | SHAP leak-hunt lab |

### Demo Requirements
- **Instructor demo:** from tuned model to a full local waterfall + reason codes in under 7 minutes, narrating each φ.
- **Student demo:** one pair presents the beeswarm and explains the top three drivers to a mock committee.
- **Expected outputs:** additivity verified, beeswarm saved, three reason-code sets, SHAP-flagged leak removed.

---

# Module 5 — Calibration and Uncertainty Estimates

## Module Overview

**Purpose.** A gradient-boosted "probability" of 0.30 does not mean 30% of such applicants default — boosted scores are excellent *rankings* but poor *probabilities*. This module fixes that. Participants learn why boosting (and especially class-weighting from Module 3) distorts probabilities, how to read a reliability diagram, how to calibrate with Platt scaling and isotonic regression, how to measure calibration with the Expected Calibration Error (ECE) and Brier score, and how to attach honest **uncertainty** to predictions using prediction intervals and conformal methods. Calibration is what makes the Module-3 cost threshold valid and the Module-4 reason codes trustworthy — it is the connective tissue of the whole course.

**Business relevance.** For a Saudi lender, a calibrated probability *is money*: expected loss = P(default) × exposure at risk. If the 0.30 score is really 0.45, the lender under-provisions and mis-prices; SAMA's IFRS-9 expected-credit-loss reporting depends on probabilities that mean what they say. The Bayes-optimal cost threshold from Module 3 (`t* = C_FP/(C_FP+C_FN)`) is only valid on calibrated probabilities. And a model that says "0.30 ± 0.02" versus "0.30 ± 0.25" is telling risk two very different things about how much to trust a single decision.

**Industry use cases.**
- Credit pricing and provisioning (Tamweel): scores become expected-loss SAR, feeding pricing and IFRS-9.
- Insurance: premium = calibrated claim probability × severity; miscalibration is a direct P&L leak.
- Medical triage: a "20% risk" must mean 20% for a clinician to act; conformal intervals bound the uncertainty.

**Expected competencies.** After this module a participant can diagnose miscalibration from a reliability diagram, choose and apply Platt vs isotonic calibration without leaking, compute ECE and Brier before/after, convert calibrated scores to expected-loss SAR, and produce distribution-free prediction sets with split conformal prediction.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 5.1 | Explain why boosted and class-weighted scores are miscalibrated | LO6 |
| 5.2 | Read a reliability diagram and quantify miscalibration with ECE and Brier score | LO6 |
| 5.3 | Apply Platt (sigmoid) and isotonic calibration without leakage | LO6 |
| 5.4 | Convert calibrated probabilities into expected-loss SAR and validate the cost threshold | LO3, LO6 |
| 5.5 | Attach distribution-free uncertainty with split conformal prediction | LO6 |

## Technical Content

### 1. Why boosted scores are not probabilities

Gradient boosting optimises log-loss but the *shrinkage*, early stopping, and especially **class-weighting / `scale_pos_weight`** from Module 3 shift the score distribution away from true frequencies. Class weighting deliberately inflates positive scores to make the rare class matter — a great idea for ranking and thresholding, but it means a raw score of 0.30 no longer corresponds to a 30% empirical default rate. Boosted models also tend to be **over-confident** near the extremes (pushing scores toward 0 and 1). The fix is a monotonic post-hoc mapping from raw score to calibrated probability, learned on held-out data — ranking (and therefore AUC) is preserved; only the *values* change.

### 2. The reliability diagram and how to read it

Bin predictions (e.g. deciles), and for each bin plot mean predicted probability (x) against observed frequency (y). Perfect calibration is the 45° line. **Below** the diagonal = over-confident (predicted higher than reality); **above** = under-confident. For Tamweel after class-weighting the curve typically sags below the diagonal in the mid-range — the model says 0.30 where reality is 0.20. Teach participants to always plot it with the bin counts (a histogram underneath), because a scary-looking deviation in a bin holding 12 applicants is noise, not miscalibration.

### 3. Measuring calibration: ECE, MCE, and the Brier score

- **Expected Calibration Error (ECE):** the count-weighted average gap between predicted and observed frequency across bins — a single number to track before/after.
- **Maximum Calibration Error (MCE):** the worst bin's gap — matters when a specific score band drives decisions.
- **Brier score:** mean squared error of the probability (`mean((p − y)²)`) — a *proper scoring rule* that decomposes into calibration + refinement, so it rewards both being right *and* being honest. Track ECE and Brier together: ECE for calibration specifically, Brier for overall probabilistic quality.

Warning to give the room: ECE is sensitive to the binning scheme; report the number of bins and prefer equal-frequency bins for imbalanced data.

### 4. Platt scaling vs isotonic regression

- **Platt (sigmoid) scaling:** fit a 1-parameter logistic mapping `σ(a·s + b)` from raw score `s` to probability. Low variance, works well with *little* calibration data, but assumes a sigmoidal distortion — can't fix arbitrary shapes.
- **Isotonic regression:** fit a free-form monotonic step function. More flexible, can correct any monotone distortion, but needs *more* data and can overfit small calibration sets (watch the tails).

Rule of thumb: isotonic when you have a few thousand+ calibration examples (Tamweel qualifies), Platt when calibration data is scarce. The non-negotiable rule: **calibrate on a held-out fold the model never trained on** (or use cross-fitting) — calibrating on training data is a leak that produces falsely perfect reliability diagrams. scikit-learn's `CalibratedClassifierCV` handles the cross-fitting for you.

### 5. From calibrated probability to expected loss (closing the Module-3 loop)

Once probabilities are honest, `expected_loss_sar = p_default × exposure_at_default × (1 − recovery_rate)`. This turns the classifier into a pricing and provisioning engine and *validates the Bayes threshold*: with calibrated `p`, the analytic optimum `t* = C_FP/(C_FP+C_FN)` from Module 3 should now match the empirically-swept optimum — the discrepancy that Lab 3's fast-finishers found was miscalibration all along. This is the module's punchline: calibration reconciles the theory and the sweep.

### 6. Uncertainty: prediction intervals and conformal prediction

A point probability hides how *sure* the model is. **Split conformal prediction** gives a distribution-free guarantee: reserve a calibration set, compute nonconformity scores, and produce prediction sets that contain the truth with probability ≥ 1−α, with no distributional assumptions. For Tamweel's binary decision this yields, per applicant, a set like {approve}, {decline}, or the *ambiguous* {approve, decline} that should be routed to a human. The size of the ambiguous region is an honest, guaranteed measure of where the model should not act alone. Production note: recompute the conformal quantile as the population drifts, and monitor realised coverage.

## Code Examples

### Reliability diagram, ECE, and Brier

```python
# src/tamweel/calibrate/metrics.py
"""Diagnose calibration: reliability curve + ECE + Brier.
Run on a held-out fold the model never saw."""
from __future__ import annotations
import numpy as np
from sklearn.metrics import brier_score_loss
from sklearn.calibration import calibration_curve

def expected_calibration_error(y_true, proba, n_bins: int = 10) -> float:
    # equal-frequency bins are fairer under imbalance
    edges = np.quantile(proba, np.linspace(0, 1, n_bins + 1))
    edges[0], edges[-1] = 0.0, 1.0
    ece, n = 0.0, len(proba)
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (proba > lo) & (proba <= hi)
        if m.sum() == 0:
            continue
        conf, acc = proba[m].mean(), y_true[m].mean()
        ece += (m.sum() / n) * abs(conf - acc)
    return float(ece)

def calibration_report(y_true, proba, n_bins: int = 10) -> dict:
    frac_pos, mean_pred = calibration_curve(
        y_true, proba, n_bins=n_bins, strategy="quantile")
    out = {
        "ece": expected_calibration_error(y_true, proba, n_bins),
        "brier": brier_score_loss(y_true, proba),
        "curve": list(zip(mean_pred.round(4), frac_pos.round(4))),
    }
    print(f"ECE={out['ece']:.4f}  Brier={out['brier']:.4f}")
    return out
```

### Calibrating without leakage (isotonic, cross-fitted)

```python
# src/tamweel/calibrate/calibrate.py
"""Post-hoc calibration that preserves ranking. CalibratedClassifierCV
cross-fits so calibration never sees the data the base model trained on."""
from sklearn.calibration import CalibratedClassifierCV
from sklearn.frozen import FrozenEstimator     # sklearn >= 1.6
import lightgbm as lgb

def calibrate_model(base_model, X_cal, y_cal, method: str = "isotonic"):
    """base_model is ALREADY fit on the training fold. We wrap and fit
    ONLY the calibrator on a separate held-out calibration fold."""
    calibrated = CalibratedClassifierCV(
        FrozenEstimator(base_model),   # freeze: do not refit the booster
        method=method, cv="prefit" if False else 5)
    calibrated.fit(X_cal, y_cal)
    return calibrated

def compare_calibration(base, calibrated, X_test, y_test):
    from tamweel.calibrate.metrics import calibration_report
    print("before:"); r0 = calibration_report(y_test,
          base.predict_proba(X_test)[:, 1])
    print("after :"); r1 = calibration_report(y_test,
          calibrated.predict_proba(X_test)[:, 1])
    print(f"ECE {r0['ece']:.4f} -> {r1['ece']:.4f}   "
          f"Brier {r0['brier']:.4f} -> {r1['brier']:.4f}")
```

### Calibrated scores to expected-loss SAR + split conformal sets

```python
# src/tamweel/calibrate/expected_loss.py
"""Turn calibrated probabilities into money and honest uncertainty."""
import numpy as np
import pandas as pd

def expected_loss_sar(p_default, exposure_sar, recovery_rate=0.35):
    return p_default * exposure_sar * (1.0 - recovery_rate)

def split_conformal_sets(cal_proba, cal_y, test_proba, alpha=0.1):
    """Distribution-free prediction sets at coverage >= 1 - alpha.
    Nonconformity = 1 - prob assigned to the true label."""
    p1 = cal_proba
    nonconf = np.where(cal_y == 1, 1 - p1, p1)          # score for true label
    qhat = np.quantile(nonconf, np.ceil((len(cal_y)+1)*(1-alpha))/len(cal_y))
    sets = []
    for p in test_proba:
        s = set()
        if (1 - p) <= qhat: s.add(1)      # include "default"
        if p <= qhat:       s.add(0)      # include "good"
        sets.append(s or {int(p >= 0.5)}) # never empty
    ambiguous = np.mean([len(s) == 2 for s in sets])
    print(f"qhat={qhat:.3f}  ambiguous(route-to-human)={ambiguous:.1%}")
    return sets
```

## Hands-on Lab 5 — Calibrate for Expected Loss

| | |
|---|---|
| **Objective** | Diagnose the Tamweel model's miscalibration, fix it with isotonic calibration without leakage, prove ECE/Brier improve, convert scores to expected-loss SAR, and confirm the Bayes threshold now matches the swept optimum |
| **Duration** | 50 minutes |
| **Setup** | Lab 3 weighted model, `git checkout lab5-start`; separate `X_cal/y_cal` calibration fold and `X_test/y_test` hold-out provided |

**Instructions & tasks**
1. *(5 min)* Run `calibration_report` on the raw (class-weighted) model's hold-out scores. Record ECE and Brier; plot the reliability diagram — note the mid-range sag.
2. *(10 min)* Calibrate with `method="isotonic"` on the calibration fold. Re-run `compare_calibration`; record ECE/Brier before→after.
3. *(5 min)* Confirm ranking is preserved: ROC-AUC before ≈ after (calibration must not change AUC).
4. *(10 min)* Convert calibrated probabilities to `expected_loss_sar` using each applicant's exposure; report portfolio expected loss before/after calibration and note the provisioning error you removed.
5. *(10 min)* Re-derive the Bayes threshold `t* = C_FP/(C_FP+C_FN)` on the *calibrated* scores; compare to Lab 3's swept optimum — they should now agree closely. Explain the earlier gap.
6. *(10 min)* Run `split_conformal_sets` at α=0.1; report the ambiguous fraction routed to human review. Write `CALIBRATION.md`; commit.

**Expected output**
```
before:  ECE=0.0912  Brier=0.0631
after :  ECE=0.0180  Brier=0.0571
ECE 0.0912 -> 0.0180   Brier 0.0631 -> 0.0571
AUC check: 0.7901 -> 0.7899   (ranking preserved)
portfolio expected loss: SAR 41.7M (raw) -> SAR 33.9M (calibrated)  # over-provisioned before
Bayes t* (calibrated) = 0.0217 ; swept optimum (recomputed) = 0.023  -> now agree
qhat=0.214  ambiguous(route-to-human)=8.4%
```

**Acceptance criteria:** ECE reduced by a clear margin; AUC unchanged within ±0.002 (no ranking damage); expected-loss SAR reported before/after; the Bayes-vs-swept threshold reconciliation demonstrated; conformal ambiguous fraction reported.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Calibration makes ECE *worse* | Calibrated on training data (leak) or too-small isotonic set | Use a separate calibration fold; switch to Platt if data scarce |
| AUC changes after calibration | Non-monotonic mapping or refit the base model | Ensure `FrozenEstimator`/`cv="prefit"`; isotonic/Platt are monotone |
| Reliability curve wildly jagged | Too many bins for the data | Fewer, equal-frequency bins; show bin counts |
| Bayes t* still disagrees | Residual miscalibration in the decision band | Check ECE in that specific band (MCE); recalibrate |

**Instructor notes.** The reconciliation in task 5 is the intellectual peak of Day 3 — the Module-3 fast-finishers' "why don't the analytic and swept thresholds match?" is answered here: they didn't match *because the scores weren't probabilities*. Draw the before/after reliability diagrams on the board. Fast finishers: compare isotonic vs Platt on a deliberately small calibration fold (500 rows) and watch isotonic overfit the tails.

## Mini Exercises

**Quiz (5 questions)**
1. Does calibration change a model's AUC? → No — it is a monotonic transform; ranking is preserved.
2. Over-confident predictions sit where relative to the reliability diagonal? → below it.
3. Isotonic vs Platt with only 400 calibration rows — which? → Platt (fewer parameters, less overfit).
4. Why is the Brier score called a *proper* scoring rule? → it is minimised by reporting true probabilities (rewards honesty + accuracy).
5. True/False: you may calibrate on the same data the model trained on. → **False** (leak; falsely perfect reliability).

**Coding exercise.** Extend `calibration_report` to also return MCE (max bin gap) and flag the single worst-calibrated score band.

**Debugging exercise.** After calibration, ECE dropped but the Day-2 cost at `t*` went *up*. Give two plausible causes (threshold recomputed on old scores; conformal/segment mismatch) and the check for each.

**Discussion questions.**
- IFRS-9 provisioning uses your probabilities directly. What is the business cost of a 0.09 ECE?
- When would you route an applicant to a human even though the point probability is confidently low?

## Case Study — The Over-Provisioned Portfolio

**Scenario.** A Saudi lender's risk team noticed loan-loss provisions consistently exceeded realised losses by ~20%, tying up capital. The model ranked well (AUC 0.79) but its probabilities were taken at face value for IFRS-9 without a calibration step.

**Business context.** Class-weighting (added to catch more defaults) had inflated probabilities; provisions computed from raw scores over-reserved by hundreds of millions of SAR, a real cost of capital even though no loan decision was "wrong."

**Technical challenge.** Insert a leak-free calibration layer, prove provisions align to realised losses, and preserve the ranking that the approval decision relies on.

**Constraints.** IFRS-9 requires documented, back-tested probability estimates; the calibration must be re-fittable as vintages roll; auditors will back-test predicted vs realised default rates by band.

**Solution approach (facilitate, don't lecture).** (1) Diagnose with a reliability diagram — clear mid-range over-confidence; (2) isotonic-calibrate on a held-out vintage; (3) show ECE 0.09 → 0.02 and provisions realigning; (4) confirm AUC unchanged so approvals are unaffected; (5) institute quarterly recalibration with a back-test report.

**Discussion questions.**
1. How can a model be well-ranked yet cost the business through miscalibration?
2. Why does class-weighting specifically create this problem?
3. What back-test would satisfy an IFRS-9 auditor?
4. How often should calibration be refreshed, and what signals trigger it?

## Benchmarks and Evaluation

| Metric | Category | Target after M5 | How measured |
|---|---|---|---|
| ECE (after calibration) | Calibration | ≤ 0.03 | `expected_calibration_error` |
| Brier score | Probabilistic quality | improved vs raw | `brier_score_loss` |
| AUC change from calibration | Ranking safety | within ±0.002 | before/after AUC |
| Bayes t* vs swept optimum | Consistency | agree within ±0.01 | recomputed on calibrated scores |
| Portfolio expected-loss error | Business impact | provisions align to realised | expected-loss vs actuals |
| Conformal coverage (α=0.1) | Uncertainty | realised ≥ 0.90 | held-out coverage check |

**Example benchmark table (filled during lab):**

| Stage | ECE | Brier | AUC | Notes |
|---|---|---|---|---|
| Raw (class-weighted) | 0.091 | 0.0631 | 0.7901 | over-confident mid-range |
| Platt-calibrated | 0.031 | 0.0588 | 0.7900 | good with less data |
| Isotonic-calibrated | 0.018 | 0.0571 | 0.7899 | best here (ample data) |

## Required Visuals and Training Assets

### Diagrams
1. **Anatomy of a reliability diagram** — *Purpose:* teach the read. *Elements:* the 45° line, an over-confident curve below it, bin-count histogram beneath, over/under-confident regions labelled. *Style:* annotated line chart, English with Arabic subtitles.
2. **Platt vs isotonic** — *Purpose:* choose the right method. *Elements:* the same raw scores mapped by a smooth sigmoid vs a monotone step function. *Style:* two-panel mapping.
3. **Score → probability → SAR** — *Purpose:* connect to money. *Elements:* raw score → calibrated p → expected-loss SAR pipeline with a worked applicant. *Style:* left-to-right flow.
4. **Conformal prediction sets** — *Purpose:* visualise guaranteed uncertainty. *Elements:* applicants sorted by p with {approve}/{decline}/{ambiguous} bands and the qhat cut. *Style:* banded strip.

### Images (screenshots)
1. **Before/after reliability diagrams**: *why:* the calibration payoff; *content:* sagging curve straightening to the diagonal.
2. **ECE/Brier terminal output**: *why:* expected-output reference; *content:* the before→after line.
3. **Expected-loss table**: *why:* business framing; *content:* portfolio provision before vs after.

### Simulations
1. **Miscalibration dial** — *Setup:* slider on `scale_pos_weight`; the reliability curve sags further as weighting increases. *Learning objective:* class-weighting trades calibration for recall.
2. **Isotonic-overfit** — *Setup:* shrink the calibration set; isotonic tails wobble while Platt stays smooth. *Learning objective:* method choice depends on data volume.

### Interactive Activities
- **Guess-the-frequency (10 min):** show applicants scored 0.30; pairs bet on the observed default rate before the reliability bin is revealed.
- **Route-or-decide (10 min):** given conformal sets, pairs decide which applicants a human must see and justify the coverage guarantee.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tamweel_cal_fold.parquet` | Held-out calibration vintage | Parquet | 8,000 rows | Leak-free calibration |
| `exposure_recovery.csv` | Per-applicant exposure and recovery-rate assumptions | CSV | 40,000 rows | Expected-loss SAR |
| `realised_losses.csv` | Actual outcomes for the back-test | CSV | 12,000 rows | IFRS-9 back-test |

### Demo Requirements
- **Instructor demo:** raw → calibrated reliability diagram plus the Bayes-vs-swept reconciliation in under 8 minutes.
- **Student demo:** one pair presents before/after ECE and explains the provisioning impact.
- **Expected outputs:** ECE ≤ 0.03, AUC unchanged, expected-loss realigned, conformal coverage reported.

---

# Module 6 — Ensembling and Stacking Strategies

## Module Overview

**Purpose.** A single well-tuned LightGBM is a strong model; the last honest increment of performance usually comes from combining *diverse* models so their errors cancel. This module teaches ensembling as an engineering discipline, not a Kaggle party trick: the bias/variance intuition behind bagging, boosting, and blending; why **diversity** matters more than individual strength; how to build a **leak-free out-of-fold (OOF) stack**; and — crucially — when ensembling helps versus when it just adds latency, cost, and opacity for 0.002 AUC. Participants build a stacked ensemble of LightGBM + XGBoost + a linear model on the Tamweel golden thread and decide, with evidence, whether it earns its place in production.

**Business relevance.** In Saudi banking and telecom, a 0.5-point AUC gain on a large book can be worth millions in avoided loss — but only if it survives production and passes model-risk review. A stacked ensemble that adds 0.004 AUC while tripling inference latency, doubling the SHAP-explanation cost, and complicating governance is often a *net negative*. This module trains the judgement to tell a worthwhile ensemble from a vanity one, and to keep the whole thing calibratable (Module 5) and explainable (Module 4).

**Industry use cases.**
- Credit default (Tamweel): a GBDT + linear stack where the linear model adds a monotone, auditable component.
- Fraud: heterogeneous models (trees + a rules model + an anomaly score) blended for coverage of different fraud types.
- Demand forecasting: ensembles across model families to hedge regime uncertainty (previews SDA-DSC-212).

**Expected competencies.** After this module a participant can build bagged and blended ensembles, construct a correct OOF stack whose meta-features never leak, measure ensemble diversity, decide whether an ensemble is worth its cost, and keep the final ensemble calibrated and explainable.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 6.1 | Contrast bagging, boosting, blending, and stacking and their bias/variance effects | LO5 |
| 6.2 | Explain why ensemble *diversity* drives gains and how to measure it | LO5, LO6 |
| 6.3 | Build a leak-free out-of-fold stack with a meta-learner | LO2, LO5 |
| 6.4 | Decide when ensembling is worth its latency, cost, and governance overhead | LO5, LO6 |
| 6.5 | Keep the final ensemble calibrated and explainable end-to-end | LO4, LO6 |

## Technical Content

### 1. The ensemble family and what each does to bias/variance

- **Bagging** (bootstrap aggregating, e.g. Random Forest, or GBDTs on bootstraps): trains models on resampled data and averages — primarily **reduces variance**. Boosting already reduces bias within itself.
- **Boosting** (our GBDTs): sequential bias reduction; a single GBDT is itself an ensemble of trees.
- **Blending / simple averaging:** average the probabilities of several finished models — cheap, robust, no meta-model to overfit. Weighted averaging is a one-line upgrade.
- **Stacking:** train a **meta-learner** on the base models' out-of-fold predictions, letting it learn *how* to combine them (and when to trust each). Most powerful, most dangerous (leakage), most complex.

The mental model to leave the room with: bagging fights variance, boosting fights bias, stacking fights *systematic combination error* — and each layer adds risk and cost that must be justified.

### 2. Diversity beats strength

Averaging two identical models gains nothing; averaging two models that are individually weaker but **make different mistakes** can beat both. The theory: ensemble error falls as the base models' errors *decorrelate*. Practical sources of diversity: different **algorithm families** (trees vs linear vs kNN), different **feature subsets**, different **preprocessing** (target-encoded vs one-hot), different **seeds/hyperparameters**. Measure it: the **correlation of the models' out-of-fold errors** (or of their probability outputs). Two models correlated at 0.99 will not help each other; at 0.85 they might. Teach participants to *look at the error correlation before stacking* — it predicts whether stacking can possibly help.

### 3. Out-of-fold stacking done correctly (the leakage trap returns)

Stacking's fatal error is training the meta-learner on base predictions that saw their own training rows — a Module-2 leak wearing a fancy hat. The correct recipe:

1. Split into K folds. For each base model, for each fold, train on the other K−1 folds and predict the held-out fold → assemble a full column of **out-of-fold predictions** (each row predicted by a model that never saw it).
2. Stack these OOF columns as meta-features; train the meta-learner on them.
3. For inference, retrain each base model on *all* the data and feed their predictions to the frozen meta-learner.

The meta-learner should be **simple** (logistic regression is the default) — a complex meta-learner over-fits the base predictions. sklearn's `StackingClassifier` implements this cross-fitting; understanding the manual version is what lets participants trust (or debug) it.

### 4. Choosing and constraining the meta-learner

Logistic regression as meta-learner is interpretable (its coefficients tell you how much each base model is trusted) and rarely overfits. Constrain it further when governance demands: **non-negative weights** (a base model can't get a negative vote) turn stacking into learned weighted averaging — often just as strong and far easier to defend. Avoid GBDT meta-learners unless you have abundant data; they overfit the handful of base-prediction features. Always report the learned weights — "0.55 LightGBM, 0.30 XGBoost, 0.15 linear" is a governable statement.

### 5. When ensembling is *not* worth it

The honest cost/benefit checklist to teach:

- **Latency & cost:** N models = N× inference and N× the SHAP-explanation cost; a real-time scorer may not afford it.
- **Marginal gain:** if the OOF AUC lift is within the fold-to-fold noise band (Module 2's std), it is not real — do not ship it.
- **Governance & explainability:** each added model is another artefact to document, monitor, and calibrate; reason codes (Module 4) get harder.
- **Diversity absent:** if base models are near-duplicates, stacking cannot help — spend the effort on features instead.

For Tamweel the ensemble ships only if it beats the best single model by more than the fold std *and* remains calibratable and explainable. Sometimes the right professional answer is "the single LightGBM wins on total value" — and saying so is a mark of seniority.

### 6. Common mistakes & production considerations

1. **Leaky stacking** — meta-features from in-sample base predictions; use OOF strictly.
2. **Over-complex meta-learner** — a GBDT on three columns overfits; use (non-negative) logistic regression.
3. **Chasing noise** — a lift smaller than the CV std is not a lift.
4. **Ignoring calibration** — an averaged/stacked score is usually miscalibrated; recalibrate the *ensemble* (Module 5), not just the bases.
5. **Explainability debt** — plan how you will produce reason codes for an ensemble before you ship it (SHAP the final combined output, or the dominant base).
6. **Production parity & versioning** — every base model plus the meta-learner is a versioned artefact; a mismatched base at serving time silently corrupts the meta-features. Pin and hash all of them.

## Code Examples

### Measure diversity before you stack

```python
# src/tamweel/ensemble/diversity.py
"""If base models' OOF probabilities are ~0.99 correlated, stacking
cannot help. Check first."""
import numpy as np
import pandas as pd

def oof_correlation(oof: dict[str, np.ndarray]) -> pd.DataFrame:
    """oof: {model_name: out-of-fold probability vector}."""
    df = pd.DataFrame(oof)
    corr = df.corr()
    print("OOF probability correlation:\n", corr.round(3))
    print("\n-> pairs below ~0.95 offer real diversity")
    return corr
```

### A correct out-of-fold stack, from scratch and with sklearn

```python
# src/tamweel/ensemble/stack.py
"""Leak-free OOF stacking. Base models: LightGBM + XGBoost + linear.
Meta-learner: non-negative logistic regression."""
from __future__ import annotations
import numpy as np
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score
import lightgbm as lgb
import xgboost as xgb

def make_bases():
    return {
        "lgbm": lambda: lgb.LGBMClassifier(
            learning_rate=0.03, n_estimators=600, num_leaves=41,
            random_state=42, verbose=-1),
        "xgb": lambda: xgb.XGBClassifier(
            tree_method="hist", learning_rate=0.03, n_estimators=600,
            max_depth=6, random_state=7, verbosity=0),
        "linear": lambda: LogisticRegression(max_iter=2000, C=1.0),
    }

def build_oof(X, y, groups):
    """Returns OOF meta-features (n_rows x n_models). Each prediction is
    made by a base model that never saw that row."""
    cv = StratifiedGroupKFold(n_splits=5)
    bases = make_bases()
    oof = {name: np.zeros(len(y)) for name in bases}
    for tr, va in cv.split(X, y, groups):
        for name, ctor in bases.items():
            m = ctor()
            m.fit(X.iloc[tr], y.iloc[tr])
            oof[name][va] = m.predict_proba(X.iloc[va])[:, 1]
    for name, p in oof.items():
        print(f"{name:7s} OOF AUC={roc_auc_score(y, p):.4f}")
    return oof

def fit_meta(oof, y):
    Z = np.column_stack(list(oof.values()))
    meta = LogisticRegression(positive=True, max_iter=1000)  # non-negative weights
    meta.fit(Z, y)
    p = meta.predict_proba(Z)[:, 1]
    weights = dict(zip(oof.keys(), meta.coef_[0].round(3)))
    print(f"stack OOF AUC={roc_auc_score(y, p):.4f}  "
          f"PR-AUC={average_precision_score(y, p):.4f}  weights={weights}")
    return meta
```

### sklearn StackingClassifier + is-it-worth-it gate

```python
# src/tamweel/ensemble/worth_it.py
"""Ship the ensemble only if its lift exceeds the CV noise band."""
import numpy as np
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedGroupKFold

def stacking_estimator(bases):
    return StackingClassifier(
        estimators=list(bases.items()),
        final_estimator=LogisticRegression(positive=True, max_iter=1000),
        stack_method="predict_proba", cv=5, n_jobs=-1)

def worth_it(single_auc_mean, single_auc_std, ensemble_auc_mean) -> bool:
    lift = ensemble_auc_mean - single_auc_mean
    verdict = lift > single_auc_std          # lift must exceed fold noise
    print(f"single={single_auc_mean:.4f}±{single_auc_std:.4f}  "
          f"ensemble={ensemble_auc_mean:.4f}  lift={lift:+.4f}  "
          f"-> {'SHIP' if verdict else 'KEEP SINGLE MODEL'}")
    return verdict
```

## Hands-on Lab 6 — The Stacked Ensemble

| | |
|---|---|
| **Objective** | Build a leak-free OOF stack of LightGBM + XGBoost + linear on Tamweel, measure diversity, compare to the best single model against the fold-noise band, recalibrate the ensemble, and make a ship/no-ship decision with evidence |
| **Duration** | 50 minutes |
| **Setup** | Lab 5 calibrated model, `git checkout lab6-start`; the Module-2 group-aware CV harness is reused |

**Instructions & tasks**
1. *(5 min)* Build OOF predictions for the three bases with `build_oof` (group-aware folds from Module 2). Record each base's OOF AUC.
2. *(5 min)* Run `oof_correlation`. Identify the most diverse pair; predict whether stacking can help before you try it.
3. *(10 min)* Fit the non-negative logistic meta-learner (`fit_meta`); record the stack OOF AUC/PR-AUC and the learned weights.
4. *(10 min)* Run the `worth_it` gate: compare the stack's mean AUC to the best single model's mean ± fold std. Decide SHIP or KEEP SINGLE — and justify with the numbers.
5. *(10 min)* Recalibrate the *ensemble* output (Module 5 isotonic); confirm the stacked score's ECE is acceptable — an uncalibrated ensemble is not shippable.
6. *(10 min)* Write `ENSEMBLE_DECISION.md`: the diversity finding, the lift-vs-noise verdict, the learned weights, the calibrated ECE, and your ship decision. Commit.

**Expected output**
```
lgbm    OOF AUC=0.7912
xgb     OOF AUC=0.7889
linear  OOF AUC=0.7401
OOF probability correlation:
        lgbm    xgb    linear
lgbm    1.000  0.972   0.804
xgb     0.972  1.000   0.799
linear  0.804  0.799   1.000
stack OOF AUC=0.7951  PR-AUC=0.3461  weights={'lgbm': 0.61, 'xgb': 0.27, 'linear': 0.18}
single=0.7912±0.0090  ensemble=0.7951  lift=+0.0039  -> KEEP SINGLE MODEL
ensemble ECE after isotonic: 0.021
```

**Acceptance criteria:** OOF built without leakage (group-aware); diversity reported; stack AUC compared to the fold-noise band with an explicit ship/no-ship verdict; the ensemble recalibrated with ECE reported; decision documented with numbers, not vibes.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Stack AUC *below* best base | Meta-learner overfit or a weak/harmful base included | Use non-negative logistic; drop the harmful base; check OOF integrity |
| Suspiciously large lift (>0.02) | In-sample base predictions (leak) | Verify each OOF row was predicted out-of-fold; rebuild `build_oof` |
| Linear base drags the stack | Unscaled features for logistic regression | Standardise numerics in a pipeline for the linear base only |
| Ensemble miscalibrated | Averaging distorts probabilities | Recalibrate the *combined* output (Module 5), not just bases |

**Instructor notes.** This lab's teachable twist is that the honest verdict is often **KEEP SINGLE MODEL**: the lgbm/xgb pair is 0.97-correlated (little diversity), the linear model is weak, and the +0.004 lift is inside the ±0.009 fold noise. Reward the participants who *don't* ship the ensemble — mature judgement is the objective, not maximal complexity. Fast finishers: add a genuinely diverse base (a target-encoded kNN or a monotone-constrained GBDT) and re-test whether the lift now clears the noise band.

## Mini Exercises

**Quiz (5 questions)**
1. Which ensemble type mainly reduces variance? → bagging.
2. Two base models correlate at 0.99. Will stacking help? → almost certainly not (no diversity).
3. Why must stacking use out-of-fold base predictions? → in-sample predictions leak, inflating the meta-learner.
4. Preferred meta-learner and why? → (non-negative) logistic regression — interpretable, low overfit.
5. True/False: an ensemble's probabilities are automatically well-calibrated. → **False** (recalibrate the ensemble).

**Coding exercise.** Implement `weighted_average_search` that grid-searches convex weights over the three bases' OOF predictions to maximise PR-AUC, and compare to the learned meta-learner weights.

**Debugging exercise.** A participant's stack scores 0.84 OOF but 0.79 on the hold-out. Identify the most likely cause (OOF leak in the stacking construction) and the exact code check.

**Discussion questions.**
- Your ensemble adds 0.003 AUC and 40 ms latency per request. How do you decide? What else do you need to know?
- How would you produce a single adverse-action reason code for a three-model stack?

## Case Study — The Ensemble That Wasn't Worth It

**Scenario.** A telecom churn team proudly shipped a seven-model stacked ensemble that beat their single LightGBM by 0.006 AUC offline. Six months later, on-call fatigue and a governance review forced a reckoning: the ensemble was expensive to serve, impossible to explain to the retention team, and its offline lift had evaporated in production.

**Business context.** The 0.006 AUC never translated to measurable retention lift, while inference cost rose 7×, SHAP explanations became infeasible, and every base model was a separate monitoring and retraining burden. The "win" was a net loss.

**Technical challenge.** Quantify the true marginal value of the ensemble versus its single-model core, and decide what to keep.

**Constraints.** Real-time scoring with a tight latency budget; the retention team needs per-customer reasons; model-risk wants a minimal, governable footprint.

**Solution approach (facilitate, don't lecture).** (1) Re-measure the lift against fold-noise and against a *business* metric, not AUC; (2) check the ensemble base correlations — most were near-duplicates; (3) retire five bases, keep a two-model diverse blend only if it clears the noise band on the business metric; (4) recalibrate and re-enable explanations; (5) document the decision.

**Discussion questions.**
1. Why is offline AUC lift a poor sole justification for shipping an ensemble?
2. How do latency, explainability, and monitoring cost enter the decision?
3. What correlation among bases would have predicted the wasted effort up front?
4. When is "we kept the single model" the senior, correct answer?

## Benchmarks and Evaluation

| Metric | Category | Target after M6 | How measured |
|---|---|---|---|
| Base-model OOF AUCs | Diversity input | reported per model | `build_oof` |
| OOF error correlation | Diversity | reported; pairs identified | `oof_correlation` |
| Stack OOF AUC vs best single | Value | lift vs fold std, explicit verdict | `worth_it` gate |
| Stacking leakage | Integrity | none (OOF only) | code review / hold-out parity |
| Ensemble ECE (after recal) | Calibration | ≤ 0.03 | Module-5 metrics on ensemble |
| Ship/no-ship decision | Judgement | documented with numbers | `ENSEMBLE_DECISION.md` |

**Example benchmark table (filled during lab):**

| Model | OOF AUC | PR-AUC | Latency (rel.) | Verdict |
|---|---|---|---|---|
| Best single (LightGBM) | 0.7912 | 0.3402 | 1× | baseline |
| Simple average (3) | 0.7936 | 0.3438 | 3× | lift within noise |
| Non-neg logistic stack | 0.7951 | 0.3461 | 3× | +0.004 < fold std → keep single |

## Required Visuals and Training Assets

### Diagrams
1. **Ensemble family map** — *Purpose:* organise the zoo. *Elements:* bagging / boosting / blending / stacking, each with a mini schematic and its bias/variance effect. *Style:* four-quadrant, English with Arabic subtitles.
2. **OOF stacking flow** — *Purpose:* prevent the leak. *Elements:* K-fold construction of out-of-fold meta-features feeding the meta-learner, with the retrain-on-all step for inference. *Style:* fold-by-fold flow.
3. **Diversity vs gain** — *Purpose:* the core intuition. *Elements:* two error-correlation scatters (0.99 vs 0.85) with the resulting ensemble gain. *Style:* paired scatter.
4. **Worth-it decision gate** — *Purpose:* the judgement tool. *Elements:* lift vs fold-noise band with SHIP/KEEP-SINGLE branches and cost/explainability annotations. *Style:* decision diagram.

### Images (screenshots)
1. **OOF correlation matrix**: *why:* diversity made numeric; *content:* the 3×3 correlation heatmap.
2. **Stack weights + AUC terminal output**: *why:* expected-output reference; *content:* the learned weights and lift-vs-noise verdict.
3. **Calibrated ensemble reliability diagram**: *why:* ensembles need recalibration; *content:* before/after on the stacked score.

### Simulations
1. **Diversity dial** — *Setup:* interpolate a second base from a copy of the first toward a genuinely different model; watch the stack gain appear as correlation drops. *Learning objective:* diversity, not strength, unlocks stacking.
2. **Meta-learner complexity** — *Setup:* swap the meta-learner from logistic to a deep GBDT; watch OOF-vs-holdout gap explode. *Learning objective:* keep the meta-learner simple.

### Interactive Activities
- **Ship-or-not debate (15 min):** given a lift, latency, and explainability profile, two teams argue ship vs keep-single; class votes with reasons.
- **Build-a-diverse-base (10 min):** pairs propose a base model maximally different from LightGBM and predict its correlation before it is run.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tamweel_oof_matrix.parquet` | Precomputed OOF predictions for the three bases | Parquet | 40,000 × 4 | Stacking without waiting for base training |
| `base_model_registry.yaml` | Base model configs + version hashes | YAML | small | Reproducible, versioned ensemble |
| `latency_profile.csv` | Measured per-model inference latency | CSV | small | Worth-it cost analysis |

### Demo Requirements
- **Instructor demo:** build the OOF stack, show the correlation matrix, run the worth-it gate, and reach a ship/no-ship verdict in under 8 minutes.
- **Student demo:** one pair presents their diversity finding and defends their ship decision with numbers.
- **Expected outputs:** leak-free OOF stack, diversity reported, lift-vs-noise verdict, ensemble recalibrated, decision documented.

---

# Module 7 — Applied Modelling Challenge

## Module Overview

**Purpose.** Modules 1–6 built the skills; Module 7 forges them into a single, defensible deliverable under time pressure — the shape of work a specialist data scientist actually ships. Participants receive a fresh modelling brief on the Tamweel golden thread, plan and run experiments against a **private leaderboard scored on business cost (SAR), not raw AUC**, and by the end own a documented, calibrated, explainable model plus a model card they defend to a panel. This is the integrative capstone-in-miniature that de-risks the full SDA-DSC-390 Data Science Capstone: everything here — honest validation, cost thresholds, SHAP, calibration, ensembling judgement — is exercised together against a held-out ledger they never see.

**Business relevance.** Real modelling never happens one technique at a time. The challenge mirrors a genuine Saudi lending scenario: a new product line, a shifted population, a fixed manual-review capacity, a fairness constraint, and a risk committee that will sign or reject. Winning is defined the way the business defines it — minimum expected SAR loss under operational and fairness constraints — which forces participants to spend effort where value is, exactly the judgement the whole course cultivates.

**Industry use cases.**
- Model bake-offs / internal leaderboards for a new credit product (this challenge).
- Vendor-model evaluation: scoring a purchased model on your own held-out ledger and cost metric.
- Regulatory model submission: the model card + validation + fairness pack is the submission format.

**Expected competencies.** After this module a participant can scope a modelling problem end-to-end, run disciplined experiments under time and compute budgets, select an operating point under real constraints, assemble a model card, and defend validation, calibration, cost, and fairness choices to a non-technical panel.

## Learning Objectives (mapped)

| # | Objective | Maps to |
|---|---|---|
| 7.1 | Plan and prioritise experiments under time, compute, and data budgets | LO1, LO5 |
| 7.2 | Integrate validation, imbalance, interpretability, calibration, and ensembling into one pipeline | LO2, LO3, LO4, LO5, LO6 |
| 7.3 | Select an operating point under capacity and fairness constraints | LO3, LO6 |
| 7.4 | Assemble a model card that documents performance, calibration, explanations, and limits | LO4, LO6 |
| 7.5 | Defend modelling and validation decisions to a mixed technical/business panel | LO6 |

## Technical Content

### 1. Reading the brief and defining "win"

The first hour is not coding — it is comprehension. The brief specifies the target (`default_90dpd` on a new "Tamweel Youth" salary-advance product), the **business cost metric** (expected SAR loss under the signed cost matrix), the **operational constraint** (review capacity), and the **fairness guardrail** (false-decline parity across regions). Participants must restate the objective in one sentence and identify the *binding* constraint before touching a model. The most common failure is optimising AUC when the leaderboard scores SAR — teach them to build the scoring function *first* and score every experiment with it.

### 2. Experiment planning under a budget

With ~2.5 hours of build time, effort allocation is the skill. A sound plan: (a) reproduce a strong single-model baseline fast (Module 1 + the Module 2 harness), (b) get honest OOF predictions once and reuse them, (c) invest in features and the cost threshold (Module 3) — usually the highest-value hour, (d) calibrate (Module 5) so the threshold is valid, (e) only then consider an ensemble (Module 6) *if* the noise-band gate says it helps. A written experiment log with a hypothesis per run prevents flailing. The anti-pattern is 200 Optuna trials for 0.002 AUC while the threshold and calibration go untouched.

### 3. Feature engineering on the golden thread

The last real gains usually come from features, not hyperparameters: ratios (`dti`, `amount_to_income`), recency (`num_recent_inquiries`, `months_since_last_default` — verified application-time-only), stability (income volatility), and safe target-encodings of `employer_id`/`merchant_category` *inside* the CV pipeline. Every new feature must pass the Module-2 leak audit before it is trusted — the leaderboard punishes leaks brutally because the held-out ledger is a genuinely future vintage.

### 4. Assembling the integrated pipeline

The challenge model is a single pipeline that chains everything: leak-audited features → group/time CV → class-weighted GBDT → cost-threshold selection under capacity → isotonic calibration → optional recalibrated ensemble → SHAP reason codes. Each stage has an owner test (audit passes, ECE ≤ 0.03, threshold feasible, fairness gap within tolerance). Participants should be able to run the whole thing with one command and regenerate the submission deterministically under a fixed seed.

### 5. The model card and the defence

The deliverable is not just a score — it is a **model card**: intended use and out-of-scope use, training data and vintages, validation methodology, performance (AUC/PR-AUC + business SAR cost at the chosen operating point), calibration (ECE, reliability diagram), top SHAP drivers and sample reason codes, fairness analysis (false-decline parity by region), known limitations, and monitoring plan. The panel defence tests whether the participant can explain *why the honest 0.79 model with the right threshold beats a leaky 0.93*, and can answer a risk officer's "what breaks this model?" This is the professional artefact SDA-DSC-390 will demand at full scale.

### 6. Common mistakes & production considerations

1. **Optimising the wrong metric** — score every experiment on SAR cost, not AUC, from the first hour.
2. **Leak on a new feature** — a shiny feature that wins CV and dies on the ledger; audit every one.
3. **Thresholding uncalibrated scores** — calibrate before you finalise the operating point.
4. **Shipping an unjustified ensemble** — the noise-band gate governs; simpler defends better.
5. **No model card** — an undocumented model fails the panel regardless of score.
6. **Non-reproducible submission** — unseeded runs that can't be regenerated; fix and log every seed, hash the artefacts.

## Code Examples

### The leaderboard scorer (build this first)

```python
# src/tamweel/challenge/score.py
"""The ONLY metric that counts: expected SAR loss on the held-out ledger,
under the review-capacity constraint. Score every experiment with this."""
from __future__ import annotations
import numpy as np
import pandas as pd

C_FP, C_FN = 400.0, 18_000.0

def business_cost(y_true, proba, threshold, review_capacity=None) -> dict:
    pred = (proba >= threshold).astype(int)
    if review_capacity is not None and pred.sum() > review_capacity:
        # keep only the highest-risk within capacity
        cutoff = np.sort(proba)[::-1][review_capacity - 1]
        pred = (proba >= cutoff).astype(int)
    fp = int(((pred == 1) & (y_true == 0)).sum())
    fn = int(((pred == 0) & (y_true == 1)).sum())
    tp = int(((pred == 1) & (y_true == 1)).sum())
    cost = fp * C_FP + fn * C_FN
    return {"cost_sar": cost, "flagged": int(pred.sum()),
            "recall": tp / max(int(y_true.sum()), 1),
            "fp": fp, "fn": fn}

def leaderboard_entry(name, y_true, proba, threshold, capacity) -> pd.Series:
    r = business_cost(y_true, proba, threshold, capacity)
    print(f"{name:24s} cost=SAR {r['cost_sar']:>12,.0f}  "
          f"recall={r['recall']:.1%}  flagged={r['flagged']}")
    return pd.Series({"model": name, **r})
```

### The integrated challenge pipeline (one command, deterministic)

```python
# src/tamweel/challenge/pipeline.py
"""Chains the whole course: audit -> CV -> weighted GBDT -> calibrate ->
cost threshold under capacity -> fairness check -> submission."""
from __future__ import annotations
import numpy as np, pandas as pd
from tamweel.validation.leakage_audit import audit
from tamweel.validation.cv import time_group_folds
from tamweel.calibrate.calibrate import calibrate_model
from tamweel.imbalance.cost_threshold import expected_cost_curve
from tamweel.challenge.score import business_cost
import lightgbm as lgb

SEED = 42

def run_challenge(train_df, holdout_df, capacity=600) -> dict:
    y = train_df["default_90dpd"].astype(int)
    X = train_df.drop(columns=["default_90dpd", "application_id", "decision_date"])
    audit(X, y)                                    # gate 1: no leaks

    # honest OOF probabilities via the Module-2 harness
    oof = np.zeros(len(y))
    for tr, va in time_group_folds(train_df):
        m = lgb.LGBMClassifier(learning_rate=0.03, n_estimators=800,
                               num_leaves=41, scale_pos_weight=12.5,
                               random_state=SEED, verbose=-1)
        m.fit(X.iloc[tr], y.iloc[tr])
        oof[va] = m.predict_proba(X.iloc[va])[:, 1]

    # choose the operating point on OOF, under capacity
    curve, best = expected_cost_curve(y.values, oof, review_capacity=capacity)
    t_star = float(best.threshold)

    # refit on all data, calibrate, score the held-out ledger
    final = lgb.LGBMClassifier(learning_rate=0.03, n_estimators=800,
                               num_leaves=41, scale_pos_weight=12.5,
                               random_state=SEED, verbose=-1).fit(X, y)
    calibrated = calibrate_model(final, X, y, method="isotonic")
    Xh = holdout_df.drop(columns=["default_90dpd", "application_id", "decision_date"])
    ph = calibrated.predict_proba(Xh)[:, 1]
    result = business_cost(holdout_df["default_90dpd"].values, ph, t_star, capacity)
    print(f"LEDGER cost=SAR {result['cost_sar']:,.0f}  t*={t_star:.3f}  "
          f"recall={result['recall']:.1%}")
    return {"threshold": t_star, "ledger": result, "proba": ph}
```

### Fairness guardrail — false-decline parity

```python
# src/tamweel/challenge/fairness.py
"""False-decline (FP) rate parity across regions. A cheaper cost that
fails fairness must not win the challenge."""
import numpy as np, pandas as pd

def false_decline_parity(y_true, pred, segment) -> pd.DataFrame:
    df = pd.DataFrame({"y": y_true, "pred": pred, "seg": segment})
    good = df[df.y == 0]
    rates = good.groupby("seg").apply(
        lambda g: (g.pred == 1).mean(), include_groups=False)
    gap = rates.max() - rates.min()
    print(f"false-decline rates by region:\n{rates.round(3)}\n"
          f"parity gap = {gap:.3f} (target < 0.05)")
    return pd.DataFrame({"false_decline_rate": rates})
```

## Hands-on Lab 7 — The Challenge Sprint

| | |
|---|---|
| **Objective** | Produce the best (lowest-SAR-cost) constraint-satisfying Tamweel Youth model, an entry on the private leaderboard, a model card, and a panel defence |
| **Duration** | ~3.5 hours across Day-4 (briefing + two sprints + assembly + defence) |
| **Setup** | Full course repo, `git checkout challenge-start`; `tamweel_youth_train.parquet` provided; the held-out `tamweel_youth_ledger.parquet` is instructor-only |

**Instructions & tasks**
1. *(Briefing, 30 min)* Read the brief; write the one-sentence objective and name the binding constraint. Build/verify `business_cost` and the submission format *before* modelling.
2. *(Sprint 1, 50 min)* Reproduce a leak-audited baseline through the Module-2 harness; engineer 3–5 application-time-only features; score each experiment on SAR cost. Keep an experiment log.
3. *(Sprint 2, 50 min)* Add class-weighting + cost-threshold under capacity; calibrate; run the fairness parity check; decide (via the noise-band gate) whether an ensemble earns its place. Finalise the operating point.
4. *(Assembly, 50 min)* Freeze the pipeline (fixed seed), generate the submission file, and assemble `MODEL_CARD.md` (use, data, validation, performance+SAR, calibration, SHAP reason codes, fairness, limits, monitoring).
5. *(Submission)* Submit the probability file by the deadline; the instructor scores it on the held-out ledger.
6. *(Defence, 20 min slot)* Present the business-metric result and defend validation, calibration, and fairness to the panel.

**Expected output**
```
objective: minimise expected SAR loss on Tamweel Youth under 600/day review capacity
           and region false-decline parity gap < 0.05
baseline (leak-audited)        cost=SAR    3,180,000  recall=58.0%  flagged=612
+ engineered features          cost=SAR    2,760,000  recall=64.0%  flagged=598
+ calibrated + cost-threshold  cost=SAR    2,510,000  recall=67.0%  flagged=600
false-decline rates by region: Central 0.031  West 0.037  East 0.041  South 0.049
parity gap = 0.018 (target < 0.05)   PASS
ensemble lift +0.003 < fold std 0.010  -> KEEP SINGLE MODEL
LEDGER cost=SAR 2,548,000  t*=0.104  recall=66.1%      # held-out, revealed at Hour 5
```

**Acceptance criteria:** submission scored on the held-out ledger; SAR cost beats the provided baseline; review-capacity and fairness constraints satisfied; model card complete; reproducible under a fixed seed; panel defence delivered.

**Troubleshooting guidance**

| Symptom | Cause | Fix |
|---|---|---|
| Great OOF cost, terrible ledger cost | A new feature leaks | Re-run `audit`; drop the offender; the ledger is a future vintage |
| Fairness gap fails despite low cost | Threshold declines one region disproportionately | Consider segment-aware thresholds within legal limits; document |
| Can't regenerate the submission | Unseeded step (Optuna/SMOTE/split) | Set and log every seed; hash artefacts |
| Over budget on time | Chasing AUC in Optuna | Reallocate to features + threshold + calibration; cap trials |

**Instructor notes.** Protect the sprints from theory creep — they are deliberately continuous. Collect submissions at the end of Sprint 2 so scoring finishes before the reveal. The pedagogical climax is when a leaky 0.93-CV entry lands near the *bottom* of the SAR leaderboard while an honest 0.79 model with the right threshold and calibration wins — the entire course argued for this moment. Fast finishers help peers with model-card assembly, not with more Optuna trials.

## Mini Exercises

**Quiz (5 questions)**
1. What metric decides the leaderboard? → expected SAR business cost on the held-out ledger, not AUC.
2. What should you build before your first model? → the business-cost scorer and submission format.
3. Where does the highest-value hour usually go? → features + cost threshold + calibration, not extra Optuna trials.
4. Why can a 0.93-CV model lose to a 0.79 model here? → leakage collapses on the future ledger; the honest model with the right operating point wins on SAR.
5. True/False: a great score with a failing fairness gap wins. → **False** (constraint violated).

**Coding exercise.** Write `experiment_log(entry)` that appends each run's hypothesis, change, OOF SAR cost, and calibration ECE to a CSV — the evidence trail the panel expects.

**Debugging exercise.** Your ledger cost is double your OOF cost and recall collapsed. List the three most likely causes ranked (feature leak; population shift; threshold set on uncalibrated scores) and the check for each.

**Discussion questions.**
- With one hour left and a choice between an ensemble (+0.003 AUC) and calibration (ECE 0.09→0.02), which do you do and why?
- How would you explain to the panel that your *lower*-AUC model is the right one to ship?

## Case Study — The Leaderboard Upset

**Scenario.** In a Tamweel Youth bake-off, one team topped the *public* CV board at 0.94 AUC; a quieter team sat mid-table at 0.80. On the held-out ledger scored by SAR cost, the 0.94 team fell to last and the 0.80 team won by a wide margin.

**Business context.** The 0.94 relied on `utilisation_next_month`, a feature that only exists after onboarding — invisible in CV, absent (and useless) on the genuinely-future ledger. The 0.80 team had audited features, calibrated, and chosen a cost-optimal threshold under capacity — so their honest model turned into the lowest realised SAR loss.

**Technical challenge.** Diagnose why the leaderboard inverted and codify the practices that made the winning model win.

**Constraints.** The winning model also had to pass fairness parity and be explainable to the committee — a high score alone would not have won.

**Solution approach (facilitate, don't lecture).** (1) Trace the 0.94 collapse to leakage via the audit and SHAP; (2) show the 0.80 model's honest validation, calibration (ECE 0.02), and cost threshold; (3) confirm its fairness gap and reason codes; (4) declare the business metric, not AUC, the arbiter; (5) fold the lesson into the model-card standard.

**Discussion questions.**
1. Why did the public CV board mislead so badly, and what would have exposed it earlier?
2. Which single practice (audit, calibration, cost threshold) contributed most to the win?
3. How do you institutionalise "score on business cost, on a held-out ledger" in a real team?
4. What does this bake-off predict about the SDA-DSC-390 capstone?

## Benchmarks and Evaluation

| Metric | Category | Target for M7 | How measured |
|---|---|---|---|
| Ledger SAR cost | Business impact | below the provided baseline | `business_cost` on held-out ledger |
| Leak-free features | Integrity | audit passes; ledger ≈ OOF | `audit` + OOF/ledger parity |
| Calibration (ECE) | Trust | ≤ 0.03 on the ledger band | Module-5 metrics |
| Review-capacity satisfied | Operability | flagged ≤ capacity | scorer under constraint |
| Fairness parity gap | Fairness | < 0.05 false-decline gap | `false_decline_parity` |
| Model card completeness | Documentation | all sections present | rubric check |
| Reproducibility | Rigour | submission regenerable | fixed-seed rerun |

**Example benchmark table (filled during challenge):**

| Entry | CV AUC | Ledger SAR cost | Fairness gap | Verdict |
|---|---|---|---|---|
| Leaky champion | 0.94 | 4,910,000 | 0.061 | disqualified (leak + fairness) |
| Honest single + calib | 0.80 | 2,548,000 | 0.018 | winner |
| Honest + ensemble | 0.80 | 2,540,000 | 0.020 | marginal; kept single |

## Required Visuals and Training Assets

### Diagrams
1. **Challenge pipeline map** — *Purpose:* the integrative picture. *Elements:* audit → CV → weighted GBDT → cost threshold → calibration → fairness → model card, each labelled with its owner test. *Style:* end-to-end flow, English with Arabic subtitles.
2. **Effort-allocation clock** — *Purpose:* budget discipline. *Elements:* a 2.5-hour clock partitioned into baseline / features / threshold / calibration / (maybe) ensemble. *Style:* pie/clock.
3. **Public-CV vs ledger inversion** — *Purpose:* the course thesis. *Elements:* two ranked boards with the leaky entry swapping from top to bottom. *Style:* paired ranking chart.
4. **Model-card anatomy** — *Purpose:* the deliverable template. *Elements:* the model-card sections as labelled blocks. *Style:* printable A4 template.

### Images (screenshots)
1. **Leaderboard terminal output**: *why:* expected-output reference; *content:* SAR-cost entries ranked.
2. **Fairness parity table**: *why:* constraint evidence; *content:* per-region false-decline rates with the gap.
3. **Final reliability + SHAP composite**: *why:* the defence evidence pack; *content:* calibrated curve beside the beeswarm.

### Simulations
1. **Ledger-reveal replay** — *Setup:* score both a leaky and an honest submission on the hidden ledger live; the ranking inverts. *Learning objective:* honest models win the business metric.
2. **Budget-tradeoff planner** — *Setup:* allocate a fixed hour to features vs tuning vs calibration; the tool estimates SAR impact. *Learning objective:* effort goes where value is.

### Interactive Activities
- **Panel defence role-play (20 min):** each team faces a mock risk committee (played by peers + instructor) and must answer "what breaks this model?" in business terms.
- **Brief-decoding sprint (10 min):** teams race to write the one-sentence objective and name the binding constraint from the brief.

### Datasets
| Dataset | Source | Format | Size | Purpose |
|---|---|---|---|---|
| `tamweel_youth_train.parquet` | New salary-advance product, shifted population | Parquet | 30,000 × 40 | Challenge training |
| `tamweel_youth_ledger.parquet` | Held-out future vintage, instructor-only | Parquet | 10,000 rows | Leaderboard scoring |
| `challenge_brief.md` | Objective, cost matrix, capacity, fairness rule | Markdown | 1 page | The task specification |

### Demo Requirements
- **Instructor demo:** run the integrated pipeline end-to-end and score a submission on the ledger in under 8 minutes.
- **Student demo:** each team presents its model card and defends the operating point to the panel.
- **Expected outputs:** ledger-scored submission beating baseline, constraints satisfied, complete reproducible model card.

---
