"""Module 1/5/7/8/9 — Rafeeq configuration.

The single source of truth for policy constants, filesystem paths and
runtime settings. Every other module imports these values rather than
re-declaring literals — duplicated policy numbers are how a "500 SAR"
refund limit quietly drifts to "550 SAR" in one code path and causes an
audit finding. No third-party imports here: this module must be importable
before anything else in the tree, with nothing but the standard library.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Paths — resolved relative to the repository root, not the cwd, so tools
# work the same whether invoked from repo root, scripts/, or tests/.
# --------------------------------------------------------------------------
CORE_DIR = Path(__file__).resolve().parent          # src/rafeeq/core
SRC_DIR = CORE_DIR.parent.parent                     # src
REPO_ROOT = SRC_DIR.parent                           # tawseel-agentic-ai/

DATA_DIR = REPO_ROOT / "data"
CUSTOMERS_DIR = DATA_DIR / "customers"
ORDERS_DIR = DATA_DIR / "orders"
DELIVERIES_DIR = DATA_DIR / "deliveries"
PAYMENTS_DIR = DATA_DIR / "payments"
POLICIES_DIR = DATA_DIR / "policies"
POLICIES_SUPERSEDED_DIR = POLICIES_DIR / "superseded"
RECORDINGS_DIR = DATA_DIR / "recordings"

CUSTOMERS_SEED_PATH = CUSTOMERS_DIR / "customers_seed.json"
ORDERS_SEED_PATH = ORDERS_DIR / "orders_seed.json"
DELIVERY_EVENTS_PATH = DELIVERIES_DIR / "delivery_events.jsonl"
PAYMENTS_SEED_PATH = PAYMENTS_DIR / "payments_seed.json"
TICKETS_EVAL_PATH = DATA_DIR / "tickets_eval.jsonl"
ROUTING_EVAL_PATH = DATA_DIR / "routing_eval.jsonl"
INJECTION_NOTES_PATH = ORDERS_DIR / "INJECTION_NOTES.md"

# --------------------------------------------------------------------------
# Domain model (SPEC §4, binding) — cities, statuses, enums.
# --------------------------------------------------------------------------
CITIES: list[dict[str, object]] = [
    {"city": "Riyadh", "city_ar": "الرياض", "lat": 24.7136, "lng": 46.6753},
    {"city": "Jeddah", "city_ar": "جدة", "lat": 21.4858, "lng": 39.1925},
    {"city": "Dammam", "city_ar": "الدمام", "lat": 26.4207, "lng": 50.0888},
    {"city": "Makkah", "city_ar": "مكة المكرمة", "lat": 21.3891, "lng": 39.8579},
    {"city": "Madinah", "city_ar": "المدينة المنورة", "lat": 24.5247, "lng": 39.5692},
]
CITY_NAMES: list[str] = [c["city"] for c in CITIES]  # type: ignore[misc]
CITY_AR_BY_EN: dict[str, str] = {c["city"]: c["city_ar"] for c in CITIES}  # type: ignore[misc]

ORDER_STATUSES = ["processing", "in_transit", "out_for_delivery", "delivered", "exception"]
DELIVERY_EVENTS = [
    "accepted", "picked_up", "at_hub", "out_for_delivery",
    "delivery_attempt", "delivered", "failed", "returned",
]
EXCEPTION_CODES = [
    None, "customer_unreachable", "address_incorrect", "damaged",
    "refused", "weather", "vehicle_breakdown",
]
CUSTOMER_TIERS = ["standard", "plus", "business"]
PAYMENT_METHODS = ["mada", "visa", "applepay", "cod"]
PAYMENT_STATUSES = ["authorised", "captured", "refunded", "partially_refunded", "failed"]
TICKET_INTENTS = [
    "order_status", "track", "reschedule", "refund", "invoice", "complaint",
    "address_change", "lost_parcel", "damaged", "fraud_check",
    "out_of_scope", "multi_domain",
]

# ID formats (regexes used by generators, adapters and the LLM stub).
ORDER_ID_RE = r"TW-2026-\d{5}"
CUSTOMER_ID_RE = r"CUST-\d{4}"
DRIVER_ID_RE = r"DRV-\d{3}"
TICKET_ID_RE = r"TKT-\d{5}"
PAYMENT_ID_RE = r"PAY-\d{6}"

# --------------------------------------------------------------------------
# Policy constants (SPEC §5, BINDING). Defined ONCE. Every other module
# imports these — never re-declare a limit as a bare literal elsewhere.
# --------------------------------------------------------------------------
REFUND_LIMIT_SAR = 500.0          # above this -> human approval (M7/M8 hard gate)
AUTO_REFUND_LIMIT_SAR = 50.0      # below this -> fully autonomous
MAX_STEPS = 8                     # per-agent step budget (M1)
MAX_HANDOFFS = 4                  # global multi-agent budget (M6)
MAX_REFLECTIONS = 2               # M2
RUN_COST_CAP_USD = 0.25           # denial-of-wallet cap (M8/M9)
WALL_CLOCK_S = 30                 # M1
CURRENT_POLICY_VERSION = "2026.2"
SUPERSEDED_POLICY_VERSION = "2026.1"
SLA_HOURS = {"standard": 48, "plus": 24, "business": 12}

# Action-risk matrix categories (SPEC §5) — the canonical labels used by
# src/rafeeq/security/action_risk.py. Kept here too so config stays the
# single source of truth for anything that looks like a policy constant.
AUTONOMY_AUTONOMOUS = "autonomous"
AUTONOMY_AUTONOMOUS_WITHIN_POLICY = "autonomous_within_policy"
AUTONOMY_POLICY_CONTROLLED = "policy_controlled"
AUTONOMY_HUMAN_APPROVAL = "human_approval_required"
AUTONOMY_PROHIBITED = "prohibited"

# --------------------------------------------------------------------------
# Runtime settings — env-driven, safe defaults, no network at import time.
# --------------------------------------------------------------------------


def _env_str(name: str, default: str) -> str:
    val = os.environ.get(name)
    return val if val not in (None, "") else default


def _env_float(name: str, default: float) -> float:
    val = os.environ.get(name)
    if val in (None, ""):
        return default
    try:
        return float(val)  # type: ignore[arg-type]
    except ValueError:
        return default


def _env_bool(name: str, default: bool) -> bool:
    val = os.environ.get(name)
    if val in (None, ""):
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")  # type: ignore[union-attr]


@dataclass(frozen=True)
class Settings:
    """Env-driven runtime settings, all with safe offline defaults so the
    whole system runs with zero keys and zero network calls out of the box.
    """

    model_mode: str = field(default_factory=lambda: _env_str("RAFEEQ_MODEL_MODE", "stub"))
    embed_mode: str = field(default_factory=lambda: _env_str("RAFEEQ_EMBED_MODE", "hashing"))
    vector_mode: str = field(default_factory=lambda: _env_str("RAFEEQ_VECTOR_MODE", "simple"))

    openai_base_url: str = field(default_factory=lambda: _env_str("OPENAI_BASE_URL", ""))
    openai_api_key: str = field(default_factory=lambda: _env_str("OPENAI_API_KEY", ""))

    cheap_model_name: str = field(default_factory=lambda: _env_str("RAFEEQ_CHEAP_MODEL", "gpt-4o-mini"))
    frontier_model_name: str = field(default_factory=lambda: _env_str("RAFEEQ_FRONTIER_MODEL", "gpt-4o"))

    max_steps: int = MAX_STEPS
    max_handoffs: int = MAX_HANDOFFS
    max_reflections: int = MAX_REFLECTIONS
    run_cost_cap_usd: float = field(default_factory=lambda: _env_float("RAFEEQ_COST_CAP_USD", RUN_COST_CAP_USD))
    wall_clock_s: float = field(default_factory=lambda: _env_float("RAFEEQ_WALL_CLOCK_S", WALL_CLOCK_S))

    refund_limit_sar: float = REFUND_LIMIT_SAR
    auto_refund_limit_sar: float = AUTO_REFUND_LIMIT_SAR

    log_level: str = field(default_factory=lambda: _env_str("RAFEEQ_LOG_LEVEL", "INFO"))
    seed: int = field(default_factory=lambda: int(_env_float("RAFEEQ_SEED", 20260311.0)))

    def is_offline(self) -> bool:
        """True when nothing in this run touches the network."""
        return self.model_mode != "live" and self.embed_mode != "live" and self.vector_mode != "qdrant"


def get_settings() -> Settings:
    """Fresh Settings read from the current environment. Cheap — construct
    per call rather than caching, so tests can flip env vars freely."""
    return Settings()
