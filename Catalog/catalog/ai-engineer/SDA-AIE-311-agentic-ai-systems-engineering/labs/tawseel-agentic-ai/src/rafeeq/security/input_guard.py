"""Module 8 — the input guardrail: `screen_input`, extended.

TEACHING POINT (read this before you trust this module too much): an
input guardrail is a FILTER, not a WALL. It reduces the volume of
injection attempts that reach the reasoning model and masks PII before it
reaches memory — it does NOT and CANNOT catch every injection; a novel
phrasing, a translated payload, a base64-wrapped instruction, or a
payload arriving via a TOOL RESULT (a poisoned delivery note, not the
customer's own message) will slip past some of these regexes. That is
why `output_guard.py` + `action_risk.py` + `security/authz.py` +
`flows/refund_flow.py`'s amount gate exist: they hold even when THIS
module misses. Never wire a refund limit, an authorisation check, or any
consequential decision behind "did `screen_input` flag it" — this module
only ever *raises scrutiny and logs*, it never itself authorises or
denies an action.

Bilingual (SPEC §7's "customer-facing" bar does not apply to internal
detection, but the course's own lesson does: English-only guardrails
fail on Arabic input, and this repo's attack corpus is roughly half
Arabic — see `security/README.md`). Every pattern category below has at
least one Arabic and one English variant; `INJECTION_PATTERNS` holds 18+
total across six families named in the SPEC: instruction-override, false
authority, role-play, encoded/obfuscated, delimiter-escape, and
urgency/social-engineering.

Dependency-free (Layer A): stdlib only (`re`, `base64`, `dataclasses`).
"""
from __future__ import annotations

import base64
import binascii
import re
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# Injection patterns, grouped by attack family (SPEC §6's AgentDojo-style
# taxonomy). Each tuple is (family, compiled pattern). Kept as a flat list
# (not a dict-of-lists) so `screen_input` can report the family per flag
# without a second lookup, and so `len(INJECTION_PATTERNS) >= 18` is easy
# to assert in `tests/security/test_input_guard.py`.
# --------------------------------------------------------------------------
_FLAGS = re.IGNORECASE | re.UNICODE

INJECTION_PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    # (family, pattern_id, compiled_pattern)

    # --- instruction-override: telling the model to drop its own rules --
    ("instruction_override", "ignore_instructions_en",
     re.compile(r"ignore\s+(all|any|every|the)?\s*(previous|prior|earlier|above)?\s*instructions?", _FLAGS)),
    ("instruction_override", "ignore_instructions_ar",
     re.compile(r"تجاهل\s*(كل|جميع)?\s*(التعليمات|الأوامر)\s*(السابقة)?", _FLAGS)),
    ("instruction_override", "disregard_policy_en",
     re.compile(r"disregard\s+(all\s+)?(prior|previous|the)?\s*(polic(y|ies)|rules?|limits?|guardrails?)", _FLAGS)),
    ("instruction_override", "disregard_policy_ar",
     re.compile(r"تجاهل\s*(كل|جميع)?\s*(السياسات|القواعد|الحدود|الضوابط)\s*(السابقة)?", _FLAGS)),
    ("instruction_override", "forget_everything_en",
     re.compile(r"forget\s+(everything|all)\s+(you\s+)?(were\s+told|know|learned)", _FLAGS)),
    ("instruction_override", "new_instructions_en",
     re.compile(r"(your\s+)?new\s+instructions?\s+(are|is)\b", _FLAGS)),

    # --- false authority: claiming to be system/compliance/developer ----
    ("false_authority", "system_override_en",
     re.compile(r"system\s*[:\-]?\s*override", _FLAGS)),
    ("false_authority", "system_override_ar",
     re.compile(r"تعليمات\s*النظام|أمر\s*النظام", _FLAGS)),
    ("false_authority", "authorised_by_en",
     re.compile(r"authoris(ed|ation)\s+by\s+(compliance|finance|management|admin|support)", _FLAGS)),
    ("false_authority", "authorised_by_ar",
     re.compile(r"بموافقة\s*(الإدارة|الامتثال|الدعم الفني)", _FLAGS)),
    ("false_authority", "developer_mode_en",
     re.compile(r"(developer|debug|maintenance|admin)\s+mode\s+(enabled|activated|on)\b", _FLAGS)),

    # --- role-play: reframing the model as an unconstrained persona -----
    ("role_play", "you_are_now_en",
     re.compile(r"you\s+are\s+now\s+(a|an|no\s+longer)", _FLAGS)),
    ("role_play", "you_are_now_ar",
     re.compile(r"أنت\s+الآن\s+(مساعد|شخصية|بدون)", _FLAGS)),
    ("role_play", "act_as_en",
     re.compile(r"\bact\s+as\s+(if\s+you|an?)\b.*(no\s+rules|unrestricted|dan\b)", _FLAGS)),
    ("role_play", "pretend_en",
     re.compile(r"pretend\s+(you\s+)?(are|have)\s+no\s+(rules|restrictions|limits|policy)", _FLAGS)),

    # --- delimiter-escape: fake system/end-of-context markers ------------
    ("delimiter_escape", "fake_system_tag_en",
     re.compile(r"\[?\s*(system|assistant)\s*\]?\s*[:\]]\s*", _FLAGS)),
    ("delimiter_escape", "end_context_marker_en",
     re.compile(r"(---|###|```)\s*(end\s+of\s+(context|instructions|policy)|new\s+context)", _FLAGS)),
    ("delimiter_escape", "fake_system_tag_ar",
     re.compile(r"\[?\s*(النظام|المساعد)\s*\]?\s*[:\]]\s*", _FLAGS)),

    # --- urgency / social engineering: pressure to skip a check ---------
    ("urgency_social_engineering", "immediately_no_approval_en",
     re.compile(r"immediately[,\s]+no\s+approval\s+needed", _FLAGS)),
    ("urgency_social_engineering", "immediately_no_approval_ar",
     re.compile(r"فوراً\s*دون\s*(الحاجة\s*ل)?أي\s*موافقة", _FLAGS)),
    ("urgency_social_engineering", "urgent_ceo_en",
     re.compile(r"(urgent|asap|right\s+now)[,:\s].{0,40}(ceo|manager|director|boss)\b", _FLAGS)),
    ("urgency_social_engineering", "or_you_will_be_fired_en",
     re.compile(r"(you\s+will\s+be\s+(fired|shut\s+down|replaced))|(this\s+is\s+your\s+last\s+chance)", _FLAGS)),

    # --- encoded / obfuscated: base64/hex/zero-width tricks to smuggle
    # an instruction past a naive substring filter -----------------------
    ("encoded_obfuscated", "base64_blob",
     re.compile(r"[A-Za-z0-9+/]{24,}={0,2}")),  # long base64-looking run; decoded & re-scanned below
    ("encoded_obfuscated", "zero_width_chars",
     re.compile(r"[​‌‍⁠﻿]")),
    ("encoded_obfuscated", "excessive_char_spacing",
     re.compile(r"(?:[a-zA-Z]\s){6,}[a-zA-Z]")),  # "i g n o r e   i n s t r u c t i o n s"
    ("encoded_obfuscated", "leet_ignore",
     re.compile(r"[i1!][g9][n][o0][r][e3]\s+[i1!][n][s5$][t][r][u][c][t]", _FLAGS)),
]

assert len(INJECTION_PATTERNS) >= 18, "SPEC requires at least 18 bilingual injection patterns"

# --------------------------------------------------------------------------
# Saudi-shaped PII patterns. Masked BEFORE anything reaches memory (SPEC
# §7 mistake #5: never store raw hostile/PII payloads into long-term
# memory — mask/summarise first).
# --------------------------------------------------------------------------
PII_PATTERNS: dict[str, re.Pattern[str]] = {
    # Saudi national ID / iqama: 10 digits, starts with 1 (citizen) or 2 (resident).
    "national_id": re.compile(r"\b[12]\d{9}\b"),
    # Saudi IBAN: SA + 22 digits (24 chars total after the country code).
    "iban": re.compile(r"\bSA\d{22}\b", re.IGNORECASE),
    # 16-digit payment card, optionally grouped in 4s with spaces/dashes.
    "card": re.compile(r"\b(?:\d[ -]?){15}\d\b"),
    # Saudi mobile: +9665XXXXXXXX or 05XXXXXXXX (9 digits after the 5).
    "phone": re.compile(r"(?:\+?9665\d{8}|05\d{8})\b"),
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
}


def _looks_like_base64_injection(token: str) -> str | None:
    """Best-effort: decode a base64-looking run and re-scan it for a
    plain-text override pattern. Returns the matched family name if the
    DECODED text itself contains an instruction-override/false-authority
    phrase, else None. Deliberately narrow (only the two highest-signal
    families) to keep false positives low on legitimate base64 (order
    references, tracking tokens) that just happens to appear in text."""
    if len(token) < 24 or len(token) % 4 not in (0, 2, 3):
        return None
    try:
        decoded = base64.b64decode(token + "=" * (-len(token) % 4), validate=False).decode("utf-8", errors="strict")
    except (binascii.Error, UnicodeDecodeError, ValueError):
        return None
    for family, _pid, pattern in INJECTION_PATTERNS:
        if family in ("instruction_override", "false_authority") and pattern.search(decoded):
            return family
    return None


@dataclass
class GuardResult:
    """`allow` stays True even when flags are present — SPEC's own
    reference implementation and Lab 8 Task 1 are explicit that injection
    is FLAGGED (raises scrutiny + logging) not silently trusted-away, and
    NOT itself a block — blocking is a structural decision made downstream
    (`output_guard.py`, `action_risk.py`), never this filter's job alone.
    `risk_score` is a 0.0-1.0 heuristic (families matched / weighted) for
    routing/triage, e.g. "route anything >= 0.5 to extra scrutiny"."""

    allow: bool
    flags: list[str]
    families: list[str]
    cleaned: str
    risk_score: float
    pii_found: list[str] = field(default_factory=list)


_FAMILY_WEIGHT: dict[str, float] = {
    "instruction_override": 0.35,
    "false_authority": 0.30,
    "role_play": 0.20,
    "delimiter_escape": 0.25,
    "urgency_social_engineering": 0.20,
    "encoded_obfuscated": 0.30,
}


def screen_input(text: str) -> GuardResult:
    """Screen ONE piece of untrusted text (a customer message, OR a tool
    result / retrieved memory chunk being fed back to the model — this
    function does not care about the SOURCE, only the content, which is
    exactly why `output_guard.py` also screens tool results with the same
    PII patterns) before it reaches the reasoning model or long-term
    memory.

    Returns a `GuardResult` whose `cleaned` text has every PII match
    masked (`[label_REDACTED]`) — callers should persist/forward
    `cleaned`, never the raw `text`, once this has run. `flags`/`families`
    are diagnostic only; `allow` is always True (see `GuardResult`'s
    docstring) — THIS FUNCTION NEVER BLOCKS, it only flags and masks.
    """
    text = text or ""
    flags: list[str] = []
    families: set[str] = set()

    for family, pattern_id, pattern in INJECTION_PATTERNS:
        if pattern_id == "base64_blob":
            for token in pattern.findall(text):
                decoded_family = _looks_like_base64_injection(token)
                if decoded_family:
                    flags.append(f"injection:encoded_obfuscated:{pattern_id}:decodes_to:{decoded_family}")
                    families.add("encoded_obfuscated")
            continue
        if pattern.search(text):
            flags.append(f"injection:{family}:{pattern_id}")
            families.add(family)

    pii_found: list[str] = []
    for label, pattern in PII_PATTERNS.items():
        if pattern.search(text):
            flags.append(f"pii:{label}")
            pii_found.append(label)

    cleaned = text
    for label, pattern in PII_PATTERNS.items():
        cleaned = pattern.sub(f"[{label}_REDACTED]", cleaned)  # mask BEFORE anything reaches memory

    risk_score = min(1.0, sum(_FAMILY_WEIGHT.get(f, 0.15) for f in families) + (0.15 * bool(pii_found)))

    return GuardResult(
        allow=True,  # a filter flags; it never itself authorises or denies (see docstring)
        flags=flags,
        families=sorted(families),
        cleaned=cleaned,
        risk_score=round(risk_score, 3),
        pii_found=pii_found,
    )


def screen_and_log(text: str, source: str = "customer_message") -> GuardResult:
    """Convenience wrapper: `screen_input` plus a `log_security_event`
    call for every non-empty flag set, so callers do not have to remember
    to wire logging themselves. `source` names WHERE this text came from
    (`customer_message` | `tool_result` | `memory_chunk`) — logged so a
    reviewer can see at a glance whether injection attempts are arriving
    via the customer or via a poisoned backend/memory (the M8/AgentDojo
    indirect-injection distinction)."""
    result = screen_input(text)
    if result.flags:
        from rafeeq.security.events import log_security_event  # lazy: avoid import-order coupling

        severity = "high" if result.risk_score >= 0.5 else "medium"
        log_security_event(
            "input_guard_flagged",
            {"source": source, "families": result.families, "flags": result.flags,
             "risk_score": result.risk_score, "pii_found": result.pii_found},
            severity=severity,
        )
    return result
