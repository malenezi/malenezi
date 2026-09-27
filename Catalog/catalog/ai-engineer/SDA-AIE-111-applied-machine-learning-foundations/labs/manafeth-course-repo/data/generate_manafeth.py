"""
Manafeth synthetic dataset generator — SDA-AIE-111 (Applied Machine Learning Foundations)
==========================================================================================
Regenerates the golden-thread course datasets at seed 42, per the instructor package:

  * manafeth_customers  — 48,000 rows x 19 cols, churn rate exactly 14.0%,
    three planted leaky columns (refund_issued, support_ticket_after_snapshot,
    next_month_orders), avg_rating ~31% missing (new customers),
    last_promo_used ~22% missing, KSA cities, SAR amounts.
  * manafeth_orders     — 610,000 rows x 11 cols, order-level companion with
    Ramadan seasonality (evening volume roughly doubles) and Fri/Sat weekend pattern.
  * Case-study samples  — markabat_listings_sample (2,000), jeddah_requests_sample
    (12,000), jubail_sensors_sample (5,000), makkah_demand_sample (8,000),
    shifted_month (threshold-drift simulation).

Snapshot date: 2025-11-01. All code targets Python 3.12, pandas >= 2.2, pyarrow.
Run:  python generate_manafeth.py
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from pathlib import Path

SEED = 42
N = 48_000
SNAPSHOT = pd.Timestamp("2025-11-01")
CHURN_RATE = 0.14                      # exactly 6,720 churners
OUT = Path("data")
OUT.mkdir(exist_ok=True)

rng = np.random.default_rng(SEED)

# Ramadan windows relevant to the data horizon (approximate Umm al-Qura dates)
RAMADAN = {
    2024: (pd.Timestamp("2024-03-11"), pd.Timestamp("2024-04-09")),
    2025: (pd.Timestamp("2025-03-01"), pd.Timestamp("2025-03-30")),
    2026: (pd.Timestamp("2026-02-18"), pd.Timestamp("2026-03-19")),
}

# ----------------------------------------------------------------------------- customers
print("Generating manafeth_customers ...")

customer_id = np.array([f"C{i:06d}" for i in range(1, N + 1)])

city = rng.choice(["Riyadh", "Jeddah", "Dammam"], size=N, p=[0.50, 0.30, 0.20])
city_tier = pd.Series(city).map({"Riyadh": 1, "Jeddah": 2, "Dammam": 3}).to_numpy()
device = rng.choice(["iOS", "Android"], size=N, p=[0.46, 0.54])
payment_method = rng.choice(
    ["mada", "credit_card", "apple_pay", "cash_on_delivery"],
    size=N, p=[0.42, 0.24, 0.22, 0.12],
)

# Tenure: many new customers (post-Ramadan acquisition), long right tail
tenure_months = np.clip(rng.gamma(shape=1.6, scale=9.0, size=N), 0.5, 60).round(1)
signup_date = SNAPSHOT - pd.to_timedelta((tenure_months * 30.44).round(), unit="D")

# Engagement latent factor drives most behaviour
engagement = rng.normal(0, 1, N) + 0.25 * (tenure_months / 24)

orders_per_month = np.clip(
    np.exp(0.75 + 0.55 * engagement + rng.normal(0, 0.30, N)), 0.2, 40
).round(2)
avg_basket_sar = np.clip(
    np.exp(4.32 + 0.34 * engagement
           + 0.14 * (payment_method == "credit_card")
           + 0.08 * (city == "Riyadh")
           + rng.normal(0, 0.33, N)), 18, 1400
).round(2)
distinct_categories = np.clip(
    (2 + 2.1 * np.maximum(engagement + 1.2, 0) + rng.normal(0, 1.2, N)).round(), 1, 18
).astype(int)
promo_usage_rate = np.clip(
    0.30 - 0.06 * engagement + rng.normal(0, 0.16, N), 0, 1
).round(3)

# Recency — the dominant churn signal (heavier tail for disengaged customers)
days_since_last_order = np.clip(
    rng.exponential(scale=np.clip(16 - 7 * engagement, 3, 60)), 0, 120
).round().astype(int)

# Ramadan-seasonal shoppers: over-index in Ramadan, quiet otherwise (planted FP cluster)
ramadan_shopper = rng.random(N) < 0.12
ramadan_order_share = np.clip(
    np.where(ramadan_shopper,
             rng.beta(8, 2.5, N),        # most of their orders in the Ramadan window
             rng.beta(1.2, 14, N)),      # everyone else: barely any
    0, 1,
).round(3)
weekend_order_share = np.clip(rng.beta(3.2, 5.5, N)
                              + 0.05 * (device == "Android"), 0, 1).round(3)

# Two latents that are deliberately NOT snapshot columns — they are recoverable
# only by engineering features from the orders table, which is what makes the
# Lab 3 feature-engineering lift real rather than rhetorical:
#   basket_decline — recent baskets shrink before churn (recovered by basket_trend)
#   slowdown       — recent order frequency drops below the historical average
#                    in orders_per_month (recovered by orders_90d)
basket_decline = rng.normal(0, 1, N)
slowdown = rng.normal(0, 1, N)

# avg_rating: missing for ~31% (overwhelmingly NEW customers — missingness is signal)
p_missing = np.clip(0.82 - 0.16 * np.log1p(tenure_months), 0.02, 0.95)
p_missing *= 0.31 / p_missing.mean()
rating_missing = rng.random(N) < np.clip(p_missing, 0, 1)
avg_rating = np.clip(rng.normal(4.15 + 0.10 * engagement, 0.45, N), 1, 5).round(2)
avg_rating[rating_missing] = np.nan

# last_promo_used: ~22% missing (never used a promo)
promos = ["RMDN25", "WELCOME10", "FLASH15", "WKND20", "BULK30"]
last_promo_used = rng.choice(promos, size=N,
                             p=[0.30, 0.24, 0.20, 0.16, 0.10]).astype(object)
promo_missing = rng.random(N) < np.clip(0.22 + 0.10 * (promo_usage_rate < 0.05), 0, 1)
promo_missing = _pm = (rng.random(N) < (0.22 / max((promo_usage_rate < 0.98).mean(), 1e-9)) * 1.0)
# simpler exact-ish control: mark the lowest promo users as missing plus noise
order_low = np.argsort(promo_usage_rate + rng.normal(0, 0.05, N))
promo_missing = np.zeros(N, dtype=bool)
promo_missing[order_low[: int(0.22 * N)]] = True
last_promo_used[promo_missing] = None

# --------------------------------------------------------------- churn target (exactly 14.0%)
z = (
    -2.05
    + 0.007 * days_since_last_order
    # hazard ACCELERATES after ~18 quiet days — the Lab 5 partial-dependence
    # reading ("the 21-day heuristic was nearly right") and one reason tree
    # ensembles beat the linear model on this data
    + 0.055 * np.maximum(days_since_last_order - 18, 0)
    # seasonal shoppers: long silence does not mean gone (they return next
    # Ramadan) — the planted Lab 4 false-positive cluster, an interaction
    # only models WITH the engineered ramadan_order_share feature can learn
    - 0.042 * days_since_last_order * ramadan_order_share
    - 0.95 * np.log1p(orders_per_month)
    + 1.00 * slowdown                       # recent-frequency drop (orders_90d recovers this)
    + 1.00 * basket_decline                 # shrinking baskets precede churn (basket_trend recovers this)
    - 0.025 * tenure_months
    + 1.10 * (tenure_months < 3)            # newcomer cliff — a step the linear model misses
    + 2.20 * (promo_usage_rate - 0.30)
    + 1.30 * (promo_usage_rate > 0.65)      # deal-hunter cliff — another tree-learnable step
    + 2.10 * ramadan_order_share            # main effect: seasonal shoppers lapse more overall
    - 0.50 * (distinct_categories - 4) / 4
    + 0.15 * (city == "Dammam")
    + 0.45 * rating_missing                 # new customers churn differently
    + 1.00 * (avg_basket_sar < 45)             # top-up samplers: tiny baskets churn (non-monotone in basket)
    + 1.30 * ((slowdown > 0.6) & (basket_decline > 0.6))  # compound fade — an interaction trees can find
    + rng.normal(0, 0.62, N)                # irreducible noise keeps PR-AUC honest
)
p = 1 / (1 + np.exp(-z))
churn_draw = rng.random(N) < p
target_n = int(round(CHURN_RATE * N))       # 6,720
# adjust to the exact count by flipping the most marginal rows
diff = churn_draw.sum() - target_n
if diff > 0:                                # too many churners: un-flip lowest-p churners
    idx = np.where(churn_draw)[0]
    churn_draw[idx[np.argsort(p[idx])[:diff]]] = False
elif diff < 0:                              # too few: flip highest-p non-churners
    idx = np.where(~churn_draw)[0]
    churn_draw[idx[np.argsort(-p[idx])[: -diff]]] = True
churned_30d = churn_draw.astype(int)
assert churned_30d.mean() == CHURN_RATE, churned_30d.mean()

# ------------------------------------------------------------------ planted leaky columns
# These only exist AFTER the snapshot — the timestamp test fails all three.
refund_issued = (
    rng.random(N) < np.where(churned_30d == 1, 0.36, 0.045)
).astype(int)
support_ticket_after_snapshot = (
    rng.random(N) < np.where(churned_30d == 1, 0.33, 0.06)
).astype(int)
next_month_orders = np.where(
    churned_30d == 1,
    0,
    rng.poisson(np.clip(orders_per_month, 0.2, 40)),
).astype(int)

customers = pd.DataFrame({
    "customer_id": customer_id,
    "signup_date": signup_date.normalize(),
    "snapshot_date": SNAPSHOT,
    "city": city,
    "city_tier": city_tier,
    "device": device,
    "payment_method": payment_method,
    "tenure_months": tenure_months,
    "orders_per_month": orders_per_month,
    "avg_basket_sar": avg_basket_sar,
    "days_since_last_order": days_since_last_order,
    "distinct_categories": distinct_categories,
    "promo_usage_rate": promo_usage_rate,
    "avg_rating": avg_rating,
    "last_promo_used": last_promo_used,
    "churned_30d": churned_30d,
    "refund_issued": refund_issued,                                  # LEAK (planted)
    "support_ticket_after_snapshot": support_ticket_after_snapshot,  # LEAK (planted)
    "next_month_orders": next_month_orders,                          # LEAK (planted)
})
assert customers.shape == (N, 19), customers.shape
assert customers["customer_id"].is_unique

customers.to_csv(OUT / "manafeth_customers.csv", index=False)
customers.to_parquet(OUT / "manafeth_customers.parquet", index=False)
print(f"  manafeth_customers: {customers.shape}, churn {customers.churned_30d.mean():.3f}, "
      f"avg_rating missing {customers.avg_rating.isna().mean():.2f}, "
      f"last_promo missing {customers.last_promo_used.isna().mean():.2f}")

# ------------------------------------------------------------------------------- orders
print("Generating manafeth_orders (this takes ~1 min) ...")
TOTAL_ORDERS = 610_000

# Expected order counts proportional to rate x observed window, capped at 18 months
window_days = np.minimum(tenure_months * 30.44, 548)
raw = orders_per_month * window_days / 30.44
counts = rng.poisson(raw * (TOTAL_ORDERS / raw.sum()))
diff = TOTAL_ORDERS - counts.sum()
adj_idx = rng.choice(N, size=abs(int(diff)), replace=True, p=raw / raw.sum())
np.add.at(counts, adj_idx, 1 if diff > 0 else -1)
counts = np.maximum(counts, 0)
short = TOTAL_ORDERS - counts.sum()
if short != 0:
    counts[np.argmax(counts)] += short
assert counts.sum() == TOTAL_ORDERS

cust_idx = np.repeat(np.arange(N), counts)

# Timestamps: coherent with the snapshot columns —
#   * each customer's MOST RECENT order sits exactly days_since_last_order
#     back from the snapshot (so Lab 3's recomputed recency matches the table)
#   * a customer's orders land in the Ramadan window with probability equal
#     to their latent ramadan_order_share (so the engineered share feature
#     recovers the latent that drives churn — the Lab 3 lift is real)
start_off = np.asarray(np.minimum((SNAPSHOT - pd.DatetimeIndex(signup_date)).days, 548))
so_o = start_off[cust_idx]
dslo_o = days_since_last_order[cust_idx]

u = rng.random(TOTAL_ORDERS)
# slowdown latent skews a customer's orders away from the recent window:
# u**k with k<1 pushes draws toward the far past (fewer recent orders than
# the historical orders_per_month implies) — orders_90d recovers this.
k_skew = np.exp(-0.90 * slowdown)[cust_idx]
days_back = (dslo_o + (u ** k_skew) * np.maximum(so_o - dslo_o, 1)).astype(int)

# Ramadan-2025 window in days-before-snapshot terms
RAM25_LO = (SNAPSHOT - RAMADAN[2025][1]).days          # 216
RAM25_HI = (SNAPSHOT - RAMADAN[2025][0]).days          # 245
covers_ram25 = so_o >= RAM25_LO + 5
use_ram = (rng.random(TOTAL_ORDERS) < 0.34 * ramadan_order_share[cust_idx]) & covers_ram25
ram_days = (RAM25_LO + rng.random(TOTAL_ORDERS)
            * (np.minimum(RAM25_HI, so_o) - RAM25_LO)).astype(int)
days_back = np.where(use_ram, np.maximum(ram_days, dslo_o), days_back)

# Coherence: the first generated order per customer is their most recent one
first_of_customer = np.zeros(TOTAL_ORDERS, dtype=bool)
first_of_customer[np.unique(cust_idx, return_index=True)[1]] = True
days_back = np.where(first_of_customer, dslo_o, days_back)

ts = SNAPSHOT - pd.to_timedelta(days_back, unit="D")
in_ramadan = np.zeros(TOTAL_ORDERS, dtype=bool)
for a, b in RAMADAN.values():
    in_ramadan |= (ts >= a) & (ts <= b)

# Hour of day: evening-heavy; Ramadan orders cluster post-Iftar/late night
base_hours = rng.choice(24, size=TOTAL_ORDERS,
                        p=np.array([1,1,1,1,1,1,2,3,4,5,5,6,7,6,5,5,6,8,10,11,10,8,5,4], float)
                          / 116)
ram_hours = rng.choice([19, 20, 21, 22, 23, 0, 1, 2], size=TOTAL_ORDERS,
                       p=[0.16, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06])
hour = np.where(in_ramadan, ram_hours, base_hours)
order_ts = (pd.DatetimeIndex(ts).normalize()
            + pd.to_timedelta(hour, unit="h")
            + pd.to_timedelta(rng.integers(0, 60, TOTAL_ORDERS), unit="m"))

t_frac = 1.0 - days_back / np.maximum(so_o, 1)         # 0 at signup -> 1 near snapshot
basket = np.clip(
    avg_basket_sar[cust_idx] * np.exp(rng.normal(0, 0.35, TOTAL_ORDERS))
    * np.exp(-0.65 * basket_decline[cust_idx] * t_frac)   # decliners' recent baskets shrink
    * np.where(in_ramadan, 1.18, 1.0),
    12, 3000,
).round(2)
items = np.clip(rng.poisson(np.clip(basket / 22, 1, 60)), 1, 80).astype(int)
categories = rng.choice(
    ["fresh_produce", "dairy_eggs", "bakery", "beverages", "snacks",
     "household", "meat_poultry", "frozen", "personal_care", "baby_kids"],
    size=TOTAL_ORDERS,
    p=[0.17, 0.14, 0.11, 0.12, 0.11, 0.09, 0.09, 0.06, 0.06, 0.05])
slot = rng.choice(["express_30min", "same_day", "scheduled"],
                  size=TOTAL_ORDERS, p=[0.55, 0.30, 0.15])
promo_used = rng.random(TOTAL_ORDERS) < np.clip(promo_usage_rate[cust_idx], 0, 1)
promo_code = np.where(promo_used,
                      rng.choice(promos, size=TOTAL_ORDERS), None)
order_rating = np.clip(rng.normal(4.2, 0.7, TOTAL_ORDERS), 1, 5).round(0)
order_rating[rng.random(TOTAL_ORDERS) < 0.55] = np.nan   # most orders unrated

orders = pd.DataFrame({
    "order_id": [f"O{i:07d}" for i in range(1, TOTAL_ORDERS + 1)],
    "customer_id": customer_id[cust_idx],
    "order_ts": order_ts,
    "basket_sar": basket,
    "items_count": items,
    "top_category": categories,
    "delivery_slot": slot,
    "payment_method": payment_method[cust_idx],
    "promo_code": promo_code,
    "delivery_city": city[cust_idx],
    "order_rating": order_rating,
}).sort_values("order_ts").reset_index(drop=True)
orders["order_id"] = [f"O{i:07d}" for i in range(1, TOTAL_ORDERS + 1)]
assert orders.shape == (TOTAL_ORDERS, 11), orders.shape

orders.to_csv(OUT / "manafeth_orders.csv", index=False)
orders.to_parquet(OUT / "manafeth_orders.parquet", index=False)
rt = orders.set_index("order_ts")
ram25 = rt.loc["2025-03-01":"2025-03-30"].shape[0] / 30
feb25 = rt.loc["2025-02-01":"2025-02-27"].shape[0] / 27
print(f"  manafeth_orders: {orders.shape}; Ramadan-25 daily volume x{ram25/feb25:.2f} vs Feb")

# ---------------------------------------------------------------- shifted month (M4 drift sim)
print("Generating shifted_month.parquet ...")
shift = customers.sample(9_000, random_state=SEED).copy()
shift["snapshot_date"] = pd.Timestamp("2025-12-01")
shift["days_since_last_order"] = np.clip(
    shift["days_since_last_order"] + rng.integers(4, 14, len(shift)), 0, 150)
shift["orders_per_month"] = (shift["orders_per_month"] * rng.uniform(0.82, 0.95, len(shift))).round(2)
shift = shift.drop(columns=["churned_30d", "refund_issued",
                            "support_ticket_after_snapshot", "next_month_orders"])
shift.to_parquet(OUT / "shifted_month.parquet", index=False)

# ------------------------------------------------------------------- case-study samples
print("Generating case-study samples ...")

# Markabat used-car listings (M2 case study) — 2,000 rows
n = 2_000
makes = rng.choice(["Toyota", "Hyundai", "Nissan", "Kia", "Ford", "Chevrolet",
                    "Lexus", "Mercedes", "BMW", "Mazda"],
                   size=n, p=[0.26, 0.16, 0.12, 0.10, 0.08, 0.07, 0.06, 0.06, 0.05, 0.04])
year = rng.integers(2008, 2026, n)
age = 2026 - year
km = np.clip(rng.normal(19_000 * age, 9_000 * np.sqrt(age)), 500, 500_000).round(-2)
lux = np.isin(makes, ["Lexus", "Mercedes", "BMW"])
base_price = np.where(lux, 210_000, 78_000) * np.exp(-0.11 * age)
price = np.clip(base_price * np.exp(rng.normal(0, 0.28, n)) - 0.06 * km / 10, 8_000, 900_000)
markabat = pd.DataFrame({
    "listing_id": [f"L{i:05d}" for i in range(1, n + 1)],
    "make": makes,
    "model_year": year,
    "mileage_km": km.astype(int),
    "city": rng.choice(["Riyadh", "Jeddah", "Dammam", "Makkah", "Madinah"], n,
                       p=[0.38, 0.26, 0.16, 0.12, 0.08]),
    "condition_grade": rng.choice(["excellent", "good", "fair"], n, p=[0.3, 0.5, 0.2]),
    "photos_count": rng.integers(3, 25, n),
    "days_on_platform": rng.integers(0, 90, n),
    "listed_month": rng.choice(pd.period_range("2024-01", "2025-10", freq="M").astype(str), n),
    "sale_price_sar": price.round(-2).astype(int),
})
markabat.to_csv(OUT / "markabat_listings_sample.csv", index=False)

# Jeddah municipal service requests (M6 case study) — 12,000 rows, district-aggregated
n = 12_000
jr = pd.DataFrame({
    "request_id": [f"R{i:06d}" for i in range(1, n + 1)],
    "district": rng.choice([f"district_{i:02d}" for i in range(1, 25)], n),
    "category": rng.choice(["road_damage", "waste", "lighting", "flooding", "encroachment"],
                           n, p=[0.28, 0.30, 0.18, 0.12, 0.12]),
    "hour_of_day": rng.integers(0, 24, n),
    "day_of_week": rng.choice(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], n),
    "month": rng.integers(1, 13, n),
    "is_ramadan": (rng.random(n) < 0.09).astype(int),
    "resolution_hours": np.clip(rng.gamma(2.2, 26, n), 1, 600).round(1),
})
jr.to_csv(OUT / "jeddah_requests_sample.csv", index=False)

# Jubail compressor sensors (M5 case study) — 5,000 machine-hour rows
n = 5_000
trip_soon = rng.random(n) < 0.02
jub = pd.DataFrame({
    "compressor_id": rng.choice([f"K-{i:03d}" for i in range(1, 29)], n),
    "reading_ts": pd.Timestamp("2025-06-01")
                  + pd.to_timedelta(rng.integers(0, 24 * 120, n), unit="h"),
    "vibration_mm_s": np.clip(rng.normal(2.4 + 2.6 * trip_soon, 0.8, n), 0.3, 12).round(2),
    "vibration_trend_7d": np.clip(rng.normal(0.02 + 0.5 * trip_soon, 0.15, n), -1, 2).round(3),
    "bearing_temp_c": np.clip(rng.normal(68 + 14 * trip_soon, 7, n), 40, 130).round(1),
    "temp_delta_24h": np.clip(rng.normal(0.4 + 5.5 * trip_soon, 2.2, n), -10, 30).round(1),
    "discharge_pressure_bar": np.clip(rng.normal(18.5, 2.1, n), 10, 30).round(2),
    "running_hours": rng.integers(100, 60_000, n),
    "trip_within_72h": trip_soon.astype(int),
})
jub.to_parquet(OUT / "jubail_sensors_sample.parquet", index=False)

# Makkah nightly hotel demand (M7 case study) — 8,000 property-nights
dates = pd.date_range("2024-01-01", periods=730, freq="D")
props = [f"P-{i:02d}" for i in range(1, 12)]
grid = pd.MultiIndex.from_product([props, dates], names=["property_id", "night"]).to_frame(index=False)
grid = grid.sample(8_000, random_state=SEED).reset_index(drop=True)
ram_mask = np.zeros(len(grid), dtype=bool)
for a, b in RAMADAN.values():
    ram_mask |= (grid["night"] >= a) & (grid["night"] <= b)
hajj = ((grid["night"] >= "2024-06-10") & (grid["night"] <= "2024-06-24")) | \
       ((grid["night"] >= "2025-05-30") & (grid["night"] <= "2025-06-13"))
base = rng.normal(0.62, 0.12, len(grid))
occ = np.clip(base + 0.28 * ram_mask + 0.34 * hajj.values
              + 0.05 * grid["night"].dt.dayofweek.isin([3, 4]).values, 0.05, 1.0)
grid["occupancy_rate"] = occ.round(3)
grid["adr_sar"] = np.clip(rng.normal(520, 120, len(grid))
                          * (1 + 0.9 * ram_mask + 1.4 * hajj.values), 150, 4000).round(0)
grid["is_ramadan"] = ram_mask.astype(int)
grid["is_hajj_window"] = hajj.astype(int)
grid.to_parquet(OUT / "makkah_demand_sample.parquet", index=False)

print("All datasets written to ./data")
