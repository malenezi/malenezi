"""
tayseer_viz — the course chart + measure library for SDA-DSC-112.

Everything the six labs share lives here so that each notebook can stay about
the *teaching point* rather than about plumbing:

  * DATA          — path resolution, so notebooks run from anywhere
  * measures      — the NON-ADDITIVE measure rules, implemented once, correctly
  * theme         — the Okabe-Ito colour-blind-safe palette and a decluttered
                    matplotlib theme (Module 3's `apply_theme`)
  * charts        — `sorted_bar`, the principle-compliant workhorse (Module 2)
  * arabic        — reshape + bidi + an Arabic-capable font (Module 3)
  * save_fig      — every figure lands in notebooks/out/ at dpi=150

The measure formulas are NOT invented here. They are transcribed from
`data/supporting/kpi_targets.csv`, which is the programme's own semantic layer.
"""
from __future__ import annotations

import os
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# 1. Paths
# --------------------------------------------------------------------------
PKG = Path(__file__).resolve().parent.parent          # .../pkg
DATA = PKG / "data"
DOCS = PKG / "docs"
OUT = PKG / "notebooks" / "out"
OUT.mkdir(parents=True, exist_ok=True)

CORE = DATA / "core"
DIMS = DATA / "dimensions"
SUPP = DATA / "supporting"
INST = DATA / "instructional"


def load(name: str, **kw) -> pd.DataFrame:
    """Load any packaged CSV by bare filename. Files are UTF-8 with BOM."""
    hits = list(DATA.rglob(name if name.endswith(".csv") else name + ".csv"))
    if not hits:
        raise FileNotFoundError(f"{name} not found under {DATA}")
    kw.setdefault("encoding", "utf-8-sig")
    return pd.read_csv(hits[0], **kw)


def load_facts() -> pd.DataFrame:
    """The golden thread: 28,080 rows at month x region x service_category x channel."""
    return load("tayseer_services.csv", parse_dates=["month"])


# --------------------------------------------------------------------------
# 2. Measures — the rules the whole course exists to enforce
# --------------------------------------------------------------------------
# Additive        : transactions, complaints            -> SUM at any grain
# Semi-additive   : unique_users                        -> SUM within a month only
# NON-additive    : digital_adoption_pct, cost_per_txn_sar, csat,
#                   avg_completion_min, sla_met_pct     -> NEVER average;
#                                                          recompute from components
ADDITIVE = ["transactions", "complaints"]
SEMI_ADDITIVE = ["unique_users"]
NON_ADDITIVE = {
    # column                 : weight column  (from kpi_targets.csv)
    "digital_adoption_pct": "unique_users",   # KPI-01
    "cost_per_txn_sar": "transactions",       # KPI-02
    "csat": "transactions",                   # KPI-03
    "avg_completion_min": "transactions",     # KPI-04
    "sla_met_pct": "transactions",            # KPI-05
}

TARGET_ADOPTION = 65.0     # %,   KPI-01 target_2026
TARGET_COST = 18.0         # SAR, KPI-02 target_2026
TARGET_CSAT = 4.3          # 1-5, KPI-03 target_2026

STALLED = ["Jazan", "Najran", "Al-Baha", "Asir", "Northern Borders"]  # Tier 1
SEVERE = ["Jazan", "Najran", "Al-Baha"]        # more than 9pp below target


def wmean(frame: pd.DataFrame, col: str, weight: str | None = None) -> float:
    """Weighted recomputation of a non-additive measure. The ONLY safe rollup.

    `weight` defaults to the weight `kpi_targets.csv` specifies for that column.
    """
    if weight is None:
        if col not in NON_ADDITIVE:
            raise KeyError(
                f"{col!r} has no declared weight. Additive columns use .sum(); "
                f"non-additive ones are {list(NON_ADDITIVE)}."
            )
        weight = NON_ADDITIVE[col]
    w = frame[weight]
    if w.sum() == 0:
        return float("nan")
    return float((frame[col] * w).sum() / w.sum())


def adoption(frame: pd.DataFrame) -> float:
    """KPI-01. SUM(adoption/100 * unique_users) / SUM(unique_users) * 100."""
    return wmean(frame, "digital_adoption_pct", "unique_users")


def cost_per_txn(frame: pd.DataFrame) -> float:
    """KPI-02. SUM(cost * transactions) / SUM(transactions)."""
    return wmean(frame, "cost_per_txn_sar", "transactions")


def csat(frame: pd.DataFrame) -> float:
    """KPI-03. SUM(csat * transactions) / SUM(transactions)."""
    return wmean(frame, "csat", "transactions")


def completion_min(frame: pd.DataFrame) -> float:
    """KPI-04."""
    return wmean(frame, "avg_completion_min", "transactions")


def sla_met(frame: pd.DataFrame) -> float:
    """KPI-05."""
    return wmean(frame, "sla_met_pct", "transactions")


_MEASURE_FN = {
    "digital_adoption_pct": adoption,
    "cost_per_txn_sar": cost_per_txn,
    "csat": csat,
    "avg_completion_min": completion_min,
    "sla_met_pct": sla_met,
}


def by(frame: pd.DataFrame, keys, col: str, name: str | None = None) -> pd.DataFrame:
    """Group and correctly recompute a non-additive measure at that grain.

    Returns a tidy DataFrame with the grouping keys plus one measure column.
    This is the function that replaces every `.groupby(...).mean()` in the course.
    """
    keys = [keys] if isinstance(keys, str) else list(keys)
    if col in ADDITIVE:
        out = frame.groupby(keys, as_index=False)[col].sum()
    elif col in _MEASURE_FN:
        fn = _MEASURE_FN[col]
        out = (
            frame.groupby(keys)
            .apply(fn, include_groups=False)
            .reset_index(name=col)
        )
    else:
        raise KeyError(f"{col!r} is not a declared measure")
    return out.rename(columns={col: name}) if name else out


def naive_by(frame: pd.DataFrame, keys, col: str) -> pd.DataFrame:
    """The BUG, on purpose: a plain AVERAGE of a non-additive column.

    Only ever used in the labs to show the size of the error it produces.
    """
    keys = [keys] if isinstance(keys, str) else list(keys)
    return frame.groupby(keys, as_index=False)[col].mean()


# --------------------------------------------------------------------------
# 3. Theme — Okabe-Ito, colour-blind safe (Module 3)
# --------------------------------------------------------------------------
CATEGORICAL = ["#0072B2", "#E69F00", "#009E73", "#CC79A7",
               "#56B4E9", "#D55E00", "#F0E442"]
GREY = "#B8B8B8"        # context: everything that is not the signal
GREY_DARK = "#5A5A5A"   # text, reference lines
ACCENT = "#D55E00"      # the ONE pre-attentive pop per chart (Okabe-Ito vermillion)
ACCENT_2 = "#0072B2"    # a second, only when two series genuinely compete
SEQUENTIAL = "Blues"    # single hue, light -> dark
DIVERGING = "RdBu_r"    # two hues; ALWAYS centre on the meaningful midpoint

INK = "#1F2933"


def apply_theme() -> None:
    """Set the course defaults once; every chart inherits a decluttered look."""
    plt.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.edgecolor": "#CCCCCC",
        "axes.labelcolor": GREY_DARK,
        "axes.titlelocation": "left",
        "axes.titleweight": "bold",
        "axes.titlecolor": INK,
        "axes.titlesize": 13,
        "axes.titlepad": 14,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": "#EDEDED",
        "grid.linewidth": 0.8,
        "xtick.color": GREY_DARK,
        "ytick.color": GREY_DARK,
        "xtick.bottom": True,
        "ytick.left": False,
        "font.size": 10.5,
        "figure.dpi": 110,
        "savefig.dpi": 150,
        "savefig.bbox": "tight",
        "legend.frameon": False,
    })


def highlight_palette(categories, signal) -> list[str]:
    """Grey the context, accent the signal. One pop, not thirteen."""
    signal = {signal} if isinstance(signal, str) else set(signal)
    return [ACCENT if c in signal else GREY for c in categories]


# --------------------------------------------------------------------------
# 4. Charts
# --------------------------------------------------------------------------
def sorted_bar(data: pd.DataFrame, cat: str, val: str, *,
               highlight=None, title: str = "", xlabel: str = "",
               reference: float | None = None, reference_label: str = "",
               ascending: bool = True, fmt: str = "{:.1f}", ax=None):
    """Horizontal sorted bar with the five design principles baked in.

    1 honest baseline (x starts at 0)   2 sorted by value   3 direct value labels
    4 optional reference line           5 one accent, grey context
    """
    d = data.sort_values(val, ascending=ascending).reset_index(drop=True)
    if ax is None:
        _, ax = plt.subplots(figsize=(8.5, 0.42 * len(d) + 2.0))
    colors = highlight_palette(d[cat], highlight) if highlight else [ACCENT_2] * len(d)
    ax.barh(d[cat], d[val], color=colors, height=0.72)
    hi = float(d[val].max())
    ax.set_xlim(0, hi * 1.18)                        # principle 1
    for y, v in enumerate(d[val]):                   # principle 3
        ax.text(v + hi * 0.015, y, fmt.format(v), va="center",
                fontsize=9, color=GREY_DARK, zorder=5,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.9))
    if reference is not None:                        # principle 4
        ax.axvline(reference, color=INK, ls="--", lw=1.1, zorder=3.5)
        ax.text(reference, len(d) - 0.35, "  " + (reference_label or f"{reference:g}"),
                fontsize=9, color=INK, va="bottom")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(axis="y", visible=False)
    return ax


def save_plotly(fig, name: str, width: int = 1200, height: int = 720) -> dict:
    """Write a Plotly figure as self-contained HTML, and a PNG *if* static export works.

    Plotly's PNG export (kaleido) needs a Chrome binary. On a machine without one the
    HTML is still the real deliverable; this function says so instead of failing.
    """
    name = name[:-5] if name.endswith(".html") else name
    html = OUT / f"{name}.html"
    fig.write_html(html, include_plotlyjs="cdn", full_html=True)
    result = {"html": html, "png": None}
    try:
        png = OUT / f"{name}.png"
        fig.write_image(png, width=width, height=height, scale=2)
        result["png"] = png
    except Exception as exc:                                    # pragma: no cover
        result["png_error"] = f"{type(exc).__name__}: {str(exc).splitlines()[0][:120]}"
    return result


def set_out_dir(path) -> Path:
    """Redirect save_fig(). Starter notebooks point this at out/starter/ so a
    student's run never overwrites the instructor's reference figures."""
    global OUT
    OUT = Path(path)
    OUT.mkdir(parents=True, exist_ok=True)
    return OUT


def save_fig(fig, name: str, dpi: int = 150) -> Path:
    """Save to notebooks/out/<name>.png at dpi=150 and return the path."""
    if not name.endswith(".png"):
        name += ".png"
    path = OUT / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    return path


# --------------------------------------------------------------------------
# 5. Arabic / RTL  (Module 3, section 5)
# --------------------------------------------------------------------------
_AR_CANDIDATES = [
    "/usr/share/fonts/opentype/fonts-hosny-amiri/Amiri-Regular.ttf",
    "/usr/share/fonts/truetype/scheherazade/Scheherazade-Regular.ttf",
    "/usr/share/fonts/truetype/kacst/KacstOne.ttf",
    "/usr/share/fonts/truetype/kacst-one/KacstOne.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
]

ARABIC_FONT: str | None = None
ARABIC_OK = False


def setup_arabic() -> tuple[bool, str | None]:
    """Register an Arabic-capable font with matplotlib.

    Returns (ok, font_name). If this returns False the notebook MUST say so
    in text rather than shipping a chart full of tofu boxes.
    """
    global ARABIC_FONT, ARABIC_OK
    from matplotlib import font_manager as fm

    for p in _AR_CANDIDATES:
        if os.path.exists(p):
            try:
                fm.fontManager.addfont(p)
                ARABIC_FONT = fm.FontProperties(fname=p).get_name()
                break
            except Exception:                                   # pragma: no cover
                continue
    try:
        import arabic_reshaper  # noqa: F401
        from bidi.algorithm import get_display  # noqa: F401
        shaping = True
    except Exception:                                           # pragma: no cover
        shaping = False
    ARABIC_OK = bool(ARABIC_FONT) and shaping
    if not ARABIC_OK:
        warnings.warn(
            "Arabic rendering unavailable: "
            f"font={'ok' if ARABIC_FONT else 'MISSING'}, "
            f"reshaper/bidi={'ok' if shaping else 'MISSING'}. "
            "Charts will fall back to English labels — say so on the slide."
        )
    return ARABIC_OK, ARABIC_FONT


def ar(text: str) -> str:
    """Reshape + bidi an Arabic string so matplotlib draws joined, ordered glyphs.

    Without this step matplotlib renders Arabic as isolated letters in LTR order,
    which reads as gibberish to an Arabic-first audience.
    """
    if not ARABIC_OK:
        return text
    import arabic_reshaper
    from bidi.algorithm import get_display
    return get_display(arabic_reshaper.reshape(str(text)))


def arabic_kwargs() -> dict:
    """Font kwargs to pass to any matplotlib text call carrying Arabic."""
    return {"fontname": ARABIC_FONT} if ARABIC_FONT else {}


__all__ = [
    "PKG", "DATA", "OUT", "load", "load_facts",
    "ADDITIVE", "SEMI_ADDITIVE", "NON_ADDITIVE",
    "TARGET_ADOPTION", "TARGET_COST", "TARGET_CSAT", "STALLED", "SEVERE",
    "wmean", "adoption", "cost_per_txn", "csat", "completion_min", "sla_met",
    "by", "naive_by",
    "CATEGORICAL", "GREY", "GREY_DARK", "ACCENT", "ACCENT_2", "INK",
    "SEQUENTIAL", "DIVERGING", "apply_theme", "highlight_palette",
    "sorted_bar", "save_fig", "save_plotly", "set_out_dir",
    "setup_arabic", "ar", "arabic_kwargs", "ARABIC_OK", "ARABIC_FONT",
]
