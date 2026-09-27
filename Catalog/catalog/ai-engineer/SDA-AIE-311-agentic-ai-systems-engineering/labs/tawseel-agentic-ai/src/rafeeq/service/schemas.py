"""Module 8/9/final capstone — request/response contracts for `/v1/resolve`.

`TicketIn` is what a client (the sync HTTP API, or the offline eval
replay driver — `service/api.py`'s two entry points) sends in; `Resolution`
is what comes back: the reply, WHERE it can be inspected further
(`trace_id`), WHAT it cost, and WHAT was flagged — never just a string.

`pydantic` v2 is a Layer-A-safe dependency (SPEC §1 lists it alongside
the stdlib for the build sandbox), so this module imports it directly —
no import guard needed here, unlike `langgraph`/`fastapi`.
"""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

from rafeeq.core.config import TICKET_INTENTS


class TicketIn(BaseModel):
    """One inbound customer ticket — the same shape as a
    `data/tickets_eval.jsonl` row's core fields (SPEC §4), so a row from
    that file can be sent to `/v1/resolve` unmodified for a live smoke
    test against the offline replay's own fixtures."""

    ticket_id: str = Field(..., description="TKT-NNNNN")
    text: str = Field(..., min_length=1, description="The customer's message, AR or EN.")
    locale: Literal["ar", "en"] = "en"
    customer_id: str | None = None
    order_id: str | None = None
    intent_hint: str | None = Field(default=None, description=f"One of {sorted(TICKET_INTENTS)}, optional.")
    agent_id: str = Field(default="customer_agent", description="Authorisation identity (security.authz.POLICY key).")


class ToolCallOut(BaseModel):
    """One tool call the run made, as seen from the OUTSIDE — name and
    whether it errored, never raw args/result (those stay in the audit
    log, PII-masked, not on the wire to an API caller)."""

    name: str
    ok: bool


class Resolution(BaseModel):
    """What `/v1/resolve` returns. `trace_id` is the pointer into
    `reports/traces/<trace_id>.json` for full inspection — the response
    itself stays small and customer-safe."""

    ticket_id: str
    trace_id: str
    resolution: Literal["resolved", "escalated", "refused"]
    reply_text: str
    locale: Literal["ar", "en"]
    specialist: str | None = None
    tool_calls: list[ToolCallOut] = Field(default_factory=list)
    escalated: bool = False
    escalation_reason: str | None = None
    cost_usd: float = 0.0
    cost_sar_equivalent: float = 0.0
    latency_s: float = 0.0
    flags: list[str] = Field(default_factory=list)
    routed_model: str | None = None


class HealthStatus(BaseModel):
    status: Literal["ok", "degraded", "down"]
    checks: dict[str, Any] = Field(default_factory=dict)
