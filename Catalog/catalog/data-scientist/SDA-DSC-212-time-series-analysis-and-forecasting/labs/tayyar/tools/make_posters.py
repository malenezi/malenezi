"""A4 landscape posters for the classroom wall."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
OUT=Path("instructor/posters"); OUT.mkdir(parents=True, exist_ok=True)
INK="#0E1B2B"; MID="#13497B"; TEAL="#1C7293"; BAD="#A11B2A"; GOOD="#1E7A4D"
WARN="#C2601B"; SKY="#8FB8DE"; MUT="#5A6B7C"; GOLD="#D9A441"
A4=(11.69,8.27)

def frame(title, sub=None):
    fig,ax=plt.subplots(figsize=A4); ax.set_xlim(0,10); ax.set_ylim(0,7.2); ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.text(0.25,6.85,title,fontsize=22,fontweight="bold",color=INK,va="top")
    if sub: ax.text(0.25,6.28,sub,fontsize=11,color=MUT,va="top")
    ax.text(9.75,-0.10,"SDA-DSC-212 · SDAIA Academy",fontsize=7.5,color=MUT,ha="right")
    return fig,ax
def box(ax,x,y,w,h,t,fc,tc="white",fs=10,bold=True):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0,rounding_size=0.05",fc=fc,ec=fc))
    ax.text(x+w/2,y+h/2,t,ha="center",va="center",color=tc,fontsize=fs,
            fontweight="bold" if bold else "normal",linespacing=1.5)

# ---------------------------------------------------- P1 leakage smells -----
fig,ax=frame("The four leakage smells",
  "If you see one of these, the accuracy number on the slide is not real. Point at this poster.")
smells=[("train_test_split(\n    shuffle=True)","Test rows end up preceding\ntraining rows. The model is scored\non hours whose future it has seen.",
         "Split by TIME. Always.\nThere is no exception for\n'just a quick check'."),
        ("rolling(w,\n    center=True)","The window spans [t−12, t+11]\nfor w = 24 — it swallows the target\nhour and its neighbours.",
         "y.shift(1).rolling(\n    w, center=False)\nThe window must END before t."),
        ("scaler.fit(\n    all_data)","The mean and standard deviation\nof the future are subtracted\nfrom the past.",
         "Fit every scaler, encoder and\nimputer on the training slice\nonly, inside the backtest loop."),
        ("exog =\n    realised_temp","At 14:00 you do not have\ntomorrow's realised temperature.\nYou have a forecast of it.",
         "Use the FORECAST of the\ncovariate, and let its error\nwiden your interval honestly.")]
ax.text(3.85,5.92,"why it is a leak",fontsize=9,color=MUT,fontweight="bold")
ax.text(7.15,5.92,"the fix",fontsize=9,color=MUT,fontweight="bold")
for i,(smell,why,fix) in enumerate(smells):
    y=4.62-i*1.24
    box(ax,0.25,y,3.35,1.10,"",BAD if i<2 else WARN)
    ax.text(0.45,y+0.90,"✕",fontsize=13,color="white",fontweight="bold",va="center")
    ax.text(0.45,y+0.42,smell,fontsize=10,color="white",fontweight="bold",family="monospace",
            va="center",linespacing=1.5)
    ax.text(3.85,y+0.55,why,fontsize=9,color=INK,va="center",linespacing=1.6)
    ax.text(7.15,y+0.55,fix,fontsize=9,color=GOOD,va="center",linespacing=1.6,fontweight="bold",
            family="monospace" if i<2 else "sans-serif")
ax.text(0.25,0.30,"Every feature, every split and every scaler must be computable using only data that existed at the forecast origin.",
        fontsize=12,style="italic",color=MID)
fig.savefig(OUT/"P1_leakage_smells.pdf",bbox_inches="tight"); fig.savefig(OUT/"P1_leakage_smells.png",dpi=150,bbox_inches="tight"); plt.close()

# ---------------------------------------------------- P2 ADF/KPSS -----------
fig,ax=frame("ADF and KPSS have opposite null hypotheses",
  "ADF  H₀ = unit root → a small p means STATIONARY        KPSS  H₀ = stationary → a small p means NON-STATIONARY")
ax.text(3.5,5.55,"KPSS says stationary\np > 0.05",ha="center",fontsize=12,fontweight="bold",color=INK)
ax.text(7.3,5.55,"KPSS says non-stationary\np < 0.05",ha="center",fontsize=12,fontweight="bold",color=INK)
ax.text(1.1,3.95,"ADF says\nstationary\np < 0.05",ha="center",va="center",fontsize=12,fontweight="bold",color=INK)
ax.text(1.1,1.75,"ADF says\nnon-stationary\np > 0.05",ha="center",va="center",fontsize=12,fontweight="bold",color=INK)
for x,y,c,t in [(2.1,3.1,GOOD,"STATIONARY\n\nproceed — no differencing"),
                (5.9,3.1,WARN,"DIFFERENCE-STATIONARY\n\ndifference once, then re-test"),
                (2.1,0.9,TEAL,"TREND-STATIONARY\n\ndetrend, or add a trend\nregressor — do not difference"),
                (5.9,0.9,BAD,"NON-STATIONARY\n\ndifference and re-test")]:
    box(ax,x,y,2.8,1.9,t,c,fs=11)
ax.text(0.25,0.35,"Difference as little as possible. Seasonal first, then regular. Over-differencing injects artificial negative lag-1 autocorrelation.",
        fontsize=11,style="italic",color=MID)
fig.savefig(OUT/"P2_adf_kpss.pdf",bbox_inches="tight"); fig.savefig(OUT/"P2_adf_kpss.png",dpi=150,bbox_inches="tight"); plt.close()

# ---------------------------------------------------- P3 metric decision ----
fig,ax=frame("Which metric, and what it hides",
  "Report MASE alongside a percentage metric. The percentage is what a planner feels; the MASE is what makes it comparable.")
rows=[("MAE","mean |y − ŷ|","same units, robust","not comparable across series of different scale",MID),
      ("RMSE","√ mean (y − ŷ)²","penalises large misses","dominated by outliers; scale-bound",MID),
      ("MAPE","mean |y − ŷ| / |y|","scale-free, intuitive","explodes near zero; over-forecasts capped at 100%",WARN),
      ("sMAPE","symmetric percentage","bounded","still unstable near zero; awkward to interpret",WARN),
      ("MASE","MAE / MAE of seasonal-naive","scale-free, symmetric, defined at zero","needs a sensible baseline period m",GOOD),
      ("Pinball","the quantile loss, averaged","a PROPER score — rewards honest calibration","only meaningful for a probabilistic forecast",GOOD),
      ("Coverage","P(y inside the interval)","the number operations feels","marginal coverage hides conditional holes",GOOD)]
ax.text(0.30,5.85,"metric",fontsize=9,color=MUT,fontweight="bold")
ax.text(1.55,5.85,"formula",fontsize=9,color=MUT,fontweight="bold")
ax.text(4.30,5.85,"strength",fontsize=9,color=MUT,fontweight="bold")
ax.text(6.60,5.85,"fails when",fontsize=9,color=MUT,fontweight="bold")
for i,(m,f,s,w,c) in enumerate(rows):
    y=5.25-i*0.72
    ax.add_patch(Rectangle((0.25,y),9.5,0.62,fc="#F1F5F9" if i%2 else "white",ec="none"))
    ax.add_patch(Rectangle((0.25,y),0.09,0.62,fc=c,ec="none"))
    ax.text(0.52,y+0.31,m,fontsize=11,fontweight="bold",color=c,va="center")
    ax.text(1.55,y+0.31,f,fontsize=9.5,color=INK,va="center",family="monospace")
    ax.text(4.30,y+0.31,s,fontsize=9.5,color=INK,va="center")
    ax.text(6.60,y+0.31,w,fontsize=9.5,color=MUT,va="center")
ax.text(0.25,0.30,"MASE < 1 beats the free seasonal-naive baseline · MASE = 1 ties it · MASE > 1 means you should have shipped the baseline.",
        fontsize=11.5,style="italic",color=MID)
fig.savefig(OUT/"P3_metrics.pdf",bbox_inches="tight"); fig.savefig(OUT/"P3_metrics.png",dpi=150,bbox_inches="tight"); plt.close()

# ---------------------------------------------------- P4 ACF/PACF card ------
import numpy as np
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import acf, pacf
np.random.seed(7)
series={"AR(2)":ArmaProcess([1,-0.6,-0.25],[1]).generate_sample(900),
        "MA(1)":ArmaProcess([1],[1,0.75]).generate_sample(900),
        "ARMA(1,1)":ArmaProcess([1,-0.6],[1,0.5]).generate_sample(900),
        "Random walk":np.cumsum(np.random.normal(size=900))}
verdict={"AR(2)":"PACF cuts off after lag 2\n→ AR(2)","MA(1)":"ACF cuts off after lag 1\n→ MA(1)",
         "ARMA(1,1)":"both tail off\n→ ARMA; use AICc/BIC","Random walk":"ACF decays slowly and linearly\n→ NOT stationary. Difference first."}
fig=plt.figure(figsize=A4); fig.patch.set_facecolor("white")
fig.suptitle("The correlogram fingerprint", fontsize=22, fontweight="bold", color=INK, x=0.055, ha="left", y=0.975)
fig.text(0.055,0.925,"AR → PACF cuts off · MA → ACF cuts off · ARMA → both tail off · slow linear decay → difference before reading further",
         fontsize=11,color=MUT)
for j,(n,x) in enumerate(series.items()):
    a=acf(x,nlags=14); p=pacf(x,nlags=14); band=1.96/np.sqrt(len(x))
    for i,(v,t) in enumerate([(a,"ACF"),(p,"PACF")]):
        A=fig.add_subplot(3,4,j+1+i*4)
        A.bar(range(len(v)),v,color=MID,width=.55); A.axhspan(-band,band,color=SKY,alpha=.35)
        A.set_ylim(-1.05,1.05); A.tick_params(labelsize=7); A.grid(alpha=.2)
        A.set_title(f"{n} — {t}" if i==0 else t, fontsize=10 if i==0 else 9,
                    color=INK if i==0 else MUT, fontweight="bold" if i==0 else "normal")
        for sp in ("top","right"): A.spines[sp].set_visible(False)
    B=fig.add_subplot(3,4,j+9); B.axis("off")
    B.add_patch(FancyBboxPatch((0.02,0.15),0.96,0.7,boxstyle="round,pad=0,rounding_size=0.06",
        fc="#EAF2EC" if n!="Random walk" else "#FBEEEC",ec="none",transform=B.transAxes))
    B.text(0.5,0.5,verdict[n],ha="center",va="center",fontsize=10,fontweight="bold",
           color=GOOD if n!="Random walk" else BAD, transform=B.transAxes, linespacing=1.6)
fig.text(0.055,0.035,'"Cuts off" means it drops inside the ±1.96/√n band. The default lags=20 never reaches lag 24 — set lags ≥ 2m or the seasonal spike is invisible.',
         fontsize=10.5,style="italic",color=MID)
plt.tight_layout(rect=[0.03,0.06,0.98,0.90])
fig.savefig(OUT/"P4_fingerprint.pdf",bbox_inches="tight"); fig.savefig(OUT/"P4_fingerprint.png",dpi=150,bbox_inches="tight"); plt.close()

# ---------------------------------------------------- P5 additive anchor ----
fig,ax=frame("Every series is three things at once",
             "The shared vocabulary between the data scientist and the decision-maker.")
box(ax,0.25,4.55,9.5,1.55,"",  "#0D2136")
ax.text(0.75,5.62,"yₜ  =  Tₜ  +  Sₜ  +  Rₜ",fontsize=26,color="white",fontweight="bold",va="center",family="serif")
ax.text(0.75,4.95,"additive",fontsize=11,color=GOLD,fontweight="bold",va="center")
ax.text(5.4,5.62,"yₜ  =  Tₜ × Sₜ × Rₜ",fontsize=26,color="white",fontweight="bold",va="center",family="serif")
ax.text(5.4,4.95,"multiplicative  ⟺  log y = log T + log S + log R",fontsize=11,color=GOLD,fontweight="bold",va="center")
parts=[("Tₜ  trend","the long-run level — growth, decline, a structural break","#F08A5D"),
       ("Sₜ  seasonality","the repeating pattern of KNOWN period: 24, 168, 8766","#6BCB77"),
       ("Rₜ  remainder","what neither explains — and where a missing covariate hides","#8FB8DE")]
for i,(k,v,c) in enumerate(parts):
    y=3.55-i*0.85
    ax.add_patch(Rectangle((0.25,y),0.12,0.68,fc=c,ec="none"))
    ax.text(0.62,y+0.34,k,fontsize=13,fontweight="bold",color=INK,va="center")
    ax.text(3.1,y+0.34,v,fontsize=11.5,color=MUT,va="center")
box(ax,0.25,0.55,9.5,0.75,"Decide on EVIDENCE: correlate the per-cycle level with the per-cycle amplitude.\nIf the swing grows with the level, the series is multiplicative — model log(y).",
    "#F1F5F9",tc=MID,fs=11.5)
fig.savefig(OUT/"P5_additive_model.pdf",bbox_inches="tight"); fig.savefig(OUT/"P5_additive_model.png",dpi=150,bbox_inches="tight"); plt.close()

# ---------------------------------------------------- combined booklet ------
with PdfPages(OUT/"ALL_POSTERS.pdf") as pdf:
    for f in ["P1_leakage_smells","P2_adf_kpss","P3_metrics","P4_fingerprint","P5_additive_model"]:
        import matplotlib.image as mpimg
        img=mpimg.imread(OUT/f"{f}.png")
        fg,axx=plt.subplots(figsize=A4); axx.imshow(img); axx.axis("off")
        pdf.savefig(fg,bbox_inches="tight"); plt.close(fg)
print("posters written to", OUT)
