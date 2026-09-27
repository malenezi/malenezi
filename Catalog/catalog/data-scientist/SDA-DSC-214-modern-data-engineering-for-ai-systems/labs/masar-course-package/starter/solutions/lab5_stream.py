"""Lab 5 solution — exactly-once GPS ingest and event-time windowing.

Blocks completed here:
  * ``src/masar/stream/gps_producer.py``      :: emit (the partition key)
  * ``src/masar/stream/ingest_gps_stream.py`` :: write_batch (idempotent write)
  * ``src/masar/stream/zone_demand.py``       :: the watermarked window
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from kafka import KafkaProducer
    from pyspark.sql import DataFrame


# --------------------------------------------------------------------------
# TODO(lab-5) in src/masar/stream/gps_producer.py :: emit
# --------------------------------------------------------------------------
def emit(producer: KafkaProducer, ping: dict, topic: str) -> None:
    """Send one ping, keyed by ``trip_id``.

    Kafka guarantees order WITHIN a partition, and the partition is chosen by
    ``hash(key)``. A stable ``trip_id`` key therefore puts every ping for one
    trip in one partition, in order.

    Drop the key and Kafka round-robins. The pings all still arrive — nothing
    errors, no metric moves — but "0 -> 80 -> 40 km/h" becomes an unordered
    bag of speeds, and every trajectory feature computed from it is noise.
    """
    producer.send(topic, key=ping["trip_id"], value=ping)


# --------------------------------------------------------------------------
# TODO(lab-5) in src/masar/stream/ingest_gps_stream.py :: write_batch
# --------------------------------------------------------------------------
def write_batch(batch_df: DataFrame, batch_id: int, bronze_path: str, txn_app_id: str) -> None:
    """Write one micro-batch to bronze, idempotently.

    Exactly-once is the COMPOSITION of two mechanisms, and the kill/restart
    drill exists to make both visible:

      1. **Checkpointed Kafka offsets.** On restart the query resumes from the
         last COMMITTED offset. This is what stops Spark from REPLAYING a
         batch it already wrote.

      2. **Delta's atomic per-batch commit + txnAppId/txnVersion.** If a batch
         id is replayed anyway — a restored checkpoint, a manual re-run, a
         copied checkpoint directory — Delta DROPS it. This is what stops the
         table from ACCEPTING a replay.

    Mechanism 1 without 2 is "exactly-once as long as nothing unusual happens",
    which is the definition of at-least-once. The second is one line.

    Partitioning by ``ingest_date`` (processing date, from ``_kafka_ts``) keeps
    the write local to one or two partitions per batch; partitioning bronze by
    event date would scatter every late ping across the whole table.
    """
    from pyspark.sql import functions as F

    out = (
        batch_df.withColumn("_batch_id", F.lit(batch_id).cast("long"))
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("ingest_date", F.to_date(F.col("_kafka_ts")))
    )
    (
        out.write.format("delta")
        .mode("append")
        .partitionBy("ingest_date")
        .option("txnAppId", txn_app_id)  # idempotent-write guard
        .option("txnVersion", batch_id)  # a replayed batch_id is dropped
        .option("mergeSchema", "false")  # bronze schema is fixed; drift must be visible
        .save(bronze_path)
    )


# --------------------------------------------------------------------------
# TODO(lab-5) in src/masar/stream/zone_demand.py :: run
# --------------------------------------------------------------------------
def zone_demand(events: DataFrame, window: str = "5 minutes", watermark: str = "3 minutes"):
    """Event-time windowed demand with a watermark.

    Two decisions, both load-bearing:

    **Event time, not processing time.** A ping that arrives at 08:07 about
    something that happened at 08:03 belongs in the 08:00-08:05 window.
    Aggregate on arrival and your demand curve is a picture of your consumer
    lag — and it looks perfectly reasonable, which is why nobody catches it.

    **The watermark.** ``withWatermark("event_ts", "3 minutes")`` says: wait up
    to three minutes for stragglers, then finalise the window and free its
    state. Without it the state grows forever and the job dies on a Sunday
    night. Too short and late events are silently dropped. That is the design
    trade-off, and it is yours to justify in LAB5_NOTES.md:

        watermark too short -> data loss you cannot see
        watermark too long  -> state growth and latency you can see

    Append output mode is only safe BECAUSE the watermark finalises windows —
    it is what tells Spark a window will never change again.
    """
    from pyspark.sql import functions as F

    return (
        events.withWatermark("event_ts", watermark)
        .groupBy(F.window("event_ts", window).alias("w"), F.col("vehicle_id"))
        .agg(
            F.countDistinct("trip_id").alias("trips_active"),
            F.avg("speed_kmh").alias("avg_speed_kmh"),
            F.count("*").alias("pings"),
        )
    )


#: What the restart drill proves, in the order it proves it.
RESTART_DRILL = """
1. Record the pre-kill state:
     python -m masar.tools.count --table bronze.gps_events --distinct event_id
2. Re-arm the producer so there is in-flight work to interrupt.
3. Kill the streaming job MID-BATCH (Ctrl-C during a micro-batch).
4. Restart it with no flags changed.
5. Count again.

Expected: the total continues from where it stopped, with NO duplicates. The
distinct/total gap is unchanged — it reflects the 0.4% duplicate event_id
seeded in the SOURCE, which is a data property, not a pipeline property.
Telling those two apart is the point of counting distinct as well as total.
"""

LAB5_ANSWERS = {
    "what guarantees ordering": "Per-partition order, with a stable partition key.",
    "which two mechanisms give exactly-once": (
        "Checkpointed Kafka offsets (no replay) + Delta's atomic per-batch "
        "commit with txnAppId/txnVersion (no acceptance of a replay)."
    ),
    "why event time": "So a late event counts in the window it actually belongs to.",
    "what a watermark bounds": "How long late data is awaited, and how much state is kept.",
    "can two queries share a checkpoint": "No. One checkpoint per query, always.",
}
