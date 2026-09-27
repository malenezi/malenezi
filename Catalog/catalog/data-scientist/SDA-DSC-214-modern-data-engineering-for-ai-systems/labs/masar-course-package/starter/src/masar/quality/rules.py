"""The Masar data-quality rules, expressed once, in pure Python.

Why this module exists at all: the gate needs the same rule in two shapes.
Great Expectations tells you WHICH RULE failed on a batch; Spark tells you
WHICH ROWS failed it. Writing the rule twice — once as an expectation, once as
a Spark predicate — is how the two silently drift apart, and then a row is
quarantined for a reason the report does not mention.

So the rule is declared HERE, once, as data:

  * :data:`QUARANTINE_RULES` / :data:`FAIL_FAST_RULES` — the catalogue.
  * :func:`evaluate_row` — evaluates the catalogue against a plain ``dict``.
    Pure Python, no Spark: this is what the unit tests exercise.
  * ``masar.quality.gate`` compiles the same catalogue into Spark columns.

Response classes (see ``quality/gate_config.yml``):

  FAIL_FAST   integrity. Promoting anything from this batch is worse than
              promoting nothing. Raise, block, page someone.
  QUARANTINE  partial. Isolate the bad rows with their reason, promote the
              good ones, alert either way.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from masar.config import KSA_CITIES, PAYMENT_TYPES, TRIP_STATUS

FAIL_FAST = "FAIL_FAST"
QUARANTINE = "QUARANTINE"


@dataclass(frozen=True)
class Rule:
    """One data-quality rule.

    Attributes:
        name: stable identifier. It is written into the quarantine row, shown
            in the alert and referenced in ``gate_config.yml`` — so renaming
            one is a breaking change to the evidence trail.
        response_class: ``FAIL_FAST`` or ``QUARANTINE``.
        column: the column the rule is about, or ``None`` for table-level.
        description: what a human should understand from a violation.
        predicate: returns ``True`` when the row VIOLATES the rule. Violation-
            positive (not validity-positive) because the gate's job is to
            collect reasons, and a reason is a thing that went wrong.
    """

    name: str
    response_class: str
    column: str | None
    description: str
    predicate: Callable[[Mapping[str, Any]], bool]


def _num(row: Mapping[str, Any], key: str) -> float | None:
    """Best-effort numeric read. Returns ``None`` for missing/unparseable values.

    Bronze lands everything as STRING on purpose, so a rule that assumes
    ``float`` would fail on exactly the rows it exists to catch.
    """
    value = row.get(key)
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _missing(row: Mapping[str, Any], key: str) -> bool:
    """A key is missing if it is absent, ``None``, or the empty string."""
    value = row.get(key)
    return value is None or (isinstance(value, str) and value.strip() == "")


# --------------------------------------------------------------------------
# Fail-fast: integrity. Nothing about this batch can be trusted row-by-row.
# --------------------------------------------------------------------------

FAIL_FAST_RULES: tuple[Rule, ...] = (
    Rule(
        "trip_id_null",
        FAIL_FAST,
        "trip_id",
        "Unkeyed row: nothing downstream can merge, dedupe or erase it.",
        lambda r: _missing(r, "trip_id"),
    ),
    Rule(
        "pickup_ts_null",
        FAIL_FAST,
        "pickup_ts",
        "No event time: the row cannot be placed in any window or partition.",
        lambda r: _missing(r, "pickup_ts"),
    ),
    Rule(
        "rider_id_null",
        FAIL_FAST,
        "rider_id",
        "No data subject: a PDPL erasure request could never reach this row.",
        lambda r: _missing(r, "rider_id"),
    ),
)


# --------------------------------------------------------------------------
# Quarantine: partial. These rows are wrong; the rest of the batch is fine.
# --------------------------------------------------------------------------

QUARANTINE_RULES: tuple[Rule, ...] = (
    Rule(
        "fare_non_positive",
        QUARANTINE,
        "fare_sar",
        "A completed trip with a fare of zero or less is not a trip.",
        lambda r: (v := _num(r, "fare_sar")) is not None and v <= 0,
    ),
    Rule(
        "fare_implausible",
        QUARANTINE,
        "fare_sar",
        "Fare above SAR 5,000 — the currency-shift fixture's signature.",
        lambda r: (v := _num(r, "fare_sar")) is not None and v > 5000,
    ),
    Rule(
        "duration_non_positive",
        QUARANTINE,
        "duration_min",
        "Negative or zero duration: the source ships a few of these on purpose.",
        lambda r: (v := _num(r, "duration_min")) is not None and v <= 0,
    ),
    Rule(
        "duration_implausible",
        QUARANTINE,
        "duration_min",
        "Over 600 minutes: a ten-hour taxi ride is a data problem, not a trip.",
        lambda r: (v := _num(r, "duration_min")) is not None and v > 600,
    ),
    Rule(
        "distance_non_positive",
        QUARANTINE,
        "distance_km",
        "Zero or negative distance makes fare_per_km undefined.",
        lambda r: (v := _num(r, "distance_km")) is not None and v <= 0,
    ),
    Rule(
        "distance_implausible",
        QUARANTINE,
        "distance_km",
        "Over 400 km: outside the intra-city domain Masar operates in.",
        lambda r: (v := _num(r, "distance_km")) is not None and v > 400,
    ),
    Rule(
        "city_not_in_ksa_set",
        QUARANTINE,
        "city",
        "City outside the operating set — the dirty batch injects bad codes.",
        lambda r: not _missing(r, "city") and str(r["city"]) not in KSA_CITIES,
    ),
    Rule(
        "status_unknown",
        QUARANTINE,
        "status",
        "Status outside the four values the source contract allows.",
        lambda r: not _missing(r, "status") and str(r["status"]) not in TRIP_STATUS,
    ),
    Rule(
        "payment_type_unknown",
        QUARANTINE,
        "payment_type",
        "Payment method outside the accepted set.",
        lambda r: not _missing(r, "payment_type") and str(r["payment_type"]) not in PAYMENT_TYPES,
    ),
    Rule(
        "surge_out_of_range",
        QUARANTINE,
        "surge_multiplier",
        "Surge outside [1.0, 5.0] — either a pricing bug or a parsing bug.",
        lambda r: (v := _num(r, "surge_multiplier")) is not None and not (1.0 <= v <= 5.0),
    ),
    Rule(
        "dropoff_before_pickup",
        QUARANTINE,
        "dropoff_ts",
        "Time runs forwards. A reversed pair is a clock or a timezone fault.",
        lambda r: _timestamps_reversed(r),
    ),
)

ALL_RULES: tuple[Rule, ...] = FAIL_FAST_RULES + QUARANTINE_RULES
RULES_BY_NAME: dict[str, Rule] = {r.name: r for r in ALL_RULES}


# --------------------------------------------------------------------------
# Timestamp handling: the source ships TWO formats in the same column.
# --------------------------------------------------------------------------

_ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(:\d{2})?")
_EU_RE = re.compile(r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}")


def timestamp_format(value: object) -> str:
    """Classify a raw timestamp string.

    Returns:
        ``"iso"`` for ``YYYY-MM-DD HH:MM[:SS]``, ``"eu"`` for
        ``DD/MM/YYYY HH:MM``, ``"missing"`` for null/empty, ``"unknown"``
        otherwise.

    Roughly 2% of Masar's raw rows use the ``eu`` form. Landing with
    ``inferSchema=True`` would silently null exactly those rows — destroying
    the evidence before anyone had looked at it. That is why bronze lands
    everything as STRING and this function exists.
    """
    if value is None or (isinstance(value, str) and not value.strip()):
        return "missing"
    text = str(value).strip()
    if _ISO_RE.match(text):
        return "iso"
    if _EU_RE.match(text):
        return "eu"
    return "unknown"


def parse_timestamp(value: object) -> object | None:
    """Parse either supported format into a ``datetime``; ``None`` if neither.

    Mirrors the ``coalesce(to_timestamp(...), to_timestamp(...))`` in
    ``stg_trips.sql``. Kept in Python so the rule can be unit-tested without
    starting a JVM.
    """
    from datetime import datetime

    kind = timestamp_format(value)
    text = str(value).strip() if value is not None else ""
    try:
        if kind == "iso":
            fmt = "%Y-%m-%d %H:%M:%S" if len(text) > 16 else "%Y-%m-%d %H:%M"
            return datetime.strptime(text.replace("T", " ")[:19], fmt)
        if kind == "eu":
            return datetime.strptime(text[:16], "%d/%m/%Y %H:%M")
    except ValueError:
        return None
    return None


def _timestamps_reversed(row: Mapping[str, Any]) -> bool:
    """True when ``dropoff_ts <= pickup_ts`` and both parse."""
    a, b = parse_timestamp(row.get("pickup_ts")), parse_timestamp(row.get("dropoff_ts"))
    return a is not None and b is not None and b <= a


# --------------------------------------------------------------------------
# Evaluation
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class RowVerdict:
    """The gate's decision about a single row.

    Attributes:
        blocked_by: FAIL_FAST rules the row violated. Any entry means the
            WHOLE batch is blocked — one unkeyed row is a broken batch.
        quarantined_by: QUARANTINE rules the row violated.
    """

    blocked_by: tuple[str, ...]
    quarantined_by: tuple[str, ...]

    @property
    def promotable(self) -> bool:
        """True when the row may be promoted to silver as-is."""
        return not self.blocked_by and not self.quarantined_by


def evaluate_row(row: Mapping[str, Any]) -> RowVerdict:
    """Apply every rule to one row.

    Args:
        row: a mapping of column name to value. Values may be strings (as
            they arrive from bronze) or already-typed Python objects.

    Returns:
        A :class:`RowVerdict` naming every rule the row violated.
    """
    blocked = tuple(r.name for r in FAIL_FAST_RULES if r.predicate(row))
    quarantined = tuple(r.name for r in QUARANTINE_RULES if r.predicate(row))
    return RowVerdict(blocked_by=blocked, quarantined_by=quarantined)


def evaluate_batch(rows: list[Mapping[str, Any]]) -> dict[str, Any]:
    """Apply the rule catalogue to a whole batch and summarise the outcome.

    Args:
        rows: the candidate batch.

    Returns:
        ``{"blocked": bool, "promoted": int, "quarantined": int,
        "reasons": {rule_name: count}, "duplicate_keys": int}``.

        ``blocked`` is the gate's headline decision: if a single row trips a
        FAIL_FAST rule, nothing is promoted. Duplicate business keys are
        counted as an integrity failure too — a MERGE on an ambiguous key is
        not idempotent, it is a coin flip.
    """
    verdicts = [evaluate_row(r) for r in rows]
    reasons: dict[str, int] = {}
    for v in verdicts:
        for name in v.blocked_by + v.quarantined_by:
            reasons[name] = reasons.get(name, 0) + 1

    dupes = duplicate_key_count(rows, "trip_id")
    blocked = any(v.blocked_by for v in verdicts) or dupes > 0
    if dupes:
        reasons["trip_id_duplicate"] = dupes

    return {
        "blocked": blocked,
        "promoted": 0 if blocked else sum(1 for v in verdicts if v.promotable),
        "quarantined": 0 if blocked else sum(1 for v in verdicts if v.quarantined_by),
        "reasons": reasons,
        "duplicate_keys": dupes,
    }


def duplicate_key_count(rows: list[Mapping[str, Any]], key: str = "trip_id") -> int:
    """Number of EXTRA rows sharing a business key (0 when every key is unique).

    Two rows with the same ``trip_id`` count as 1 duplicate, three count as 2.
    Bronze is allowed duplicates — it is an append-only ledger — but silver is
    not, and a MERGE against an ambiguous source is undefined behaviour.
    """
    seen: dict[Any, int] = {}
    for row in rows:
        value = row.get(key)
        if value is None or value == "":
            continue
        seen[value] = seen.get(value, 0) + 1
    return sum(count - 1 for count in seen.values() if count > 1)
