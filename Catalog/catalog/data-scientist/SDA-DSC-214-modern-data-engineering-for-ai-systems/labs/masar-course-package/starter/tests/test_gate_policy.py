"""The gate policy — is the fail-fast / quarantine routing sound?

``quality/gate_config.yml`` decides which failures STOP the platform and which
merely isolate rows. Getting it wrong fails silently in both directions:

  * a rule mis-typed in the YAML never fail-fasts, and nobody notices until a
    batch with duplicate keys is promoted;
  * an over-eager fail-fast rule halts the pipeline nightly, somebody adds a
    bypass flag, and the gate becomes decoration.

Neither shows up as an error, so the policy is tested.
"""

from __future__ import annotations

import pytest

from masar.quality.policy import (
    FAIL_FAST,
    QUARANTINE,
    load_policy,
    validate_policy,
)
from masar.quality.rules import RULES_BY_NAME


@pytest.fixture(scope="module")
def policy(repo_root):
    """The shipped policy, loaded from the repository."""
    return load_policy(str(repo_root / "quality" / "gate_config.yml"))


def test_policy_loads_and_is_internally_valid(policy):
    """No duplicate rules, no invalid classes, no unjustified entries."""
    assert validate_policy(policy) == []


def test_integrity_failures_are_fail_fast(policy):
    """Null keys, duplicate keys and schema changes must stop the batch.

    These are the failures where promoting ANY row is worse than promoting
    none: an unkeyed row cannot be merged or erased, a duplicated key makes
    MERGE undefined, and a schema change breaks every consumer at once.
    """
    fail_fast = set(policy.dataset("silver_trips").by_class(FAIL_FAST))
    assert {"trip_id_null", "trip_id_unique", "pickup_ts_null", "schema_columns"} <= fail_fast


def test_value_failures_are_quarantined_not_blocking(policy):
    """Blocking 48,000 good trips for 120 bad fares is a control people bypass."""
    quarantine = set(policy.dataset("silver_trips").by_class(QUARANTINE))
    assert {"fare_non_positive", "city_not_in_ksa_set", "duration_implausible"} <= quarantine

    fail_fast = set(policy.dataset("silver_trips").by_class(FAIL_FAST))
    assert not (quarantine & fail_fast), "a rule cannot be in both classes"


def test_unknown_rules_default_to_quarantine(policy):
    """A check merged without a policy entry must not be able to halt the platform."""
    assert policy.dataset("silver_trips").response_class("some_new_rule") == QUARANTINE


def test_every_quarantine_rule_has_a_row_predicate(policy):
    """The policy and the evaluator must name the same rules.

    GX tells you WHICH RULE failed; Spark tells you WHICH ROWS failed it. If a
    policy rule has no matching predicate in ``masar.quality.rules``, the gate
    can report the failure but cannot quarantine the rows — which means it
    promotes them.
    """
    for rule in policy.dataset("silver_trips").by_class(QUARANTINE):
        if rule.endswith("_drift") or rule == "dropoff_geohash_missing":
            continue  # batch-level distribution checks have no row predicate
        assert rule in RULES_BY_NAME, f"policy rule {rule!r} has no predicate"


def test_every_entry_states_why(policy):
    """A fail-fast rule with no justification is an outage nobody can argue against."""
    for dataset in policy.datasets.values():
        for entry in dataset.entries:
            assert entry.why, f"{dataset.dataset}.{entry.rule} has no 'why'"


def test_the_speed_drift_rule_is_grouped_by_producer_version(repo_root):
    """The incident's detection rule must group, or the alert is not actionable.

    An ungrouped drift alert says "something changed". Grouped by
    producer_version it says "2.5.0 changed and 2.4.0 did not", which names a
    deployment, which has an owner and a rollback.
    """
    import yaml

    raw = yaml.safe_load((repo_root / "quality" / "gate_config.yml").read_text())
    speed_rule = next(
        r for r in raw["gps_events"]["distribution"] if r["rule"] == "speed_mean_drift"
    )
    assert speed_rule["group_by"] == "producer_version"
    assert "m/s" in speed_rule["why"]


def test_escalation_threshold_exists_and_is_below_one(policy):
    """A batch where most rows quarantine is a BATCH problem, not a row problem.

    Promoting the minority that happened to pass would be the wrong answer, so
    a high quarantine ratio escalates to fail-fast.
    """
    assert 0 < policy.escalation_ratio < 1
