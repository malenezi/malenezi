"""Module 8 — pytest-style tests for `src/rafeeq/security/action_risk.py`.

Covers the SPEC §5 matrix as data: static classifications, the amount-
banded `issue_refund` rows, fail-closed on an unknown tool, and the
build-time guarantee (`assert_matrix_covers_registry`) that every real
tool in `tools/registry.py` has a risk classification.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rafeeq.core.config import (
    AUTO_REFUND_LIMIT_SAR,
    AUTONOMY_AUTONOMOUS,
    AUTONOMY_HUMAN_APPROVAL,
    AUTONOMY_POLICY_CONTROLLED,
    AUTONOMY_PROHIBITED,
    REFUND_LIMIT_SAR,
)
from rafeeq.security.action_risk import assert_matrix_covers_registry, classify, explain_matrix


class TestStaticClassifications:
    @pytest.mark.parametrize("tool_name", ["track_shipment", "estimate_eta", "get_delivery_events",
                                            "get_order", "get_customer"])
    def test_read_only_tools_autonomous(self, tool_name):
        assert classify(tool_name).autonomy == AUTONOMY_AUTONOMOUS

    @pytest.mark.parametrize("tool_name", ["change_customer_identity", "override_fraud_flag", "delete_order"])
    def test_prohibited_tools(self, tool_name):
        decision = classify(tool_name)
        assert decision.autonomy == AUTONOMY_PROHIBITED
        assert decision.prohibited is True

    def test_mark_refunded_requires_human_approval(self):
        assert classify("mark_refunded").autonomy == AUTONOMY_HUMAN_APPROVAL

    def test_unknown_tool_fails_closed_to_prohibited(self):
        decision = classify("some_tool_nobody_registered")
        assert decision.autonomy == AUTONOMY_PROHIBITED
        assert decision.reason == "unclassified_tool"


class TestRefundBanding:
    def test_auto_band(self):
        decision = classify("issue_refund", {"amount_sar": AUTO_REFUND_LIMIT_SAR})
        assert decision.autonomy == AUTONOMY_AUTONOMOUS
        assert decision.requires_human_approval is False

    def test_policy_controlled_band(self):
        decision = classify("issue_refund", {"amount_sar": (AUTO_REFUND_LIMIT_SAR + REFUND_LIMIT_SAR) / 2})
        assert decision.autonomy == AUTONOMY_POLICY_CONTROLLED
        assert decision.requires_logging is True
        assert decision.requires_human_approval is False

    def test_human_approval_band(self):
        decision = classify("issue_refund", {"amount_sar": REFUND_LIMIT_SAR + 0.01})
        assert decision.autonomy == AUTONOMY_HUMAN_APPROVAL
        assert decision.requires_human_approval is True

    def test_the_9500_sar_case_study_amount(self):
        decision = classify("issue_refund", {"amount_sar": 9500.0})
        assert decision.requires_human_approval is True

    def test_unparseable_amount_fails_closed_to_human_approval(self):
        decision = classify("issue_refund", {"amount_sar": "not-a-number"})
        assert decision.autonomy == AUTONOMY_HUMAN_APPROVAL

    def test_amount_key_alias_amount_also_read(self):
        decision = classify("issue_refund", {"amount": 9000.0})
        assert decision.requires_human_approval is True


class TestMatrixCoversRegistry:
    def test_assert_matrix_covers_registry_passes(self):
        assert_matrix_covers_registry()  # must not raise

    def test_explain_matrix_renders_every_tool(self):
        rendered = explain_matrix()
        assert "issue_refund" in rendered
        assert "prohibited" in rendered
        assert "change_customer_identity" in rendered
