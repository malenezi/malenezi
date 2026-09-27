"""Lab 5, Task 1/5 — structural context isolation (a PDPL control, not a prompt).

Fill in the TODOs so the Billing specialist CANNOT see shipment/address
fields — not because a prompt tells it not to, but because nothing in its
allow-list names them. Zero third-party dependencies: pure data + a pure
function, importable under plain python3.
"""
from __future__ import annotations

from typing import Any, Mapping

# TODO(lab 5.1): define what each specialist is ALLOWED to see. All three
# specialists need at least {"customer_id", "locale", "order_id",
# "messages"} — assert (in your own test) that the BILLING entry contains
# NO address/geo/shipment field.
SCOPE: dict[str, frozenset[str]] = {
    "orders": frozenset(),        # TODO(lab 5.1)
    "logistics": frozenset(),     # TODO(lab 5.1)
    "billing": frozenset(),       # TODO(lab 5.1) — no address/geo/delivery_note field, ever
}

# Defence-in-depth: fields that must NEVER reach a given specialist even if
# SCOPE is accidentally widened later.
FORBIDDEN_FIELDS: dict[str, frozenset[str]] = {
    "billing": frozenset({
        "address", "shipment_address", "delivery_address", "geo", "lat", "lng",
        "delivery_note", "delivery_note_ar", "national_id_masked",
    }),
}


def scoped_input(state: Mapping[str, Any], specialist: str) -> dict[str, Any]:
    """TODO(lab 5.1/5.5): project `state` down to `SCOPE[specialist]`.

    1. If `specialist` is not in `SCOPE`, raise `KeyError` (fail loud on
       an unknown specialist — never silently "allow everything").
    2. Build `payload = {k: v for k, v in state.items() if k in
       SCOPE[specialist]}`.
    3. Raise `ValueError` if `payload` contains ANY key from
       `FORBIDDEN_FIELDS.get(specialist, frozenset())` — this is the
       "context-isolation test" Task 5 asks you to write: assert the
       Billing agent's input never contains a shipment-address field, by
       constructing a state dict WITH one and confirming this raises.
    4. Return `payload`.
    """
    raise NotImplementedError("TODO(lab 5.1/5.5): implement scoped_input")
