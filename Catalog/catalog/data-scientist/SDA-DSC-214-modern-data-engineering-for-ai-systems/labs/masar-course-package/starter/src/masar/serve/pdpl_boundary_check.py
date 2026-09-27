"""Assert that no personal identifier crosses into a gold product or Redis.

This is a TEST, not a document. Governance that lives in a policy PDF is
checked when someone remembers; governance that lives in a build step is
checked every time. Exits non-zero on any violation, so it belongs in CI.

CLI::

    python -m masar.serve.pdpl_boundary_check
"""

from __future__ import annotations

import argparse
import json

from masar import config
from masar.governance.classification import check_serving_boundary
from masar.serve.materialize_online import KEY, redis_client
from masar.spark import get_spark

#: dataset -> (path, explicitly allowed columns with their justification)
#: Each allow-list entry is a DOCUMENTED exception, justified in
#: docs/GOVERNANCE_TEMPLATE.md. An exception with no justification recorded
#: there is a leak with a comment in front of it.
BOUNDARY_TARGETS: dict[str, tuple[str, tuple[str, ...]]] = {
    # rider_pseudonym: cohort analysis without the identifier.
    # driver_key: driver-level BI is a stated business purpose; the driver is
    #   an employee-equivalent, not an anonymous data subject, and the exposure
    #   is to a named analyst role — not to the online store.
    "gold.fact_trip": (
        config.TABLES["gold.fact_trip"].path,
        ("rider_pseudonym", "driver_key"),
    ),
    # dim_driver exists to label driver-level reporting; national_id_hash and
    # phone_hash are NOT selected into it, and that is what the check enforces.
    "gold.dim_driver": (
        config.TABLES["gold.dim_driver"].path,
        ("driver_id", "driver_key", "full_name_en"),
    ),
    # No exceptions. The feature table is zone- and trip-grained; if a personal
    # column appears here it reaches the model AND the online store.
    "gold.eta_features": (config.TABLES["gold.eta_features"].path, ()),
    "gold.zone_hourly_demand": (config.TABLES["gold.zone_hourly_demand"].path, ()),
    "gold.trip_features": (config.TABLES["gold.trip_features"].path, ("driver_id",)),
    "gold.bi_trips_safe": (config.TABLES["gold.bi_trips_safe"].path, ("rider_pseudonym",)),
}


def check_tables() -> list:
    """Check every gold product's column list against the classification."""
    from delta.tables import DeltaTable

    spark = get_spark("pdpl-boundary")
    verdicts = []
    for dataset, (path, allow) in BOUNDARY_TARGETS.items():
        if not DeltaTable.isDeltaTable(spark, path):
            print(f"[pdpl] {dataset:<28} (not built yet — skipped)")
            continue
        columns = spark.read.format("delta").load(path).columns
        verdict = check_serving_boundary(dataset, columns, allow=allow)
        print(verdict.render())
        verdicts.append(verdict)
    return verdicts


def check_online_store() -> list:
    """Check the Redis payloads: right grain, no personal fields.

    The grain matters as much as the fields. A key of
    ``masar:features:rider:{rider_id}`` would be a register of riders in a
    cache with no access log — personal data in the least governed place in
    the platform. Zone grain is the design decision that prevents it.
    """
    try:
        client = redis_client()
        keys = list(client.scan_iter(match=KEY.format(zone_id="*"), count=1000))
    except Exception as exc:  # noqa: BLE001 - Redis is optional before Lab 8
        print(f"[pdpl] redis {KEY.format(zone_id='*')}  (unreachable: {exc}) — skipped")
        return []

    fields: set[str] = set()
    for key in keys[:200]:
        raw = client.get(key)
        if raw:
            fields.update(json.loads(raw))

    verdict = check_serving_boundary(f"redis {KEY.format(zone_id='*')}", sorted(fields))
    print(f"{verdict.render()}  keys={len(keys)}  grain=zone (not rider, not vehicle)")
    return [verdict]


def main() -> None:
    """CLI entry point. Exits 1 on any boundary violation."""
    argparse.ArgumentParser(description="PDPL serving-boundary assertions").parse_args()
    verdicts = check_tables() + check_online_store()
    failures = [v for v in verdicts if not v.ok]
    if failures:
        for v in failures:
            print(f"[pdpl] VIOLATION in {v.dataset}: {list(v.violations)}")
        raise SystemExit(1)
    print(f"[pdpl] {len(verdicts)} boundary assertions passed")


if __name__ == "__main__":
    main()
