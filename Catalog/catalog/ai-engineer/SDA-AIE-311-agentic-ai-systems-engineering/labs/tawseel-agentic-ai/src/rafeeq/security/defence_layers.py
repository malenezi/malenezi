"""Module 8 — the layered defence, documented IN CODE.

TEACHING POINT: this module has no behaviour of its own to speak of — it
exists so the "defence in depth" diagram (`docs/SECURITY_MODEL.md`) is
not just a slide but a structure `assert_layers_wired()` can check
against the real modules, and so a participant can `python3 -m
rafeeq.security.defence_layers` and get the same table the instructor
draws on the board. Each layer names what it catches, what it CANNOT
catch alone, and which OWASP Agentic Top 10 2026 category (see
`docs/SECURITY_MODEL.md` for the full mapping and its caveats) it
addresses — so "why do we need five layers" has a concrete answer per
layer, not a hand-wave.

Dependency-free (Layer A): stdlib only.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DefenceLayer:
    name: str
    module: str
    catches: str
    cannot_catch: str
    owasp_categories: tuple[str, ...]


LAYERS: list[DefenceLayer] = [
    DefenceLayer(
        name="1. Input filter",
        module="rafeeq.security.input_guard.screen_input",
        catches=(
            "Known injection phrasings (instruction-override, false authority, "
            "role-play, delimiter-escape, urgency/social-engineering, encoded/"
            "obfuscated) in the customer's own message, bilingual AR/EN; PII "
            "(national id, IBAN, card, phone, email) masked before it reaches "
            "memory or the model."
        ),
        cannot_catch=(
            "Novel phrasings this regex library has never seen; injection "
            "arriving via a TOOL RESULT rather than the customer message "
            "(a poisoned delivery note only reaches this filter if the "
            "caller also screens tool output — see layer 4); a jailbreak "
            "the model complies with despite no matched pattern. IT NEVER "
            "BLOCKS BY ITSELF (see the module's own docstring) — it only "
            "flags and masks."
        ),
        owasp_categories=("agent goal/instruction manipulation", "memory poisoning"),
    ),
    DefenceLayer(
        name="2. Structural authorisation",
        module="rafeeq.security.authz.agent_may_access",
        catches=(
            "Any tool call outside the calling agent identity's granted "
            "domains, an explicitly denied tool, or a cross-customer call "
            "from a same-customer-only identity — enforced server-side, "
            "before the tool executes, independent of what the model was "
            "told or persuaded to believe."
        ),
        cannot_catch=(
            "An amount WITHIN a granted domain that is still too large "
            "(authz answers 'may this identity touch billing at all', not "
            "'is 9,500 SAR too much') — that is layer 3's job; a prohibited "
            "action attempted through a tool this table has never heard of "
            "(fails closed as unknown_tool, which is correct, but is still "
            "worth naming as a gap this layer alone cannot express as an "
            "explicit deny)."
        ),
        owasp_categories=("tool misuse", "privilege compromise", "identity/impersonation"),
    ),
    DefenceLayer(
        name="3. Deterministic flow gate",
        module="rafeeq.flows.refund_flow (amount_gate, eligibility_gate)",
        catches=(
            "The refund amount band itself — <= 50 SAR auto, <= 500 SAR "
            "policy-controlled, > 500 SAR human approval, no exceptions — "
            "as a plain Python branch on a number read from the order "
            "record, never from conversation text. Cannot be talked past "
            "by wording because it never reads the conversation at all."
        ),
        cannot_catch=(
            "A call that bypasses the flow entirely and hits the tool "
            "layer directly (a different code path, a different agent) — "
            "which is exactly why the SAME limit is re-enforced at the "
            "output guard (layer 4) and, in production, the MCP server "
            "boundary too: one gate in one call path is not defence in "
            "depth."
        ),
        owasp_categories=("tool misuse", "resource/denial-of-wallet"),
    ),
    DefenceLayer(
        name="4. Output guard",
        module="rafeeq.security.output_guard (guard_tool_call, guard_response, guard_tool_result)",
        catches=(
            "Every tool call, classified against the FULL action-risk "
            "matrix (not just refunds) immediately before execution; PII "
            "in a candidate customer-facing response; a foreign customer "
            "id about to be quoted back; injection-shaped content inside a "
            "TOOL RESULT (the indirect-injection entry point layer 1 alone "
            "cannot see). THE MOST RELIABLE LAYER: it inspects the "
            "concrete artefact about to happen, not predicted intent."
        ),
        cannot_catch=(
            "An action that never reaches this checkpoint at all (a new "
            "code path that calls a tool's `*_impl` directly without "
            "routing through `guard_tool_call`) — a guard that is not on "
            "every call path is not a guard; wiring it in is the "
            "integration work, not this module's job."
        ),
        owasp_categories=(
            "tool misuse", "privilege compromise", "insufficient observability",
            "resource/denial-of-wallet",
        ),
    ),
    DefenceLayer(
        name="5. Audit / monitoring",
        module="rafeeq.security.events (log_security_event, read_events) + reports/security_events.jsonl",
        catches=(
            "A durable, greppable record of every guardrail trip, authz "
            "denial, and red-team finding — the thing that turns 'we "
            "think we're safe' into 'here is proof, and here is the "
            "regression test that reproduces it'; feeds the red-team "
            "suite's oracles and CI."
        ),
        cannot_catch=(
            "NOTHING — this layer detects and records after the fact, it "
            "does not itself prevent an action. It is the layer that "
            "makes every OTHER layer's failure visible and reviewable, "
            "not a preventive control on its own."
        ),
        owasp_categories=("insufficient observability", "cascading/multi-agent failures"),
    ),
]


def explain_layers() -> str:
    """Render the layered-defence table for the classroom
    (`python3 -m rafeeq.security.defence_layers`)."""
    lines = ["Rafeeq's layered defence (SPEC M8 §4) — each layer alone is insufficient:", ""]
    for layer in LAYERS:
        lines.append(f"{layer.name}  [{layer.module}]")
        lines.append(f"    catches:      {layer.catches}")
        lines.append(f"    cannot catch: {layer.cannot_catch}")
        lines.append(f"    OWASP:        {', '.join(layer.owasp_categories)}")
        lines.append("")
    lines.append(
        "No single layer above is sufficient alone (this is the point, not a "
        "gap): Lab 8 Task 3 proves layers 2-5 still hold with layer 1 disabled."
    )
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover - manual classroom demo
    print(explain_layers())
