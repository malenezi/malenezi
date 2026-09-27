"""Module 3 — shared MCP server bootstrap.

Every server in this directory (`orders_server.py`, `logistics_server.py`,
`billing_server.py`, `customer_server.py`) imports from here instead of
each re-implementing the same three things:

1. An import-guarded `FastMCP` — the `mcp` package is a Layer-B dependency
   (SPEC §1) not installed in the Layer-A sandbox. This module, and every
   server built on it, MUST still import cleanly and expose plain,
   directly-callable functions without `mcp` installed; only `serve()`
   actually needs the real package.
2. `guarded_tool` — a decorator that enforces `agent_may_access` (the
   module's central lesson: authorisation lives at the SERVER, never in
   the agent's prompt — SPEC §7 mistake #6) BEFORE a tool body runs, and
   writes an audit record AFTER. It registers the wrapped function with a
   real `FastMCP` instance when one is available, and always returns the
   plain wrapped function so tests and `mcp_client.py`'s local fallback
   can call it directly either way.
3. `serve(mcp)` — the stdio-transport entrypoint every server's
   `if __name__ == "__main__":` block calls. Prints a clear hint instead
   of crashing when `mcp` is not installed.
"""
from __future__ import annotations

import functools
import sys
from pathlib import Path
from typing import Any, Callable

# Make `rafeeq` importable when a server is launched directly
# (`python3 mcp_servers/orders_server.py`) regardless of PYTHONPATH — the
# same pattern `scripts/selfcheck.py` uses, so the servers are runnable
# standalone exactly as the module package's Lab 3 instructs.
_REPO_ROOT = Path(__file__).resolve().parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.security.authz import agent_may_access  # noqa: E402 - after sys.path fixup

try:
    from mcp.server.fastmcp import FastMCP

    MCP_AVAILABLE = True
except ImportError:  # pragma: no cover - expected in the Layer-A sandbox
    FastMCP = None  # type: ignore[assignment,misc]
    MCP_AVAILABLE = False

MISSING_DEP_HINT = (
    "The `mcp` package is not installed in this environment, so this "
    "server cannot actually serve over stdio. Run `pip install mcp` (a "
    "Layer-B dependency, SPEC §1) to run it as a real MCP server. Until "
    "then every tool function below is still a plain, directly-callable "
    "Python function — import this module and call e.g. `track_shipment"
    "(order_id=..., agent_id=..., customer_id=...)` yourself, or use "
    "`rafeeq.tools.mcp_client.load_tools_local()` for the in-process "
    "equivalent tool surface."
)


def make_server(name: str) -> Any:
    """`FastMCP(name)` when `mcp` is installed, else `None`. Every server
    module calls this once at import time and passes the result to every
    `@guarded_tool(mcp, ...)` — `guarded_tool` itself handles `mcp is
    None` by simply not registering, so the rest of a server file reads
    identically whether or not the dependency is present."""
    return FastMCP(name) if MCP_AVAILABLE else None


def guarded_tool(mcp: Any, *, domain: str) -> Callable[[Callable[..., dict]], Callable[..., dict]]:
    """Decorator factory: wrap a tool FUNCTION so that, on every call:

      1. Authorisation is checked FIRST, via `agent_may_access`, against
         the caller-supplied `agent_id` and `customer_id` keyword
         arguments — BEFORE the wrapped function's body runs at all. A
         denial never reaches the backend adapter.
      2. The wrapped function runs, defensively caught so a bug in a tool
         body still returns an error VALUE (SPEC §7 mistake #4) rather
         than crashing the server process.
      3. An audit record is written AFTER, success or failure, via
         `_audit` (best-effort, mirrors `authz.py`'s lazy-import pattern
         for `security/events.py`).

    `domain` is recorded on the audit entry for the trust-boundary table
    in `mcp_servers/README.md`; the actual authorisation domain lookup
    itself comes from `rafeeq.tools.registry.TOOL_DOMAIN` inside
    `agent_may_access`, so `domain` here is documentation/audit context,
    not a second source of truth.

    The wrapped function's OWN signature is the tool's schema — it must
    accept `agent_id: str` and `customer_id: str` as keyword arguments in
    addition to its business arguments, exactly as the module package's
    `logistics_server.py` example shows.
    """

    def _decorator(func: Callable[..., dict]) -> Callable[..., dict]:
        tool_name = func.__name__

        @functools.wraps(func)
        def _wrapped(*args: Any, **kwargs: Any) -> dict:
            agent_id = kwargs.get("agent_id")
            customer_id = kwargs.get("customer_id")
            # Authorisation CONTEXT, not a business argument: popped out of
            # kwargs so it is never forwarded into `func` (whose signature
            # does not declare it) but IS passed to `agent_may_access`,
            # whose same-customer-only policies (security/authz.py) key
            # off it. A caller omitting it is exactly how a
            # same-customer-only agent gets fail-closed-denied below.
            session_customer_id = kwargs.pop("session_customer_id", None)

            if not agent_id or not customer_id:
                return {"error": "missing_authz_context", "detail": "agent_id and customer_id are required"}

            if not agent_may_access(agent_id, tool_name, customer_id, session_customer_id=session_customer_id):
                _audit(tool_name, domain, agent_id, customer_id, ok=False, code="not_authorised")
                return {"error": "not_authorised"}

            try:
                result = func(*args, **kwargs)
            except Exception as exc:  # noqa: BLE001 - a tool must never crash the server (SPEC §7 mistake #4)
                _audit(tool_name, domain, agent_id, customer_id, ok=False, code="server_exception")
                return {"error": "server_exception", "detail": str(exc)}

            failed = isinstance(result, dict) and result.get("error")
            _audit(tool_name, domain, agent_id, customer_id, ok=not failed,
                   code=(result.get("error") if failed else None))
            return result

        if MCP_AVAILABLE and mcp is not None:
            mcp.tool()(_wrapped)
        return _wrapped

    return _decorator


def _audit(tool_name: str, domain: str, agent_id: str, customer_id: str, *, ok: bool, code: str | None) -> None:
    """Best-effort audit log, same lazy-import-with-fallback shape as
    `rafeeq.security.authz._log_denial` — `security/events.py` is owned
    elsewhere in this build and may not exist yet or may expose a
    different function name; a logging failure must never affect the
    tool call's own result."""
    try:
        from rafeeq.security import events as _events

        log_fn = getattr(_events, "log_tool_call", None) or getattr(_events, "log_event", None)
        if log_fn is None:
            raise ImportError("rafeeq.security.events has no logging entry point yet")
        try:
            log_fn(event="mcp_tool_call", tool_name=tool_name, domain=domain,
                   agent_id=agent_id, customer_id=customer_id, ok=ok, code=code)
        except TypeError:
            log_fn(tool_name, domain, agent_id, customer_id, ok, code)
    except Exception:  # noqa: BLE001 - audit logging must never break a tool call
        import logging

        logging.getLogger("rafeeq.mcp_servers.audit").info(
            "tool_call: tool=%s domain=%s agent=%s customer=%s ok=%s code=%s",
            tool_name, domain, agent_id, customer_id, ok, code,
        )


def serve(mcp: Any) -> None:
    """Run `mcp` over stdio transport, exactly as the module package's
    `mcp.run(transport="stdio")` — or, when `mcp` (the package) is not
    installed and `make_server` therefore returned `None`, print
    `MISSING_DEP_HINT` instead of crashing so a participant sees a clear
    next step rather than an ImportError traceback."""
    if not MCP_AVAILABLE or mcp is None:
        print(MISSING_DEP_HINT)
        return
    mcp.run(transport="stdio")
