"""Shared style for the SDA-DSC-112 critique-canon recreations."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# SDAIA Academy deck palette (extracted from SDA-DSC-112_Instructor_Training_Deck.pptx)
NAVY="#1D2A5C"; TEAL="#00A79D"; ORANGE="#E8833A"; PURPLE="#6C4FA1"; GREEN="#3FAE5A"
BLUE="#2E5AAC"; GREY="#6B7280"; LIGHT="#D9DEE8"; PANEL="#F4F6FB"; INK="#343A4E"
MUTED="#9AA3B2"; RED="#D9534F"; AMBER="#E6B325"

plt.rcParams.update({
    "font.family": "Liberation Sans",
    "font.size": 9,
    "axes.edgecolor": LIGHT, "axes.linewidth": 0.8,
    "axes.labelcolor": INK, "axes.titlecolor": NAVY,
    "xtick.color": GREY, "ytick.color": GREY,
    "xtick.labelsize": 8, "ytick.labelsize": 8,
    "axes.titlesize": 11, "axes.labelsize": 8.5,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white", "savefig.bbox": "tight", "savefig.pad_inches": 0.10,
    "legend.frameon": False,
})

W, H, DPI = 12.13, 4.45, 200          # fills the deck's content area at 13.33x7.5in

def despine(ax, keep=("left","bottom")):
    for s in ("top","right","left","bottom"):
        ax.spines[s].set_visible(s in keep)

def head(ax, kicker, title, color=TEAL, dy=0.0):
    """Kicker + title drawn above the axes, never colliding."""
    ax.text(0, 1.155+dy, kicker.upper(), transform=ax.transAxes, fontsize=7.5,
            color=color, fontweight="bold", va="bottom")
    ax.text(0, 1.045+dy, title, transform=ax.transAxes, fontsize=11.5,
            color=NAVY, fontweight="bold", va="bottom")

def fit_equal(ax, xlim, ylim, box_aspect):
    """Keep aspect='equal' but pad the LONG axis so the map fills its allotted box."""
    (x0,x1),(y0,y1)=xlim,ylim
    xs, ys = x1-x0, y1-y0
    if xs/ys < box_aspect:
        need = ys*box_aspect; c=(x0+x1)/2; x0,x1 = c-need/2, c+need/2
    else:
        need = xs/box_aspect; c=(y0+y1)/2; y0,y1 = c-need/2, c+need/2
    ax.set_xlim(x0,x1); ax.set_ylim(y0,y1); ax.set_aspect("equal")

def footnote(fig, text, width=215):
    import textwrap
    lines = []
    for para in text.split("\n"):
        lines += textwrap.wrap(" ".join(para.split()), width=width) or [""]
    fig.text(0.006, -0.030, "\n".join(lines), fontsize=7, color=GREY,
             ha="left", va="top", linespacing=1.45)

def save(fig, name):
    p = f"/home/claude/work/canon/out/{name}.png"
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    print("wrote", p)
    return p
