"""Great Expectations plumbing: context, datasource, assets, docs.

Great Expectations 0.18 needs a filesystem-backed context, a Spark datasource
and one asset per table before a suite can be attached to anything. That is
boilerplate, it is the same every time, and every minute spent on it in Lab 6
is a minute not spent on the interesting question — which failures should
block, and which should quarantine.

So it lives here, once.

No cloud, no telemetry, no account: ``quality/gx/`` is a directory in the repo
and the data docs are an HTML file you open with a browser.

CLI::

    python -m masar.quality.bootstrap --init
    python -m masar.quality.bootstrap --validate --suite silver_trips.contract --build-docs
    python -m masar.quality.bootstrap --build-docs
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from masar import config

GX_ROOT = "./quality/gx"
DATASOURCE = "masar_lakehouse"

#: asset name -> lakehouse path. Asset names are referenced by the suites in
#: ``quality/suites/``; renaming one breaks them, so treat these as an API.
ASSETS: dict[str, str] = {
    "silver_trips": config.TABLES["silver.trips"].path,
    "silver_vehicle_positions": config.TABLES["silver.vehicle_positions"].path,
    "bronze_gps_events": config.TABLES["bronze.gps_events"].path,
    "silver_trips_quarantine": config.TABLES["silver.trips_quarantine"].path,
}


def get_context(root: str = GX_ROOT) -> Any:
    """Return (creating if needed) a filesystem-backed GX context."""
    import great_expectations as gx

    Path(root).mkdir(parents=True, exist_ok=True)
    return gx.get_context(context_root_dir=root)


def init(root: str = GX_ROOT) -> Any:
    """Create the context, the Spark datasource and one asset per table.

    Assets are registered as Delta paths read through Spark, so a suite
    validates the SAME bytes the pipeline reads — not a CSV export that
    drifted from it three weeks ago.
    """
    import great_expectations as gx
    from delta.tables import DeltaTable

    from masar.spark import get_spark

    print(f"[gx] great_expectations {gx.__version__}")
    context = get_context(root)
    print(f"[gx] context root: {root}")

    try:
        datasource = context.get_datasource(DATASOURCE)
    except (KeyError, ValueError):
        datasource = context.sources.add_spark(name=DATASOURCE)
    print(f"[gx] datasource   : {DATASOURCE}   (spark, delta)")

    spark = get_spark("gx-bootstrap")
    registered: list[str] = []
    for asset_name, path in ASSETS.items():
        if not DeltaTable.isDeltaTable(spark, path):
            print(f"[gx] asset skipped: {asset_name} ({path} does not exist yet)")
            continue
        try:
            datasource.get_asset(asset_name)
        except (LookupError, KeyError, ValueError):
            df = spark.read.format("delta").load(path)
            datasource.add_dataframe_asset(name=asset_name, dataframe=df)
        registered.append(asset_name)

    print(f"[gx] assets       : {', '.join(registered) or '(none — build the tables first)'}")
    print(f"[gx] data docs    : {root}/uncommitted/data_docs/local_site/index.html")
    print("[gx] ready")
    return context


def validate(suite_name: str, asset: str | None = None, root: str = GX_ROOT) -> Any:
    """Validate an asset against a saved suite and print the pass/fail summary.

    Args:
        suite_name: e.g. ``silver_trips.contract``.
        asset: defaults to the suite name's prefix (``silver_trips``).
        root: GX context root.

    Returns:
        The GX validation result — hand it straight to
        ``masar.quality.gate.gate_and_promote``, which reads the
        ``response_class`` meta off each failed expectation.
    """
    context = get_context(root)
    asset = asset or suite_name.split(".")[0]
    suite = context.get_expectation_suite(suite_name)
    batch_request = context.get_datasource(DATASOURCE).get_asset(asset).build_batch_request()
    validator = context.get_validator(batch_request=batch_request, expectation_suite=suite)

    result = validator.validate()
    stats = result["statistics"]
    print(f"[gx] validating {suite_name} against {asset}")
    print(
        f"[gx]   {stats['evaluated_expectations']} expectations : "
        f"{stats['successful_expectations']} passed, {stats['unsuccessful_expectations']} failed"
    )
    print(f"[gx]   success = {result['success']}")
    for r in result["results"]:
        if not r["success"]:
            cfg = r["expectation_config"]
            cls = cfg["meta"].get("response_class", "UNCLASSIFIED")
            column = cfg["kwargs"].get("column", "<table>")
            print(f"[gx]   FAILED [{cls}] {column}: {cfg['expectation_type']}")
    return result


def build_docs(root: str = GX_ROOT) -> str:
    """Render the data docs and return the index path.

    The docs are the lab's evidence artefact: a reviewable HTML report of what
    was checked, on which batch, with what outcome. Copy it into
    ``quality/evidence/`` and it becomes part of the audit trail.
    """
    context = get_context(root)
    context.build_data_docs()
    index = f"{root}/uncommitted/data_docs/local_site/index.html"
    print(f"[gx] data docs written: {index}")
    return index


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Great Expectations bootstrap for Masar")
    p.add_argument("--init", action="store_true", help="create context, datasource and assets")
    p.add_argument("--validate", action="store_true", help="validate a suite")
    p.add_argument("--suite", default="silver_trips.contract")
    p.add_argument("--asset", default=None)
    p.add_argument("--build-docs", action="store_true")
    p.add_argument("--root", default=GX_ROOT)
    a = p.parse_args()

    if a.init:
        init(a.root)
    if a.validate:
        validate(a.suite, a.asset, a.root)
    if a.build_docs:
        build_docs(a.root)
    if not (a.init or a.validate or a.build_docs):
        p.print_help()


if __name__ == "__main__":
    main()
