"""Module 9 — SLOs and alerts: the capstone monitoring-dashboard extension.

Cost is not the only signal (module overview §4): latency, tool error
rate, escalation rate, guardrail-trip rate, and step/handoff distribution
are the early warnings that something regressed. `check_slos` takes an
`evaluations.metrics.Metrics` snapshot (the SAME 12-dimension dashboard
object the eval harness and TawseelBench already produce — one source of
truth, not a second metrics pipeline) and returns the `Alert`s that
would fire, each naming the metric, its threshold, the actual value, and
a severity — the artefact the capstone's optional monitoring-dashboard
extension and `deployment/runbook.md`'s `sim-incident` drill both consume.

Dependency-free (Layer A): stdlib + `rafeeq.core.config` +
`evaluations.metrics.Metrics` (imported lazily so this module never
forces the evaluations package to import just to define the SLO
thresholds/dataclasses — see `check_slos`).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from rafeeq.core.config import RUN_COST_CAP_USD

# --------------------------------------------------------------------------
# Default targets. Sources, so a reader can see these are not arbitrary:
#   - p95_latency_s_max: Module 9's own benchmark target ("p95 latency <=
#     2.5 s" — Benchmarks and Evaluation table).
#   - cost_per_contact_usd_max: the module's "+ retrieval caching" example
#     benchmark row (0.008 USD/contact) with headroom (1.5x) before it
#     alerts, so the SLO catches genuine drift, not run-to-run noise.
#   - escalation_rate_max: a defensible operations target (SDA-AIE-311
#     classroom default) — raise/lower per the SLO-workshop exercise.
#   - unsafe_action_rate_max: 0.0, matching the capstone rubric's "0 open
#     high-severity findings" bar — any unsafe action is a page, not a
#     trend to watch.
# --------------------------------------------------------------------------
DEFAULT_P95_LATENCY_S_MAX = 2.5
DEFAULT_COST_PER_CONTACT_USD_MAX = 0.008 * 1.5
DEFAULT_ESCALATION_RATE_MAX = 0.20
DEFAULT_UNSAFE_ACTION_RATE_MAX = 0.0
# A run-level companion to the above: RUN_COST_CAP_USD is the PER-RUN
# denial-of-wallet ceiling (core/config.py, M8/M9) — useful here too as a
# sanity bound (`cost_per_contact_usd_max` should never exceed it).
_ = RUN_COST_CAP_USD


@dataclass(frozen=True)
class SLOs:
    """One SLO set. Construct with overrides for a workshop exercise
    ("groups set cost/latency/escalation SLOs for Rafeeq") without editing
    this module."""

    p95_latency_s_max: float = DEFAULT_P95_LATENCY_S_MAX
    cost_per_contact_usd_max: float = DEFAULT_COST_PER_CONTACT_USD_MAX
    escalation_rate_max: float = DEFAULT_ESCALATION_RATE_MAX
    unsafe_action_rate_max: float = DEFAULT_UNSAFE_ACTION_RATE_MAX


DEFAULT_SLOS = SLOs()

SEVERITY_ORDER = ("low", "medium", "high", "critical")


@dataclass(frozen=True)
class Alert:
    metric: str
    threshold: float
    actual: float
    severity: str
    message: str
    owner: str

    def to_dict(self) -> dict[str, Any]:
        return dict(self.__dict__)

    def __str__(self) -> str:  # pragma: no cover - display only
        return f"[{self.severity.upper()}] {self.metric}: {self.actual:.4g} > {self.threshold:.4g} — {self.message}"


# metric -> (attribute name on Metrics, comparison, severity, owner, message template)
_RULES: list[tuple[str, str, str, str, str]] = [
    ("p95_latency_s", "p95_latency_s_max", "high", "platform-eng",
     "p95 latency is above the customer-felt-latency SLO"),
    ("avg_cost_usd_per_task", "cost_per_contact_usd_max", "medium", "finance+platform-eng",
     "blended cost/contact is drifting back up — check for a routing/caching regression"),
    ("escalation_rate", "escalation_rate_max", "high", "ops-lead",
     "escalation rate is climbing — the agent is resolving less, not just seeing less volume"),
    ("unsafe_action_rate", "unsafe_action_rate_max", "critical", "security-lead",
     "an unsafe action was recorded — page immediately, do not wait for a trend"),
]


def check_slos(metrics: Any, slos: SLOs = DEFAULT_SLOS) -> list[Alert]:
    """Compare a `Metrics` snapshot (see `evaluations/metrics.py`) against
    `slos` and return every `Alert` that fires. `metrics` is duck-typed
    (any object with the four attribute names in `_RULES` — a plain dict
    with those keys also works, so a live monitoring loop that only has a
    dict of recent numbers need not construct a full `Metrics`)."""
    alerts: list[Alert] = []
    for attr, threshold_attr, severity, owner, message in _RULES:
        actual = _get(metrics, attr)
        if actual is None:
            continue
        threshold = getattr(slos, threshold_attr)
        if actual > threshold:
            alerts.append(Alert(metric=attr, threshold=threshold, actual=float(actual),
                                  severity=severity, message=message, owner=owner))
    alerts.sort(key=lambda a: SEVERITY_ORDER.index(a.severity), reverse=True)
    return alerts


def _get(metrics: Any, attr: str) -> float | None:
    if isinstance(metrics, dict):
        return metrics.get(attr)
    return getattr(metrics, attr, None)


def render_alerts(alerts: list[Alert]) -> str:
    """Render `check_slos`' output as a markdown alert list — empty
    input renders a clean "all SLOs green" line rather than an empty
    table, so a report/CI log always says something explicit."""
    if not alerts:
        return "All SLOs green — no alert fired."
    lines = ["| Severity | Metric | Threshold | Actual | Owner | Message |",
             "|---|---|---|---|---|---|"]
    for a in alerts:
        lines.append(f"| {a.severity} | {a.metric} | {a.threshold:.4g} | {a.actual:.4g} | {a.owner} | {a.message} |")
    return "\n".join(lines)
