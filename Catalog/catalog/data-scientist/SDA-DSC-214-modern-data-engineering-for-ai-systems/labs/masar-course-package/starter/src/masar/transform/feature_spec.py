"""Feature-window specifications, and the leakage lint that guards them.

A feature is point-in-time correct when it uses ONLY information that existed
at prediction time. Break that and the offline metric goes up, the live metric
does not, and the model is quietly worse than the heuristic it replaced. It is
the most expensive bug in applied ML because it presents as success.

The whole failure reduces to arithmetic on a window's bounds, so that is what
this module models — no Spark, no data, just the two integers that decide
whether a feature is honest.

Spark windows are expressed as ``rangeBetween(start, end)`` in SECONDS
relative to the current row's ordering value:

    rangeBetween(-3600, -1)      prior hour, strictly before   -> CORRECT
    rangeBetween(-3600,  0)      prior hour, INCLUDING now     -> LEAKS on ties
    rangeBetween(-3600, +3600)   centred window                -> LEAKS badly
    rangeBetween(-450,  +450)    centred 15-min window         -> LEAKS badly

``end == 0`` looks harmless and is not: ``rangeBetween`` is inclusive of both
bounds, so a row ordered by ``pickup_epoch`` includes every OTHER trip that
started in the same second. In a busy zone that is several trips that had not
happened yet from the model's point of view.
"""

from __future__ import annotations

from dataclasses import dataclass

HOUR_S = 3600
DAY_S = 86_400
MONTH_S = 30 * DAY_S


class LeakageError(AssertionError):
    """Raised when a feature window admits information from at or after t=0."""


@dataclass(frozen=True)
class FeatureWindow:
    """A rolling feature window, in seconds relative to the event.

    Attributes:
        name: the feature column this window produces.
        start: lower bound, negative = seconds before the event.
        end: upper bound. Must be strictly negative to be point-in-time
            correct; ``-1`` means "up to and including the previous second".
        rationale: why this width. A window with no rationale is a guess, and
            guesses do not survive an incident review.
    """

    name: str
    start: int
    end: int
    rationale: str = ""

    @property
    def is_point_in_time(self) -> bool:
        """True when the window is strictly in the past.

        Two conditions, both necessary:
          * ``end < 0`` — nothing at or after the event enters the window;
          * ``start <= end`` — the window is not inside out.
        """
        return self.end < 0 and self.start <= self.end

    @property
    def width_seconds(self) -> int:
        """How much history the window spans."""
        return self.end - self.start + 1

    def explain(self) -> str:
        """One line a human can check in review."""
        verdict = "point-in-time" if self.is_point_in_time else "LEAKS"
        return (
            f"{self.name}: rangeBetween({self.start}, {self.end}) "
            f"= {self.width_seconds / 60:.0f} min of history -> {verdict}"
        )

    def assert_point_in_time(self) -> None:
        """Raise :class:`LeakageError` if the window is not strictly prior.

        Call this from a build task, not from a code review. A lint that runs
        is worth more than a rule everyone agrees with.
        """
        if self.is_point_in_time:
            return
        if self.end == 0:
            detail = (
                "end=0 includes the current row's own timestamp; on ties this "
                "admits events from the same second, i.e. the future"
            )
        elif self.end > 0:
            detail = f"end={self.end} reaches {self.end}s PAST the event — direct leakage"
        else:
            detail = f"start={self.start} is after end={self.end}: the window is inverted"
        raise LeakageError(f"feature {self.name!r} is not point-in-time correct: {detail}")


#: The declared window for every rolling column of ``gold.eta_features``.
#: This is the contract Lab 8's leakage drill repairs the code to match.
ETA_FEATURE_WINDOWS: dict[str, FeatureWindow] = {
    "rolling_zone_demand_15m": FeatureWindow(
        "rolling_zone_demand_15m",
        -900,
        -1,
        "Trips started in this zone in the prior 15 minutes. Known at pickup; "
        "a centred window would count trips that start after this one.",
    ),
    "rolling_avg_speed_10m": FeatureWindow(
        "rolling_avg_speed_10m",
        -600,
        -1,
        "Average speed of vehicles in the zone over the prior 10 minutes. "
        "Averaging THIS trip's own pings uses the trip's outcome as its input.",
    ),
    "driver_recent_trip_count": FeatureWindow(
        "driver_recent_trip_count",
        -DAY_S,
        -1,
        "Driver's completed trips in the prior 24 hours, strictly before.",
    ),
    "historical_route_duration": FeatureWindow(
        "historical_route_duration",
        -MONTH_S,
        -1,
        "Mean duration on this origin-destination pair over the prior 30 days.",
    ),
}


#: Features that must be recomputable at inference time from data the serving
#: path actually has. ``distance_km`` in the raw feed is the ACTUAL distance
#: driven — only known once the trip is over — so the honest feature is the
#: PLANNED distance from the routing engine, under the same column name.
UNAVAILABLE_AT_INFERENCE: dict[str, str] = {
    "distance_km": (
        "actual distance driven, known only at dropoff; at prediction time the "
        "platform has the ROUTED distance — same name, different provenance"
    ),
    "duration_min": "this is the label",
    "dropoff_ts": "the trip has not ended yet",
    "label_actual_duration_min": "this is the label",
}


def validate_windows(windows: dict[str, FeatureWindow]) -> list[str]:
    """Validate a set of windows; return one message per offending feature.

    Returns:
        An empty list when every window is point-in-time correct. Otherwise a
        list of human-readable failures, in declaration order.
    """
    problems: list[str] = []
    for window in windows.values():
        try:
            window.assert_point_in_time()
        except LeakageError as exc:
            problems.append(str(exc))
    return problems


def audit_feature_set(
    columns: list[str], windows: dict[str, FeatureWindow] | None = None
) -> dict[str, list[str]]:
    """Audit a feature table's column list before it is trained on.

    Args:
        columns: the feature table's columns.
        windows: declared windows; defaults to :data:`ETA_FEATURE_WINDOWS`.

    Returns:
        ``{"leaking": [...], "unavailable_online": [...], "undeclared": [...]}``

        * ``leaking`` — a declared window that reaches the present or future.
        * ``unavailable_online`` — a column the serving path cannot produce.
        * ``undeclared`` — a rolling-looking column with no declared window.
          Not automatically wrong, but nobody has said why it is right.
    """
    windows = windows if windows is not None else ETA_FEATURE_WINDOWS
    leaking = [w.name for w in windows.values() if w.name in columns and not w.is_point_in_time]
    unavailable = [c for c in columns if c in UNAVAILABLE_AT_INFERENCE]
    undeclared = [
        c
        for c in columns
        if c not in windows
        and any(token in c for token in ("rolling_", "_prev_", "recent_", "historical_"))
    ]
    return {
        "leaking": leaking,
        "unavailable_online": unavailable,
        "undeclared": undeclared,
    }


def correlation_is_suspicious(pearson_r: float, threshold: float = 0.90) -> bool:
    """True when a feature correlates with the label so well it is confessing.

    A feature at |r| > 0.90 against the target is usually the target wearing a
    hat. It is not proof of leakage — ``distance_km`` genuinely predicts trip
    duration — but it is the correlation that earns an explanation before the
    model ships.
    """
    return abs(pearson_r) >= threshold
