"""Module 8 — the course's conscience, made real: FAILS the build if a
monetary limit or an authorisation rule lives ONLY inside a string that is
actually sent to a model (a `SystemMessage`/`HumanMessage`/`AIMessage`
call, or a `*PROMPT*`-named assignment) anywhere under `src/rafeeq/`
OTHER than the one deliberately preserved anti-pattern foil
(`reasoning/refund_prompt_only.py`, Module 7's own worked example).

See `tests/security/_governance_scan.py` for the AST-based scanner this
file (and its stdlib mirror, `tests/security/run_without_pytest.py`) runs
— both call the SAME implementation, not two hand-typed copies, because
this scan is exactly the kind of check that must not silently drift.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
_TESTS_SECURITY = Path(__file__).resolve().parent
for _p in (_SRC, _TESTS_SECURITY):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import _governance_scan as gs  # noqa: E402


class TestGovernanceScanFindsTheKnownAntiPattern:
    """Sanity: the detector is not vacuously blind — it MUST find the
    documented anti-pattern when pointed straight at it, or a "zero
    violations" result elsewhere would prove nothing."""

    def test_refund_prompt_only_is_flagged(self):
        violations = gs.scan_file(gs.SRC_DIR / "reasoning" / "refund_prompt_only.py")
        assert len(violations) >= 1
        assert any(v.kind == "money" for v in violations)


class TestNoPromptOnlyRulesInProduction:
    """The real gate: nothing OTHER than the whitelisted foil may state a
    money limit or an authorisation rule only in a prompt string."""

    def test_no_money_or_authz_rule_strings_outside_whitelisted_anti_pattern(self):
        violations = gs.scan_tree(exclude=gs.WHITELISTED_ANTI_PATTERN_FILES)
        assert violations == [], (
            f"{len(violations)} file(s) state a monetary limit or authorisation rule "
            f"ONLY inside a prompt string, with no structural backing: {violations}. "
            "Move the rule into core.config + a deterministic gate (flows/refund_flow.py, "
            "security/action_risk.py) instead."
        )

    def test_whitelist_is_exactly_the_documented_foil(self):
        """The whitelist must never grow silently — any addition to it is
        a deliberate, reviewable decision, not a way to quiet this test."""
        assert gs.WHITELISTED_ANTI_PATTERN_FILES == frozenset({
            "src/rafeeq/reasoning/refund_prompt_only.py",
        })


class TestAntiPatternFileIsInert:
    """The foil is allowed to exist ONLY because nothing real depends on
    it — verified here, not assumed."""

    def test_anti_pattern_file_not_imported_by_production_packages(self):
        importers = gs.anti_pattern_file_importers()
        assert importers == [], (
            f"reasoning/refund_prompt_only.py (the documented anti-pattern) is imported "
            f"by production code: {importers}. It must stay a teaching foil only, wired "
            f"solely through reasoning/compare.py's explicit before/after demonstration."
        )


class TestRealEnforcementImportsTheSingleSourceOfTruth:
    """The positive half of the same lesson: the modules that DO enforce
    the refund limit must import it from `core.config`, never redeclare a
    bare literal — SPEC §7's "never duplicate policy literals" rule made
    testable for the three files that matter most."""

    @pytest.mark.parametrize("relative_path", [
        "flows/refund_flow.py",
        "security/action_risk.py",
        "security/output_guard.py",
    ])
    def test_imports_refund_limit_constants(self, relative_path):
        text = (gs.SRC_DIR / relative_path).read_text(encoding="utf-8")
        assert "REFUND_LIMIT_SAR" in text
        assert "from rafeeq.core.config import" in text or "from ..core.config import" in text
