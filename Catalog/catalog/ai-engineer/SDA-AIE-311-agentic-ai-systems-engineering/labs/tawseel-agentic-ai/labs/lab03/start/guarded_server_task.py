"""Lab 3, Task 2 — an MCP server with authorisation enforced AT THE SERVER.

The teachable contrast: a prompt saying "never refund over 500 SAR" is
advice a crafted input can argue past. The SAME rule enforced HERE, before
a tool body runs at all, cannot be talked around by anything the model
says — because the model never gets a vote (SPEC §7 mistake #6).

Fill in the TODOs. This file needs no `mcp` package to be USEFUL: like the
real `mcp_servers/common.py`, `guarded_tool` wraps and returns a plain,
directly-callable Python function either way, and only real network
serving needs the `mcp` package installed.
"""
from __future__ import annotations

import functools
import sys
from pathlib import Path
from typing import Any, Callable

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.security.authz import agent_may_access

try:
    import tools_task  # this lab's own Task 1 module
except ImportError:  # running from elsewhere
    from labs.lab03.start import tools_task  # type: ignore[no-redef]


def guarded_tool(*, domain: str) -> Callable[[Callable[..., dict]], Callable[..., dict]]:
    """TODO(lab 3.2): a decorator factory. The wrapped function must, on
    every call:

    1. Read `agent_id` and `customer_id` from `kwargs` (they are passed as
       part of the tool's own keyword arguments, exactly like the real
       `mcp_servers/common.py::guarded_tool`). If either is missing,
       return `{"error": "missing_authz_context"}` WITHOUT calling the
       wrapped function.
    2. Call `agent_may_access(agent_id, tool_name, customer_id)` — if it
       returns `False`, return `{"error": "not_authorised"}` WITHOUT
       calling the wrapped function. `tool_name` is `func.__name__`.
    3. Otherwise call the wrapped function and return its result.
    4. Wrap the call in a `try/except Exception` so a bug in the tool body
       returns `{"error": "server_exception", "detail": str(exc)}` rather
       than crashing the whole server process — a tool must never take
       the server down (SPEC §7 mistake #4, at the server this time).

    `domain` is documentation context only (matches the real signature) —
    the actual authorisation lookup happens inside `agent_may_access`.
    """
    def _decorator(func: Callable[..., dict]) -> Callable[..., dict]:
        raise NotImplementedError("TODO(lab 3.2): implement the wrapping logic")
    return _decorator


# TODO(lab 3.2): apply `@guarded_tool(domain="logistics")` to a function
# `track_shipment(order_id: str, agent_id: str, customer_id: str) -> dict`
# that calls `tools_task.track_shipment_impl(order_id)` — this is the
# worked example the Module 3 package's `logistics_server.py` shows.
