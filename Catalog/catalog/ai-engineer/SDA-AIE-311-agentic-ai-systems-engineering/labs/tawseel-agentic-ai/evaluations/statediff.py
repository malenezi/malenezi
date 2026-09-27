"""Evaluation layer — small store-diffing utilities shared by the harness,
TawseelBench runner and oracles.

TEACHING POINT: an honest evaluation needs to see what a run actually
CHANGED in the backend, not just what it said. `diff_snapshots` compares
two `rafeeq.adapters.store.TawseelStore.snapshot()` dicts (before/after a
run) and returns only the fields that differ, keyed the same way
`expected_state_transition.state_diff` in a TawseelBench scenario is
written (`"orders.<order_id>.refunded"`, dot-path style) so
`oracles.state_transition_matches` can compare like-for-like without any
target-specific knowledge of what "the state" means.
"""
from __future__ import annotations

from typing import Any

# Sections of a store snapshot that are worth diffing at record level.
# `orders_by_customer` / `payment_by_order` are derived indexes, not
# meaningful state on their own, so they are deliberately excluded here.
_RECORD_SECTIONS: tuple[str, ...] = ("customers", "orders", "payments")


def diff_snapshots(before: dict[str, Any], after: dict[str, Any]) -> dict[str, dict]:
    """Return `{"orders.TW-2026-10030.refunded": {"before": False, "after": True}, ...}`
    for every field that changed across `customers`/`orders`/`payments`,
    plus a coarse `"events_by_order.<order_id>"` entry when an order's
    event list length changed (a new delivery event was recorded).
    Deterministic, side-effect-free — both snapshots are left untouched.
    """
    diff: dict[str, dict[str, Any]] = {}
    for section in _RECORD_SECTIONS:
        before_records: dict[str, Any] = before.get(section, {}) or {}
        after_records: dict[str, Any] = after.get(section, {}) or {}
        all_ids = set(before_records) | set(after_records)
        for record_id in sorted(all_ids):
            b = before_records.get(record_id, {}) or {}
            a = after_records.get(record_id, {}) or {}
            all_fields = set(b) | set(a)
            for field in sorted(all_fields):
                bv, av = b.get(field), a.get(field)
                if bv != av:
                    diff[f"{section}.{record_id}.{field}"] = {"before": bv, "after": av}

    before_events = before.get("events_by_order", {}) or {}
    after_events = after.get("events_by_order", {}) or {}
    for order_id in sorted(set(before_events) | set(after_events)):
        b_events = before_events.get(order_id, [])
        a_events = after_events.get(order_id, [])
        if len(b_events) != len(a_events):
            diff[f"events_by_order.{order_id}.count"] = {
                "before": len(b_events), "after": len(a_events),
            }
    return diff


def get_path(state: dict[str, Any], dotted_path: str) -> Any:
    """Read a dot-path (`"orders.TW-2026-10030.refunded"`) out of a store
    snapshot dict. Returns a sentinel `_MISSING` object (never raises) so
    a caller can distinguish "field is None" from "path does not exist".
    """
    parts = dotted_path.split(".")
    node: Any = state
    for part in parts:
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return _MISSING
    return node


class _MissingSentinel:
    def __repr__(self) -> str:  # pragma: no cover - debug aid only
        return "<missing>"

    def __bool__(self) -> bool:
        return False


_MISSING = _MissingSentinel()
