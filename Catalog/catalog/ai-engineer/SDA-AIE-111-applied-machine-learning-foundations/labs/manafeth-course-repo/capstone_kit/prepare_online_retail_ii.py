"""Prepare the UCI Online Retail II dataset for the SDA-AIE-111 capstone.

Turns 1,067,371 raw transactions (two years of real UK online-retail data,
CC BY 4.0) into a customer-snapshot table that mirrors the Manafeth golden
thread: one row = one customer at a snapshot date, with RFM aggregates,
cancellation behaviour, and a churn proxy label computed over a forward
horizon.

THE TRANSFORMATION *IS* THE ASSESSMENT. This script exists for instructors
(to pre-verify the dataset) and as the reference solution. Capstone teams are
expected to build their own customer-snapshot table — the graded traps live
exactly here:

  * unit of analysis: transactions must become customer-snapshots with NO
    future rows contaminating features (the prediction-time rule)
  * cancellations: invoices starting with "C" carry negative quantities —
    dropping them silently, or counting them as purchases, both bias RFM
  * ~23% of rows have no Customer ID — they cannot join a customer table
  * the churn label must be computed ONLY from the forward window, and the
    forward window must never feed a feature

Usage:
    # 1) Download from https://archive.ics.uci.edu/dataset/502/online+retail+ii
    #    (file: online_retail_II.xlsx — two sheets, 2009-2010 and 2010-2011)
    # 2) python prepare_online_retail_ii.py --xlsx online_retail_II.xlsx \
    #        --out ../data/capstone/
    # Options: --snapshot 2011-09-01  --horizon-days 90  --lookback-days 365

Output:
    online_retail_ii_customers.parquet  (+ .csv mirror)
    A printed audit block (row counts, churn rate, sanity checks).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

EXPECTED_COLS = ["Invoice", "StockCode", "Description", "Quantity",
                 "InvoiceDate", "Price", "Customer ID", "Country"]


def load_transactions(xlsx_path: Path) -> pd.DataFrame:
    """Load and concatenate both sheets of online_retail_II.xlsx."""
    sheets = pd.read_excel(xlsx_path, sheet_name=None, engine="openpyxl")
    df = pd.concat(sheets.values(), ignore_index=True)
    missing = [c for c in EXPECTED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Unexpected file format — missing columns: {missing}")
    return df


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise names, type the timestamp, keep identifiable customers.

    Cancellations are KEPT and flagged — they are behaviour, not noise.
    """
    out = df.rename(columns={
        "Invoice": "invoice", "StockCode": "stock_code", "Description": "description",
        "Quantity": "quantity", "InvoiceDate": "invoice_ts", "Price": "price",
        "Customer ID": "customer_id", "Country": "country",
    }).copy()
    out["invoice_ts"] = pd.to_datetime(out["invoice_ts"])
    out["invoice"] = out["invoice"].astype(str)
    out["is_cancellation"] = out["invoice"].str.startswith("C")
    out["revenue"] = out["quantity"] * out["price"]

    n_total = len(out)
    out = out[out["customer_id"].notna()].copy()          # the 23%-anonymous trap
    out["customer_id"] = out["customer_id"].astype(int).astype(str)
    print(f"clean: kept {len(out):,}/{n_total:,} rows with a Customer ID "
          f"({1 - len(out)/n_total:.0%} anonymous, excluded); "
          f"cancellation rows: {out['is_cancellation'].mean():.1%}")
    return out


def build_customer_snapshot(tx: pd.DataFrame,
                            snapshot: pd.Timestamp,
                            horizon_days: int = 90,
                            lookback_days: int = 365) -> pd.DataFrame:
    """One row = one customer active in the lookback window before `snapshot`.

    Features: ONLY transactions in [snapshot - lookback, snapshot).
    Label:    churned = no purchase invoice in [snapshot, snapshot + horizon).
    """
    past = tx[(tx["invoice_ts"] < snapshot)
              & (tx["invoice_ts"] >= snapshot - pd.Timedelta(days=lookback_days))]
    future = tx[(tx["invoice_ts"] >= snapshot)
                & (tx["invoice_ts"] < snapshot + pd.Timedelta(days=horizon_days))]

    purchases = past[~past["is_cancellation"]]
    if purchases.empty:
        raise ValueError("No purchase rows before the snapshot — check the dates.")

    # Invoice-level view for frequency & basket stats (a basket = one invoice)
    inv = (purchases.groupby(["customer_id", "invoice"])
           .agg(invoice_ts=("invoice_ts", "first"), basket_value=("revenue", "sum"),
                items=("quantity", "sum"))
           .reset_index())

    g_inv = inv.groupby("customer_id")
    g_line = purchases.groupby("customer_id")
    feats = pd.DataFrame({
        "recency_days": (snapshot - g_inv["invoice_ts"].max()).dt.days,
        "frequency_12m": g_inv["invoice"].count(),
        "monetary_12m": g_inv["basket_value"].sum(),
        "avg_basket_value": g_inv["basket_value"].mean(),
        "median_basket_value": g_inv["basket_value"].median(),
        "avg_items_per_order": g_inv["items"].mean(),
        "distinct_products": g_line["stock_code"].nunique(),
        "first_purchase_days": (snapshot - g_inv["invoice_ts"].min()).dt.days,
    })
    # Mean gap between consecutive invoices (NaN for single-invoice customers —
    # missingness is signal, exactly like Manafeth's avg_rating)
    gaps = (inv.sort_values("invoice_ts").groupby("customer_id")["invoice_ts"]
            .apply(lambda s: s.diff().dt.days.mean()))
    feats["mean_interpurchase_days"] = gaps

    # Cancellation behaviour (the trap: these rows must not count as purchases)
    canc = past[past["is_cancellation"]].groupby("customer_id")["invoice"].nunique()
    feats["cancelled_invoices"] = canc
    feats["cancellation_rate"] = (feats["cancelled_invoices"]
                                  / (feats["frequency_12m"] + feats["cancelled_invoices"]))
    feats = feats.fillna({"cancelled_invoices": 0, "cancellation_rate": 0.0})

    # Country (kept raw — encoding cardinality is the participant's decision)
    feats["country"] = g_line["country"].agg(lambda s: s.mode().iloc[0])

    # The label — forward window only, purchases only
    future_buyers = set(future.loc[~future["is_cancellation"], "customer_id"])
    feats["churned"] = (~feats.index.isin(future_buyers)).astype(int)

    out = feats.reset_index().assign(snapshot_date=snapshot)
    return out


def audit(snap: pd.DataFrame, horizon_days: int) -> None:
    print("\n--- audit ------------------------------------------------------")
    print(f"customers at snapshot: {len(snap):,}")
    print(f"churn rate ({horizon_days}-day horizon): {snap['churned'].mean():.3f}")
    print(f"monetary_12m: median {snap['monetary_12m'].median():.0f}, "
          f"p99 {snap['monetary_12m'].quantile(0.99):.0f}  (long tail -> log it)")
    print(f"mean_interpurchase_days missing: {snap['mean_interpurchase_days'].isna().mean():.1%} "
          "(single-invoice customers — missingness is signal)")
    print(f"country cardinality: {snap['country'].nunique()}")
    mono = snap.groupby(pd.qcut(snap["recency_days"], 5, duplicates="drop"),
                        observed=True)["churned"].mean().round(3).tolist()
    print(f"churn by recency quintile: {mono}  (should rise monotonically)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xlsx", required=True, help="path to online_retail_II.xlsx")
    ap.add_argument("--out", default=".", help="output directory")
    ap.add_argument("--snapshot", default="2011-09-01",
                    help="snapshot date (default 2011-09-01 leaves a clean 90-day horizon)")
    ap.add_argument("--horizon-days", type=int, default=90)
    ap.add_argument("--lookback-days", type=int, default=365)
    args = ap.parse_args()

    tx = clean_transactions(load_transactions(Path(args.xlsx)))
    snap = build_customer_snapshot(tx, pd.Timestamp(args.snapshot),
                                   args.horizon_days, args.lookback_days)
    audit(snap, args.horizon_days)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    snap.to_parquet(out_dir / "online_retail_ii_customers.parquet", index=False)
    snap.to_csv(out_dir / "online_retail_ii_customers.csv", index=False)
    print(f"\nwrote {out_dir / 'online_retail_ii_customers.parquet'} (+ .csv mirror)")


if __name__ == "__main__":
    main()
