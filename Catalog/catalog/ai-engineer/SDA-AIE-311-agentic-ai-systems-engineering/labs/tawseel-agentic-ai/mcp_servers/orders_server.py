"""Module 3 — the Tawseel Order-Management MCP server.

TRUST BOUNDARY: read-only surface over order records for every authorised
agent identity — no write tool exists in this server at all, so even a
fully compromised or jailbroken calling agent cannot mutate an order
through it; the worst it can do is over-read (mitigated by `agent_may_access`
scoping below). OWASP risk addressed: Excessive Agency — the blast radius
of this server is capped at "read orders" by construction, not by prompt
instruction, regardless of what an agent is talked into requesting.

Run standalone: `python3 mcp_servers/orders_server.py` (stdio transport).
"""
from __future__ import annotations

import sys
from pathlib import Path

# So `python3 mcp_servers/orders_server.py` works standalone regardless of
# cwd/PYTHONPATH: put the repo root on sys.path before importing the
# `mcp_servers` package (this file's own directory is already sys.path[0]
# when run directly, but its PARENT — needed for `mcp_servers.common` —
# is not, unless we add it here).
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from mcp_servers.common import guarded_tool, make_server, serve  # noqa: E402

from rafeeq.tools.orders import get_order_impl, get_order_items_impl, list_orders_impl  # noqa: E402

mcp = make_server("tawseel-orders")


@guarded_tool(mcp, domain="orders")
def get_order(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Get the full order record for ONE order by its id (status, amount,
    city, refund state). Authorisation is enforced HERE via
    `agent_may_access`, not in the calling agent's prompt.
    order_id format: TW-YYYY-NNNNN."""
    return get_order_impl(order_id)


@guarded_tool(mcp, domain="orders")
def list_orders(customer_id: str, agent_id: str) -> dict:
    """List all of `customer_id`'s orders. Authorisation is enforced HERE.
    customer_id format: CUST-NNNN."""
    return list_orders_impl(customer_id)


@guarded_tool(mcp, domain="orders")
def get_order_items(order_id: str, agent_id: str, customer_id: str) -> dict:
    """Get the item count (not a line-item breakdown) for ONE order.
    Authorisation is enforced HERE. order_id format: TW-YYYY-NNNNN."""
    return get_order_items_impl(order_id)


if __name__ == "__main__":
    serve(mcp)
