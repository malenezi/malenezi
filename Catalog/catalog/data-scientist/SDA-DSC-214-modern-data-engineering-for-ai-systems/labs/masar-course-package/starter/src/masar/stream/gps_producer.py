"""Replay Masar GPS pings into Kafka at a controllable rate.

Key = ``trip_id``. That single choice is what gives ordering: Kafka guarantees
order WITHIN a partition, and a stable key sends every ping for one trip to
one partition. Without a key the producer round-robins and per-trip order is
lost — the pings still all arrive, but "the vehicle went 0 -> 80 -> 40 km/h"
becomes an unordered bag of speeds.

CLI::

    python -m masar.stream.gps_producer --limit 50000 --rate 2000
    python -m masar.stream.gps_producer --source data/raw/gps/gps_2026-06-05.ndjson.gz
"""

from __future__ import annotations

import argparse
import glob
import gzip
import io
import json
import sys
import time
from pathlib import Path
from typing import TYPE_CHECKING

from masar import config

if TYPE_CHECKING:  # pragma: no cover
    from kafka import KafkaProducer

TOPIC = config.KAFKA_TOPIC
BOOTSTRAP = config.KAFKA_BOOTSTRAP


def make_producer(bootstrap: str = BOOTSTRAP) -> KafkaProducer:
    """Build a durable, modestly batched producer.

    ``acks="all"`` waits for the replicas, which on a single-broker classroom
    cluster costs almost nothing and keeps the semantics honest.
    ``linger_ms=20`` batches for 20 ms; setting it to 0 sends one request per
    ping and turns a 50,000-ping replay into 50,000 round trips.
    """
    from kafka import KafkaProducer

    return KafkaProducer(
        bootstrap_servers=bootstrap,
        key_serializer=lambda k: k.encode("utf-8"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        acks="all",
        linger_ms=20,
        retries=5,
    )


def emit(producer: KafkaProducer, ping: dict, topic: str = TOPIC) -> None:
    """Send one ping, keyed by ``trip_id``.

    Ping shape (``data/raw/gps/gps_YYYY-MM-DD.ndjson``)::

        {"event_id", "vehicle_id", "driver_id", "trip_id", "ts",
         "payload": {"lat","lon","speed_kmh","heading_deg","accuracy_m"},
         "producer_version"}
    """
    # ── TODO(lab-5): key the message so per-trip order survives ───────────
    #   What : send `ping` to `topic` with key=ping["trip_id"].
    #   Why  : the partition is chosen by hash(key). One trip -> one
    #          partition -> strict order. Drop the key and Kafka round-robins;
    #          the pings arrive, but the sequence that makes them a TRAJECTORY
    #          does not.
    #   Ref  : solutions/lab5_stream.py :: emit
    producer.send(topic, key=ping["trip_id"], value=ping)
    # ── end TODO(lab-5) ───────────────────────────────────────────────────


def _open_source(path: str):
    """Open an NDJSON source, transparently handling ``.gz``.

    Accepts a glob so ``--source 'data/raw/gps/gps_2026-06-*'`` works; the
    course ships the GPS feed gzipped and the labs refer to it by either name.
    """
    matches = sorted(glob.glob(path)) or sorted(glob.glob(f"{path}*"))
    if not matches:
        raise FileNotFoundError(f"no GPS source matched {path!r}")
    chosen = matches[0]
    if chosen.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(chosen, "rb"), encoding="utf-8"), chosen
    return Path(chosen).open(encoding="utf-8"), chosen


def replay(
    path: str,
    rate_hz: float = 2000.0,
    limit: int | None = 50_000,
    topic: str = TOPIC,
    bootstrap: str = BOOTSTRAP,
) -> int:
    """Replay an NDJSON GPS file into Kafka.

    Args:
        path: NDJSON source (``.ndjson`` or ``.ndjson.gz``, glob allowed).
        rate_hz: pings per second; ``0`` means as fast as the broker accepts.
        limit: stop after this many pings; ``None`` for the whole file.
        topic: Kafka topic.
        bootstrap: broker address.

    Returns:
        Number of pings sent.
    """
    producer = make_producer(bootstrap)
    handle, chosen = _open_source(path)
    delay = 0.0 if rate_hz <= 0 else 1.0 / rate_hz
    sent = 0
    try:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            emit(producer, json.loads(line), topic)
            sent += 1
            if sent % 1000 == 0:
                print(f"  … {sent:>7,} pings sent", flush=True)
            if limit and sent >= limit:
                break
            if delay:
                time.sleep(delay)
    finally:
        handle.close()
        producer.flush()
    print(f"[producer] {sent:,} pings -> {topic} from {Path(chosen).name}")
    return sent


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Replay Masar GPS pings into Kafka")
    p.add_argument("--source", default=f"{config.RAW_ROOT}/gps/gps_{config.BUSINESS_DATE}.ndjson*")
    p.add_argument("--rate", type=float, default=2000.0, help="pings/sec; 0 = unthrottled")
    p.add_argument("--limit", type=int, default=50_000, help="0 = whole file")
    p.add_argument("--topic", default=TOPIC)
    p.add_argument("--bootstrap", default=BOOTSTRAP)
    a = p.parse_args()
    sent = replay(a.source, a.rate, a.limit or None, a.topic, a.bootstrap)
    sys.exit(0 if sent else 1)


if __name__ == "__main__":
    main()
