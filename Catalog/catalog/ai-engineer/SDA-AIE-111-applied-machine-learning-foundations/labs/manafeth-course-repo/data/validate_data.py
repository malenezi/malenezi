"""Sanity checks mirroring the SDA-AIE-111 Lab 1-2 workflow (seed 42)."""
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import average_precision_score, mean_absolute_error

RS, TARGET = 42, "churned_30d"
LEAKY = ["refund_issued", "support_ticket_after_snapshot", "next_month_orders"]
c = pd.read_parquet("data/manafeth_customers.parquet")
lines = []
lines.append(f"shape: {c.shape}  | customer_id unique: {c.customer_id.is_unique}")
lines.append(f"churn rate: {c[TARGET].mean():.3f}  (target 0.140)")
lines.append(f"missingness: avg_rating {c.avg_rating.isna().mean():.2f} (spec 0.31), "
             f"last_promo_used {c.last_promo_used.isna().mean():.2f} (spec 0.22)")
new = c.tenure_months < 4
lines.append(f"avg_rating missing among new (<4mo) customers: {c.loc[new,'avg_rating'].isna().mean():.2f} "
             f"vs established: {c.loc[~new,'avg_rating'].isna().mean():.2f}  (missingness is signal)")

num = ["orders_per_month","avg_basket_sar","days_since_last_order","tenure_months",
       "distinct_categories","promo_usage_rate","avg_rating","ramadan_order_share"] 
num = [x for x in num if x in c.columns]
X = c.drop(columns=[TARGET, "customer_id", *LEAKY])
y = c[TARGET]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.20, stratify=y, random_state=RS)
lines.append(f"split: train {len(X_tr):,} / test {len(X_te):,}  churn {y_tr.mean():.3f} / {y_te.mean():.3f}")

# Dummies
d = DummyClassifier(strategy="stratified", random_state=RS).fit(X_tr[num], y_tr)
lines.append(f"dummy (stratified) PR-AUC: {average_precision_score(y_tr, d.predict_proba(X_tr[num])[:,1]):.3f}  (~0.14)")
dr = DummyRegressor(strategy="mean").fit(X_tr[["orders_per_month"]], X_tr["avg_basket_sar"])
lines.append(f"dummy regressor MAE on avg_basket_sar: {mean_absolute_error(X_tr['avg_basket_sar'], dr.predict(X_tr)):.1f} SAR")

# 21-day heuristic
Xv = X_tr.copy(); Xv["y"] = y_tr
rank = Xv.sort_values("days_since_last_order", ascending=False)
top = rank.head(int(0.20*len(rank)))
lines.append(f"21-day-silence heuristic recall@20%: {top['y'].sum()/Xv['y'].sum():.2f}  (spec ~0.41)")

# Honest logistic on numeric features
imp = SimpleImputer(strategy="median"); sc = StandardScaler()
Xa, Xb, ya, yb = train_test_split(X_tr[num], y_tr, test_size=0.25, stratify=y_tr, random_state=RS)
Xa_ = sc.fit_transform(imp.fit_transform(Xa)); Xb_ = sc.transform(imp.transform(Xb))
clf = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=RS).fit(Xa_, ya)
proba = clf.predict_proba(Xb_)[:,1]
prauc = average_precision_score(yb, proba)
budget = int(0.20*len(yb)); tops = np.argsort(-proba)[:budget]
rec20 = yb.iloc[tops].sum()/yb.sum()
lines.append(f"logistic (honest, numeric only) PR-AUC: {prauc:.3f}  recall@20%: {rec20:.2f}  (spec ballpark 0.44 / 0.57)")

# Leak inflation
XaL = pd.concat([Xa.reset_index(drop=True),
                 c.loc[Xa.index, LEAKY].reset_index(drop=True)], axis=1)
XbL = pd.concat([Xb.reset_index(drop=True),
                 c.loc[Xb.index, LEAKY].reset_index(drop=True)], axis=1)
XaL_ = sc.fit_transform(imp.fit_transform(XaL)); XbL_ = sc.transform(imp.transform(XbL))
clfL = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=RS).fit(XaL_, ya)
lines.append(f"logistic WITH the 3 planted leaks PR-AUC: "
             f"{average_precision_score(yb, clfL.predict_proba(XbL_)[:,1]):.3f}  (fiction — leaks work)")

# Shuffled-label test
ysh = ya.sample(frac=1.0, random_state=RS).reset_index(drop=True)
clfS = LogisticRegression(class_weight="balanced", max_iter=1000).fit(Xa_, ysh)
lines.append(f"shuffled-label test PR-AUC: {average_precision_score(yb, clfS.predict_proba(Xb_)[:,1]):.3f}  (~0.14 = honest)")

# Orders / Ramadan
o = pd.read_parquet("data/manafeth_orders.parquet").set_index("order_ts")
r25 = len(o.loc["2025-03-01":"2025-03-30"])/30; f25 = len(o.loc["2025-02-01":"2025-02-27"])/27
ev = o.loc["2025-03-01":"2025-03-30"].index.hour
lines.append(f"orders: {len(o):,} rows; Ramadan-25 daily volume x{r25/f25:.2f}; "
             f"share of Ramadan orders 19:00-02:59: {np.isin(ev,[19,20,21,22,23,0,1,2]).mean():.2f}")

seg = c.groupby(pd.qcut(c.days_since_last_order, 5, duplicates="drop"), observed=True)[TARGET].mean()
lines.append(f"churn by recency quintile: {seg.round(3).tolist()}  (monotone signal)")

# ------------------------------------------------------------------ course-arc checks (v2 data)
# The three golden-thread claims, verified end-to-end:
#   (1) engineered order-history features lift the linear model (Lab 3)
#   (2) tree ensembles beat the linear model on the same features (Lab 5)
#   (3) both effects survive cross-validation (Lab 4 harness)
orders_df = o.reset_index()
SNAP = pd.Timestamp("2025-11-01")
past = orders_df[orders_df["order_ts"] < SNAP]
w90 = past[past["order_ts"] >= SNAP - pd.Timedelta(days=90)]
eng = pd.DataFrame({
    "orders_90d": w90.groupby("customer_id")["order_id"].count(),
    "avg_basket_90d": w90.groupby("customer_id")["basket_sar"].mean(),
})
eng["basket_trend"] = (eng["avg_basket_90d"] / past.groupby("customer_id")["basket_sar"].mean()).replace([np.inf,-np.inf],1.0)
ram_lo, ram_hi = pd.Timestamp("2025-03-01"), pd.Timestamp("2025-03-31")
past2 = past.assign(is_ram=((past["order_ts"]>=ram_lo)&(past["order_ts"]<ram_hi)).astype(int),
                    is_we=past["order_ts"].dt.dayofweek.isin([4,5]).astype(int))
eng["ramadan_order_share"] = past2.groupby("customer_id")["is_ram"].mean()
eng["weekend_order_share"] = past2.groupby("customer_id")["is_we"].mean()
cf = c.merge(eng.reset_index(), on="customer_id", how="left").fillna(
    {"orders_90d":0,"basket_trend":1.0,"ramadan_order_share":0,"weekend_order_share":0})

from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
CVo = StratifiedKFold(5, shuffle=True, random_state=RS)
base_num = ["orders_per_month","avg_basket_sar","days_since_last_order","tenure_months",
            "distinct_categories","promo_usage_rate","avg_rating"]
eng_num = base_num + ["orders_90d","basket_trend","ramadan_order_share","weekend_order_share"]
cats = ["city","device","payment_method"]
Xf = cf.drop(columns=[TARGET,"customer_id",*LEAKY]); yf = cf[TARGET]
Xf_tr, _, yf_tr, _ = train_test_split(Xf, yf, test_size=0.20, stratify=yf, random_state=RS)
def prep(nums):
    from sklearn.preprocessing import OneHotEncoder
    return ColumnTransformer([
        ("num", Pipeline([("i", SimpleImputer(strategy="median", add_indicator=True)), ("s", StandardScaler())]), nums),
        ("cat", Pipeline([("i", SimpleImputer(strategy="constant", fill_value="missing")),
                          ("o", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), cats)],
        remainder="drop")
lr_b = Pipeline([("p", prep(base_num)), ("m", LogisticRegression(class_weight="balanced", max_iter=1000, random_state=RS))])
lr_e = Pipeline([("p", prep(eng_num)), ("m", LogisticRegression(class_weight="balanced", max_iter=1000, random_state=RS))])
s_b = cross_val_score(lr_b, Xf_tr, yf_tr, cv=CVo, scoring="average_precision", n_jobs=-1).mean()
s_e = cross_val_score(lr_e, Xf_tr, yf_tr, cv=CVo, scoring="average_precision", n_jobs=-1).mean()
lines.append(f"[arc 1] logistic CV PR-AUC: snapshot-only {s_b:.3f} -> +engineered {s_e:.3f}  (features beat models)")
try:
    from xgboost import XGBClassifier
    xg = Pipeline([("p", prep(eng_num)), ("m", XGBClassifier(n_estimators=400, learning_rate=0.05,
        max_depth=4, subsample=0.8, colsample_bytree=0.8, scale_pos_weight=6.1,
        eval_metric="aucpr", random_state=RS, n_jobs=-1))])
    s_x = cross_val_score(xg, Xf_tr, yf_tr, cv=CVo, scoring="average_precision", n_jobs=-1).mean()
    lines.append(f"[arc 2] xgboost CV PR-AUC on same features: {s_x:.3f}  (ensembles beat linear)")
except ImportError:
    lines.append("[arc 2] xgboost not installed — skipped")
rec_match = (abs((SNAP - past.groupby("customer_id")["order_ts"].max()).dt.days
             - c.set_index("customer_id")["days_since_last_order"]) <= 1).mean()
lines.append(f"[coherence] recomputed recency matches table within 1 day: {rec_match:.3f}")

report = "MANAFETH DATA VALIDATION REPORT (seed 42)\n" + "="*60 + "\n" + "\n".join(lines) + "\n"
print(report)
open("data/validation_report.txt","w").write(report)
