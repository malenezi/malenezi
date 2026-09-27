"""The leakage demonstration, done at the horizon the service actually forecasts.

Same LightGBM, same features, one target: demand 24 hours ahead.
Only the *evaluation design* and one feature change.
"""
import sys, json, warnings, numpy as np, pandas as pd
sys.path.insert(0,"src"); warnings.filterwarnings("ignore")
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from tayyar.data.load import load_demand, load_calendar, join_calendar
from tayyar.features.build import build_features

df = join_calendar(load_demand("data/ksa_grid_demand.csv"), load_calendar("data/ksa_calendar.csv"))
F = build_features(df[["demand_mw","temp_c","is_weekend","is_ramadan","is_eid","is_national_day"]])
X = F[[c for c in F.columns if c!="demand_mw"]].astype(float)
y = F["demand_mw"]
Y24 = y.shift(-24)                      # the day-ahead target

# the planted leak: a CENTRED 24h window — "the past day's average" that isn't
Xleak = X.copy()
Xleak["roll_mean24_centred"] = y.rolling(24, center=True, min_periods=1).mean()
Xleak["roll_max24_centred"]  = y.rolling(24, center=True, min_periods=1).max()
Xleak["demand_next_day_mean"] = y.shift(-24).rolling(6, min_periods=1).mean()  # exog "known" that isn't

ok = X.notna().all(axis=1) & Y24.notna()
P = dict(n_estimators=300, learning_rate=.06, num_leaves=63, verbose=-1, random_state=1)
mape = lambda a,b: float(np.mean(np.abs((np.asarray(a)-np.asarray(b))/np.asarray(a)))*100)

# A. shuffle split + leaky features  -> the number that gets a model promoted
Xa,Xb,ya,yb = train_test_split(Xleak[ok], Y24[ok], test_size=.2, random_state=0, shuffle=True)
A = mape(yb, lgb.LGBMRegressor(**P).fit(Xa,ya).predict(Xb))

# B. shuffle split, clean features   -> how much of it was the split alone
Xa,Xb,ya,yb = train_test_split(X[ok], Y24[ok], test_size=.2, random_state=0, shuffle=True)
B = mape(yb, lgb.LGBMRegressor(**P).fit(Xa,ya).predict(Xb))

# C. time-ordered split, clean features -> honest single split
n = int(ok.sum()*.8); Xo, Yo = X[ok], Y24[ok]
C_ = mape(Yo.iloc[n:], lgb.LGBMRegressor(**P).fit(Xo.iloc[:n],Yo.iloc[:n]).predict(Xo.iloc[n:]))

# D. rolling-origin backtest, clean features -> decision-grade evidence
errs=[]
for k in range(8):
    cut = int(len(Xo)*(0.70+0.03*k))
    m = lgb.LGBMRegressor(**P).fit(Xo.iloc[:cut], Yo.iloc[:cut])
    errs.append(mape(Yo.iloc[cut:cut+720], m.predict(Xo.iloc[cut:cut+720])))
D = float(np.mean(errs))

res = {"A_shuffle_plus_leaky_features": round(A,3), "B_shuffle_clean_features": round(B,3),
       "C_time_split_clean": round(C_,3), "D_rolling_origin_clean": round(D,3),
       "D_spread": [round(min(errs),2), round(max(errs),2)]}
json.dump(res, open("leak_results.json","w"), indent=2); print(json.dumps(res, indent=2))

plt.rcParams.update({"figure.dpi":150,"savefig.dpi":150,"font.size":9,"axes.grid":True,
  "grid.alpha":.25,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white"})
fig, ax = plt.subplots(figsize=(8.6,4.0))
labs=["A  Shuffle split\n+ leaky features","B  Shuffle split\nclean features",
      "C  Time-ordered split\nclean features","D  Rolling-origin backtest\nclean features"]
vals=[A,B,C_,D]; cols=["#A11B2A","#C2601B","#D9A441","#1E7A4D"]
b=ax.bar(labs, vals, color=cols, width=.62)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2, v+.05, f"{v:.2f}%", ha="center", fontweight="bold", fontsize=11)
ax.set_ylabel("day-ahead MAPE (%)"); ax.set_ylim(0, max(vals)*1.25)
ax.set_title("One model, one dataset, one target — four evaluation designs.\nOnly D is a number you could defend to a regulator.", fontsize=10.5)
plt.tight_layout(); plt.savefig("figures/08_leakage.png"); plt.close()
print("wrote figures/08_leakage.png")
