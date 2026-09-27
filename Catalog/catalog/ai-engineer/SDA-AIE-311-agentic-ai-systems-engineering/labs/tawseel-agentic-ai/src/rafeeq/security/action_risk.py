"""Module 8 — the action-risk matrix (SPEC §5) as DATA, not prose.

TEACHING POINT: "issue_refund needs approval above 500 SAR" written in a
system prompt is a sentence a crafted input can argue with. Written here
— a lookup table plus a pure function every caller (the output guard,
`flows/refund_flow.py`, `mcp_servers/*_server.py`) can import and run
against the CONCRETE tool name and arguments about to execute — it is
structure. This module does not itself gate anything (that is
`output_guard.py`'s job, and `flows/refund_flow.py`'s amount_gate, and
the MCP servers' `guarded_tool`); it is the single canonical SOURCE OF
the classification those gates consult, so the matrix cannot silently
drift between the flow, the output guard, and the classroom slide.

Autonomy levels (SPEC §5, `core.config.AUTONOMY_*`):
  - autonomous                    -> no gate, no log required beyond normal tracing
  - autonomous_within_policy      -> autonomous, but bounded by a policy check (e.g. SLA)
  - policy_controlled             -> autonomous execution IS allowed, but MUST be logged
                                      as a security event (amount-banded refunds, 50-500 SAR)
  - human_approval_required       -> must NOT execute without a recorded human approval
  - prohibited                    -> must NEVER execute, for anyone, ever

Dependency-free (Layer A): stdlib + `rafeeq.core.config` +
`rafeeq.tools.registry` only.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from rafeeq.core.config import (
    AUTO_REFUND_LIMIT_SAR,
    AUTONOMY_AUTONOMOUS,
    AUTONOMY_AUTONOMOUS_WITHIN_POLICY,
    AUTONOMY_HUMAN_APPROVAL,
    AUTONOMY_POLICY_CONTROLLED,
    AUTONOMY_PROHIBITED,
    REFUND_LIMIT_SAR,
)

Autonomy = str  # one of the AUTONOMY_* constants above; kept as str for JSON round-tripping

# --------------------------------------------------------------------------
# RISK — SPEC §5's matrix, keyed by tool name, for every NON-amount-banded
# tool. `issue_refund` is handled specially by `classify()` below because
# its autonomy depends on the call's `amount` argument, not the tool name
# alone — a single dict entry cannot express a banded rule.
# --------------------------------------------------------------------------
RISK: dict[str, Autonomy] = {
    # --- autonomous: read-only, no side effects, no policy judgement ----
    "track_shipment": AUTONOMY_AUTONOMOUS,
    "estimate_eta": AUTONOMY_AUTONOMOUS,
    "get_delivery_events": AUTONOMY_AUTONOMOUS,
    "get_order": AUTONOMY_AUTONOMOUS,
    "get_order_items": AUTONOMY_AUTONOMOUS,
    "list_orders": AUTONOMY_AUTONOMOUS,
    "get_driver_status": AUTONOMY_AUTONOMOUS,
    "find_delivery_exception": AUTONOMY_AUTONOMOUS,
    "get_invoice": AUTONOMY_AUTONOMOUS,
    "get_payment": AUTONOMY_AUTONOMOUS,
    "get_customer": AUTONOMY_AUTONOMOUS,
    "get_customer_tickets": AUTONOMY_AUTONOMOUS,
    "read_policy": AUTONOMY_AUTONOMOUS,

    # --- autonomous within policy: a write, but bounded by a deterministic
    # rule the tool/flow enforces itself (SLA windows, no double-booking) --
    "reschedule_delivery": AUTONOMY_AUTONOMOUS_WITHIN_POLICY,

    # --- policy-controlled: allowed autonomously but MUST be logged -----
    "add_case_note": AUTONOMY_POLICY_CONTROLLED,

    # --- human approval required: reconciliation-only, moves money on the
    # order record outside the normal refund flow ------------------------
    "mark_refunded": AUTONOMY_HUMAN_APPROVAL,

    # --- prohibited: SPEC §5's three explicit prohibitions, mirrored from
    # `security/authz.py::PROHIBITED_TOOLS` so both tables agree ----------
    "change_customer_identity": AUTONOMY_PROHIBITED,
    "override_fraud_flag": AUTONOMY_PROHIBITED,
    "delete_order": AUTONOMY_PROHIBITED,
}

# `issue_refund` is intentionally NOT a flat entry in RISK: see classify().
REFUND_TOOL_NAME = "issue_refund"

# Tools whose autonomy this module knows is amount- or context-dependent
# and therefore computed by `classify()` rather than looked up directly —
# `assert_matrix_covers_registry()` treats membership here as equivalent
# coverage to a RISK entry.
_DYNAMIC_TOOLS: frozenset[str] = frozenset({REFUND_TOOL_NAME})


@dataclass(frozen=True)
class Decision:
    """The result of classifying ONE tool call. `reason` names WHICH row
    of the matrix (or which band, for issue_refund) produced the verdict
    — so a block is debuggable, not a bare autonomy string."""

    tool_name: str
    autonomy: Autonomy
    reason: str
    requires_logging: bool
    requires_human_approval: bool
    prohibited: bool


def _decision(tool_name: str, autonomy: Autonomy, reason: str) -> Decision:
    return Decision(
        tool_name=tool_name,
        autonomy=autonomy,
        reason=reason,
        requires_logging=autonomy in (AUTONOMY_POLICY_CONTROLLED, AUTONOMY_HUMAN_APPROVAL, AUTONOMY_PROHIBITED),
        requires_human_approval=autonomy == AUTONOMY_HUMAN_APPROVAL,
        prohibited=autonomy == AUTONOMY_PROHIBITED,
    )


def classify(tool_name: str, args: dict[str, Any] | None = None, context: dict[str, Any] | None = None) -> Decision:
    """Classify ONE prospective tool call against the action-risk matrix.

    `args` carries the call's arguments (used only for `issue_refund`'s
    amount band today); `context` is reserved for future context-dependent
    rules (e.g. a fraud_flag=true customer tightening the band) and is
    accepted-but-currently-unused so callers can pass it uniformly.

    A tool name absent from BOTH `RISK` and `_DYNAMIC_TOOLS` classifies as
    `prohibited` with reason `unclassified_tool` — fail CLOSED, never
    silently autonomous, for a tool this table has never seen (this is
    what makes `assert_matrix_covers_registry()` meaningful: a genuinely
    new tool must be classified here before it can ever run).
    """
    args = args or {}

    if tool_name == REFUND_TOOL_NAME:
        amount = args.get("amount_sar", args.get("amount", 0))
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            # Cannot even parse the amount: fail closed to human approval,
            # never assume it is small.
            return _decision(tool_name, AUTONOMY_HUMAN_APPROVAL, "unparseable_amount")
        if amount <= AUTO_REFUND_LIMIT_SAR:
            return _decision(tool_name, AUTONOMY_AUTONOMOUS, f"amount<={AUTO_REFUND_LIMIT_SAR}_sar_auto_band")
        if amount <= REFUND_LIMIT_SAR:
            return _decision(tool_name, AUTONOMY_POLICY_CONTROLLED, f"amount<={REFUND_LIMIT_SAR}_sar_policy_band")
        return _decision(tool_name, AUTONOMY_HUMAN_APPROVAL, f"amount>{REFUND_LIMIT_SAR}_sar_human_band")

    autonomy = RISK.get(tool_name)
    if autonomy is None:
        return _decision(tool_name, AUTONOMY_PROHIBITED, "unclassified_tool")
    return _decision(tool_name, autonomy, "matrix_lookup")


def explain_matrix() -> str:
    """Render the full action-risk matrix as a fixed-width table for the
    classroom (`python3 -m rafeeq.security.action_risk`) — mirrors
    `tools/registry.py::describe_catalogue`'s presentation so the two
    "print the governed surface" demos feel like one family."""
    rows: list[tuple[str, str, str]] = []
    for name in sorted(RISK):
        rows.append((name, RISK[name], "static"))
    rows.append((REFUND_TOOL_NAME, f"banded: <= {AUTO_REFUND_LIMIT_SAR} auto / "
                                    f"<= {REFUND_LIMIT_SAR} policy-controlled / "
                                    f"> {REFUND_LIMIT_SAR} human-approval", "amount-dependent"))
    rows.sort(key=lambda r: r[0])

    name_w = max(len(r[0]) for r in rows)
    autonomy_w = max(len(r[1]) for r in rows)
    header = f"{'tool':<{name_w}}  {'autonomy':<{autonomy_w}}  kind"
    lines = [header, "-" * len(header)]
    for name, autonomy, kind in rows:
        lines.append(f"{name:<{name_w}}  {autonomy:<{autonomy_w}}  {kind}")
    lines.append("")
    lines.append(f"{len(rows)} tools classified "
                 f"({sum(1 for r in rows if r[1] == AUTONOMY_PROHIBITED)} prohibited, "
                 f"{sum(1 for r in rows if r[1] == AUTONOMY_HUMAN_APPROVAL)} human-approval-only, "
                 f"1 amount-banded).")
    return "\n".join(lines)


def assert_matrix_covers_registry() -> None:
    """Fail loudly if `tools/registry.py::ALL_TOOLS` contains a tool this
    matrix has never classified. This is the structural guarantee behind
    `classify()`'s fail-closed default: it is meaningless to say "an
    unknown tool is prohibited" if nobody ever checks that every REAL tool
    is in fact known. Run this at build/CI time (SPEC §8) and on every
    change to `tools/registry.py` or this module.

    Raises `AssertionError` naming the exact uncovered tool names.
    """
    from rafeeq.tools.registry import ALL_TOOLS  # lazy: avoid import-order coupling at module load

    def _tool_name(t: Any) -> str:
        return getattr(t, "name", None) or getattr(t, "__name__", str(t))

    registry_tools = {_tool_name(t) for t in ALL_TOOLS}
    known = set(RISK) | _DYNAMIC_TOOLS
    uncovered = sorted(registry_tools - known)
    assert not uncovered, (
        f"action_risk.py does not classify {len(uncovered)} registered tool(s): {uncovered}. "
        "Every tool in tools/registry.py::ALL_TOOLS must have a RISK entry (or be added to "
        "_DYNAMIC_TOOLS with amount/context-dependent classification logic in classify())."
    )

    # The reverse gap is a smell too (a matrix entry for a tool that no
    # longer exists) but not a build error worth failing on — tools get
    # renamed mid-refactor; surface it as a soft check callers may print.


def unreachable_matrix_entries() -> list[str]:
    """Soft check (not asserted): RISK entries with no matching registered
    tool AND no matching PROHIBITED_TOOLS entry — usually a rename that
    left a stale row. Returns the stale names, or an empty list."""
    from rafeeq.security.authz import PROHIBITED_TOOLS  # lazy: avoid a hard import cycle
    from rafeeq.tools.registry import ALL_TOOLS

    def _tool_name(t: Any) -> str:
        return getattr(t, "name", None) or getattr(t, "__name__", str(t))

    registry_tools = {_tool_name(t) for t in ALL_TOOLS}
    return sorted(set(RISK) - registry_tools - set(PROHIBITED_TOOLS))


if __name__ == "__main__":  # pragma: no cover - manual classroom demo
    print(explain_matrix())
    try:
        assert_matrix_covers_registry()
        print("\nOK: every registered tool is classified.")
    except AssertionError as exc:
        print(f"\nFAIL: {exc}")
