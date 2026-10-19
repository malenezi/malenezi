# Customer Churn Prediction for Proactive Retention

Predicting which telecom subscribers will cancel their service, so the retention team can call them
**before** they leave — with an operating threshold, explanations and a calibration check, not just a score.

**Headline result (untouched hold-out, 1,409 customers):**
**PR-AUC 0.650** against a 0.265 base rate (**2.5×** the no-skill line) · **ROC-AUC 0.847** ·
catching **79% of churners** at **51% precision**, with well-calibrated probabilities (Brier 0.135).

## Course

**Advanced Machine Learning Methods — SDAIA Academy** (SDA-DSC-211)
Final Applied Project · tabular binary classification · Days 1–3 methods only.

## Problem Statement

A telecom operator loses roughly one subscriber in four. Winning a customer back after they cancel costs
far more than keeping one who is still active, so the retention team needs to intervene *before* the
cancellation. This project predicts, for each currently-active subscriber, whether they will cancel their
service before the next billing cycle, and converts that probability into a ranked weekly call list.

- **Prediction moment:** at the close of a billing cycle, for a customer whose account is **still active**,
  using only account-state information visible on the customer record at that moment (contract, tenure to
  date, subscribed services, billing method, charges to date).
- **Decision supported:** whether to place this customer on the outbound retention list for the coming
  cycle — a discounted-contract or service-upgrade offer. **Acted on by:** the customer-retention team,
  which has a finite weekly calling capacity.
- **Why the errors are asymmetric:** a false negative loses the account's entire remaining lifetime value;
  a false positive costs one phone call. That asymmetry is what justifies moving the threshold well below
  0.5 — and it is why recall carries more weight than precision here.

## Dataset

- **Name:** Telco Customer Churn (IBM sample dataset)
- **Source / link:** https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv
- **Provider:** IBM (`IBM/telco-customer-churn-on-icp4d` repository)
- **Licence:** Apache License 2.0 · **Redistribution permitted:** yes
- **Size:** 7,043 rows × 21 columns (1 identifier + 19 features + 1 target)
- **Target:** `Churn` · **Positive class (=1):** the customer cancelled their service
- **Class balance:** **26.54%** positive (1,869 churned / 5,174 stayed)

### Why this dataset was selected

It is flat tabular data with a clean binary target and a genuine business decision behind it. It is large
enough for a 60/20/20 train / calibration / hold-out split that still leaves **374 positive cases in the
hold-out** — comfortably above the ~50-positive guidance — yet small enough that a LightGBM model trains
in under two seconds, which keeps the whole workflow inside the five-hour budget. Its moderate 26.5%
imbalance makes PR-AUC the meaningful headline and makes the threshold decision real rather than academic,
and its mix of 16 categorical and 3 numeric columns supports genuine preprocessing, leakage analysis, SHAP
interpretation and a calibration assessment. It is a synthetic sample published under Apache 2.0, so it
contains no real personal data and may be redistributed — the CSV is committed, and the notebook runs with
no manual download step.

## Methodology

### Validation

**Stratified 5-fold cross-validation on a 60% training portion, with a 20% calibration split and a 20%
untouched hold-out**, because this dataset is a single account snapshot with **exactly one row per
customer** (`customerID`: 7,043 unique values in 7,043 rows) and **no date column**. There are therefore
no repeated entities to leak across folds and no deployment time order to respect. Stratification is used
because the positive class is the minority.

This mirrors deployment because in production the model is fitted on the customers known today and scored
on *different* customers at the close of the next cycle — a customer-disjoint split reproduces exactly
that relationship. A time-aware split is impossible here (no timestamp to order on) and a group-aware
split would be degenerate (the group key is unique per row). Per the project guide, Stratified K-Fold is
the **correct** answer for this data structure, not a shortcut, and the notebook says so explicitly.

| Split | Share | Rows | Positives | Used for |
|---|---|---|---|---|
| Training | 60% | 4,225 | 1,121 | 5-fold CV: OOF predictions, imbalance test, threshold sweep, Optuna |
| Calibration | 20% | 1,409 | 374 | Fitting and assessing the calibrator only |
| Hold-out | 20% | 1,409 | 374 | Opened **once**, at the end |

### Leakage Controls

All five types were inspected and documented:

- **Post-outcome:** *none found.* Every one of the 19 modelling columns was reviewed against the stated
  prediction moment. All describe account state visible while the customer is active; nothing records the
  cancellation, its reason or its date. `TotalCharges` is billing *to date*, known at prediction time.
- **ID:** *controlled.* `customerID` is a pure row identifier (7,043 distinct values in 7,043 rows) and is
  dropped before modelling.
- **Temporal:** *not applicable.* No date column exists. `tenure` is an elapsed-months duration, not a
  calendar position, and is legitimately known at the prediction moment.
- **Group:** *not applicable.* Exactly one row per customer, so rows are independent and no group guard is
  needed.
- **Preprocessing:** *controlled* (this one always applies). All learned transforms — imputers and the
  ordinal encoder — sit inside a scikit-learn `Pipeline` that is cloned and re-fitted on the training rows
  of every fold. The calibration and hold-out splits are transformed with a preprocessor fitted only on the
  training portion.

An automated single-feature AUC screen (threshold 0.85) was run as a cross-check and **flagged nothing**.
The strongest single feature is the engineered `monthly_per_service` at 0.770, then `Contract` (0.744) and
`tenure` (0.741) — all legitimately strong for well-understood commercial reasons. No leak was invented in
order to have something to remove.

**Removed columns:** `customerID` (identifier — no legitimate signal, and an ID correlated with the target
would be pure leakage).

### Model

**LightGBM**, seed 42, learning rate 0.019 (Optuna-tuned), with **early stopping** choosing the number of
trees on each validation fold — never on the hold-out. The final tree count (172) is the median across CV
folds, which deliberately avoids spending the calibration split on early stopping.
Data split: train **60%** / calibration **20%** / hold-out **20%**, stratified.
XGBoost was also trained as bonus work for comparison and ensembling.

**Feature engineering (bonus):** 8 derived features, all stateless and row-wise — `avg_monthly_spend`,
`charge_drift`, `n_services`, `n_protection`, `no_protection_at_all`, `monthly_per_service`,
`is_new_customer`, `tenure_years`. The engineered `monthly_per_service` ("value for money") became the
**2nd most important feature** by mean |SHAP|, ahead of every raw billing column.

### Metrics

ROC-AUC, **PR-AUC (headline)**, precision, recall, confusion matrix and Brier score. All cross-validation
results are reported as **mean ± std across folds**. PR-AUC is read against the **0.265 base rate**, never
against 0.5. Accuracy is not used as a headline: predicting "nobody churns" already scores 73.5%.

### Imbalance Handling

**None applied — measured and rejected on evidence.** At 26.5% positive the imbalance is mild, so the
analysis is required but the intervention is not. `class_weight='balanced'` was tested on identical folds:

**Effect on PR-AUC: 0.6690 → 0.6697 (+0.0007)** — roughly a tenth of the ±0.0065 fold spread, i.e. not a
gain at all. Meanwhile it pushed the mean predicted probability from 0.264 to **0.409** against a 0.265
base rate and worsened Brier from 0.1355 to **0.1654**. It would have bought nothing in ranking quality
while destroying the interpretable probability scale that the threshold and calibration work depend on.
The unweighted model is carried forward.

### Threshold Strategy

**Rule used: target recall ≥ 80%** — among all thresholds still meeting the requirement, take the
strictest (highest) one, which gives the best precision and the smallest call list.

**Selected threshold = 0.27** because the cost asymmetry is real and one-directional (a lost account
versus one phone call), and the retention team expresses its requirement as a catch rate. An
expected-cost rule was **deliberately not used**: no documented figures exist for retention-call cost or
subscriber lifetime value, and the guide is explicit that inventing a cost matrix earns nothing.

At this threshold (out-of-fold): **precision 0.526, recall 0.801, flag rate 40.4%.**

**Operational trade-off, presented rather than hidden.** A 41% flag rate is a large call list. If the team
can only work a 20% list, the threshold rises to 0.50 and **recall collapses to 50%** — half the churners
are never called. That is a staffing decision, not a modelling one, so the list should be worked in
descending probability order and truncated by real capacity. The default 0.5 cut-off, for contrast,
catches only 47% of churners.

### Hyperparameter Tuning

Optuna, **30 trials**, `TPESampler(seed=42)` with a `MedianPruner` (bonus), optimising mean CV PR-AUC on
the same fixed splitter. 29 trials completed, 1 pruned.

**Best value: 0.6784 ± 0.0145. Gain vs baseline: +0.0094 (baseline fold spread: ±0.0065).**
The gain does **not** clear the 2×-spread rule of thumb (0.013), the tuned model's own fold spread
*widened* to ±0.0145, and `best_value` is a maximum over 30 trials and so is optimistically biased. It is
recorded as a **marginal, not clearly-real** improvement — and the hold-out later confirmed that
scepticism.

### Interpretability

- **Global:** permutation importance on held-out data (`Contract` 0.115, `tenure` 0.060,
  `monthly_per_service` 0.032) plus a SHAP beeswarm.
- **Local:** a SHAP waterfall for a customer sitting exactly on the decision boundary (p = 0.270),
  translated into three plain-language reason codes.
- The **permutation-importance correlation trap** is demonstrated deliberately: `tenure_years` was
  engineered as an exact duplicate of `tenure` and does not appear in the top 12 at all, because shuffling
  it alone barely hurts while its twin still carries the information.

### Calibration

**Final model calibrated on the calibration split using: none — the raw probabilities were already
calibrated.** Mean predicted 0.2641 vs actual base rate 0.2654; **Brier 0.1378, ECE 0.0180**.

Sigmoid and isotonic were both fitted and compared (bonus). **Brier: 0.1378 → 0.1386 (sigmoid, worse).**
Isotonic reported a perfect ECE of 0.0000 — but measured **in-sample** on the 1,409 rows it was fitted on,
while its PR-AUC *fell* (0.6412 → 0.6390), the step-function behaviour the guide warns about on small
calibration sets. The decision to ship uncalibrated was made on the calibration split **before** the
hold-out was opened; the hold-out later confirmed it (uncalibrated ECE 0.0228 vs sigmoid 0.0439 and
isotonic 0.0250). Ranking metrics were essentially unchanged under sigmoid, exactly as expected —
calibration is a monotone reshaping.

## Results

All cross-validation rows are scored on **identical folds**. The final row is the one-time hold-out.

| Model | ROC-AUC | PR-AUC | Result @ threshold (precision @ recall ≥ 80%) | Brier | Complexity |
|---|---|---|---|---|---|
| Baseline (LightGBM) | 0.8457 ± 0.0107 | 0.6690 ± 0.0065 | 0.5167 (t=0.26, flag 41.1%) | 0.1355 | Low |
| + imbalance lever (balanced) | 0.8455 ± 0.0101 | 0.6697 ± 0.0067 | 0.5102 (t=0.47, flag 41.9%) | 0.1654 | Low |
| XGBoost (bonus) | 0.8461 ± 0.0097 | 0.6723 ± 0.0067 | 0.5079 (t=0.26, flag 41.8%) | 0.1349 | Low |
| **Optuna-tuned LightGBM** | **0.8504 ± 0.0108** | **0.6784 ± 0.0145** | 0.5258 (t=0.27, flag 40.4%) | **0.1336** | Medium |
| Simple average LGB+XGB (bonus) | 0.8463 ± 0.0102 | 0.6705 ± 0.0051 | 0.5088 (t=0.26, flag 41.8%) | 0.1348 | High |
| OOF stack, LR meta (bonus) | 0.8489 ± 0.0102 | 0.6743 ± 0.0099 | 0.5147 (t=0.20, flag 41.9%) | 0.1358 | High |
| **FINAL — hold-out result** | **0.8467** | **0.6499** | **0.5130 (t=0.27, recall 0.789)** | **0.1353** | Medium |

## Final Model Selection

**We selected the Optuna-tuned LightGBM, uncalibrated, at threshold 0.27**, because on cross-validation
evidence — gathered before the hold-out was opened — it leads on discrimination (PR-AUC 0.6784) *and* on
probability quality (Brier 0.1336), needs one model in production rather than three, and its probabilities
are trustworthy without a calibrator.

**We rejected:**
- the **class-weighted model**, which bought +0.0007 PR-AUC while wrecking the probability scale;
- the **simple average and the OOF stack**, which both scored *below* the tuned single model (0.6705 and
  0.6743 vs 0.6784) at two-to-three times the operational complexity — the two base models' OOF
  predictions correlate at **0.99**, so there was no diversity left to exploit;
- **sigmoid and isotonic calibration**, which made already-calibrated probabilities worse.

**Hold-out performance:** ROC-AUC **0.8467** | PR-AUC **0.6499** | precision **0.513** | recall **0.789**.

## Key Findings

1. **Contract type dominates everything else.** Month-to-month customers face no exit cost and can act on
   dissatisfaction immediately. `Contract` scores 0.115 on permutation importance — double the next
   feature — and 2.6× the runner-up on mean |SHAP|. It is also the driver the business can most directly
   change, which makes it the natural retention lever.
2. **Value-for-money beats raw price.** The engineered `monthly_per_service` ranks 2nd by SHAP, above
   every raw billing column: a customer paying $90 across six services reads as invested, while the same
   $90 for one service reads as a bad deal. Raw `MonthlyCharges` alone is a much weaker signal.
3. **The ensembling bonus argued against itself — correctly.** Averaging and stacking both underperformed
   a single tuned model because the two base learners agree 99% of the time. Reporting that, with the
   numbers, is the right professional answer; shipping the stack because it was optional-and-impressive
   would not have been.
4. **The hold-out caught the tuning optimism.** PR-AUC fell 0.6784 → 0.6499, about 2× the fold spread and
   below even the untuned baseline's CV score — exactly the direction and magnitude flagged when the
   +0.0094 gain was described as marginal. The ranking (ROC-AUC 0.847) and the threshold (79% recall
   against an 80% target) both transferred intact.
5. **Account state beats demographics.** `gender`, `Partner` and `Dependents` are nearly worthless, while
   the absence of support add-ons matters. Who you are predicts churn far less well than what your account
   looks like — a welcome result, since account state is actionable and demographics are not.

## Limitations

- **No time dimension, so no temporal validation.** This is a static snapshot with no event dates, so the
  model cannot be tested on a train-on-past / predict-on-future split — which is how it would really run.
  Concept drift is invisible here. This is the largest gap between the reported number and production
  reality, and it needs different data, not better modelling.
- **The dataset is an IBM sample, not a real subscriber base** — cleaner than any real CRM extract, so
  real-world performance should be expected to be lower.
- **No documented costs**, so the threshold rests on a stated recall target rather than a measured optimum.
- **A single 1,409-row hold-out carries its own sampling error**; part of the CV-to-hold-out gap is simply
  which 20% of customers landed there. Repeated nested CV would separate that from tuning optimism.
- **The model predicts churn, not the effect of intervening.** Acting on the ranking is uplift modelling
  done implicitly, and no observational dataset can identify uplift — only a randomised holdback can.
- **Fairness was not audited.** Demographic columns are in the feature set; they carry little importance,
  but "unimportant" is not "unbiased", and subgroup error rates were not measured.

## Is 0.85 Actually Good? Measuring the Ceiling

Rather than assume ROC-AUC 0.847 was the best available, I measured whether it *is*. Three independent
analyses agree this dataset is **information-limited, not model-limited**:

- **Irreducible label noise.** 49.5% of rows have an exact categorical twin, and **25.5% of all rows sit
  in a group where identical customers had opposite outcomes**. The unbiased pair-disagreement estimator
  puts **56–66% of label variance beyond reach of these 19 features**. An omniscient model with the
  measured signal variance would score ROC-AUC **0.87–0.90** — the tuned model at 0.850 is within about
  two points of the theoretical maximum. ROC-AUC 0.95 would require the features to explain ~62% of label
  variance; they explain 35–44%.
- **Learning curve.** A 20× increase in training rows buys +0.025 ROC-AUC. Extrapolating, 0.95 would need
  on the order of 10⁹ rows. The constraint is the columns, not the row count.
- **Feature and model saturation.** 31 structurally different feature sets all landed in ROC-AUC
  0.845–0.851. 19 model families combined by 21 ensembling strategies (including nested-CV stacking and
  Caruana greedy selection) all landed in 0.846–0.852. The accurate learners correlate at r = 0.93–0.99
  *including logistic regression* — the signal is additive and low-order, and everything competent has
  already found it.

**On the "0.95 on Telco churn" claims found online.** They are artefacts. I reproduced the mechanism on
this exact data with the same model, changing only the order of two lines:

| Pipeline | ROC-AUC | PR-AUC |
|---|---|---|
| SMOTE applied **inside** each training fold (correct) | 0.821 | 0.602 |
| SMOTE applied to the whole dataset, **then** split | 0.934 | 0.940 |
| Random oversampling **before** the split | **0.964** | **0.962** |

Resampling before the split leaks synthetic copies of validation rows into training, and it also
rebalances the evaluation set, silently moving the PR no-skill baseline from 0.265 to 0.500. The honest
published range for this dataset is ROC-AUC 0.83–0.86 / PR-AUC 0.63–0.69; this project sits at the top of
it. **0.85 here is near-optimal, not mediocre.**

## How to Run

```bash
pip install -r requirements.txt
```

The dataset is already committed at `data/Telco-Customer-Churn.csv` (Apache 2.0 permits redistribution),
so no download is needed — see `data/README.md` for the source and for how to fetch it yourself.
Then open `project.ipynb` and run all cells from top to bottom (`Kernel → Restart and Run All`).
Full runtime is roughly 4 minutes, most of it the 30-trial Optuna study.

Every seed is fixed at 42 (model, splitter, Optuna sampler), so every number, table and figure in the
notebook reproduces exactly.

## Repository Structure

```
advanced-ml-final-project/
├── README.md                 # this file
├── project.ipynb             # the full project, 16 sections, runs top to bottom
├── requirements.txt          # pinned library versions
├── .gitignore
├── data/
│   ├── README.md             # source, licence, how to obtain, data quirks
│   └── Telco-Customer-Churn.csv
├── images/                   # 12 saved figures
│   ├── pr_curve.png                 ├── shap_summary.png
│   ├── roc_curve.png                ├── shap_waterfall.png
│   ├── confusion_matrix.png         ├── permutation_importance.png
│   ├── class_balance.png            ├── calibration_curve.png
│   ├── threshold_curve.png          ├── seed_stability.png
│   ├── optuna_history.png           └── holdout_evaluation.png
└── results/
    ├── model_results.csv            ├── threshold_sweep.csv
    ├── best_params.json             ├── calibration_comparison.csv
    ├── imbalance_before_after.csv   ├── holdout_calibration_check.csv
    ├── permutation_importance.csv   └── shap_importance.csv
```

## Requirements

pandas, numpy, scikit-learn, xgboost, lightgbm, shap, optuna, matplotlib
(exact versions pinned in `requirements.txt`; scikit-learn ≥ 1.6 is required for
`sklearn.frozen.FrozenEstimator`, used in the calibration section)

## Notebook Contents

| Section | Contents |
|---|---|
| 0. Problem and Dataset Selection | Problem, target, positive class, prediction moment, decision, source, licence |
| 1. Project Overview | What was built and what it is for |
| 2. Business Problem | Decision context, who acts and when, cost asymmetry |
| 3. Dataset Overview | Rows, columns, class balance, feature types, missing values |
| 4. Validation Strategy | Scheme, justification, three-way split, leakage controls |
| 5. Data Preparation | Feature engineering, pipeline, five-type leakage inspection, AUC screen |
| 6. Baseline Model | LightGBM, early stopping, seeds, OOF predictions |
| 7. Imbalanced Learning | Balance analysis, lever tested, before/after table, verdict |
| 8. Model Evaluation | ROC-AUC, PR-AUC ± std, confusion matrix, PR curve, interpretation |
| 9. Decision Threshold | Sweep, curve, operating rule, capacity trade-off |
| 10. Hyperparameter Optimization | Optuna study, pruner, history, honest gain assessment |
| 11. Model Interpretability | Permutation importance, SHAP beeswarm + waterfall, reason codes |
| 12. Calibration | Reliability curve, Brier/ECE, sigmoid vs isotonic |
| 13. Model Comparison | XGBoost, average, stack, seed stability, full comparison table |
| 14. Final Model Selection and Hold-Out Evaluation | Selection statement, one-time hold-out |
| 15. Conclusions, Limitations and Recommendations | Recommendations, limitations, next steps |

**Bonus work included:** both XGBoost and LightGBM trained and compared · simple-average ensemble ·
out-of-fold logistic-regression stack · Optuna pruning and optimisation-history plot · sigmoid vs isotonic
calibration compared with ECE · seed-stability analysis across 5 seeds · 8 engineered features.

## Author

Majed Alotaibi

## Acknowledgment

This project was completed as part of the **Advanced Machine Learning Methods** training program at
**SDAIA Academy**.

SDAIA Academy GitHub: https://github.com/SDAIAAcademy
