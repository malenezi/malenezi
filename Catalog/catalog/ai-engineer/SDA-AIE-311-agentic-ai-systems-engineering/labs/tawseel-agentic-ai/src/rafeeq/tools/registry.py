"""Module 3 — the governed tool catalogue.

Single source of truth for WHICH tools exist, WHICH domain each belongs to,
and WHICH are safe to retry. Nothing else in this repo should hand-roll a
tool list or duplicate the idempotent/write split — `security/authz.py`
looks up `TOOL_DOMAIN` here to apply per-domain trust boundaries (SPEC §6),
and Module 9's retry logic is meant to key off `IDEMPOTENT` so a transient
tool failure is only ever retried automatically when the tool is read-only
(SPEC §7 mistake #5: never blindly retry a write).

Deliberately does NOT include `tawseel.py`'s `track_shipment` — that file
is the instructor package's standalone worked example, not part of the
production catalogue (which gets its `track_shipment` from `logistics.py`,
the file that also carries the rest of the LaDe-shaped tool suite).
"""
from __future__ import annotations

from typing import Any

from rafeeq.tools import billing, customer, logistics, orders

# --------------------------------------------------------------------------
# ALL_TOOLS — every governed tool object, ready to bind to a model
# (`model.bind_tools(ALL_TOOLS)`) or hand to an MCP server registration
# loop. Assembled from each domain module's own `TOOLS` list so adding a
# tool to e.g. `billing.py` only requires updating ONE list, here nothing.
# --------------------------------------------------------------------------
ALL_TOOLS: list[Any] = [*orders.TOOLS, *logistics.TOOLS, *billing.TOOLS, *customer.TOOLS]


def _tool_name(t: Any) -> str:
    return getattr(t, "name", None) or getattr(t, "__name__", str(t))


# --------------------------------------------------------------------------
# WRITE_TOOLS — mutate backend state. Never retried blindly; every one of
# these requires an idempotency key, a status precondition, or is flagged
# reconciliation-only in its own docstring.
# --------------------------------------------------------------------------
WRITE_TOOLS: frozenset[str] = frozenset({
    "reschedule_delivery",   # logistics.py — autonomous within policy (SPEC §5)
    "issue_refund",          # billing.py   — idempotency-key gated, never retried
    "mark_refunded",         # billing.py   — reconciliation only, not idempotent
    "add_case_note",         # customer.py  — appends; calling twice double-notes
})

# --------------------------------------------------------------------------
# IDEMPOTENT — read-safe tools only. Safe for M9's retry policy to retry
# automatically on a transient failure; a tool NOT in this set must never
# be auto-retried by that policy. Derived, not hand-maintained twice: every
# tool that is not a WRITE_TOOLS entry is read-only by construction (SPEC
# §7: "one tool, one job" — a tool is never both read and write).
# --------------------------------------------------------------------------
IDEMPOTENT: frozenset[str] = frozenset(
    _tool_name(t) for t in ALL_TOOLS if _tool_name(t) not in WRITE_TOOLS
)

# --------------------------------------------------------------------------
# TOOL_DOMAIN — tool name -> owning trust domain. Backs
# `security/authz.py`'s per-domain policy table and
# `mcp_servers/*_server.py`'s one-server-per-domain split (SPEC §6: "one
# MCP server per trust boundary, not one mega-server").
# --------------------------------------------------------------------------
TOOL_DOMAIN: dict[str, str] = {}
for _mod, _domain in ((orders, "orders"), (logistics, "logistics"),
                       (billing, "billing"), (customer, "customer")):
    for _t in _mod.TOOLS:
        TOOL_DOMAIN[_tool_name(_t)] = _domain
del _mod, _domain, _t  # keep the module namespace clean of loop leftovers

# Sanity: every tool name is unique across domains and every tool has a
# domain — a duplicate or orphaned tool name is a build error, not
# something that should silently ship.
assert len(TOOL_DOMAIN) == len(ALL_TOOLS), "duplicate tool name across domains"
assert IDEMPOTENT | WRITE_TOOLS == set(TOOL_DOMAIN), "every tool must be exactly one of read/write"
assert not (IDEMPOTENT & WRITE_TOOLS), "a tool cannot be both idempotent-read and write"


def describe_catalogue() -> str:
    """Render the tool catalogue as a fixed-width table for the classroom
    demo (`python3 -m rafeeq.tools.registry`) — one glance shows the whole
    governed surface: which domain owns each tool and whether it is safe
    to retry."""
    rows = []
    for name in sorted(TOOL_DOMAIN):
        kind = "write" if name in WRITE_TOOLS else "read (idempotent)"
        rows.append((name, TOOL_DOMAIN[name], kind))

    name_w = max(len(r[0]) for r in rows)
    domain_w = max(len(r[1]) for r in rows)
    kind_w = max(len(r[2]) for r in rows)
    header = f"{'tool':<{name_w}}  {'domain':<{domain_w}}  {'kind':<{kind_w}}"
    lines = [header, "-" * len(header)]
    for name, domain, kind in rows:
        lines.append(f"{name:<{name_w}}  {domain:<{domain_w}}  {kind:<{kind_w}}")
    lines.append("")
    lines.append(f"{len(rows)} tools total: {len(IDEMPOTENT)} read (idempotent), {len(WRITE_TOOLS)} write.")
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover - manual classroom demo
    print(describe_catalogue())
