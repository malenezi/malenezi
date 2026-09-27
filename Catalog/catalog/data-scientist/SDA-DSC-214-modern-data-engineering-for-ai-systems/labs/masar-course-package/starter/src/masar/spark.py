"""The one place a Spark session is built.

Every lab calls :func:`get_spark`. Nobody reconfigures Spark ad hoc in a
notebook — that is how a "Delta is not a valid Spark SQL Data Source" ticket
is born, and how two processes end up disagreeing about what ``bronze.trips``
means.

Storage and compute are separate even on a laptop: the data lives under
``./lakehouse`` (a stand-in for ``s3://masar-lakehouse``), the compute is this
JVM. Kill the JVM and the data is still there — that is Module 2's whole
argument, made physical.

PySpark is imported INSIDE the function so that ``import masar.spark`` works
on a machine with no Spark at all (``scripts/doctor.py`` depends on this).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from masar import config

if TYPE_CHECKING:  # pragma: no cover - typing only, never imported at runtime
    from pyspark.sql import SparkSession

# The Kafka connector is not bundled with PySpark. Lab 5 needs it; Labs 1-4
# do not, so it is requested only when `kafka=True` to keep session start-up
# fast (and offline-friendly) for everybody else.
_KAFKA_PACKAGE = "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"


def get_spark(app_name: str = config.SPARK_APP_NAME, *, kafka: bool = False) -> SparkSession:
    """Build (or return) the Masar Spark 3.5 + Delta Lake 3.2 session.

    Args:
        app_name: shows up in the Spark UI and in every log line. Name it
            after the job, not after the person running it.
        kafka: also pull the ``spark-sql-kafka-0-10`` connector. Only Lab 5's
            streaming ingest needs it; requesting it always would make every
            other lab wait on an Ivy resolution it never uses.

    Returns:
        A live ``SparkSession``. ``getOrCreate`` means calling this ten times
        in one process is free — but note that the FIRST call decides the
        configuration for the whole JVM, so ``kafka=True`` must be requested
        by the first caller in a streaming job.

    Notes:
        ``enableHiveSupport()`` gives a persistent catalog, so ``bronze.trips``
        resolves to the same table in this process, in the next one, and in
        dbt (Lab 3). Without it, every process would see an empty catalog and
        the labs would degrade into path-only access.
    """
    from delta import configure_spark_with_delta_pip
    from pyspark.sql import SparkSession

    config.ensure_dirs()

    builder = (
        SparkSession.builder.appName(app_name)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        # Local stand-in for an object-storage bucket.
        .config("spark.sql.warehouse.dir", config.LAKEHOUSE_ROOT)
        # 8, not the 200 default: on a laptop, 200 shuffle partitions means
        # 200 tiny files and a minute of scheduling overhead per stage.
        .config("spark.sql.shuffle.partitions", str(config.SPARK_SHUFFLE_PARTITIONS))
        # Keep the guard ON. Disabling it is how someone VACUUMs with RETAIN 0
        # HOURS and destroys the audit history in Lab 4.
        .config("spark.databricks.delta.retentionDurationCheck.enabled", "true")
        # Delta writes a checkpoint every 10 commits; the labs make dozens of
        # commits, and the smaller interval keeps DESCRIBE HISTORY fast.
        .config("spark.databricks.delta.properties.defaults.checkpointInterval", "10")
        .config("spark.ui.showConsoleProgress", "false")
        .enableHiveSupport()
    )

    # The `delta-spark` PIP package ships the Python API only — the Delta JARs
    # are resolved from Maven at session start. `configure_spark_with_delta_pip`
    # adds the matching `io.delta:delta-spark_2.12:<version>` coordinate, which
    # is why the first run prints a wall of Ivy resolution and takes a minute.
    # Skip this and every Delta read fails with "not a valid Spark SQL Data
    # Source" — a message that sounds like a missing pip install and is not.
    extra_packages = [_KAFKA_PACKAGE] if kafka else []
    spark = configure_spark_with_delta_pip(builder, extra_packages=extra_packages).getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    return spark


def warm() -> None:
    """Start a session, round-trip five rows through Delta, and report.

    ``python -m masar.spark --warm`` is the first thing to run on a new
    machine: it forces the Delta jars to resolve once, so the first real lab
    command is not also a two-minute Ivy download.
    """
    import time

    t0 = time.time()
    spark = get_spark("masar-warm")
    probe = f"{config.LAKEHOUSE_ROOT}/_probe/warm"
    spark.range(5).write.format("delta").mode("overwrite").save(probe)
    n = spark.read.format("delta").load(probe).count()
    print(f"[spark] session up in {time.time() - t0:.1f}s")
    print(f"[spark] version      {spark.version}")
    print(f"[spark] warehouse    {spark.conf.get('spark.sql.warehouse.dir')}")
    print(f"[spark] delta probe  {n} rows round-tripped at {probe}")


def main() -> None:
    """CLI: ``python -m masar.spark --warm``."""
    import argparse

    p = argparse.ArgumentParser(description="Masar Spark session utilities")
    p.add_argument("--warm", action="store_true", help="start a session and round-trip Delta")
    args = p.parse_args()
    if args.warm:
        warm()
    else:
        p.print_help()


if __name__ == "__main__":
    main()
