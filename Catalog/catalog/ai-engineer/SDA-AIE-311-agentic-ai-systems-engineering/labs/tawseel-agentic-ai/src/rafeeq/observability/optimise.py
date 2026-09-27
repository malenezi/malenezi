"""Module 9 — the package's two highest-impact cost levers.

**Caching**: identical inputs should not be recomputed. `cached_policy`
caches KB retrieval keyed on the question, the LOCALE, and the CURRENT
policy version — never serve stale (the M4 link: a superseded policy
served with confidence is worse than no policy at all). `CacheStats`
turns "we cache" into a measured lever: hit rate and USD/latency saved,
so Lab 9 Task 3 can report a number, not an assertion.

**Model routing**: `route_model` sends the confident, simple majority to
the cheap model and reserves the frontier model for the genuine hard
tail — a direct application of M2 (pattern choice) and M7 (deterministic
routing), not a model call itself.

These compound with flow engineering (M7, which removes model calls
entirely for rule-shaped work): flow removes calls, cache removes
repeats, routing cheapens what is left.

Dependency-free (Layer A): stdlib + `rafeeq.core.config` +
`rafeeq.core.llm` only. `rafeeq.memory.knowledge_base.policy_context` is
imported LAZILY (inside `cached_policy`) so this module never forces the
vector-store machinery to import just to compute a cache key or a
routing decision — `route_model`/`CacheStats` are useful standalone.
"""
from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from threading import Lock
from typing import Any, Callable

from rafeeq.core.config import CURRENT_POLICY_VERSION
from rafeeq.core.llm import estimate_cost_usd

# --------------------------------------------------------------------------
# CacheStats — makes the caching lever measurable, not just assertable.
# --------------------------------------------------------------------------
@dataclass
class CacheStats:
    hits: int = 0
    misses: int = 0
    usd_saved: float = 0.0
    seconds_saved: float = 0.0

    @property
    def total(self) -> int:
        return self.hits + self.misses

    @property
    def hit_rate(self) -> float:
        return (self.hits / self.total) if self.total else 0.0

    def record_hit(self, usd_saved: float = 0.0, seconds_saved: float = 0.0) -> None:
        self.hits += 1
        self.usd_saved += usd_saved
        self.seconds_saved += seconds_saved

    def record_miss(self) -> None:
        self.misses += 1

    def to_dict(self) -> dict[str, Any]:
        return {
            "hits": self.hits, "misses": self.misses, "total": self.total,
            "hit_rate": round(self.hit_rate, 4),
            "usd_saved": round(self.usd_saved, 6),
            "seconds_saved": round(self.seconds_saved, 4),
        }

    def __str__(self) -> str:  # pragma: no cover - display only
        return (f"CacheStats(hits={self.hits}, misses={self.misses}, "
                f"hit_rate={self.hit_rate:.1%}, usd_saved=${self.usd_saved:.5f})")


# --------------------------------------------------------------------------
# Scoped, versioned policy-retrieval cache.
#
# TEACHING POINT (Lab 9 troubleshooting row / the module's code-review
# exercise): a cache keyed on the question string ALONE serves a stale or
# wrong-language policy the moment the policy version bumps or a second
# locale asks the same question. The key here is
# `(question, locale, policy_version)` — every one of those three is part
# of "what was actually asked and against what policy", and a version
# bump changes the key, which is a cache-wide invalidation by construction
# (no TTL clock to get wrong, no stale entry can survive a policy edit).
# --------------------------------------------------------------------------
_policy_cache: dict[tuple[str, str, str], str] = {}
_policy_cache_lock = Lock()
POLICY_CACHE_STATS = CacheStats()

# A representative KB-retrieval cost/latency, used only to size
# `CacheStats`' savings estimate on a hit (we do not re-run the retrieval
# to find out what it WOULD have cost — that would defeat the cache).
_ASSUMED_RETRIEVAL_USD = 0.00015   # ~ one cheap-model embedding-sized call
_ASSUMED_RETRIEVAL_SECONDS = 0.35  # a KB similarity search + rerank, offline


def _question_key(question: str) -> str:
    return hashlib.sha256(question.strip().lower().encode("utf-8")).hexdigest()[:16]


def cached_policy(question: str, locale: str, version: str = CURRENT_POLICY_VERSION,
                   stats: CacheStats | None = None) -> str:
    """Cache `rafeeq.memory.knowledge_base.policy_context(question, locale)`
    keyed on `(question, locale, version)`. Callers should always pass
    `version=CURRENT_POLICY_VERSION` explicitly in production code (the
    default exists for convenience, not to encourage forgetting it) — the
    version is read at CALL time, not once at import time, so a policy
    edit followed by `seed_kb()` starts producing fresh cache keys on the
    very next call, no process restart required.
    """
    stats = stats if stats is not None else POLICY_CACHE_STATS
    key = (_question_key(question), locale, version)
    with _policy_cache_lock:
        cached = _policy_cache.get(key)
    if cached is not None:
        stats.record_hit(usd_saved=_ASSUMED_RETRIEVAL_USD, seconds_saved=_ASSUMED_RETRIEVAL_SECONDS)
        return cached

    stats.record_miss()
    from rafeeq.memory.knowledge_base import policy_context  # lazy: avoid forcing the vector store to import

    result = policy_context(question, locale)
    with _policy_cache_lock:
        _policy_cache[key] = result
    return result


def clear_policy_cache() -> None:
    """Test/lab helper: drop every cached entry and reset the shared
    stats. Never called from production request handling."""
    with _policy_cache_lock:
        _policy_cache.clear()
    POLICY_CACHE_STATS.hits = 0
    POLICY_CACHE_STATS.misses = 0
    POLICY_CACHE_STATS.usd_saved = 0.0
    POLICY_CACHE_STATS.seconds_saved = 0.0


# --------------------------------------------------------------------------
# Generic memoising cache for ANY deterministic, scoped computation — the
# same pattern `cached_policy` hand-rolls above, reusable for e.g. a
# retrieval or a deterministic reasoning step keyed on more than one
# field. Deliberately NOT `functools.lru_cache`: an lru_cache key is
# positional-args-only and invisible in `CacheStats`, which is exactly
# the "unscoped key" failure mode this module exists to avoid teaching.
# --------------------------------------------------------------------------
def scoped_cache(fn: Callable[..., Any], stats: CacheStats | None = None) -> Callable[..., Any]:
    """Wrap `fn` so calls with an IDENTICAL keyword-argument set are
    served from a dict cache. Every keyword the caller passes is part of
    the key — there is no way to under-scope it by accident, unlike a
    positional `lru_cache` where a forgotten argument silently drops out
    of the key. Intended for KEYWORD-ONLY deterministic functions
    (`fn(question=..., locale=..., version=...)`), not for tools with
    side effects — never wrap a WRITE tool in this."""
    cache: dict[tuple[tuple[str, Any], ...], Any] = {}
    lock = Lock()
    local_stats = stats if stats is not None else CacheStats()

    def wrapped(**kwargs: Any) -> Any:
        key = tuple(sorted(kwargs.items()))
        with lock:
            if key in cache:
                local_stats.record_hit()
                return cache[key]
        local_stats.record_miss()
        result = fn(**kwargs)
        with lock:
            cache[key] = result
        return result

    wrapped.stats = local_stats  # type: ignore[attr-defined]
    return wrapped


# --------------------------------------------------------------------------
# Model routing — the second lever.
# --------------------------------------------------------------------------
# Intents the module's benchmark table treats as the confident, simple
# majority: routine, single-fact lookups with essentially no policy
# judgement involved. Anything else — or a low-confidence classification
# of even THESE intents — still goes to the frontier model.
_CHEAP_ELIGIBLE_INTENTS: frozenset[str] = frozenset({"order_status", "track"})
CHEAP_CONFIDENCE_THRESHOLD = 0.8


def route_model(intent: str | None, confidence: float):
    """Confident, simple intents -> the cheap model; the hard tail ->
    frontier. Returns a model object (same call surface either way —
    `.invoke`, `.bind_tools`, `.with_structured_output`; see
    `core.llm.get_model`), so a caller never branches on WHICH model it
    got, only on cost. A deterministic rule, not a model call — routing
    must not itself cost a token."""
    from rafeeq.core.llm import get_cheap_model, get_frontier_model  # lazy: matches core.llm's own lazy live-mode import

    if intent in _CHEAP_ELIGIBLE_INTENTS and confidence >= CHEAP_CONFIDENCE_THRESHOLD:
        return get_cheap_model()
    return get_frontier_model()


def route_model_name(intent: str | None, confidence: float) -> str:
    """The routing decision as a plain model NAME (`"gpt-4o-mini"` /
    `"gpt-4o"`), for callers that only want to log/trace the decision
    without constructing a model object (e.g. `service/api.py` recording
    which tier a request was routed to before the run even starts)."""
    from rafeeq.core.config import get_settings

    settings = get_settings()
    if intent in _CHEAP_ELIGIBLE_INTENTS and confidence >= CHEAP_CONFIDENCE_THRESHOLD:
        return settings.cheap_model_name
    return settings.frontier_model_name


def estimate_routing_saving(intent: str | None, confidence: float, input_text: str, output_text: str) -> float:
    """USD saved by routing this ONE call to the cheap model instead of
    the frontier model, for the same input/output token counts —
    `route_model`'s own measured lever, used by `service/api.py` to log a
    per-run saving estimate next to the trace."""
    from rafeeq.core.config import get_settings

    settings = get_settings()
    if not (intent in _CHEAP_ELIGIBLE_INTENTS and confidence >= CHEAP_CONFIDENCE_THRESHOLD):
        return 0.0
    cheap = estimate_cost_usd(settings.cheap_model_name, input_text, output_text)
    frontier = estimate_cost_usd(settings.frontier_model_name, input_text, output_text)
    return max(0.0, frontier - cheap)
