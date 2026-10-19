# Time Series Forecasting AI Systems — SDAIA Academy

## Project Overview

This project focuses on forecasting daily retail demand using the `retail_demand.csv` dataset.

The analysis focuses on **Grocery demand in Riyadh**, using daily `units_sold` as the forecasting target.

The project implements an end-to-end time-series forecasting workflow covering:

1. Time-series decomposition and diagnostics
2. Classical forecasting using SARIMA
3. Machine Learning forecasting using Gradient Boosting
4. Expanding-window walk-forward backtesting
5. Forecast evaluation using multiple metrics
6. Conformal probabilistic forecasting
7. Model comparison and deployment considerations

---

## Dataset

* **Dataset:** `retail_demand.csv`
* **Region:** Riyadh
* **Category:** Grocery
* **Frequency:** Daily
* **Target variable:** `units_sold`
* **Time variable:** `date`

The dataset is filtered to focus on Grocery demand in Riyadh and transformed into a daily time series.

### Why this dataset?

Retail demand forecasting is a practical time-series forecasting problem where historical demand patterns can be used to support planning, inventory management, and operational decision-making.

---

## Technical Approach

### 1. Data Preparation

The dataset is filtered using:

```text
region = Riyadh
category = Grocery
```

The `date` column is converted into a datetime index, and the data is organized at a daily frequency.

Missing observations are handled using time-based interpolation where required.

---

### 2. Time-Series Diagnostics

The time series is analyzed using:

* Time-series visualization
* Trend analysis
* Seasonal pattern analysis
* ACF and PACF
* Stationarity testing
* Differencing where required
* Residual diagnostics

The analysis is used to identify important temporal patterns before model development.

---

### 3. SARIMA Forecasting

SARIMA is used as the classical statistical forecasting model.

The model captures:

* Autoregressive relationships
* Differencing
* Moving-average effects
* Seasonal patterns

A seasonal period of **7 days** is used to represent weekly demand patterns.

Residual diagnostics, including the Ljung-Box test, are used to evaluate remaining autocorrelation.

---

### 4. Machine Learning Forecasting

`HistGradientBoostingRegressor` is used as the Machine Learning forecasting model.

The model uses temporal features such as:

* Lag 1
* Lag 7
* Lag 14
* Lag 28
* Rolling statistics
* Day-of-week features
* Calendar features
* Time-based trend features

Lag and rolling features are constructed using historical observations to reduce future-data leakage.

For multi-step forecasting, recursive predictions are used so that future actual target values are not used during forecasting.

---

## Walk-Forward Backtesting

Expanding-window walk-forward validation is used to evaluate forecasting performance over multiple forecasting periods.

The process follows:

```text
Train → Forecast → Evaluate
          ↓
     Expand Training Window
          ↓
       Forecast Again
```

This approach better represents how the models would operate in a real-world forecasting environment, where future observations are not available at the time of prediction.

---

## Evaluation Metrics

The forecasting models are evaluated using:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

### RMSE — Root Mean Squared Error

Penalizes larger forecasting errors more heavily than MAE.

### MASE — Mean Absolute Scaled Error

Compares forecasting performance against a naive benchmark.

### WAPE — Weighted Absolute Percentage Error

Measures total absolute error relative to total actual demand.

Multiple metrics are used to provide a more complete evaluation rather than relying on a single error measure.

---

## Probabilistic Forecasting

Conformal prediction is used to generate prediction intervals around the forecasts.

The analysis reports:

* Point forecast
* Lower prediction bound
* Upper prediction bound
* Empirical coverage
* Mean interval width

This provides uncertainty estimates in addition to point forecasts.

---

## Model Comparison

SARIMA and Gradient Boosting are compared based on:

* Forecast accuracy
* Performance across walk-forward folds
* Weekly seasonality handling
* Interpretability
* Prediction interval behavior
* Computational requirements
* Operational considerations

The final model selection is based on the backtesting results and the requirements of the forecasting application rather than relying on a single metric.

---

## Deployment Considerations

For a production forecasting system, the following considerations are important:

* Retraining models only using observations available at the forecast origin
* Preventing data leakage during feature generation
* Recomputing lag and rolling features using historical data
* Monitoring forecasting errors over time
* Monitoring prediction interval coverage
* Recalibrating conformal prediction intervals when demand behavior changes
* Monitoring changes in weekly seasonal patterns

---

## Project Structure

```text
sdaia-time-series-forecasting/
│
├── data/
│   └── retail_demand.csv
│
├── time_series_forecasting.ipynb
├── README.md
└── .gitignore
```

---

## How to Run

The project is designed to run using **Google Colab**.

### Option 1 — Google Colab

Open the notebook in Google Colab and run the cells from top to bottom.

The notebook uses the following dataset:

```text
retail_demand.csv
```

### Option 2 — Local Environment

Clone the repository:

```bash
git clone https://github.com/FahadAlsaadi99/sdaia-time-series-forecasting.git
cd sdaia-time-series-forecasting
```

Install the required Python packages:

```bash
pip install pandas numpy matplotlib scikit-learn statsmodels scipy
```

Then open:

```text
time_series_forecasting.ipynb
```

using Jupyter Notebook, JupyterLab, or VS Code.

---

## Training Programme

**Programme:** SDAIA Academy — Time Series Forecasting AI Systems

**Trainee:** Fahad AlSaadi

**Cohort:** second cohort

**Cohort Dates:** 20 September 2026, On-site

---

## Project Files

* `time_series_forecasting.ipynb` — Main forecasting notebook
* `retail_demand.csv` — Dataset used in the project
* `README.md` — Project documentation
* `.gitignore` — Files excluded from Git tracking

---

## SDAIA Academy

This project was completed as part of the **SDAIA Academy** training programme.

Official SDAIA Academy GitHub: `https://github.com/SDAIAAcademy`

---

## Author

**Fahad AlSaadi**
