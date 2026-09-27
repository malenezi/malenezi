"""Module 8/9/final capstone — the `/v1/resolve` service.

The capstone architecture diagram, as code:

    Client (AR/EN ticket) -> API /v1/resolve -> input guardrail -> Supervisor
                                                                       |
                                               (scoped handoff, logged, M6)
                                                                       v
                                                        Orders/Logistics/Billing
                                                                       |
                                              output guardrail -> aggregate/escalate -> response
                          cross-cutting: tracing . cost attribution . budget . audit

`resolve_ticket()` is that whole pipeline as ONE function, and it is the
single thing BOTH entry points call:

  1. the synchronous HTTP API (`build_fastapi_app()` when `fastapi` is
     installed, else `run_stdlib_server()` — a real `http.server`
     fallback, so this genuinely runs with zero extra dependencies);
  2. the offline eval replay (`replay_tickets()`, driving the exact same
     function over `data/tickets_eval.jsonl`, with no HTTP server at all).

That is the capstone's LO1 requirement ("two entry points ... driving the
SAME compiled graph") made structurally visible: there is exactly one
pipeline function, and the two entry points are thin adapters around it,
not two copies of the logic.

`resolve_ticket` calls `evaluations.targets.get_target(target_name)` for
the actual supervisor/specialist reasoning — the SAME target contract the
eval harness and TawseelBench already grade (`evaluations/targets.py`),
so "the compiled graph" is genuinely one artefact whether it is `stub`
(offline, Layer A, what this file runs under SPEC §1's sandbox) or a real
LangGraph `monolith`/`supervisor`/`agents_as_tools` target once `langgraph`
is installed (Layer B) — `resolve_ticket(ticket, target_name="supervisor")`
is the only line that would need to change.

Dependency-free core (Layer A): stdlib + pydantic + the observability/
security/orchestration modules already import-guarded elsewhere in this
tree. `fastapi`/`uvicorn` are imported lazily, only inside
`build_fastapi_app()`/`main()`, and only if present.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any

from rafeeq.core.budget import RunBudget
from rafeeq.core.config import REPO_ROOT, TICKETS_EVAL_PATH, get_settings
from rafeeq.core.errors import BudgetExceeded
from rafeeq.observability import audit, cost as cost_mod, tracing
from rafeeq.observability.optimise import route_model_name
from rafeeq.orchestration.routing import classify_intent
from rafeeq.security.input_guard import screen_and_log
from rafeeq.security.output_guard import guard_response
from rafeeq.service.health import liveness, readiness
from rafeeq.service.schemas import HealthStatus, Resolution, TicketIn, ToolCallOut

try:  # pragma: no cover - exercised only when fastapi is installed
    from fastapi import FastAPI

    FASTAPI_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    FastAPI = None  # type: ignore[assignment,misc]
    FASTAPI_AVAILABLE = False

MISSING_FASTAPI_HINT = (
    "`fastapi`/`uvicorn` are not installed, so build_fastapi_app()/main() "
    "cannot serve over the ASGI stack (pip install fastapi uvicorn). "
    "resolve_ticket()/replay_tickets() need neither and already run under "
    "plain python3; run_stdlib_server() serves the same pipeline over "
    "plain http.server with zero extra dependencies — see docs/OFFLINE_MODE.md."
)


def _require_fastapi() -> None:
    if not FASTAPI_AVAILABLE:
        raise ImportError(MISSING_FASTAPI_HINT)


# --------------------------------------------------------------------------
# The pipeline. ONE function, called by both entry points.
# --------------------------------------------------------------------------
def _extract_customer_ids(tool_calls: list[dict[str, Any]]) -> list[str]:
    """Customer ids echoed anywhere in this run's tool results — what
    `security.output_guard.guard_response`'s cross-customer-egress check
    inspects. A read tool legitimately returns the session's own
    `customer_id`; the guard only blocks when a FOREIGN one appears."""
    ids: list[str] = []
    for tc in tool_calls:
        result = tc.get("result")
        if isinstance(result, dict):
            cid = result.get("customer_id")
            if cid:
                ids.append(str(cid))
    return ids


def resolve_ticket(ticket: TicketIn, target_name: str | None = None) -> Resolution:
    """Run ONE ticket through the full pipeline: input guardrail ->
    supervisor (the compiled target) -> output guardrail -> response,
    with tracing, a run budget, and a full audit trail wired in. Never
    raises for an ordinary bad/hostile input — a guardrail trip or a
    budget breach becomes `resolution="escalated"`/`"refused"`, not an
    exception; only a genuine programming error propagates."""
    # `evaluations/` lives at the repo root, not under `src/` — add it to
    # sys.path the same way harness.py/tawseelbench/runner.py do, so this
    # module is importable regardless of how the caller set PYTHONPATH.
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from evaluations.targets import Task, get_target  # lazy: keep this module importable stand-alone

    settings = get_settings()
    target_name = target_name or os.environ.get("RAFEEQ_TARGET", "stub")
    budget = RunBudget()
    t0 = time.monotonic()

    with tracing.start_run(f"resolve:{ticket.ticket_id}", ticket_id=ticket.ticket_id,
                             locale=ticket.locale) as run:
        # -- 1. input guardrail -------------------------------------------------
        with tracing.start_span("input_guardrail", run_type="guardrail") as ispan:
            guard = screen_and_log(ticket.text, source="customer_message")
            ispan.extra["risk_score"] = guard.risk_score
            ispan.extra["families"] = guard.families
        audit.log_decision(ticket.ticket_id, "input_guard_screened",
                            rationale=f"risk_score={guard.risk_score}", families=guard.families)

        intent, confidence = classify_intent(guard.cleaned)
        effective_intent = ticket.intent_hint or intent
        run.root.extra["intent"] = effective_intent
        routed_model = route_model_name(effective_intent, confidence)
        audit.log_decision(ticket.ticket_id, "model_routed", actor="optimise.route_model",
                            rationale=f"intent={effective_intent} confidence={confidence:.2f}",
                            routed_model=routed_model)

        # -- 2. supervisor (the compiled target) ---------------------------------
        task = Task(id=ticket.ticket_id, text=guard.cleaned, locale=ticket.locale,
                    customer_id=ticket.customer_id, order_id=ticket.order_id,
                    intent_hint=ticket.intent_hint)
        target = get_target(target_name)
        with tracing.start_span("supervisor", run_type="chain", model=routed_model) as sspan:
            result = target(task)
            sspan.tokens_in = result.tokens_in
            sspan.tokens_out = result.tokens_out
            # Deliberately NOT copying result.cost_usd onto the span: the
            # `stub` target prices itself at the (free) "stub" model
            # (SPEC §2 — stub mode is genuinely zero-cost) regardless of
            # which tier `route_model_name` chose. Leaving the span's
            # `cost_usd` unset lets `cost.py` price these same tokens at
            # `routed_model` instead, so the cost report shows the REAL
            # financial effect of the routing decision — what this run
            # would have cost against the model tier it was actually
            # routed to — rather than a flat zero that would hide the
            # lever the report exists to measure.
            sspan.extra["steps"] = result.steps
            if result.specialist:
                with tracing.start_span(f"{result.specialist}_specialist", run_type="chain"):
                    pass
                audit.log_handoff(ticket.ticket_id, result.specialist, subgoal=effective_intent)
            for tc in result.tool_calls:
                tc_result = tc.get("result")
                tool_error = isinstance(tc_result, dict) and bool(tc_result.get("error"))
                with tracing.start_span(tc.get("name", "tool"), run_type="tool",
                                          tool_name=tc.get("name"), args=tc.get("args")) as tspan:
                    if tool_error:
                        tspan.error = str(tc_result.get("error"))
                audit.log_tool_call(ticket.ticket_id, tc.get("name", ""), tc.get("args", {}), tc_result)
            if result.escalated:
                audit.log_escalation(ticket.ticket_id, "escalated", reason=result.escalation_reason)

        # -- budget: bounded by construction, not by the model's own say-so ------
        try:
            budget.check({"step_count": result.steps, "cost_usd": result.cost_usd})
        except BudgetExceeded as exc:
            result.escalated = True
            result.escalation_reason = result.escalation_reason or f"budget_exceeded:{exc.detail.get('axis')}"
            audit.log_escalation(ticket.ticket_id, "escalated", reason=result.escalation_reason)

        # -- 3. output guardrail --------------------------------------------------
        response_customer_ids = _extract_customer_ids(result.tool_calls)
        with tracing.start_span("output_guardrail", run_type="guardrail") as ospan:
            safe_text = guard_response(result.reply_text, actor_customer_id=ticket.customer_id,
                                        response_customer_ids=response_customer_ids)
            blocked = safe_text != result.reply_text
            ospan.extra["blocked"] = blocked
        audit.log_decision(ticket.ticket_id, "output_guard_checked",
                            rationale="blocked" if blocked else "passed")

    latency_s = round(time.monotonic() - t0, 4)

    # -- 4. response: cost attribution from the trace we just produced -------
    breakdown = cost_mod.cost_of_run(run)
    total_usd = breakdown.total_usd or result.cost_usd
    if result.refused:
        resolution_state = "refused"
    elif result.escalated:
        resolution_state = "escalated"
    else:
        resolution_state = "resolved"

    flags = list(guard.flags)
    if blocked:
        flags.append("output_guard_blocked")

    return Resolution(
        ticket_id=ticket.ticket_id,
        trace_id=run.run_id,
        resolution=resolution_state,
        reply_text=safe_text,
        locale=ticket.locale,
        specialist=result.specialist,
        tool_calls=[
            ToolCallOut(name=tc.get("name", ""),
                        ok=not (isinstance(tc.get("result"), dict) and tc["result"].get("error")))
            for tc in result.tool_calls
        ],
        escalated=result.escalated,
        escalation_reason=result.escalation_reason,
        cost_usd=round(total_usd, 6),
        cost_sar_equivalent=round(total_usd * cost_mod.SAR_PER_USD, 4),
        latency_s=latency_s,
        flags=flags,
        routed_model=routed_model,
    )


# --------------------------------------------------------------------------
# Entry point 2: offline eval replay — the SAME pipeline, no HTTP at all.
# --------------------------------------------------------------------------
def replay_tickets(path: Path = TICKETS_EVAL_PATH, limit: int | None = None,
                    target_name: str | None = None) -> list[Resolution]:
    """Drive `resolve_ticket` over `data/tickets_eval.jsonl` (or any file
    in the same shape) with no server running at all — the offline
    replay entry point. Used by CI's eval-harness gate and by
    `docs/OBSERVABILITY.md`'s "traces feed back into evaluation datasets"
    principle: a resolved run here produces the same trace/audit/cost
    artefacts a live request would."""
    tickets: list[dict[str, Any]] = []
    with Path(path).open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                tickets.append(json.loads(line))
    if limit is not None:
        tickets = tickets[:limit]

    results: list[Resolution] = []
    for row in tickets:
        ticket = TicketIn(
            ticket_id=row["ticket_id"], text=row["text"], locale=row.get("locale", "en"),
            customer_id=row.get("customer_id"), order_id=row.get("order_id"),
            intent_hint=row.get("intent"),
        )
        results.append(resolve_ticket(ticket, target_name=target_name))
    return results


# --------------------------------------------------------------------------
# Entry point 1a: FastAPI (when installed).
# --------------------------------------------------------------------------
def build_fastapi_app() -> Any:
    _require_fastapi()
    app = FastAPI(title="Rafeeq", description="Tawseel agentic operations service", version="1.0.0")

    @app.post("/v1/resolve", response_model=Resolution)
    def _resolve(ticket: TicketIn) -> Resolution:  # pragma: no cover - exercised only with fastapi installed
        return resolve_ticket(ticket)

    @app.get("/healthz", response_model=HealthStatus)
    def _healthz() -> HealthStatus:  # pragma: no cover
        return liveness()

    @app.get("/readyz", response_model=HealthStatus)
    def _readyz() -> HealthStatus:  # pragma: no cover
        return readiness()

    return app


# --------------------------------------------------------------------------
# Entry point 1b: stdlib http.server fallback — runs with ZERO extra deps.
# --------------------------------------------------------------------------
def _build_stdlib_handler() -> type:
    from http.server import BaseHTTPRequestHandler

    class Handler(BaseHTTPRequestHandler):
        def _send_json(self, obj: dict[str, Any], status: int = 200) -> None:
            body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802 - stdlib method name
            if self.path == "/healthz":
                self._send_json(liveness().model_dump())
            elif self.path == "/readyz":
                hs = readiness()
                self._send_json(hs.model_dump(), status=200 if hs.status == "ok" else 503)
            else:
                self._send_json({"error": "not_found", "path": self.path}, status=404)

        def do_POST(self) -> None:  # noqa: N802 - stdlib method name
            if self.path != "/v1/resolve":
                self._send_json({"error": "not_found", "path": self.path}, status=404)
                return
            length = int(self.headers.get("Content-Length", "0") or "0")
            raw = self.rfile.read(length) if length else b"{}"
            try:
                payload = json.loads(raw.decode("utf-8"))
                ticket = TicketIn(**payload)
                resolution = resolve_ticket(ticket)
                self._send_json(resolution.model_dump())
            except Exception as exc:  # noqa: BLE001 - a bad request must 400, never crash the server
                self._send_json({"error": "bad_request", "detail": f"{type(exc).__name__}: {exc}"}, status=400)

        def log_message(self, fmt: str, *args: Any) -> None:  # noqa: A003 - silence default stderr access log
            pass

    return Handler


def run_stdlib_server(host: str = "0.0.0.0", port: int = 8000) -> None:
    """Serve `/v1/resolve`, `/healthz`, `/readyz` over plain
    `http.server` — no `fastapi`/`uvicorn` required, so the service
    "genuinely runs anywhere" (SPEC's own phrase for this fallback)."""
    from http.server import HTTPServer

    handler = _build_stdlib_handler()
    httpd = HTTPServer((host, port), handler)
    print(f"rafeeq stdlib server listening on http://{host}:{port} "
          f"(fastapi not installed — see MISSING_FASTAPI_HINT)", file=sys.stderr)
    httpd.serve_forever()


def main() -> None:  # pragma: no cover - process entrypoint
    host = os.environ.get("RAFEEQ_HOST", "0.0.0.0")
    port = int(os.environ.get("RAFEEQ_PORT", "8000"))
    if FASTAPI_AVAILABLE:
        try:
            import uvicorn

            uvicorn.run(build_fastapi_app(), host=host, port=port)
            return
        except ImportError:
            pass
    run_stdlib_server(host, port)


if __name__ == "__main__":  # pragma: no cover - manual run
    main()
