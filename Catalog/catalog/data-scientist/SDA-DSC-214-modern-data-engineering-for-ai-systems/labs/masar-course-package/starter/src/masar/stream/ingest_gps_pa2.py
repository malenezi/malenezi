"""PA-2 artefact — land the PA-2 GPS topic into Delta and publish "zone demand".

================================ WARNING ==================================
THIS FILE IS A DELIBERATELY BROKEN ASSESSMENT ARTEFACT.
It is the artefact under test in `labs/assessments/PA-2_Streaming_Exactly_Once.md`
and it ships with its defects intact, on purpose. DO NOT USE IT AS A
REFERENCE for Structured Streaming. The correct patterns live in
`masar.stream.ingest_gps_stream` (checkpointed, idempotent foreachBatch) and
`masar.stream.zone_demand` (event-time window + watermark).
===========================================================================

Written, in the fiction, by an engineer who was told the pipeline "basically
works". Four faults are present (PA-2 marking scheme, section 1):

  1. Query 1 has NO ``checkpointLocation``. With ``startingOffsets=earliest``
     every restart replays the whole topic, so the landing table grows on
     every deploy.
  2. Query 2 windows on ``F.current_timestamp()`` — a PROCESSING-time window.
     A ping back-dated 20 minutes is filed under the quarter-hour in which it
     happened to arrive, not the one in which it occurred.
  3. Query 2 has no watermark and uses ``outputMode("complete")`` — unbounded
     state, and a full rewrite of the sink on every trigger.
  4. ``write_batch`` has no idempotent-write guard (no ``txnAppId`` /
     ``txnVersion``), so a re-executed batch double-appends; and the grain of
     query 2 is ``trip_id``, not ``pickup_zone_id`` — it is not zone demand
     at all. (This second half is a SEMANTIC error no amount of streaming
     discipline would catch.)

Sandbox only: topic ``masar.gps.pings.pa2`` and
``./lakehouse/_assessments/pa2/*``. The cohort's ``bronze.gps_events`` is
never touched.

CLI::

    python -m masar.stream.ingest_gps_pa2

PySpark is imported inside the functions so that
``import masar.stream.ingest_gps_pa2`` works on a machine with no Spark
installed.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from masar import config

if TYPE_CHECKING:  # pragma: no cover - typing only
    from pyspark.sql import DataFrame

TOPIC = "masar.gps.pings.pa2"
BOOTSTRAP = config.KAFKA_BOOTSTRAP
BRONZE = f"{config.LAKEHOUSE_ROOT}/_assessments/pa2/gps_events"
DEMAND = f"{config.LAKEHOUSE_ROOT}/_assessments/pa2/zone_demand"
DEMAND_CHECKPOINT = f"{config.LAKEHOUSE_ROOT}/_assessments/pa2/_ckpt"


def ping_schema():
    """The CONVENTIONS wire schema for a GPS ping. Fixed — do not invent columns."""
    from pyspark.sql.types import (
        DoubleType,
        StringType,
        StructField,
        StructType,
        TimestampType,
    )

    payload = StructType(
        [
            StructField("lat", DoubleType()),
            StructField("lon", DoubleType()),
            StructField("speed_kmh", DoubleType()),
            StructField("heading_deg", DoubleType()),
            StructField("accuracy_m", DoubleType()),
        ]
    )
    return StructType(
        [
            StructField("event_id", StringType()),
            StructField("vehicle_id", StringType()),
            StructField("driver_id", StringType()),
            StructField("trip_id", StringType()),
            StructField("ts", TimestampType()),
            StructField("payload", payload),
            StructField("producer_version", StringType()),
        ]
    )


def parse(raw: DataFrame) -> DataFrame:
    """Parse the Kafka value into the CONVENTIONS ping shape plus lineage."""
    from pyspark.sql import functions as F

    return raw.select(
        F.from_json(F.col("value").cast("string"), ping_schema()).alias("p"),
        F.col("topic"),
        F.col("partition"),
        F.col("offset"),
        F.col("timestamp").alias("_kafka_ts"),
    ).select(
        F.col("p.event_id").alias("event_id"),
        F.col("p.vehicle_id").alias("vehicle_id"),
        F.col("p.driver_id").alias("driver_id"),
        F.col("p.trip_id").alias("trip_id"),
        F.col("p.ts").alias("ts"),
        F.col("p.payload").alias("payload"),
        F.col("p.producer_version").alias("producer_version"),
        F.col("_kafka_ts"),
        F.concat_ws("/", F.lit("kafka:/"), F.col("topic"), F.col("partition").cast("string")).alias(
            "_source_file"
        ),
        F.col("offset").alias("_kafka_offset"),
    )


def write_batch(batch_df: DataFrame, batch_id: int) -> None:
    """Append the micro-batch to the landing table.

    DEFECT 4a: a plain append with no ``txnAppId``/``txnVersion``. If Spark
    re-executes this batch after a failure the rows land twice, and the sink
    has no way to tell that it has already seen ``batch_id``.
    """
    from pyspark.sql import functions as F

    out = batch_df.withColumn("_batch_id", F.lit(batch_id).cast("long")).withColumn(
        "_ingested_at", F.current_timestamp()
    )
    out.write.format("delta").mode("append").save(BRONZE)
    print(f"Batch {batch_id}: appended {out.count():,} pings", flush=True)


def run() -> None:
    """Start both streaming queries and block.

    DEFECT 1: ``q1`` has no ``checkpointLocation``.
    DEFECT 2: the demand window is over ``current_timestamp()``.
    DEFECT 3: no watermark, ``outputMode("complete")``.
    DEFECT 4b: the demand grain is ``trip_id``, not ``pickup_zone_id``.
    """
    from pyspark.sql import functions as F

    from masar.spark import get_spark

    spark = get_spark("pa2-gps", kafka=True)
    raw = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", BOOTSTRAP)
        .option("subscribe", TOPIC)
        .option("startingOffsets", "earliest")
        .option("maxOffsetsPerTrigger", 8000)
        .load()
    )
    events = parse(raw)

    # ---- query 1: land to bronze -----------------------------------------
    q1 = (
        events.writeStream.queryName("pa2_bronze")
        .foreachBatch(write_batch)
        .outputMode("append")
        .trigger(processingTime="20 seconds")
        .start()
    )

    # ---- query 2: 15-minute "zone demand" --------------------------------
    demand = events.groupBy(F.window(F.current_timestamp(), "15 minutes"), F.col("trip_id")).agg(
        F.count("*").alias("pings")
    )

    q2 = (
        demand.writeStream.queryName("pa2_demand")
        .outputMode("complete")
        .format("delta")
        .option("checkpointLocation", DEMAND_CHECKPOINT)
        .trigger(processingTime="20 seconds")
        .start(DEMAND)
    )

    q1.awaitTermination()
    q2.awaitTermination()


if __name__ == "__main__":
    run()
