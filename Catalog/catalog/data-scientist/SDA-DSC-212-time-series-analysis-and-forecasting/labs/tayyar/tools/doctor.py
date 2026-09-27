"""make doctor — verify the environment before a cohort arrives."""
import importlib, platform, sys
from pathlib import Path

REQUIRED = ["pandas", "numpy", "matplotlib", "scipy", "statsmodels",
            "sklearn", "lightgbm", "openpyxl"]
OPTIONAL = ["pmdarima", "prophet", "sktime", "nbclient"]
DATA = ["ksa_grid_demand.csv", "ksa_grid_demand_clean.csv", "ksa_grid_demand_4area.csv",
        "ksa_calendar.csv", "temp_forecast_14d.csv", "temp_forecast_28d.csv"]

def check(mods, label):
    ok = True
    print(f"\n{label}")
    for m in mods:
        try:
            mod = importlib.import_module(m)
            v = getattr(mod, "__version__", "?")
            print(f"  OK    {m:<14} {v}")
        except Exception as e:
            ok = False
            print(f"  MISS  {m:<14} {type(e).__name__}")
    return ok

print(f"Python {platform.python_version()} on {platform.system()} {platform.machine()}")
if sys.version_info < (3, 10):
    print("  WARNING: this course targets Python 3.12; 3.10 is the practical minimum.")

hard = check(REQUIRED, "Required packages")
check(OPTIONAL, "Optional packages (the core labs do not need these)")

print("\nCourse datasets")
root = Path(__file__).resolve().parents[1] / "data"
data_ok = True
for f in DATA:
    p = root / f
    if p.exists():
        print(f"  OK    {f:<30} {p.stat().st_size/1e6:6.2f} MB")
    else:
        data_ok = False
        print(f"  MISS  {f:<30} run `make data`")

print("\nPackage import")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
try:
    from tayyar.data.load import load_demand           # noqa
    from tayyar.features.build import assert_no_leakage  # noqa
    from tayyar.eval.backtest import rolling_backtest    # noqa
    print("  OK    src/tayyar imports cleanly")
except Exception as e:
    hard = False
    print(f"  FAIL  src/tayyar — {type(e).__name__}: {e}")

print()
if hard and data_ok:
    print("READY. Every required package and dataset is present.")
else:
    print("NOT READY. Fix the MISS/FAIL lines above before the cohort arrives.")
    sys.exit(1)
