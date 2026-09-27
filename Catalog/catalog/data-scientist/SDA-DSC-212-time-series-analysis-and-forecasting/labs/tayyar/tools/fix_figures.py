import sys, warnings, numpy as np, pandas as pd
sys.path.insert(0,"src"); warnings.filterwarnings("ignore")
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from tayyar.data.load import load_demand, load_calendar, join_calendar
from tayyar.analysis.decompose import mstl_decompose
plt.rcParams.update({"figure.dpi":150,"savefig.dpi":150,"font.size":9,"axes.grid":True,
 "grid.alpha":.25,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white"})
C={"actual":"#1F3864","fc":"#C00000","base":"#7F7F7F","band":"#8FAADC","acc":"#2E7D32","warn":"#ED7D31"}

df = join_calendar(load_demand("data/ksa_grid_demand.csv"), load_calendar("data/ksa_calendar.csv"))
y = df["demand_mw"].astype(float)
ylog = np.log(y).interpolate("time").ffill().bfill()   # STL cannot handle NaN
dec = mstl_decompose(ylog, periods=(24,24*7))
# reattach the DatetimeIndex that MSTL drops
idx = ylog.index
tr = pd.Series(np.asarray(dec["trend"]), index=idx)
rm = pd.Series(np.asarray(dec["remainder"]), index=idx)
se = pd.Series(np.asarray(dec["seasonal"].iloc[:,0]), index=idx)
sw = pd.Series(np.asarray(dec["seasonal"].iloc[:,1]), index=idx)
sl = slice("2023-06-01","2023-08-31")
fig, ax = plt.subplots(5,1, figsize=(10,7.6), sharex=True)
np.exp(ylog[sl]).plot(ax=ax[0], color=C["actual"], lw=.6); ax[0].set_ylabel("Observed\n(MW)")
np.exp(tr[sl]).plot(ax=ax[1], color=C["fc"], lw=1.6); ax[1].set_ylabel("Trend\n(MW)")
se[sl].plot(ax=ax[2], color=C["acc"], lw=.5); ax[2].set_ylabel("Daily\nseasonal")
sw[sl].plot(ax=ax[3], color="#7030A0", lw=.7); ax[3].set_ylabel("Weekly\nseasonal")
rm[sl].plot(ax=ax[4], color=C["base"], lw=.4); ax[4].set_ylabel("Remainder")
ax[0].set_title(f"MSTL of log(demand), summer 2023  ·  daily strength {dec['strength']['seasonal_24']:.2f}"
                f"  ·  weekly {dec['strength']['seasonal_168']:.2f}  ·  trend {dec['strength']['trend']:.2f}", fontsize=10)
for a in ax: a.set_xlabel("")
ax[4].set_xlabel("")
plt.tight_layout(); plt.savefig("figures/02_mstl_panel.png"); plt.close()

# ---- 09 calendar, legend inside, no clipping
fig, ax = plt.subplots(figsize=(9,3.6))
w = y["2023-03-20":"2023-04-28"]
ax.plot(w.index, w.values, color=C["actual"], lw=.8)
TZ="Asia/Riyadh"
ax.axvspan(pd.Timestamp("2023-03-23",tz=TZ), pd.Timestamp("2023-04-20",tz=TZ), color=C["band"], alpha=.40, label="Ramadan")
ax.axvspan(pd.Timestamp("2023-04-21",tz=TZ), pd.Timestamp("2023-04-24",tz=TZ), color=C["warn"], alpha=.40, label="Eid al-Fitr")
ax.legend(frameon=False, fontsize=8.5, loc="lower left", ncols=2)
import matplotlib.dates as mdates
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
for lab in ax.get_xticklabels(): lab.set_fontsize(8)
ax.set_ylabel("MW"); ax.margins(x=0.01)
ax.set_title("Calendar shocks: the shifted post-Iftar evening peak, then the Eid trough", fontsize=10)
plt.tight_layout(); plt.savefig("figures/09_calendar.png"); plt.close()
print("02, 09 rebuilt")
