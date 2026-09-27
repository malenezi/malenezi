"""Module 5 — context isolation: a structural PDPL control, not a prompt.

`SCOPE` states, for every specialist, exactly which shared-state fields it
may read. `scoped_input(state, specialist)` projects the shared state down
to that allow-list — the Billing agent CANNOT receive shipment PII because
nothing in `SCOPE["billing"]` names a shipment/address/geo field, not
because a prompt tells it not to look. This file has zero third-party
dependencies and needs no langgraph: it is pure data plus a pure function,
importable and testable under plain python3 exactly like every other
Layer-A gate function in this repo (`flows/*.py`, `orchestration/routing.py`).
"""
from __future__ import annotations

from typing import Any, Mapping

# What each specialist is ALLOWED to see. Structural, not prompt-based
# (Module 5's central lesson). Note billing gets no address/geo field —
# `tests/unit/test_scoping.py` asserts this explicitly.
SCOPE: dict[str, frozenset[str]] = {
    "orders": frozenset({"customer_id", "locale", "order_id", "messages"}),
    "logistics": frozenset({"customer_id", "locale", "order_id", "messages"}),
    "billing": frozenset({"customer_id", "locale", "order_id", "messages"}),  # no address/geo
}

# Defence-in-depth DENY list: fields that must NEVER reach a given
# specialist even if a future edit accidentally widens `SCOPE` to include
# them. `scoped_input` asserts `SCOPE[specialist]` never overlaps this set
# (a build-time bug, caught immediately) and that the projected payload
# never contains one of these keys (a runtime bug, caught before the
# specialist ever sees the value) — TEACHING POINT (SPEC task): "a
# forbidden field raises rather than silently passing".
FORBIDDEN_FIELDS: dict[str, frozenset[str]] = {
    "billing": frozenset({
        "address", "shipment_address", "delivery_address", "geo", "lat", "lng",
        "delivery_note", "delivery_note_ar", "national_id_masked",
    }),
}


def known_specialists() -> tuple[str, ...]:
    return tuple(SCOPE.keys())


def assert_no_forbidden_leak(payload: Mapping[str, Any], specialist: str) -> None:
    """Raise `ValueError` if `payload` (an already-scoped input about to
    be handed to `specialist`) contains any field on that specialist's
    forbidden list. Exposed separately from `scoped_input` so a test can
    exercise the "raises, does not silently pass" behaviour directly by
    constructing a deliberately-leaking payload, without needing to first
    corrupt `SCOPE` itself."""
    forbidden = FORBIDDEN_FIELDS.get(specialist, frozenset())
    leaked = forbidden & payload.keys()
    if leaked:
        raise ValueError(
            f"scoped input for specialist {specialist!r} contains forbidden "
            f"field(s) {sorted(leaked)} — this is a PDPL context-isolation "
            f"bug, not a warning; fix the caller, do not widen SCOPE to hide it."
        )


def scoped_input(state: Mapping[str, Any], specialist: str) -> dict[str, Any]:
    """Project the shared state down to the fields `specialist` may read.

    Fails LOUD, never quiet, on two distinct problems:
      - an unknown `specialist` name (`KeyError`) — there is no scope to
        apply, so guessing "allow everything" would be the opposite of
        this function's purpose;
      - a forbidden field somehow present in the computed payload
        (`ValueError`, via `assert_no_forbidden_leak`) — defence in depth
        against `SCOPE` itself being widened incorrectly in the future.
    """
    if specialist not in SCOPE:
        raise KeyError(
            f"unknown specialist {specialist!r}; SCOPE only defines "
            f"{sorted(SCOPE)} — add an entry before routing to a new specialist."
        )
    allowed = SCOPE[specialist]
    forbidden = FORBIDDEN_FIELDS.get(specialist, frozenset())
    overlap = allowed & forbidden
    assert not overlap, (          # a build-time contradiction, not a runtime input problem
        f"SCOPE[{specialist!r}] illegally includes forbidden field(s) {sorted(overlap)} "
        "— fix SCOPE, never weaken this assertion to make a test pass."
    )
    payload = {k: v for k, v in state.items() if k in allowed}
    assert_no_forbidden_leak(payload, specialist)
    return payload
