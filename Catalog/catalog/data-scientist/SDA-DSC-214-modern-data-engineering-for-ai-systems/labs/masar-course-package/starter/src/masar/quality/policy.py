"""Load ``quality/gate_config.yml`` — the fail-fast vs quarantine routing policy.

The policy is data, not code, for one reason: deciding that a failure must
STOP the platform is a governance decision. It should be reviewable by someone
who does not read Python, and its diff should be legible in a pull request.

This module is pure Python (PyYAML only), so the policy can be validated in a
unit test — which matters, because the failure mode of a mis-typed rule name
is silent: the gate simply never fail-fasts on it.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

DEFAULT_CONFIG_PATH = "quality/gate_config.yml"

FAIL_FAST = "FAIL_FAST"
QUARANTINE = "QUARANTINE"


@dataclass(frozen=True)
class PolicyEntry:
    """One routed rule.

    Attributes:
        rule: the rule name, shared with ``masar.quality.rules`` and the GX
            suites' ``meta``.
        response_class: ``FAIL_FAST`` or ``QUARANTINE``.
        expectation: the GX expectation type that produces this failure.
        column: the column it is about, or ``None`` for table-level rules.
        why: the justification. Required in review: a fail-fast rule without a
            stated reason is a future outage nobody can argue against.
    """

    rule: str
    response_class: str
    expectation: str = ""
    column: str | None = None
    why: str = ""


@dataclass(frozen=True)
class DatasetPolicy:
    """The full policy for one dataset."""

    dataset: str
    suite: str
    entries: tuple[PolicyEntry, ...]

    def by_class(self, response_class: str) -> tuple[str, ...]:
        """Rule names routed to ``response_class``."""
        return tuple(e.rule for e in self.entries if e.response_class == response_class)

    def response_class(self, rule: str, default: str = QUARANTINE) -> str:
        """How a failure of ``rule`` should be handled.

        Unknown rules default to QUARANTINE on purpose: a check merged without
        a policy entry must not be able to halt the platform on its first night.
        """
        for entry in self.entries:
            if entry.rule == rule:
                return entry.response_class
        return default


@dataclass(frozen=True)
class GatePolicy:
    """The whole gate configuration."""

    version: int
    defaults: dict[str, Any]
    datasets: dict[str, DatasetPolicy]

    @property
    def escalation_ratio(self) -> float:
        """Quarantine ratio above which a batch is escalated to fail-fast.

        A batch where most rows quarantine is not a row problem: it is a batch
        problem wearing a row problem's clothes, and promoting the minority
        that happened to pass is the wrong answer.
        """
        return float(
            self.defaults.get("escalate_to_fail_fast_when", {}).get("quarantine_ratio_above", 1.0)
        )

    def dataset(self, name: str) -> DatasetPolicy:
        """Look up one dataset's policy."""
        return self.datasets[name]


def _entries(section: dict[str, Any], key: str, response_class: str) -> list[PolicyEntry]:
    """Parse one ``fail_fast`` / ``quarantine`` / ``distribution`` list."""
    out = []
    for raw in section.get(key, []) or []:
        out.append(
            PolicyEntry(
                rule=raw["rule"],
                response_class=str(raw.get("response_class", response_class)).upper(),
                expectation=raw.get("expectation", "") or "",
                column=raw.get("column"),
                why=(raw.get("why") or "").strip(),
            )
        )
    return out


@lru_cache(maxsize=8)
def load_policy(path: str = DEFAULT_CONFIG_PATH) -> GatePolicy:
    """Read and parse the gate configuration.

    Args:
        path: path to ``gate_config.yml``. Resolved relative to the working
            directory, then relative to the repository root, so it works both
            from a lab shell and from a test runner.

    Raises:
        FileNotFoundError: when the policy cannot be found. The gate must not
            silently fall back to "everything quarantines".
    """
    import yaml

    candidate = Path(path)
    if not candidate.is_file():
        repo_root = Path(__file__).resolve().parents[3]
        candidate = repo_root / path
    if not candidate.is_file():
        raise FileNotFoundError(f"gate policy not found at {path!r} or {candidate}")

    raw = yaml.safe_load(candidate.read_text())
    datasets: dict[str, DatasetPolicy] = {}
    for name, section in raw.items():
        if name in ("version", "defaults") or not isinstance(section, dict):
            continue
        entries = (
            _entries(section, "fail_fast", FAIL_FAST)
            + _entries(section, "quarantine", QUARANTINE)
            + _entries(section, "distribution", QUARANTINE)
        )
        datasets[name] = DatasetPolicy(
            dataset=name, suite=section.get("suite", ""), entries=tuple(entries)
        )

    return GatePolicy(
        version=int(raw.get("version", 1)),
        defaults=raw.get("defaults", {}) or {},
        datasets=datasets,
    )


def validate_policy(policy: GatePolicy | None = None) -> list[str]:
    """Check the policy for the mistakes that fail silently.

    Returns:
        A list of problems; empty when the policy is sound. Checked:

        * every rule name is unique within its dataset — a duplicate means one
          of the two entries is dead and nobody will notice which;
        * every entry carries a ``why`` — an unjustified fail-fast rule is an
          outage nobody can argue against at 02:00;
        * every ``response_class`` is one of the two valid values;
        * every quarantine rule the gate can actually evaluate is known to
          ``masar.quality.rules``, so the policy and the evaluator agree.
    """
    from masar.quality.rules import RULES_BY_NAME

    policy = policy or load_policy()
    problems: list[str] = []

    for name, dataset in policy.datasets.items():
        seen: set[str] = set()
        for entry in dataset.entries:
            if entry.rule in seen:
                problems.append(f"{name}: duplicate rule {entry.rule!r}")
            seen.add(entry.rule)
            if entry.response_class not in (FAIL_FAST, QUARANTINE):
                problems.append(
                    f"{name}.{entry.rule}: invalid response_class {entry.response_class!r}"
                )
            if not entry.why:
                problems.append(f"{name}.{entry.rule}: missing 'why' justification")

        if name == "silver_trips":
            evaluable = set(RULES_BY_NAME)
            for rule in dataset.by_class(QUARANTINE):
                # Distribution rules are batch-level and have no row predicate.
                if rule.endswith("_drift") or rule == "dropoff_geohash_missing":
                    continue
                if rule not in evaluable:
                    problems.append(
                        f"{name}.{rule}: quarantine rule has no predicate in masar.quality.rules"
                    )

    return problems
