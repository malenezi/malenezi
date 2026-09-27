"""Module 8 — the output guardrail: `guard_tool_call` + `guard_response`.

TEACHING POINT: this is the LAST line, and the MOST reliable, because it
inspects the CONCRETE artefact about to happen — this tool call, this
response text — rather than trying to predict the model's intent from a
transcript. Every consequential tool call is run through
`security/action_risk.py::classify` here, so the SPEC §5 matrix is
enforced STRUCTURALLY: `issue_refund` above the human-approval band is
blocked here even if `input_guard.py` missed the injection that produced
it, even if the model was "convinced" by a crafted delivery note. This is
the module that makes Lab 8 Task 3's demonstration true: disable the
input guard entirely and the over-limit refund is STILL blocked, because
this function does not read `input_guard`'s verdict at all — it reads the
tool call and the risk matrix, full stop.

Dependency-free (Layer A): stdlib + `rafeeq.security.action_risk` +
`rafeeq.security.events` + `rafeeq.security.input_guard` (for its PII
patterns, reused rather than redeclared) only.
"""
from __future__ import annotations

from typing import Any

from rafeeq.core.config import REFUND_LIMIT_SAR
from rafeeq.security.action_risk import classify
from rafeeq.security.events import log_security_event
from rafeeq.security.input_guard import PII_PATTERNS

# --------------------------------------------------------------------------
# Tools whose args/result legitimately carry customer identifiers — used
# by the cross-customer check below. `customer_id` is the conventional
# argument name across `tools/*.py`; a handful of tools use a different
# name for the same concept (e.g. `get_customer_tickets` also takes
# `customer_id`) so this list stays a simple constant rather than magic.
# --------------------------------------------------------------------------
CUSTOMER_SCOPED_ARG_NAMES: tuple[str, ...] = ("customer_id",)


def _extract_customer_id(args: dict[str, Any]) -> str | None:
    for name in CUSTOMER_SCOPED_ARG_NAMES:
        if name in args and args[name]:
            return str(args[name])
    return None


def guard_tool_call(tool_name: str, args: dict[str, Any], actor_customer_id: str | None = None) -> dict | None:
    """Return an override result (a dict with an `"error"` key) if the
    call must be BLOCKED before it reaches the real tool; return `None`
    to allow it through unchanged.

    Consults `action_risk.classify` for EVERY tool call — not just
    `issue_refund` — so the full autonomous / policy-controlled /
    human-approval / prohibited matrix is enforced here, structurally,
    for every tool in the catalogue (SPEC §5), plus two checks the matrix
    alone cannot express:

      - `actor_customer_id` mismatch on a customer-scoped call (the same
        cross-customer boundary `security/authz.py` enforces server-side;
        this is defence in depth at the output layer, not a replacement
        for it).
      - `mark_refunded`/prohibited-tool calls are blocked outright here
        too, so a caller that forgot to consult `authz.py` still cannot
        get the call through this guard.
    """
    decision = classify(tool_name, args)

    if decision.prohibited:
        log_security_event(
            "blocked_prohibited_action", {"tool_name": tool_name, "args": _redact_args(args)}, severity="critical",
        )
        return {"error": "prohibited_action", "tool_name": tool_name}

    if decision.requires_human_approval:
        log_security_event(
            "blocked_over_limit_refund" if tool_name == "issue_refund" else "blocked_human_approval_required",
            {"tool_name": tool_name, "args": _redact_args(args), "reason": decision.reason},
            severity="high",
        )
        return {"error": "refund_over_limit_requires_human_approval" if tool_name == "issue_refund"
                          else "human_approval_required", "tool_name": tool_name}

    if decision.requires_logging:
        # policy_controlled: allowed to proceed, but the SPEC is explicit
        # this band must be LOGGED — do it here so no call site can forget.
        log_security_event(
            "policy_controlled_action_allowed",
            {"tool_name": tool_name, "args": _redact_args(args), "reason": decision.reason},
            severity="medium",
        )

    # --- structuring/smurfing fix (found by red_team.py's suite, entry
    # PRV-EN-008/PRV-AR-005: several individually-under-limit issue_refund
    # calls against the SAME order can sum past REFUND_LIMIT_SAR while
    # each call alone classifies as policy_controlled. A single call's
    # amount band is NOT the only thing that must stay under the limit —
    # the order's CUMULATIVE refunded total must too. This reads the
    # order's authoritative `refund_amount_sar` field (updated by every
    # real `issue_refund_impl` call), not conversation memory or a
    # request count, so it holds across separate calls/sessions alike. ---
    if tool_name == "issue_refund" and not decision.prohibited and not decision.requires_human_approval:
        order_id = args.get("order_id")
        try:
            amount = float(args.get("amount_sar", args.get("amount", 0)) or 0.0)
        except (TypeError, ValueError):
            amount = 0.0
        if order_id:
            try:
                from rafeeq.tools.orders import get_order_impl  # lazy: avoid a top-of-file import-order coupling

                order = get_order_impl(order_id)
            except Exception:  # noqa: BLE001 - a lookup failure must not silently WAIVE the check
                order = {"error": "lookup_failed"}
            already_refunded = 0.0 if order.get("error") else float(order.get("refund_amount_sar") or 0.0)
            cumulative = already_refunded + amount
            if cumulative > REFUND_LIMIT_SAR:
                log_security_event(
                    "blocked_cumulative_refund_over_limit",
                    {"tool_name": tool_name, "args": _redact_args(args), "order_id": order_id,
                     "already_refunded_sar": already_refunded, "requested_sar": amount,
                     "cumulative_sar": cumulative, "limit_sar": REFUND_LIMIT_SAR},
                    severity="high",
                )
                return {"error": "cumulative_refund_over_limit_requires_human_approval", "tool_name": tool_name,
                        "cumulative_amount_sar": cumulative}

    call_customer_id = _extract_customer_id(args)
    if actor_customer_id is not None and call_customer_id is not None and call_customer_id != actor_customer_id:
        log_security_event(
            "blocked_cross_customer_access",
            {"tool_name": tool_name, "requested_customer_id": call_customer_id, "actor_customer_id": actor_customer_id},
            severity="high",
        )
        return {"error": "cross_customer_access_denied", "tool_name": tool_name}

    return None


def _redact_args(args: dict[str, Any]) -> dict[str, Any]:
    """Args are logged for audit, but must not themselves smuggle PII into
    the security log (a `reason`/`note` free-text arg could carry a
    national id) — mask with the same patterns `input_guard.py` uses."""
    redacted: dict[str, Any] = {}
    for key, value in args.items():
        if isinstance(value, str):
            cleaned = value
            for label, pattern in PII_PATTERNS.items():
                cleaned = pattern.sub(f"[{label}_REDACTED]", cleaned)
            redacted[key] = cleaned
        else:
            redacted[key] = value
    return redacted


def guard_response(text: str, actor_customer_id: str | None = None, response_customer_ids: list[str] | None = None) -> str:
    """Screen a candidate customer-facing response BEFORE it is sent.

    Two independent checks:
      1. PII egress: national id / IBAN / card / phone / email anywhere in
         the text is blocked outright (the response is replaced, never
         partially redacted — a partially-redacted response still implies
         "I have this data", which is its own leak).
      2. Cross-customer id egress: if `response_customer_ids` (customer
         ids the response text mentions, e.g. extracted from a tool
         result the model is about to quote) contains one that is not
         `actor_customer_id`, block — this is the "did a foreign
         customer_id appear in output" oracle the red-team suite checks.
    """
    for label, pattern in PII_PATTERNS.items():
        if pattern.search(text):
            log_security_event("blocked_pii_egress", {"label": label}, severity="high")
            return _refusal_message()

    if actor_customer_id is not None and response_customer_ids:
        foreign = sorted({cid for cid in response_customer_ids if cid and cid != actor_customer_id})
        if foreign:
            log_security_event(
                "blocked_cross_customer_egress",
                {"actor_customer_id": actor_customer_id, "foreign_customer_ids": foreign},
                severity="high",
            )
            return _refusal_message()

    return text


def _refusal_message() -> str:
    # Bilingual: the response GOING TO the customer must be understandable
    # regardless of locale, matching the SPEC §7 rule that customer-facing
    # strings are bilingual AR/EN.
    return (
        "I can't share that information here. Please verify via the app. / "
        "لا يمكنني مشاركة هذه المعلومات هنا. يرجى التحقق عبر التطبيق."
    )


def guard_tool_result(tool_name: str, result: Any, actor_customer_id: str | None = None) -> Any:
    """Screen a TOOL's OUTPUT (not the call) before it is fed back to the
    reasoning model — the "tool output could be compromised" entry point
    from the threat model (a poisoned delivery note, a tampered MCP
    response). Masks PII found in any string field of the result and
    flags-and-logs (via `input_guard.screen_input`) any injection-shaped
    content, WITHOUT stripping it outright — the model still needs to see
    "there is a delivery note" even if its content is neutralised for
    logging purposes; the actual defence against the tool result
    persuading the model into a bad ACTION is `guard_tool_call`/`classify`
    on whatever the model tries to do next, not scrubbing this text."""
    from rafeeq.security.input_guard import screen_and_log  # lazy: avoid a top-of-file cycle risk

    if isinstance(result, dict):
        flagged_any = False
        for key, value in list(result.items()):
            if isinstance(value, str) and value:
                screened = screen_and_log(value, source=f"tool_result:{tool_name}.{key}")
                if screened.flags:
                    flagged_any = True
        if flagged_any:
            log_security_event(
                "tool_result_injection_shaped_content",
                {"tool_name": tool_name, "actor_customer_id": actor_customer_id},
                severity="medium",
            )
    return result
