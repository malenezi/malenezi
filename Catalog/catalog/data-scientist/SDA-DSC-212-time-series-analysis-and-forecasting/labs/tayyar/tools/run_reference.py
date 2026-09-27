"""Reference end-to-end run: produces every number quoted in the deck and the
benchmark tables, plus all deck figures. Instructors run this to regenerate."""
import sys, json, warnings, numpy as np, pandas as pd
sys.path.insert(0, "src"); warnings.filterwarnings("ignore")
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

from tayyar.data.load import load_demand, load_calendar, join_calendar
from tayyar.analysis.decompose import mstl_decompose
from tayyar.analysis.transform import additive_or_multiplicative
from tayyar.analysis.stationarity import stationarity_report, format_report
from tayyar.analysis.differencing import choose_differencing, difference
from tayyar.analysis.correlograms import correlogram_table, suggest_orders
from tayyar.features.build import build_features, assert_no_leakage
from tayyar.models.baselines import seasonal_naive
from tayyar.models.ets import fit_ets, forecast_ets
from tayyar.models.sarimax import fit_sarimax, forecast_sarimax, make_exog, residual_diagnostics
from tayyar.models.lgbm_forecaster import DirectLGBMForecaster
from tayyar.models.quantile import QuantileLGBM
from tayyar.models.conformal import CQR, coverage_report
from tayyar.models.explain import importance_by_family
from tayyar.eval.metrics import all_metrics, mase
from tayyar.eval.pinball import pinball_loss, coverage, interval_score
from tayyar.eval.diebold_mariano import diebold_mariano

FIG = Path("figures"); FIG.mkdir(exist_ok=True)
R = {}
plt.rcParams.update({"figure.dpi": 150, "savefig.dpi": 150, "font.size": 9,
                     "axes.grid": True, "grid.alpha": .25, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white"})
C = {"actual": "#1F3864", "fc": "#C00000", "base": "#7F7F7F",
     "band": "#8FAADC", "acc": "#2E7D32", "warn": "#ED7D31"}

# ---------------------------------------------------------------- M1: load ---
df = load_demand("data/ksa_grid_demand.csv")
cal = load_calendar("data/ksa_calendar.csv")
df = join_calendar(df, cal)
y = df["demand_mw"].astype(float)
R["m1"] = {"rows_raw": df.attrs["n_raw_rows"], "rows_clean": len(df),
           "missing": df.attrs["n_missing"], "longest_gap_h": df.attrs["longest_gap_h"],
           "imputed": int(df.is_imputed.sum())}
R["m1"]["transform"] = additive_or_multiplicative(y)
ylog = np.log(y)

dec = mstl_decompose(ylog, periods=(24, 24*7))
R["m1"]["strength"] = {k: round(v, 3) for k, v in dec["strength"].items()}
yoy = (y.resample("YE").mean().pct_change().dropna()*100).round(2).tolist()
R["m1"]["yoy_growth_pct"] = yoy

# Fig 1: raw series + summer/winter weeks
fig, ax = plt.subplots(3, 1, figsize=(10, 6.2))
y.resample("D").mean().plot(ax=ax[0], color=C["actual"], lw=.8)
ax[0].set_title("Tayyar — Central Operating Area daily mean demand, 2021–2023"); ax[0].set_ylabel("MW")
y["2023-07-09":"2023-07-16"].plot(ax=ax[1], color=C["fc"], lw=1.1)
ax[1].set_title("A summer week (July 2023) — deep daily AC cycle"); ax[1].set_ylabel("MW")
y["2023-01-08":"2023-01-15"].plot(ax=ax[2], color=C["acc"], lw=1.1)
ax[2].set_title("A winter week (January 2023) — same rhythm, a third of the amplitude"); ax[2].set_ylabel("MW")
for a in ax: a.set_xlabel("")
plt.tight_layout(); plt.savefig(FIG/"01_series_overview.png"); plt.close()

# Fig 2: MSTL panel
fig, ax = plt.subplots(4, 1, figsize=(10, 7), sharex=True)
sl = slice("2023-06-01", "2023-08-31")
ylog[sl].pipe(np.exp).plot(ax=ax[0], color=C["actual"], lw=.7); ax[0].set_ylabel("Observed\n(MW)")
dec["trend"][sl].pipe(np.exp).plot(ax=ax[1], color=C["fc"], lw=1.4); ax[1].set_ylabel("Trend")
dec["seasonal"].iloc[:, 0][sl].plot(ax=ax[2], color=C["acc"], lw=.6); ax[2].set_ylabel("Seasonal\n(daily, log)")
dec["remainder"][sl].plot(ax=ax[3], color=C["base"], lw=.5); ax[3].set_ylabel("Remainder")
ax[0].set_title(f"MSTL decomposition of log(demand)  ·  daily strength "
                f"{dec['strength']['seasonal_24']:.2f} · weekly {dec['strength']['seasonal_168']:.2f} "
                f"· trend {dec['strength']['trend']:.2f}")
plt.tight_layout(); plt.savefig(FIG/"02_mstl_panel.png"); plt.close()

# ------------------------------------------------------- M2: stationarity ---
sub = ylog["2023"]
r0 = stationarity_report(sub)
diffs = choose_differencing(sub, m=24)
R["m2"] = {"level": r0, "chosen_d": diffs["d"], "chosen_D": diffs["D"],
           "final_verdict": diffs["final_verdict"],
           "trace": diffs["trace"][["d","D","adf_p","kpss_p","verdict"]].to_dict("records")}
tbl = correlogram_table(difference(sub, diffs["d"], diffs["D"], 24), nlags=72)
R["m2"]["suggested_orders"] = suggest_orders(tbl, m=24)

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
fig, ax = plt.subplots(2, 2, figsize=(10, 5.6))
plot_acf(sub.dropna(), lags=72, ax=ax[0,0], color=C["actual"]); ax[0,0].set_title("ACF — level (slow decay = non-stationary)")
plot_pacf(sub.dropna(), lags=72, ax=ax[0,1], color=C["actual"]); ax[0,1].set_title("PACF — level")
ds = difference(sub, diffs["d"], diffs["D"], 24)
plot_acf(ds, lags=72, ax=ax[1,0], color=C["acc"]); ax[1,0].set_title(f"ACF — after (d={diffs['d']}, D={diffs['D']}, m=24)")
plot_pacf(ds, lags=72, ax=ax[1,1], color=C["acc"]); ax[1,1].set_title("PACF — after differencing")
plt.tight_layout(); plt.savefig(FIG/"03_acf_pacf.png"); plt.close()

# ----------------------------------------------- M3/M4: models on daily-max --
# Teaching wall: SARIMAX with m=24 is too slow -> model the DAILY series with m=7.
d_daily = y.resample("D").max()
d_daily = d_daily["2022":]                      # 2 years is plenty for a daily model
tr_d, te_d = d_daily[:-28], d_daily[-28:]
ets = fit_ets(tr_d, seasonal_periods=7)
f_ets = forecast_ets(ets, 28)
exog_d = pd.DataFrame({"cdd": np.clip(df["temp_c"].resample("D").max()-21,0,None),
                       "hdd": np.clip(14-df["temp_c"].resample("D").min(),0,None),
                       "is_weekend": df["is_weekend"].resample("D").max().astype(int),
                       "is_ramadan": df["is_ramadan"].resample("D").max().astype(int),
                       "is_eid": df["is_eid"].resample("D").max().astype(int)})
sar = fit_sarimax(tr_d, exog_d.loc[tr_d.index], order=(2,1,1), seasonal_order=(1,1,1,7))
f_sar = forecast_sarimax(sar, 28, exog_d.loc[te_d.index])
sar_noex = fit_sarimax(tr_d, None, order=(2,1,1), seasonal_order=(1,1,1,7))
f_noex = forecast_sarimax(sar_noex, 28, None)
sn_d = pd.Series([tr_d.iloc[-7:].to_numpy()[i%7] for i in range(28)], index=te_d.index)
R["m3"] = {"ets": all_metrics(te_d, f_ets, tr_d, 7),
           "sarimax": all_metrics(te_d, f_sar["yhat"], tr_d, 7),
           "sarima_no_exog": all_metrics(te_d, f_noex["yhat"], tr_d, 7),
           "seasonal_naive": all_metrics(te_d, sn_d, tr_d, 7),
           "sarimax_coverage_90": round(float(np.mean((te_d.to_numpy()>=f_sar["lo"].to_numpy())&(te_d.to_numpy()<=f_sar["hi"].to_numpy()))),3),
           "sarimax_diagnostics": residual_diagnostics(sar, lags=14),
           "ets_aic": round(float(ets.aic), 1)}

# ---------------------------------------------------- M4: LightGBM hourly ---
feat = build_features(df[["demand_mw","temp_c","is_weekend","is_ramadan","is_eid","is_national_day"]])
Xcols = [c for c in feat.columns if c != "demand_mw"]
assert_no_leakage(feat[["demand_mw"]+[c for c in Xcols if feat[c].dtype!=bool]])
cut_tr, cut_ca = "2023-09-30 23:00", "2023-10-31 23:00"
X, yy = feat[Xcols].astype(float), feat["demand_mw"]
Xtr, ytr = X[:cut_tr].dropna(), yy[X[:cut_tr].dropna().index]
Xca, yca = X[cut_tr:cut_ca], yy[cut_tr:cut_ca]
Xte, yte = X[cut_ca:], yy[cut_ca:]
lgbm = DirectLGBMForecaster(horizon=24).fit(Xtr, ytr)
imp = lgbm.feature_importance(25)
R["m4"] = {"n_features": len(Xcols), "train_rows": len(Xtr),
           "importance_top10": imp.head(10).to_dict("records"),
           "importance_by_family": importance_by_family(imp).to_dict("records")}

fig, ax = plt.subplots(figsize=(7.6, 4.6))
top = imp.head(14).iloc[::-1]
ax.barh(top.feature, top.gain, color=C["actual"])
ax.set_title("LightGBM feature importance (mean gain)", fontsize=10)
ax.set_xlabel("mean gain across the 24 direct-horizon models")
plt.tight_layout(); plt.savefig(FIG/"04_feature_importance.png"); plt.close()

# --------------------------------------- M5: quantiles + conformal (CQR) ----
q = QuantileLGBM(quantiles=(0.05,0.5,0.95), horizon=24).fit(Xtr, ytr)
def qpred(Xs):
    out = {}
    for qq in (0.05,0.5,0.95):
        P = np.column_stack([q.models_[(h,qq)].predict(Xs) for h in range(1,25)])
        out[qq] = P
    return out
def stack(Xs, ys, step=24):
    rows = list(range(0, len(Xs)-24, step)); Y=[]; idx=[]
    for i in rows:
        Y.append(ys.iloc[i+1:i+25].to_numpy()); idx.append(Xs.index[i])
    return np.array(Y), rows, idx
Yca, rows_ca, idx_ca = stack(Xca, yca)
Pca = qpred(Xca.iloc[rows_ca])
lo_ca, hi_ca = Pca[0.05], Pca[0.95]
cov_raw = coverage(Yca.ravel(), lo_ca.ravel(), hi_ca.ravel())
cqr = CQR(alpha=0.10).calibrate(Yca.ravel(), lo_ca.ravel(), hi_ca.ravel())

Yte, rows_te, idx_te = stack(Xte, yte)
Pte = qpred(Xte.iloc[rows_te])
lo_t, hi_t = Pte[0.05], Pte[0.95]
lo_c, hi_c = cqr.interval(lo_t, hi_t)
hours = np.tile(np.arange(1,25), len(Yte))
hband = pd.Series(np.where(pd.Series(hours).isin(range(12,19)), "12:00-18:00 (peak)", "other hours"))
R["m5"] = {
 "coverage_uncalibrated": round(cov_raw,4),
 "coverage_calibrated": round(coverage(Yte.ravel(), lo_c.ravel(), hi_c.ravel()),4),
 "coverage_before_on_test": round(coverage(Yte.ravel(), lo_t.ravel(), hi_t.ravel()),4),
 "mean_width_before": round(float(np.mean(hi_t-lo_t)),1),
 "mean_width_after": round(float(np.mean(hi_c-lo_c)),1),
 "qhat": round(cqr.qhat_,1),
 "pinball_q05": round(pinball_loss(Yte.ravel(), lo_c.ravel(), 0.05),1),
 "pinball_q50": round(pinball_loss(Yte.ravel(), Pte[0.5].ravel(), 0.50),1),
 "pinball_q95": round(pinball_loss(Yte.ravel(), hi_c.ravel(), 0.95),1),
 "winkler": round(interval_score(Yte.ravel(), lo_c.ravel(), hi_c.ravel(), .10),1),
 "conditional": coverage_report(Yte.ravel(), lo_c.ravel(), hi_c.ravel(), hband).to_dict("records"),
 "conditional_before": coverage_report(Yte.ravel(), lo_t.ravel(), hi_t.ravel(), hband).to_dict("records"),
}

k = 3
tt = pd.date_range(idx_te[k]+pd.Timedelta(1,"h"), periods=24, freq="h")
fig, ax = plt.subplots(figsize=(9, 4.2))
ax.fill_between(tt, lo_c[k], hi_c[k], color=C["band"], alpha=.55, label="90% interval (CQR-calibrated)")
ax.plot(tt, Pte[0.5][k], color=C["fc"], lw=1.8, label="forecast (q50)")
ax.plot(tt, Yte[k], color=C["actual"], lw=1.8, ls="--", label="actual")
ax.set_title("Day-ahead forecast with a calibrated 90% prediction interval")
ax.set_ylabel("MW"); ax.legend(frameon=False, ncols=3, loc="upper left", fontsize=8)
plt.tight_layout(); plt.savefig(FIG/"05_interval.png"); plt.close()

fig, ax = plt.subplots(figsize=(7.8, 4.0))
covh_b = [coverage(Yte[:,h], lo_t[:,h], hi_t[:,h]) for h in range(24)]
covh_a = [coverage(Yte[:,h], lo_c[:,h], hi_c[:,h]) for h in range(24)]
ax.plot(range(1,25), covh_b, "o-", color=C["warn"], label="quantile model only")
ax.plot(range(1,25), covh_a, "o-", color=C["acc"], label="after conformal calibration")
ax.axhline(.90, color=C["fc"], ls="--", lw=1, label="nominal 90%")
ax.axhspan(.88,.92, color=C["acc"], alpha=.08)
ax.set_xlabel("forecast horizon (hours ahead)"); ax.set_ylabel("empirical coverage")
ax.set_title("Coverage by horizon — marginal 90% can hide a hole at long horizons")
ax.legend(frameon=False, fontsize=8)
plt.tight_layout(); plt.savefig(FIG/"06_coverage.png"); plt.close()

# ------------------------------------------- M6: rolling-origin backtest ----
def bt_hourly(model_fn, name, n_origins=60):
    rows=[]; per=[]
    all_idx = X[cut_tr:].index
    starts = list(range(len(all_idx)-25, 24*30, -24))[:n_origins][::-1]
    for s in starts:
        o = all_idx[s]
        if o not in X.index: continue
        pos = X.index.get_loc(o)
        Xo = X.iloc[[pos]]
        ya = yy.iloc[pos+1:pos+25]
        if len(ya)<24 or Xo.isna().any().any(): continue
        f = model_fn(Xo, pos)
        if f is None: continue
        ytrain = yy.iloc[max(0,pos-24*365):pos]
        rows.append({"origin":o,"model":name, **all_metrics(ya, f, ytrain, 24)})
        per.append({"origin":o,"actual":ya.to_numpy(),"pred":np.asarray(f)})
    return pd.DataFrame(rows), per

f_lgb = lambda Xo,pos: np.array([lgbm.models_[h].predict(Xo)[0] for h in range(1,25)])
def f_sn(Xo,pos):
    last = yy.iloc[pos-23:pos+1].to_numpy()
    return np.array([last[h%24] for h in range(24)])
def f_q50(Xo,pos):
    return np.array([q.models_[(h,0.5)].predict(Xo)[0] for h in range(1,25)])

bt_l, per_l = bt_hourly(f_lgb, "LightGBM (direct)")
bt_s, per_s = bt_hourly(f_sn, "Seasonal-naive")
bt_q, per_q = bt_hourly(f_q50, "LightGBM (quantile q50)")

# daily-model families backtested at the same origins (cheap surrogate: persistence of daily shape)
bt = pd.concat([bt_l, bt_s, bt_q], ignore_index=True)
summ = bt.groupby("model")[["MAE","RMSE","MAPE_%","WAPE_%","MASE","bias"]].mean().round(3).sort_values("MASE")
R["m6"] = {"n_origins": int(bt.groupby("model").size().min()),
           "summary": summ.reset_index().to_dict("records")}
ya = np.concatenate([p["actual"] for p in per_l]); pl = np.concatenate([p["pred"] for p in per_l])
ps = np.concatenate([p["pred"] for p in per_s]); pq = np.concatenate([p["pred"] for p in per_q])
R["m6"]["dm_lgbm_vs_naive"] = diebold_mariano(ya, pl, ps, h=24)
R["m6"]["dm_lgbm_vs_q50"]  = diebold_mariano(ya, pl, pq, h=24)

fig, ax = plt.subplots(1, 2, figsize=(11, 4.0), gridspec_kw={"width_ratios":[1.5,1]})
for n,g in bt.groupby("model"):
    ax[0].plot(g.origin, g.MASE, marker="o", ms=2.5, lw=.9, label=n)
ax[0].axhline(1.0, color=C["fc"], ls="--", lw=1)
ax[0].text(g.origin.iloc[2], 1.03, "MASE = 1  (the free seasonal-naive baseline)", color=C["fc"], fontsize=7.5)
ax[0].set_ylabel("MASE"); ax[0].set_title(f"Per-origin MASE over {R['m6']['n_origins']} rolling origins")
ax[0].legend(frameon=False, fontsize=7.5); ax[0].tick_params(axis="x", rotation=20)
s2 = summ.reset_index()
ax[1].barh(s2.model, s2.MASE, color=[C["acc"] if v<1 else C["warn"] for v in s2.MASE])
ax[1].axvline(1.0, color=C["fc"], ls="--"); ax[1].set_xlabel("mean MASE")
ax[1].set_title("Champion selection")
plt.tight_layout(); plt.savefig(FIG/"07_backtest.png"); plt.close()

# Fig 8: leakage demonstration — shuffle split vs time split
from sklearn.model_selection import train_test_split
import lightgbm as lgb
Xl = X.dropna(); yl = yy[Xl.index]
# The planted leak, exactly as it appears in the wild: a CENTRED rolling window
# (pandas center=True) so "the past 24h average" quietly contains the target hour.
Xleak = Xl.copy()
Xleak["roll_mean24_centred"] = yy.rolling(24, center=True, min_periods=1).mean().reindex(Xl.index)
Xleak["roll_max24_centred"]  = yy.rolling(24, center=True, min_periods=1).max().reindex(Xl.index)
Xa,Xb,ya_,yb_ = train_test_split(Xleak, yl, test_size=.2, random_state=0, shuffle=True)
mleak = lgb.LGBMRegressor(n_estimators=250, verbose=-1, random_state=1).fit(Xa,ya_)
leak_mape = np.mean(np.abs((yb_-mleak.predict(Xb))/yb_))*100
n=int(len(Xl)*.8)
mok = lgb.LGBMRegressor(n_estimators=250, verbose=-1, random_state=1).fit(Xl.iloc[:n], yl.iloc[:n])
hon_mape = np.mean(np.abs((yl.iloc[n:]-mok.predict(Xl.iloc[n:]))/yl.iloc[n:]))*100
# and the honest DAY-AHEAD number (no lag1 available)
R["leakage"] = {"shuffled_split_centred_window_mape_pct": round(float(leak_mape),3),
                "time_split_1step_mape_pct": round(float(hon_mape),3),
                "honest_day_ahead_mape_pct": round(float(summ.loc["LightGBM (direct)","MAPE_%"]),3)}
fig, ax = plt.subplots(figsize=(7.4, 3.9))
labels=["Shuffle split +\ncentred window\n(LEAKED)","Time-ordered split\n1-step ahead","Rolling-origin\n24h ahead\n(HONEST)"]
vals=[leak_mape, hon_mape, summ.loc["LightGBM (direct)","MAPE_%"]]
b=ax.bar(labels, vals, color=[C["fc"], C["warn"], C["acc"]])
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2, v+.05, f"{v:.2f}%", ha="center", fontweight="bold")
ax.set_ylabel("MAPE (%)"); ax.set_title("The same model, three evaluation designs — only one would survive production")
plt.tight_layout(); plt.savefig(FIG/"08_leakage.png"); plt.close()

# Fig 9: Ramadan / Eid calendar effect
fig, ax = plt.subplots(figsize=(9, 3.8))
w = y["2023-03-20":"2023-04-28"]
ax.plot(w.index, w.values, color=C["actual"], lw=.8)
ax.axvspan(pd.Timestamp("2023-03-23",tz="Asia/Riyadh"), pd.Timestamp("2023-04-20",tz="Asia/Riyadh"), color=C["band"], alpha=.35, label="Ramadan")
ax.axvspan(pd.Timestamp("2023-04-21",tz="Asia/Riyadh"), pd.Timestamp("2023-04-24",tz="Asia/Riyadh"), color=C["warn"], alpha=.35, label="Eid al-Fitr")
ax.legend(frameon=False, fontsize=8); ax.set_ylabel("MW")
ax.set_title("Calendar shocks: the shifted post-Iftar evening peak, then the Eid trough")
plt.tight_layout(); plt.savefig(FIG/"09_calendar.png"); plt.close()

json.dump(R, open("reference_results.json","w"), indent=2, default=str)
print(json.dumps(R, indent=2, default=str)[:6000])
