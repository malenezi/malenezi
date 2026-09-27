"""Module 3 — Tawseel tools: the canonical worked example.

This file is deliberately the instructor package's Module 3 code block,
verbatim in spirit: ONE narrow, typed, LLM-friendly tool, with a docstring
that IS the prompt. It exists as the teaching artefact participants read
first; the production tool surface Rafeeq actually binds lives in the
domain files next to this one (`orders.py`, `logistics.py`, `billing.py`,
`customer.py`), assembled by `registry.py`.

TEACHING POINT (schema is the prompt): an LLM calls a tool as well as its
description and parameter names let it. Compare this tool's docstring to
a vague one ("gets order stuff") and notice it states: what it does, when
to use it, when NOT to, the id format, and a worked example.

Errors are RETURN VALUES, never raises (`{"error": "order_not_found"}`) —
the agent loop must never die on a bad id (SPEC §7, Module 1's swallowed-
error lesson inverted: surface the failure INTO state, don't crash on it
and don't hide it either).
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from rafeeq.adapters.oms import OrderManagementClient
from rafeeq.core.config import ORDER_ID_RE
from rafeeq.core.errors import ToolError

import re

# --------------------------------------------------------------------------
# LangChain's @tool decorator is a Layer-B dependency (SPEC §1). Import-
# guard it: when langchain-core is not installed, fall back to a local
# no-op decorator so this module still imports and `track_shipment_impl`
# still runs under plain python3 — Layer-A tests and the MCP servers call
# the plain function directly either way.
# --------------------------------------------------------------------------
try:
    from langchain_core.tools import tool
except ImportError:  # pragma: no cover - Layer-A / plain-python3 environment
    def tool(func=None, *, return_direct: bool = False):  # type: ignore[no-redef]
        """Fallback stand-in for `langchain_core.tools.tool`. Attaches the
        `.name`/`.description` attributes a real LangChain Tool exposes so
        code that introspects a bound tool (e.g. `mcp_client.py`'s local
        fallback, `registry.describe_catalogue()`) works unmodified once
        the real dependency is installed — but returns the plain callable,
        unchanged, so it can still be invoked directly: `track_shipment(...)`."""
        def _decorate(f):
            f.name = f.__name__
            f.description = (f.__doc__ or "").strip()
            return f
        return _decorate(func) if func is not None else _decorate


_ORDER_ID_FULL_RE = re.compile(rf"^{ORDER_ID_RE}$")

_oms = OrderManagementClient()  # backend adapter — tools never touch the store directly


class ShipmentStatus(BaseModel):
    """Typed, compact tool output — exactly what the model needs to reason
    (status, ETA, SLA flag), never a raw backend blob (SPEC §7 mistake #3)."""

    order_id: str
    status: Literal["processing", "in_transit", "out_for_delivery",
                     "delivered", "exception"]
    eta: str | None
    sla_breached: bool


def track_shipment_impl(order_id: str) -> dict:
    """Get the current delivery status of ONE order by its id.

    Use for "where is my order" questions. Do NOT use for refunds — see
    `rafeeq.tools.billing.issue_refund`. Do NOT use to change a delivery
    time — see `rafeeq.tools.logistics.reschedule_delivery`.

    order_id format: TW-YYYY-NNNNN (e.g. TW-2026-88120).

    Returns on success: {"order_id", "status", "eta", "sla_breached"}
    (see `ShipmentStatus`). Returns {"error": "invalid_order_id_format"}
    for a malformed id and {"error": "order_not_found"} for an id that
    is well-formed but does not exist — never raises either way.
    """
    if not _ORDER_ID_FULL_RE.match(order_id):
        return {"error": "invalid_order_id_format"}  # value, not exception
    try:
        record = _oms.get_order(order_id)
    except ToolError:
        return {"error": "order_not_found"}
    return ShipmentStatus(
        order_id=order_id, status=record.status,
        eta=record.eta_iso, sla_breached=record.sla_breached,
    ).model_dump()


@tool
def track_shipment(order_id: str) -> dict:
    """Get the current delivery status of ONE order by its id.
    Use for 'where is my order' questions. Do NOT use for refunds.
    order_id format: TW-YYYY-NNNNN (e.g. TW-2026-88120)."""
    return track_shipment_impl(order_id)


TOOLS = [track_shipment]
