"""Lab 3, Task 1 — typed tools with error VALUES, never raises.

Fill in the TODOs. Errors are RETURN VALUES (`{"error": "..."}`), never
exceptions — the agent loop must be able to react to a bad id, not crash
on it (Module 1's swallowed-error lesson, inverted: surface the failure
INTO the return value, don't hide it and don't crash on it either).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.adapters.oms import OrderManagementClient
from rafeeq.core.config import ORDER_ID_RE
from rafeeq.core.errors import ToolError

_ORDER_ID_FULL_RE = re.compile(rf"^{ORDER_ID_RE}$")
_oms = OrderManagementClient()


class ShipmentStatus(BaseModel):
    order_id: str
    status: Literal["processing", "in_transit", "out_for_delivery", "delivered", "exception"]
    eta: str | None
    sla_breached: bool


def track_shipment_impl(order_id: str) -> dict:
    """TODO(lab 3.1a): validate `order_id` against `_ORDER_ID_FULL_RE`;
    on a mismatch return `{"error": "invalid_order_id_format"}` (a VALUE,
    do not raise). Otherwise call `_oms.get_order(order_id)`; catch
    `ToolError` and return `{"error": "order_not_found"}`. On success
    return `ShipmentStatus(order_id=..., status=record.status,
    eta=record.eta_iso, sla_breached=record.sla_breached).model_dump()`.
    """
    raise NotImplementedError("TODO(lab 3.1a): implement track_shipment_impl")


def get_order_details_impl(order_id: str) -> dict:
    """TODO(lab 3.1b): same error-value discipline as above. On success
    return a dict with at least `order_id`, `status`, `amount_sar`,
    `items`, `city`. Use `_oms.get_order(order_id)` for the record; its
    attributes mirror `data/orders/orders_seed.json`'s schema (SPEC §4).
    """
    raise NotImplementedError("TODO(lab 3.1b): implement get_order_details_impl")


# --------------------------------------------------------------------------
# Task 5 — a WRITE tool, marked non-idempotent. `add_case_note` opens a
# case note against a customer's ticket — calling it twice double-notes,
# so (unlike the two read tools above) it must never be blindly retried.
# --------------------------------------------------------------------------
def open_case_impl(customer_id: str, reason: str) -> dict:
    """TODO(lab 3.5): a minimal write tool. Return
    `{"customer_id": customer_id, "reason": reason, "opened": True}` —
    no backend call needed for this lab (the real equivalent,
    `rafeeq.tools.customer.add_case_note_impl`, actually appends to the
    in-memory store; this simplified version just proves the CONTRACT:
    the function exists, is idempotent=False by convention (see
    `IDEMPOTENT`/`WRITE_TOOLS` below), and the agent must not retry it on
    a happy path.
    """
    raise NotImplementedError("TODO(lab 3.5): implement open_case_impl")


# The governed catalogue slice THIS lab adds. Compare against
# `rafeeq.tools.registry.WRITE_TOOLS`/`IDEMPOTENT` once you are done —
# every write tool in that real catalogue follows the same split.
READ_TOOLS = {"track_shipment", "get_order_details"}
WRITE_TOOLS = {"open_case"}
