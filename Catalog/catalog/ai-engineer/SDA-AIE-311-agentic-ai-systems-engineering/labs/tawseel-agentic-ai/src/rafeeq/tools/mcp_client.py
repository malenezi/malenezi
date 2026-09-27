"""Module 3 — MCP client: discover and bind Tawseel's four MCP servers.

`load_tawseel_tools()` is Layer B: it depends on `mcp` and
`langchain-mcp-adapters`, neither of which is installed in the Layer-A
build/CI sandbox (SPEC §1), so it is import-guarded — this module always
imports cleanly under plain python3, and the dependency is only touched
inside the function body, at call time, not at import time.

`load_tools_local()` is the offline fallback SPEC asks for: it returns the
SAME governed tool objects in-process (no subprocess, no JSON-RPC) by
importing the domain tool modules directly, so every lab and the eval
harness work with zero setup even where `mcp` cannot be installed.

TEACHING POINT: the agent depends on the PROTOCOL (`load_tawseel_tools`),
not on each backend's SDK. Swap a server's implementation, or move it to
a different machine, and this file's contract is unchanged. The local
fallback trades that decoupling for offline convenience — and, just as
importantly, trades away the MCP servers' authorisation-at-the-server
enforcement (`security/authz.py` via `mcp_servers/common.py`'s
`guarded_tool`): `load_tools_local()` binds the tools directly, with no
per-call authz check in front of them. That is acceptable for a single-
learner lab sandbox and NEVER acceptable in a real deployment — production
Rafeeq always goes through `load_tawseel_tools()` so authorisation is
enforced server-side, not skipped.
"""
from __future__ import annotations

from typing import Any

from rafeeq.core.config import REPO_ROOT

MISSING_DEP_HINT = (
    "langchain-mcp-adapters (and mcp) are not installed in this "
    "environment. Run `pip install mcp langchain-mcp-adapters` to use "
    "load_tawseel_tools(); until then, call load_tools_local() for the "
    "same tool surface bound in-process (SPEC §1's offline-first rule)."
)

_SERVERS_DIR = REPO_ROOT / "mcp_servers"

# One entry per MCP server (SPEC §6: one server per trust boundary, not
# one mega-server) — stdio transport, each server a separate `python3`
# subprocess the client launches and talks JSON-RPC to over stdin/stdout.
SERVER_SPECS: dict[str, dict[str, Any]] = {
    "orders": {
        "command": "python3",
        "args": [str(_SERVERS_DIR / "orders_server.py")],
        "transport": "stdio",
    },
    "logistics": {
        "command": "python3",
        "args": [str(_SERVERS_DIR / "logistics_server.py")],
        "transport": "stdio",
    },
    "billing": {
        "command": "python3",
        "args": [str(_SERVERS_DIR / "billing_server.py")],
        "transport": "stdio",
    },
    "customer": {
        "command": "python3",
        "args": [str(_SERVERS_DIR / "customer_server.py")],
        "transport": "stdio",
    },
}


async def load_tawseel_tools() -> list[Any]:
    """Discover and bind tools from ALL FOUR Tawseel MCP servers at
    runtime via `MultiServerMCPClient`. Bind the result to a chat model
    with `model.bind_tools(tools)`.

    Requires `mcp` + `langchain-mcp-adapters` (Layer B) and a working
    python3 the client can spawn as a subprocess for each server — not
    executable in the Layer-A sandbox. Raises `ImportError` with
    `MISSING_DEP_HINT` if the adapters package is missing, so a caller
    can catch it and fall back to `load_tools_local()`.
    """
    try:
        from langchain_mcp_adapters.client import MultiServerMCPClient
    except ImportError as exc:  # pragma: no cover - Layer-B only
        raise ImportError(MISSING_DEP_HINT) from exc

    client = MultiServerMCPClient(SERVER_SPECS)
    tools = await client.get_tools()  # runtime discovery, not a hard-coded list
    return tools


def load_tools_local() -> list[Any]:
    """Offline fallback: return Rafeeq's full governed tool surface bound
    IN-PROCESS (no MCP transport, no subprocess, no per-call authz —
    see the module docstring), by delegating to
    `rafeeq.tools.registry.ALL_TOOLS`.

    Use this in labs/tests/the eval harness when `mcp` and
    `langchain-mcp-adapters` are unavailable, or simply when you do not
    need the trust-boundary/process-isolation properties MCP provides for
    a given run. Never used as a substitute for MCP in a deployed system.
    """
    from rafeeq.tools.registry import ALL_TOOLS

    return list(ALL_TOOLS)
