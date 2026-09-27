"""Module 9 — tracing: every run becomes an inspectable tree of spans.

Rafeeq was built as a state machine (M1) — every transition is already a
discrete, traceable event. This module makes that visible.

`LocalTracer` is the package's dependency-free tracer: a run is a tree of
`Span`s (`start_span` is a context manager, nestable) capturing name,
run_type, model, tokens in/out, latency, tool name, an args hash, and any
error. Every run is persisted to `reports/traces/<run_id>.json` and can be
rendered as the trace-tree anatomy diagram the module teaches
(`render_tree`).

`@traceable` is the package's LangSmith instrumentation. When `langsmith`
is installed AND `RAFEEQ_LANGSMITH=1` (or `enable_langsmith()` was called),
the real `langsmith.traceable` decorator also wraps the function so a live
run streams to LangSmith. Either way — this is the load-bearing part —
the SAME call is ALSO wrapped in a `LocalTracer` span, so a run produces a
local trace file unconditionally. TEACHING POINT: instrumentation must
degrade gracefully, not vanish, when a vendor SDK is absent (SPEC §1) —
every lab produces a trace even fully offline.

Dependency-free (Layer A): stdlib only (`contextvars`, `dataclasses`,
`hashlib`, `json`, `time`, `uuid`). `langsmith` is imported lazily, inside
`traceable`/`enable_langsmith`, and only if present.
"""
from __future__ import annotations

import contextvars
import functools
import hashlib
import json
import os
import threading
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Optional

from rafeeq.core.config import REPO_ROOT

TRACES_DIR = REPO_ROOT / "reports" / "traces"

try:  # pragma: no cover - exercised only when langsmith is installed
    import langsmith as _langsmith  # noqa: F401

    LANGSMITH_AVAILABLE = True
except ImportError:  # Layer-A / plain-python3 environment (expected here)
    LANGSMITH_AVAILABLE = False

MISSING_DEP_HINT = (
    "`langsmith` is not installed, so live LangSmith tracing is disabled "
    "(pip install langsmith to enable it). Every @traceable call still "
    "produces a full local trace tree via LocalTracer — see "
    "reports/traces/<run_id>.json and docs/OBSERVABILITY.md."
)

_write_lock = threading.Lock()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash_args(args: dict[str, Any] | None) -> str | None:
    """A short, stable hash of a tool call's args — enough to spot
    duplicate/repeated calls (a cache-hit candidate, or a looping agent)
    in a trace WITHOUT logging the raw args twice (they are already on
    the span in `extra` when the caller wants them, and the audit log —
    `audit.py` — is the place for the full, PII-masked argument record)."""
    if not args:
        return None
    try:
        blob = json.dumps(args, sort_keys=True, default=str, ensure_ascii=False)
    except TypeError:  # pragma: no cover - defensive
        blob = str(args)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


# --------------------------------------------------------------------------
# Span / Run — the trace tree.
# --------------------------------------------------------------------------
@dataclass
class Span:
    span_id: str
    name: str
    run_type: str                       # "chain" | "llm" | "tool" | "guardrail" | "router"
    parent_id: Optional[str]
    start_ts: float
    end_ts: Optional[float] = None
    model: Optional[str] = None
    tokens_in: int = 0
    tokens_out: int = 0
    tool_name: Optional[str] = None
    args_hash: Optional[str] = None
    error: Optional[str] = None
    children: list["Span"] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def latency_ms(self) -> float | None:
        if self.end_ts is None:
            return None
        return round((self.end_ts - self.start_ts) * 1000.0, 3)

    def to_dict(self) -> dict[str, Any]:
        return {
            "span_id": self.span_id,
            "name": self.name,
            "run_type": self.run_type,
            "parent_id": self.parent_id,
            "start_ts": self.start_ts,
            "end_ts": self.end_ts,
            "latency_ms": self.latency_ms,
            "model": self.model,
            "tokens_in": self.tokens_in,
            "tokens_out": self.tokens_out,
            "tool_name": self.tool_name,
            "args_hash": self.args_hash,
            "error": self.error,
            "extra": self.extra,
            "children": [c.to_dict() for c in self.children],
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Span":
        span = cls(
            span_id=d["span_id"], name=d["name"], run_type=d.get("run_type", "chain"),
            parent_id=d.get("parent_id"), start_ts=d.get("start_ts", 0.0), end_ts=d.get("end_ts"),
            model=d.get("model"), tokens_in=d.get("tokens_in", 0), tokens_out=d.get("tokens_out", 0),
            tool_name=d.get("tool_name"), args_hash=d.get("args_hash"), error=d.get("error"),
            extra=d.get("extra", {}) or {},
        )
        span.children = [cls.from_dict(c) for c in d.get("children", [])]
        return span

    def walk(self) -> Iterator["Span"]:
        """Depth-first iterator over this span and every descendant —
        what `cost.py::cost_of_run` and `render_tree` both walk."""
        yield self
        for child in self.children:
            yield from child.walk()


@dataclass
class Run:
    run_id: str
    name: str
    root: Span
    started_at: str

    def to_dict(self) -> dict[str, Any]:
        return {"run_id": self.run_id, "name": self.name, "started_at": self.started_at,
                "root": self.root.to_dict()}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Run":
        return cls(run_id=d["run_id"], name=d["name"], started_at=d.get("started_at", ""),
                    root=Span.from_dict(d["root"]))


# --------------------------------------------------------------------------
# LocalTracer — contextvar-based span stack, one active run/span per
# logical call stack (safe across threads: contextvars are per-context).
# --------------------------------------------------------------------------
class LocalTracer:
    def __init__(self) -> None:
        self._current_run: contextvars.ContextVar[Run | None] = contextvars.ContextVar("rafeeq_run", default=None)
        self._current_span: contextvars.ContextVar[Span | None] = contextvars.ContextVar("rafeeq_span", default=None)
        self._completed: dict[str, Run] = {}

    def current_run(self) -> Run | None:
        return self._current_run.get()

    def current_span(self) -> Span | None:
        return self._current_span.get()

    def start_run(self, name: str, **meta: Any):
        """Context manager. Starts a NEW run with a fresh root span and
        makes it (and the root span) current for the duration of the
        `with` block. Persists to `reports/traces/<run_id>.json` on exit,
        success or failure — a run that raised is still worth reading."""
        return _RunContext(self, name, meta)

    def start_span(self, name: str, run_type: str = "chain", **meta: Any):
        """Context manager. Nests under the current span; if no run is
        active yet, silently starts one named after this span so a bare
        `with tracer.start_span(...)` still produces a persisted trace —
        the "every lab produces a trace even offline" guarantee applies
        even to code that never explicitly calls `start_run`."""
        return _SpanContext(self, name, run_type, meta)

    def get_run(self, run_id: str) -> Run | None:
        run = self._completed.get(run_id)
        if run is not None:
            return run
        path = TRACES_DIR / f"{run_id}.json"
        if not path.exists():
            return None
        return Run.from_dict(json.loads(path.read_text(encoding="utf-8")))

    def _persist(self, run: Run) -> None:
        self._completed[run.run_id] = run
        try:
            with _write_lock:
                TRACES_DIR.mkdir(parents=True, exist_ok=True)
                (TRACES_DIR / f"{run.run_id}.json").write_text(
                    json.dumps(run.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8",
                )
        except OSError:  # noqa: BLE001 - tracing must never break the caller
            pass


class _RunContext:
    def __init__(self, tracer: LocalTracer, name: str, meta: dict[str, Any]) -> None:
        self._tracer = tracer
        self._name = name
        self._meta = meta
        self._run: Run | None = None
        self._run_token = None
        self._span_token = None

    def __enter__(self) -> Run:
        run_id = uuid.uuid4().hex[:16]
        root = Span(span_id=run_id, name=self._name, run_type="chain", parent_id=None,
                     start_ts=time.time(), extra=dict(self._meta))
        self._run = Run(run_id=run_id, name=self._name, root=root, started_at=_now_iso())
        self._run_token = self._tracer._current_run.set(self._run)
        self._span_token = self._tracer._current_span.set(root)
        return self._run

    def __exit__(self, exc_type, exc, _tb) -> bool:
        assert self._run is not None
        self._run.root.end_ts = time.time()
        if exc is not None:
            self._run.root.error = f"{exc_type.__name__}: {exc}"
        self._tracer._current_span.reset(self._span_token)
        self._tracer._current_run.reset(self._run_token)
        self._tracer._persist(self._run)
        return False  # never swallow the exception


class _SpanContext:
    def __init__(self, tracer: LocalTracer, name: str, run_type: str, meta: dict[str, Any]) -> None:
        self._tracer = tracer
        self._name = name
        self._run_type = run_type
        self._meta = meta
        self._span: Span | None = None
        self._span_token = None
        self._owns_run: _RunContext | None = None

    def __enter__(self) -> Span:
        if self._tracer.current_run() is None:
            # No active run: auto-start one so this span still lands in a
            # persisted trace file (see LocalTracer.start_span docstring).
            self._owns_run = _RunContext(self._tracer, f"auto:{self._name}", {})
            self._owns_run.__enter__()
        parent = self._tracer.current_span()
        span_id = uuid.uuid4().hex[:12]
        meta = dict(self._meta)
        tool_name = meta.pop("tool_name", None)
        args = meta.pop("args", None)
        model = meta.pop("model", None)
        tokens_in = int(meta.pop("tokens_in", 0) or 0)
        tokens_out = int(meta.pop("tokens_out", 0) or 0)
        span = Span(
            span_id=span_id, name=self._name, run_type=self._run_type,
            parent_id=parent.span_id if parent else None, start_ts=time.time(),
            model=model, tokens_in=tokens_in, tokens_out=tokens_out,
            tool_name=tool_name, args_hash=_hash_args(args), extra=meta,
        )
        if parent is not None:
            parent.children.append(span)
        self._span = span
        self._span_token = self._tracer._current_span.set(span)
        return span

    def __exit__(self, exc_type, exc, _tb) -> bool:
        assert self._span is not None
        self._span.end_ts = time.time()
        if exc is not None:
            self._span.error = f"{exc_type.__name__}: {exc}"
        self._tracer._current_span.reset(self._span_token)
        if self._owns_run is not None:
            self._owns_run.__exit__(exc_type, exc, _tb)
        return False


# --------------------------------------------------------------------------
# Module-level default tracer + convenience wrappers — the surface most
# callers use (`from rafeeq.observability import tracing; tracing.start_span(...)`).
# --------------------------------------------------------------------------
TRACER = LocalTracer()


def start_run(name: str, **meta: Any):
    return TRACER.start_run(name, **meta)


def start_span(name: str, run_type: str = "chain", **meta: Any):
    return TRACER.start_span(name, run_type=run_type, **meta)


def current_run() -> Run | None:
    return TRACER.current_run()


def current_span() -> Span | None:
    return TRACER.current_span()


def get_run(run_id: str) -> Run | None:
    return TRACER.get_run(run_id)


def enable_langsmith(project: str = "rafeeq-prod") -> bool:
    """Opt-in: set the LangSmith env vars for THIS process and return
    whether `langsmith` is actually installed. Never called at import time
    (SPEC §1: no network calls at import time) — a caller (the service
    entrypoint, a lab notebook) calls this explicitly once it has a key."""
    if not LANGSMITH_AVAILABLE:
        return False
    os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
    os.environ.setdefault("LANGCHAIN_PROJECT", project)
    return True


def traceable(run_type: str = "chain", name: str | None = None) -> Callable[[Callable], Callable]:
    """Decorator: `@traceable(run_type="chain", name="handle_ticket")`.

    ALWAYS wraps the call in a `LocalTracer` span (so a trace exists even
    fully offline). ADDITIONALLY applies `langsmith.traceable` when the
    package is installed, so the same decorated function streams to a
    real LangSmith project too, with no code change at the call site —
    exactly the degrade-gracefully contract this module's docstring
    promises.
    """

    def decorator(fn: Callable) -> Callable:
        span_name = name or getattr(fn, "__name__", "run")
        target = fn
        if LANGSMITH_AVAILABLE:  # pragma: no cover - exercised only with langsmith installed
            try:
                from langsmith import traceable as _ls_traceable

                target = _ls_traceable(run_type=run_type, name=span_name)(fn)
            except Exception:  # noqa: BLE001 - a broken langsmith install must not break tracing
                target = fn

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with start_span(span_name, run_type=run_type) as span:
                result = target(*args, **kwargs)
                _attach_result_metrics(span, result)
                return result

        wrapper.__wrapped_untraced__ = fn  # type: ignore[attr-defined]
        return wrapper

    return decorator


def _attach_result_metrics(span: Span, result: Any) -> None:
    """Best-effort: if the wrapped call returned something with the usual
    usage-metadata shape (a dict with `tokens_in`/`tokens_out`/`cost_usd`,
    or an object with `.usage_metadata`), copy it onto the span so
    `cost.py` can attribute it without every call site doing this by
    hand."""
    usage = None
    if isinstance(result, dict):
        usage = result
    else:
        usage = getattr(result, "usage_metadata", None)
    if not isinstance(usage, dict):
        return
    for key in ("tokens_in", "input_tokens"):
        if key in usage:
            span.tokens_in = int(usage[key])
            break
    for key in ("tokens_out", "output_tokens"):
        if key in usage:
            span.tokens_out = int(usage[key])
            break
    if "model" in usage and not span.model:
        span.model = usage["model"]


# --------------------------------------------------------------------------
# render_tree — the trace-tree anatomy diagram, as text.
# --------------------------------------------------------------------------
def render_tree(run: Run) -> str:
    """Render a `Run` as an indented trace-tree waterfall: each span with
    its run_type, latency, tokens, model/tool, and error — the picture
    Module 9's "Trace tree anatomy" diagram teaches, in text so it needs
    no plotting library and works in any terminal/CI log."""
    lines = [f"Run {run.run_id} — {run.name}  (started {run.started_at})"]

    def walk(span: Span, depth: int) -> None:
        indent = "  " * depth
        bits = [f"[{span.run_type}]", span.name]
        if span.model:
            bits.append(f"model={span.model}")
        if span.tokens_in or span.tokens_out:
            bits.append(f"tok_in={span.tokens_in} tok_out={span.tokens_out}")
        if span.tool_name:
            bits.append(f"tool={span.tool_name}")
        if span.args_hash:
            bits.append(f"args#{span.args_hash}")
        if span.latency_ms is not None:
            bits.append(f"{span.latency_ms}ms")
        if span.error:
            bits.append(f"ERROR: {span.error}")
        lines.append(f"{indent}└─ {' '.join(bits)}")
        for child in span.children:
            walk(child, depth + 1)

    walk(run.root, 0)
    n_spans = sum(1 for _ in run.root.walk())
    lines.append(f"\n{n_spans} span(s) total.")
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover - manual classroom demo
    # A synthetic refund run: supervisor -> billing specialist -> tool ->
    # output guardrail — the 6-span shape Module 9's expected output
    # names ("refund run: 6 spans; frontier model on supervisor = top
    # cost"). Real runs are produced by rafeeq.service.api.resolve_ticket.
    with start_run("handle_ticket:TKT-DEMO", ticket_id="TKT-DEMO", intent="refund") as run:
        with start_span("supervisor", run_type="router", model="gpt-4o", tokens_in=420, tokens_out=60):
            with start_span("input_guardrail", run_type="guardrail"):
                pass
            with start_span("billing_specialist", run_type="chain", model="gpt-4o-mini", tokens_in=310, tokens_out=90):
                with start_span("issue_refund", run_type="tool", tool_name="issue_refund",
                                 args={"order_id": "TW-2026-88120", "amount_sar": 45.0}):
                    pass
            with start_span("output_guardrail", run_type="guardrail"):
                pass
    print(render_tree(run))
