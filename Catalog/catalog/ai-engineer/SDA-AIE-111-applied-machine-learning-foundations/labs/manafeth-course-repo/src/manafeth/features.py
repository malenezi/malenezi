"""Feature engineering & preprocessing — the single source of preprocessing truth.

Imported by every notebook from Lab 3 onwards. The rules encoded here:

1. Fit on training data only — every transform lives inside a Pipeline.
2. The prediction-time rule — every aggregate uses only orders strictly
   BEFORE the snapshot date. An aggregate over all orders summarises the
   future = leakage by construction.
3. KSA calendar reality — weekend is Fri/Sat, Ramadan drives real
   seasonality, salary lands near month-end.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RANDOM_STATE = 42

# Raw snapshot columns (available in manafeth_customers at prediction time)
BASE_NUM_COLS = [
    "orders_per_month", "avg_basket_sar", "days_since_last_order",
    "tenure_months", "distinct_categories", "promo_usage_rate", "avg_rating",
]
# Engineered in Lab 3 from the orders table (temporal-safe aggregates)
ENGINEERED_NUM_COLS = ["orders_90d", "basket_trend", "days_to_ramadan"]

NUM_COLS = BASE_NUM_COLS + ENGINEERED_NUM_COLS
# What the champion model actually uses from Lab 3 onwards
MODEL_NUM_COLS = NUM_COLS + ["ramadan_order_share", "weekend_order_share"]
CAT_COLS = ["city", "device", "payment_method"]

# Planted leaks — never features. The timestamp test fails all three.
LEAKY = ["refund_issued", "support_ticket_after_snapshot", "next_month_orders"]

RAMADAN_START = {2025: pd.Timestamp("2025-03-01"), 2026: pd.Timestamp("2026-02-18")}
# KSA weekend: Friday (dayofweek 4) and Saturday (5) — NOT Sat/Sun.
KSA_WEEKEND = (4, 5)


def build_preprocessor(num_cols: list[str] | None = None,
                       cat_cols: list[str] | None = None) -> ColumnTransformer:
    """The course preprocessor: impute→scale numerics, impute→one-hot categoricals.

    - add_indicator=True: missingness is signal (avg_rating missing ⇒ new customer).
    - handle_unknown="ignore": an unseen city (the Taif launch) must not crash serving.
    - remainder="drop": unlisted columns NEVER leak in silently.
    """
    numeric = Pipeline([
        ("impute", SimpleImputer(strategy="median", add_indicator=True)),
        ("scale", StandardScaler()),
    ])
    categorical = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    return ColumnTransformer([
        ("num", numeric, num_cols if num_cols is not None else NUM_COLS),
        ("cat", categorical, cat_cols if cat_cols is not None else CAT_COLS),
    ], remainder="drop", verbose_feature_names_out=True)


def rfm_features(orders: pd.DataFrame, snapshot: pd.Timestamp) -> pd.DataFrame:
    """RFM aggregates using only orders BEFORE the snapshot.

    Returns one row per customer_id with orders_90d, avg_basket_90d, basket_trend.
    """
    past = orders[orders["order_ts"] < snapshot]  # the load-bearing line

    w90 = past[past["order_ts"] >= snapshot - pd.Timedelta(days=90)]
    feats = pd.DataFrame({
        "orders_90d": w90.groupby("customer_id")["order_id"].count(),
        "avg_basket_90d": w90.groupby("customer_id")["basket_sar"].mean(),
    })

    # basket_trend: recent basket vs the customer's own lifetime basket.
    # A ratio < 1 means recent baskets are SHRINKING — an early churn signal
    # the snapshot table cannot see. Customers with no orders in the window
    # get the neutral value 1.0 (cold-start discussion in Lab 3).
    lifetime = past.groupby("customer_id")["basket_sar"].mean()
    feats["basket_trend"] = (feats["avg_basket_90d"] / lifetime).replace(
        [np.inf, -np.inf], 1.0)

    feats = feats.fillna({"orders_90d": 0, "basket_trend": 1.0})
    return feats.reset_index()


def order_share_features(orders: pd.DataFrame, snapshot: pd.Timestamp) -> pd.DataFrame:
    """Behavioural shares from order history (pre-snapshot only).

    ramadan_order_share — share of a customer's orders placed during Ramadan
    weekend_order_share — share placed on Fri/Sat (the KSA weekend)
    Used by Lab 6 segmentation and available to the churn model.
    """
    past = orders[orders["order_ts"] < snapshot].copy()
    ts = past["order_ts"]

    in_ramadan = pd.Series(False, index=past.index)
    for year, start in RAMADAN_START.items():
        in_ramadan |= (ts >= start) & (ts < start + pd.Timedelta(days=30))
    past["is_ramadan"] = in_ramadan.astype(int)
    past["is_weekend"] = ts.dt.dayofweek.isin(KSA_WEEKEND).astype(int)

    g = past.groupby("customer_id")
    out = pd.DataFrame({
        "ramadan_order_share": g["is_ramadan"].mean(),
        "weekend_order_share": g["is_weekend"].mean(),
    })
    return out.reset_index()


def calendar_features(df: pd.DataFrame, ts_col: str = "snapshot_date") -> pd.DataFrame:
    """Snapshot-date calendar features — the features generic tutorials never have."""
    out = df.copy()
    ts = pd.to_datetime(out[ts_col])
    out["is_weekend"] = ts.dt.dayofweek.isin(KSA_WEEKEND).astype(int)
    out["days_to_ramadan"] = ts.apply(
        lambda d: min((start - d).days % 365 for start in RAMADAN_START.values()))
    out["near_salary_day"] = ts.dt.day.isin([26, 27, 28, 29]).astype(int)
    return out


def build_feature_table(customers: pd.DataFrame, orders: pd.DataFrame,
                        snapshot: pd.Timestamp | None = None) -> pd.DataFrame:
    """Lab 3 deliverable: customers + temporal-safe engineered features.

    Leaves the raw columns untouched; adds ENGINEERED_NUM_COLS plus the
    order-share behavioural features. Safe to call on any customer subset.
    """
    snapshot = snapshot or pd.to_datetime(customers["snapshot_date"]).iloc[0]
    out = customers.merge(rfm_features(orders, snapshot), on="customer_id", how="left")
    out = out.merge(order_share_features(orders, snapshot), on="customer_id", how="left")
    out = calendar_features(out, "snapshot_date")
    out = out.fillna({"orders_90d": 0, "basket_trend": 1.0,
                      "ramadan_order_share": 0.0, "weekend_order_share": 0.0})
    return out
