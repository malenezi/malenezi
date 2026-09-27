"""Kafka ``masar.gps.pings`` -> ``bronze.gps_events``, exactly-once.

Exactly-once is not a feature you switch on. It is the composition of two
mechanisms, and Lab 5's kill/restart drill exists to make you see both:

  1. **Kafka offsets recorded in the query CHECKPOINT.** On restart the query
     resumes from the last COMMITTED offset, not from wherever the consumer
     group happens to be.
  2. **Delta's atomic per-micro-batch commit**, made idempotent with
     ``txnAppId``/``txnVersion``: replaying a batch id that already committed
     is dropped by the table, not written twice.

Kill the job mid-batch and the batch either committed fully or not at all.

One checkpoint per query. Sharing a checkpoint between two queries is the
single most effective way to corrupt a stream.

CLI::

    python -m masar.stream.ingest_gps_stream
    python -m masar.stream.ingest_gps_stream --starting-offsets latest --once
"""

from __future__ import annotations

import argparse
from typing import TYPE_CHECKING

from masar import config
from masar.spark import get_spark

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

TOPIC = config.KAFKA_TOPIC
BOOTSTRAP = config.KAFKA_BOOTSTRAP
BRONZE_PATH = config.TABLES["bronze.gps_events"].path
CHECKPOINT = f"{config.CHECKPOINTS}/gps_events_bronze"  # ONE per query. Sacred.
TXN_APP_ID = "masar_gps_events_bronze"


def ping_schema():
    """The wire schema — EXACTLY ``data/raw/gps/gps_YYYY-MM-DD.ndjson``.

    Declared, not inferred. Schema inference on a stream means the schema can
    change between micro-batches without anyone noticing, which is how the
    2.5.0 incident would have arrived silently AND unlogged.
    """
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
            StructField("ts", TimestampType()),  # EVENT time, from the device
            StructField("payload", payload),
            StructField("producer_version", StringType()),
        ]
    )


def parse(raw: DataFrame) -> DataFrame:
    """Parse Kafka records into the bronze shape, keeping BOTH clocks.

    ``ts`` is event time (when the device says it happened);
    ``_kafka_ts`` is processing time (when the platform saw it). Their
    difference is the lateness that Module 5's watermark reasons about, and
    you cannot compute it after throwing one of them away.
    """
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
        F.col("p.ts").alias("ts"),  # keep the raw event time verbatim
        F.col("p.payload").alias("payload"),  # bronze keeps the struct AS RECEIVED
        F.col("p.producer_version").alias("producer_version"),
        F.col("_kafka_ts"),
        F.concat_ws("/", F.lit("kafka:/"), F.col("topic"), F.col("partition").cast("string")).alias(
            "_source_file"
        ),
        F.col("offset").alias("_kafka_offset"),
    )


def write_batch(batch_df: DataFrame, batch_id: int) -> None:
    """Write one micro-batch to bronze, idempotently.

    ``foreachBatch`` hands us the batch id, and we use it twice:
      * as the bronze lineage column ``_batch_id``;
      * as Delta's ``txnVersion``, so a replayed batch id is dropped by the
        table rather than appended a second time.
    """
    from pyspark.sql import functions as F

    out = (
        batch_df.withColumn("_batch_id", F.lit(batch_id).cast("long"))
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("ingest_date", F.to_date(F.col("_kafka_ts")))
    )

    # ── TODO(lab-5): make the batch write idempotent ──────────────────────
    #   What : append `out` to BRONZE_PATH partitioned by ingest_date, with
    #          txnAppId=TXN_APP_ID and txnVersion=batch_id.
    #   Why  : the checkpoint stops Spark REPLAYING a committed batch; the
    #          txn options stop DELTA accepting one if it is replayed anyway
    #          (a restored checkpoint, a manual re-run). Belt and braces, and
    #          the braces are one line.
    #   Ref  : solutions/lab5_stream.py :: write_batch
    (
        out.write.format("delta")
        .mode("append")
        .partitionBy("ingest_date")
        .option("txnAppId", TXN_APP_ID)
        .option("txnVersion", batch_id)
        .option("mergeSchema", "false")  # bronze schema is fixed; drift must be visible
        .save(BRONZE_PATH)
    )
    # ── end TODO(lab-5) ───────────────────────────────────────────────────

    print(f"Batch {batch_id}: appended {out.count():,} pings", flush=True)


def run(
    starting_offsets: str = "earliest",
    trigger_seconds: int = 30,
    once: bool = False,
    bootstrap: str = BOOTSTRAP,
    topic: str = TOPIC,
) -> None:
    """Start the streaming ingest and block until it is stopped.

    Args:
        starting_offsets: ``earliest`` on a first run; the checkpoint wins on
            every subsequent run, which is exactly the point.
        trigger_seconds: micro-batch interval. Smaller means lower latency and
            more small files — the trade-off Lab 5 Task 5 measures.
        once: run a single micro-batch and exit (handy in CI).
        bootstrap: broker address.
        topic: source topic.
    """
    spark = get_spark("masar-gps-events-bronze", kafka=True)
    raw = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", bootstrap)
        .option("subscribe", topic)
        .option("startingOffsets", starting_offsets)
        .option("maxOffsetsPerTrigger", 20_000)  # bounded batch => predictable latency
        .option("failOnDataLoss", "true")  # surface retention gaps loudly
        .load()
    )

    writer = (
        parse(raw)
        .writeStream.queryName("gps_events_bronze")
        .foreachBatch(write_batch)
        .outputMode("append")
        .option("checkpointLocation", CHECKPOINT)
    )
    trigger = {"availableNow": True} if once else {"processingTime": f"{trigger_seconds} seconds"}
    writer.trigger(**trigger).start().awaitTermination()


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Kafka -> bronze.gps_events, exactly-once")
    p.add_argument("--starting-offsets", default="earliest", choices=["earliest", "latest"])
    p.add_argument("--trigger-seconds", type=int, default=30)
    p.add_argument("--once", action="store_true", help="drain available data then stop")
    p.add_argument("--bootstrap", default=BOOTSTRAP)
    p.add_argument("--topic", default=TOPIC)
    a = p.parse_args()
    run(a.starting_offsets, a.trigger_seconds, a.once, a.bootstrap, a.topic)


if __name__ == "__main__":
    main()
