"""Conceptual diagrams for the deck and the A4 posters."""
import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
plt.rcParams.update({"figure.dpi":170,"savefig.dpi":170,"font.size":9,
  "figure.facecolor":"white","axes.facecolor":"white"})
INK="#0E1B2B"; MID="#13497B"; TEAL="#1C7293"; BAD="#A11B2A"; GOOD="#1E7A4D"
WARN="#C2601B"; SKY="#8FB8DE"; MUT="#5A6B7C"; GOLD="#D9A441"

def box(ax,x,y,w,h,t,fc,tc="white",fs=9,bold=True,r=0.02):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc,ec=fc)); ax.text(x+w/2,y+h/2,t,ha="center",va="center",color=tc,
        fontsize=fs,fontweight="bold" if bold else "normal",linespacing=1.4)
def arrow(ax,x1,y1,x2,y2,c=MUT,lw=1.6):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=13,
        color=c,lw=lw,shrinkA=0,shrinkB=0))

# ---------------------------------------------------------- D1 leakage split
fig,ax=plt.subplots(figsize=(9,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis("off")
ax.text(0,3.15,"WRONG — random shuffle split",color=BAD,fontsize=11,fontweight="bold")
np.random.seed(3); marks=np.sort(np.random.choice(60,14,replace=False))
for i in range(60):
    c = BAD if i in marks else SKY
    ax.add_patch(Rectangle((0.15+i*0.155,2.45),0.135,0.34,fc=c,ec="none"))
ax.text(0.15,2.22,"test points scattered through the past — the model is scored on hours it has already seen the future of",
        fontsize=7.8,color=BAD)
ax.plot([0.15,9.45],[2.05,2.05],color="#D8E0E8",lw=1)
ax.text(0,1.72,"RIGHT — past → future split",color=GOOD,fontsize=11,fontweight="bold")
for i in range(60):
    c = GOOD if i>=44 else MID
    ax.add_patch(Rectangle((0.15+i*0.155,1.0),0.135,0.34,fc=c,ec="none"))
ax.annotate("forecast origin",xy=(0.15+44*0.155,0.98),xytext=(0.15+38*0.155,0.45),
    fontsize=8,color=INK,arrowprops=dict(arrowstyle="->",color=INK,lw=1.2))
ax.text(0.2,1.42,"TRAIN — everything that existed at the origin",fontsize=8,color=MID,fontweight="bold")
ax.text(7.0,1.42,"TEST — the future",fontsize=8,color=GOOD,fontweight="bold")
ax.text(0.15,0.12,"time  ————————————————————————————————————————————————————————————▶",fontsize=8,color=MUT)
plt.tight_layout(); plt.savefig("figures/D1_leakage_split.png",bbox_inches="tight"); plt.close()

# ---------------------------------------------------------- D2 ADF/KPSS 2x2
fig,ax=plt.subplots(figsize=(7.4,4.3)); ax.set_xlim(0,10); ax.set_ylim(0,6.2); ax.axis("off")
ax.text(5.2,5.95,"ADF and KPSS have OPPOSITE null hypotheses",ha="center",fontsize=11.5,
        fontweight="bold",color=INK)
ax.text(5.2,5.6,"ADF  H₀ = unit root → small p means STATIONARY        KPSS  H₀ = stationary → small p means NON-STATIONARY",
        ha="center",fontsize=8.2,color=MUT)
ax.text(3.65,5.05,"KPSS says stationary\n(p > 0.05)",ha="center",fontsize=9,fontweight="bold",color=INK)
ax.text(7.65,5.05,"KPSS says non-stationary\n(p < 0.05)",ha="center",fontsize=9,fontweight="bold",color=INK)
ax.text(0.95,3.55,"ADF says\nstationary\n(p < 0.05)",ha="center",va="center",fontsize=9,fontweight="bold",color=INK)
ax.text(0.95,1.35,"ADF says\nnon-stationary\n(p > 0.05)",ha="center",va="center",fontsize=9,fontweight="bold",color=INK)
cells=[(2.0,2.6,GOOD,"STATIONARY\nproceed\nno differencing"),
       (6.0,2.6,WARN,"DIFFERENCE-\nSTATIONARY\ndifference once,\nre-test"),
       (2.0,0.4,TEAL,"TREND-STATIONARY\ndetrend rather\nthan difference"),
       (6.0,0.4,BAD,"NON-STATIONARY\ndifference\nand re-test")]
for x,y,c,t in cells: box(ax,x,y,3.3,1.9,t,c,fs=8.6,r=0.04)
plt.tight_layout(); plt.savefig("figures/D2_adf_kpss.png",bbox_inches="tight"); plt.close()

# ---------------------------------------------------------- D3 rolling origin
fig,ax=plt.subplots(figsize=(9,4.0)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis("off")
ax.text(0,4.35,"EXPANDING window — training set grows, keeps all history",fontsize=10,fontweight="bold",color=MID)
for k in range(4):
    y=3.65-k*0.42
    ax.add_patch(Rectangle((0.15,y),1.6+k*1.35,0.3,fc=MID,ec="none"))
    ax.add_patch(Rectangle((1.80+k*1.35,y),0.75,0.3,fc=GOOD,ec="none"))
    ax.text(9.3,y+0.15,f"origin {k+1}",fontsize=7.5,va="center",color=MUT)
ax.text(0,1.75,"SLIDING window — fixed length, forgets the oldest data",fontsize=10,fontweight="bold",color=TEAL)
for k in range(4):
    y=1.05-k*0.24 if False else 1.05-k*0.42+0.0
for k in range(4):
    y=1.30-k*0.30
    ax.add_patch(Rectangle((0.15+k*1.35,y),1.6,0.22,fc=TEAL,ec="none"))
    ax.add_patch(Rectangle((1.80+k*1.35,y),0.75,0.22,fc=GOOD,ec="none"))
ax.text(0.15,0.16,"train",fontsize=8,color=MID,fontweight="bold")
ax.text(0.95,0.16,"|  forecast horizon (24 h)",fontsize=8,color=GOOD,fontweight="bold")
ax.text(4.6,0.16,"|  refit at EVERY origin — a fit-once loop scores points the model already saw",fontsize=8,color=BAD)
plt.tight_layout(); plt.savefig("figures/D3_rolling_origin.png",bbox_inches="tight"); plt.close()

# ---------------------------------------------------------- D4 pinball loss
fig,ax=plt.subplots(figsize=(6.6,3.9))
e=np.linspace(-3,3,400)
for tau,c,ls in [(0.5,MUT,"--"),(0.9,MID,"-"),(0.05,TEAL,"-")]:
    ax.plot(e,np.maximum(tau*e,(tau-1)*e),color=c,lw=2,ls=ls,label=f"τ = {tau}")
ax.axvline(0,color="#D8E0E8",lw=1); ax.axhline(0,color="#D8E0E8",lw=1)
ax.annotate("under-forecast\n(y > ŷ) — costs τ per unit",xy=(1.55,1.40),xytext=(-0.35,2.35),
    fontsize=8,color=MID,arrowprops=dict(arrowstyle="->",color=MID))
ax.annotate("over-forecast\n(y < ŷ) — costs 1−τ per unit",xy=(-2.4,0.25),xytext=(-2.95,1.35),
    fontsize=8,color=MID,arrowprops=dict(arrowstyle="->",color=MID))
ax.set_xlabel("forecast error  e = y − ŷ"); ax.set_ylabel("pinball loss")
ax.set_title("L_τ(y, ŷ) = max( τ·e , (τ−1)·e )\nMinimising it at τ recovers the τ-th percentile",fontsize=10)
ax.legend(frameon=False,fontsize=8.5,loc="upper right"); ax.grid(alpha=.25); ax.set_ylim(-0.1,3.3)
for sp in ("top","right"): ax.spines[sp].set_visible(False)
plt.tight_layout(); plt.savefig("figures/D4_pinball.png"); plt.close()

# ---------------------------------------------------------- D5 tradeoff radar
labels=["Accuracy","Explainability","Interval\nquality","Speed /\nlatency","Low\nmaintenance"]
data={"Seasonal-naive":[1,5,1,5,5],"ETS":[3,4.2,3.5,4.6,4.4],
      "SARIMAX":[3.8,4.4,4.2,2.8,3.2],"LightGBM + CQR":[4.8,2.8,4.6,3.8,2.2]}
cols={"Seasonal-naive":MUT,"ETS":TEAL,"SARIMAX":MID,"LightGBM + CQR":GOLD}
ang=np.linspace(0,2*np.pi,len(labels),endpoint=False).tolist(); ang+=ang[:1]
fig,ax=plt.subplots(figsize=(5.6,5.2),subplot_kw=dict(polar=True))
for k,v in data.items():
    vv=v+v[:1]; ax.plot(ang,vv,color=cols[k],lw=2,label=k); ax.fill(ang,vv,color=cols[k],alpha=.09)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(labels,fontsize=9)
ax.set_yticks([1,2,3,4,5]); ax.set_yticklabels(["1","2","3","4","5"],fontsize=7,color=MUT)
ax.set_ylim(0,5.4); ax.grid(alpha=.3)
ax.set_title("No row dominates — every cell that matters is a negotiation with a constraint",
             fontsize=9.5,pad=22)
ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.06),ncols=2,frameon=False,fontsize=8.5)
plt.tight_layout(); plt.savefig("figures/D5_tradeoff_radar.png",bbox_inches="tight"); plt.close()

# ---------------------------------------------------------- D6 pipeline
fig,ax=plt.subplots(figsize=(11,2.5)); ax.set_xlim(0,11); ax.set_ylim(0,2.5); ax.axis("off")
steps=[("M1","load · index\ndecompose",MID),("M2","stationarity\n(d, D)",MID),
       ("M4","leakage-safe\nfeatures",TEAL),("M3·M5","fit candidate\nmodels",TEAL),
       ("M6","rolling-origin\nbacktest",GOOD),("M7","select · decide\nreport",INK)]
for i,(tag,t,c) in enumerate(steps):
    x=0.15+i*1.80
    box(ax,x,0.65,1.55,1.0,t,c,fs=8.6,r=0.04)
    ax.text(x+0.775,1.78,tag,ha="center",fontsize=9,fontweight="bold",color=GOLD)
    if i<5: arrow(ax,x+1.58,1.15,x+1.78,1.15)
ax.text(5.5,0.28,"config.yaml  →  one command  →  every reported number regenerated",
        ha="center",fontsize=9,style="italic",color=MUT)
plt.tight_layout(); plt.savefig("figures/D6_pipeline.png",bbox_inches="tight"); plt.close()

# ---------------------------------------------------------- D7 ACF/PACF cards
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import acf, pacf
np.random.seed(7)
series={"AR(2)":ArmaProcess([1,-0.6,-0.25],[1]).generate_sample(900),
        "MA(1)":ArmaProcess([1],[1,0.75]).generate_sample(900),
        "ARMA(1,1)":ArmaProcess([1,-0.6],[1,0.5]).generate_sample(900),
        "White noise":np.random.normal(size=900)}
fig,axes=plt.subplots(2,4,figsize=(11,4.0))
for j,(n,x) in enumerate(series.items()):
    a=acf(x,nlags=14); p=pacf(x,nlags=14); band=1.96/np.sqrt(len(x))
    for i,(v,ttl) in enumerate([(a,"ACF"),(p,"PACF")]):
        A=axes[i,j]; A.bar(range(len(v)),v,color=MID,width=.55)
        A.axhspan(-band,band,color=SKY,alpha=.35); A.set_ylim(-1.05,1.05)
        A.set_title(f"{n} — {ttl}" if i==0 else ttl,fontsize=8.5,
                    color=INK if i==0 else MUT, fontweight="bold" if i==0 else "normal")
        A.tick_params(labelsize=6.5); A.grid(alpha=.2)
        for sp in ("top","right"): A.spines[sp].set_visible(False)
axes[0,0].set_ylabel("correlation",fontsize=7.5); axes[1,0].set_ylabel("correlation",fontsize=7.5)
fig.suptitle("The fingerprint:  AR → PACF cuts off · MA → ACF cuts off · ARMA → both tail off · white noise → nothing to model",
             fontsize=9.5,y=1.0)
plt.tight_layout(); plt.savefig("figures/D7_fingerprint.png",bbox_inches="tight"); plt.close()
print("diagrams written")
