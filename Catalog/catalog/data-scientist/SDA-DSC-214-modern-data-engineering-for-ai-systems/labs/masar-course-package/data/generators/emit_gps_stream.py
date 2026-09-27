#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
emit_gps_stream.py — replay Masar GPS pings into Kafka for Module 5 / Lab 5.

Reads `data/raw/gps/gps_YYYY-MM-DD.ndjson[.gz]` (or any NDJSON of the same
shape) and produces to the topic `masar.gps.raw` at a controlled rate, with
optional live fault injection.

    # normal replay: 500 events/s, 60x wall-clock speedup
    python3 emit_gps_stream.py --date 2026-06-01 --rate 500 --speedup 60

    # the streaming-lab faults
    python3 emit_gps_stream.py --date 2026-06-05 --inject late,dupes,unit-shift

    # no broker on the machine? it still runs — writes NDJSON instead
    python3 emit_gps_stream.py --date 2026-06-01 --sink file --out ./replay.ndjson
    python3 emit_gps_stream.py --date 2026-06-01 --sink stdout | head

The Kafka path needs `kafka-python` (`pip install kafka-python`). If the library
is missing OR no broker answers, the producer **falls back to stdout/a file**,
prints a clear notice, and the lab continues — the exercise is about event time
and watermarks, and it must not be blocked by a docker-compose that did not boot.

Message contract
----------------
    topic  : masar.gps.raw
    key    : vehicle_id   (co-partitions a vehicle's pings -> per-vehicle order)
    value  : the raw ping JSON, unchanged, incl. `producer_version`
    headers: masar-replay=1, masar-inject=<flags>

Keying on `vehicle_id` (not `trip_id`) is deliberate: it keeps a vehicle's
telemetry in one partition so per-vehicle ordering survives, while still spreading
load. Lab 5 asks participants to justify this choice.
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import random
import sys
import time
from collections import deque

DEFAULT_TOPIC = "masar.gps.raw"
DEFAULT_BOOTSTRAP = "localhost:9092"
VALID_INJECTIONS = {"late", "dupes", "unit-shift", "drop", "none"}


# --------------------------------------------------------------------------
def open_ndjson(path: str):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, "r", encoding="utf-8")


def resolve_source(args) -> str:
    if args.file:
        if not os.path.exists(args.file):
            raise SystemExit(f"ERROR: --file {args.file} does not exist")
        return args.file
    base = os.path.join(args.raw, "gps", f"gps_{args.date}.ndjson")
    for cand in (base, base + ".gz"):
        if os.path.exists(cand):
            return cand
    raise SystemExit(
        f"ERROR: no GPS file for {args.date} under {os.path.join(args.raw, 'gps')}.\n"
        f"       Run:  python3 generate_masar.py --start {args.date} --days 1 "
        f"--out {args.raw} --scale 0.15 --gzip-gps")


# --------------------------------------------------------------------------
# Sinks
# --------------------------------------------------------------------------
class Sink:
    name = "abstract"

    def send(self, key: str, value: dict, headers: list[tuple[str, bytes]]) -> None:
        raise NotImplementedError

    def close(self) -> None:
        pass


class KafkaSink(Sink):
    name = "kafka"

    def __init__(self, bootstrap: str, topic: str, acks: str, timeout_ms: int):
        from kafka import KafkaProducer  # imported lazily on purpose
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap.split(","),
            key_serializer=lambda k: k.encode("utf-8"),
            value_serializer=lambda v: json.dumps(v, ensure_ascii=False,
                                                  separators=(",", ":")).encode("utf-8"),
            acks=acks if acks != "all" else "all",
            linger_ms=20,
            retries=3,
            request_timeout_ms=timeout_ms,
            api_version_auto_timeout_ms=timeout_ms,
            max_block_ms=timeout_ms,
        )

    def send(self, key, value, headers):
        self.producer.send(self.topic, key=key, value=value, headers=headers)

    def close(self):
        self.producer.flush(timeout=20)
        self.producer.close(timeout=20)


class StreamSink(Sink):
    """Fallback: NDJSON to a file or stdout. Same bytes Kafka would have carried."""

    def __init__(self, handle, name: str):
        self.fh = handle
        self.name = name

    def send(self, key, value, headers):
        self.fh.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")))
        self.fh.write("\n")

    def close(self):
        try:
            self.fh.flush()
        except Exception:
            pass
        if self.fh not in (sys.stdout, sys.stderr):
            self.fh.close()


def build_sink(args) -> Sink:
    """Kafka if asked for and reachable; otherwise degrade loudly but gracefully."""
    want_kafka = args.sink in ("kafka", "auto")
    if want_kafka:
        try:
            sink = KafkaSink(args.bootstrap, args.topic, args.acks, args.timeout_ms)
            print(f"[sink] kafka  bootstrap={args.bootstrap}  topic={args.topic}",
                  file=sys.stderr)
            return sink
        except ImportError:
            msg = ("kafka-python is not installed  (pip install kafka-python)")
        except Exception as exc:  # NoBrokersAvailable, DNS, auth, ...
            msg = f"no Kafka broker reachable at {args.bootstrap}: {type(exc).__name__}: {exc}"
        if args.sink == "kafka":
            raise SystemExit(f"ERROR: --sink kafka was requested but {msg}")
        print(f"[sink] FALLBACK — {msg}", file=sys.stderr)
        print("[sink] the lab continues: writing NDJSON instead of producing to Kafka.",
              file=sys.stderr)

    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
        fh = open(args.out, "w", encoding="utf-8")
        print(f"[sink] file   {os.path.abspath(args.out)}", file=sys.stderr)
        return StreamSink(fh, "file")
    print("[sink] stdout", file=sys.stderr)
    return StreamSink(sys.stdout, "stdout")


# --------------------------------------------------------------------------
# Fault injection
# --------------------------------------------------------------------------
class Injector:
    """Live versions of the fixtures in ../fixtures, applied during replay.

    late       hold ~1.5% of events back and release them minutes later, so an
               event-time window has already closed when they arrive.
    dupes      re-emit ~0.4% of events verbatim (same event_id).
    unit-shift THE signature incident: from --unit-shift-after onwards, ~34% of
               vehicles switch to producer_version 2.5.0 and report speed_kmh in
               METRES PER SECOND. Type-compatible, semantically wrong.
    drop       silently discard ~0.2% of events (a lossy device buffer).
    """

    def __init__(self, flags: set[str], rng: random.Random, args):
        self.flags = flags
        self.rng = rng
        self.args = args
        self.delayed: deque = deque()
        self.counts = {"late": 0, "dupes": 0, "unit_shift": 0, "drop": 0}
        self._n = 0

    def _affected_vehicle(self, vehicle_id: str) -> bool:
        return (hash((vehicle_id, "v250")) % 100) < self.args.unit_shift_fleet_pct

    def process(self, ev: dict) -> list[dict]:
        """Return the list of events to emit *now* for this input event."""
        self._n += 1
        out: list[dict] = []

        # release anything whose hold has expired
        while self.delayed and self.delayed[0][0] <= self._n:
            _, held = self.delayed.popleft()
            out.append(held)

        if "drop" in self.flags and self.rng.random() < self.args.drop_rate:
            self.counts["drop"] += 1
            return out

        # instructional metadata from the late_pings fixture is not part of the contract
        ev.pop("_note_delay_seconds", None)

        if "unit-shift" in self.flags:
            ts_hour = int(ev["ts"][11:13]) if len(ev.get("ts", "")) >= 13 else 0
            if ts_hour >= self.args.unit_shift_after and self._affected_vehicle(ev["vehicle_id"]):
                ev["payload"]["speed_kmh"] = round(float(ev["payload"]["speed_kmh"]) / 3.6, 2)
                ev["producer_version"] = "2.5.0"
                self.counts["unit_shift"] += 1

        if "late" in self.flags and self.rng.random() < self.args.late_rate:
            hold_for = self.rng.randrange(self.args.late_min_events,
                                          self.args.late_max_events)
            self.delayed.append((self._n + hold_for, ev))
            self.counts["late"] += 1
            return out

        out.append(ev)

        if "dupes" in self.flags and self.rng.random() < self.args.dup_rate:
            out.append(json.loads(json.dumps(ev)))
            self.counts["dupes"] += 1
        return out

    def drain(self) -> list[dict]:
        rest = [e for _, e in self.delayed]
        self.delayed.clear()
        return rest


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Replay Masar GPS pings to Kafka topic masar.gps.raw.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    src = p.add_argument_group("source")
    src.add_argument("--raw", default="../raw")
    src.add_argument("--date", default="2026-06-01", help="which gps_<date>.ndjson to replay")
    src.add_argument("--file", default=None, help="replay this NDJSON file instead")
    src.add_argument("--limit", type=int, default=0, help="stop after N events (0 = all)")
    src.add_argument("--loop", action="store_true", help="restart at EOF (endless stream)")

    snk = p.add_argument_group("sink")
    snk.add_argument("--sink", choices=["auto", "kafka", "file", "stdout"], default="auto",
                     help="'auto' tries Kafka and falls back to file/stdout")
    snk.add_argument("--bootstrap", default=os.environ.get("KAFKA_BOOTSTRAP", DEFAULT_BOOTSTRAP))
    snk.add_argument("--topic", default=DEFAULT_TOPIC)
    snk.add_argument("--acks", default="all", choices=["0", "1", "all"])
    snk.add_argument("--timeout-ms", type=int, default=5000)
    snk.add_argument("--out", default=None, help="fallback/file-sink output path")

    pace = p.add_argument_group("pacing")
    pace.add_argument("--rate", type=float, default=500.0,
                      help="hard ceiling in events/second (0 = unthrottled)")
    pace.add_argument("--speedup", type=float, default=60.0,
                      help="event-time speedup: 60 = one hour of pings per minute; "
                           "0 = ignore event time and just use --rate")

    inj = p.add_argument_group("fault injection")
    inj.add_argument("--inject", default="",
                     help="comma-separated: late,dupes,unit-shift,drop (or none)")
    inj.add_argument("--late-rate", type=float, default=0.015)
    inj.add_argument("--late-min-events", type=int, default=2_000)
    inj.add_argument("--late-max-events", type=int, default=20_000)
    inj.add_argument("--dup-rate", type=float, default=0.004)
    inj.add_argument("--drop-rate", type=float, default=0.002)
    inj.add_argument("--unit-shift-after", type=int, default=9,
                     help="UTC hour from which producer_version 2.5.0 appears")
    inj.add_argument("--unit-shift-fleet-pct", type=int, default=34)
    inj.add_argument("--seed", type=int, default=20260601)

    p.add_argument("--progress-every", type=int, default=25_000)
    args = p.parse_args(argv)

    flags = {f.strip() for f in args.inject.split(",") if f.strip()}
    flags.discard("none")
    bad = flags - VALID_INJECTIONS
    if bad:
        raise SystemExit(f"ERROR: unknown --inject flag(s): {', '.join(sorted(bad))}. "
                         f"Valid: {', '.join(sorted(VALID_INJECTIONS))}")

    path = resolve_source(args)
    rng = random.Random(args.seed)
    injector = Injector(flags, rng, args)
    sink = build_sink(args)

    print(f"[src ] {path}", file=sys.stderr)
    print(f"[pace] rate<={args.rate or '∞'} ev/s   event-time speedup={args.speedup or 'off'}x",
          file=sys.stderr)
    if flags:
        print(f"[inj ] {', '.join(sorted(flags))}", file=sys.stderr)

    headers = [("masar-replay", b"1"),
               ("masar-inject", ",".join(sorted(flags)).encode("utf-8") or b"none")]

    sent = 0
    read = 0
    t0 = time.monotonic()
    first_event_epoch: float | None = None
    min_interval = 1.0 / args.rate if args.rate > 0 else 0.0
    next_slot = time.monotonic()

    def parse_epoch(ts: str) -> float | None:
        # "2026-06-01T05:12:33Z"
        try:
            import datetime as _dt
            return _dt.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=_dt.timezone.utc).timestamp()
        except Exception:
            return None

    try:
        while True:
            with open_ndjson(path) as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        ev = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    read += 1

                    # ---- event-time pacing -------------------------------
                    if args.speedup and args.speedup > 0:
                        ep = parse_epoch(ev.get("ts", ""))
                        if ep is not None:
                            if first_event_epoch is None:
                                first_event_epoch = ep
                            target = t0 + (ep - first_event_epoch) / args.speedup
                            delay = target - time.monotonic()
                            if delay > 0:
                                time.sleep(min(delay, 5.0))

                    for out_ev in injector.process(ev):
                        # ---- rate ceiling --------------------------------
                        if min_interval:
                            now = time.monotonic()
                            if now < next_slot:
                                time.sleep(next_slot - now)
                                now = next_slot
                            next_slot = max(now, next_slot) + min_interval
                        sink.send(out_ev["vehicle_id"], out_ev, headers)
                        sent += 1

                    if args.progress_every and sent and sent % args.progress_every == 0:
                        el = time.monotonic() - t0
                        print(f"[.... ] read={read:,} sent={sent:,} "
                              f"({sent / max(el, 1e-6):,.0f} ev/s)", file=sys.stderr)
                    if args.limit and read >= args.limit:
                        raise StopIteration
            if not args.loop:
                break
            first_event_epoch = None
            t0 = time.monotonic()
    except (KeyboardInterrupt, StopIteration):
        print("[stop] interrupted — flushing", file=sys.stderr)
    finally:
        for ev in injector.drain():
            sink.send(ev["vehicle_id"], ev, headers)
            sent += 1
        sink.close()

    elapsed = time.monotonic() - t0
    print("-" * 72, file=sys.stderr)
    print(f"[done] sink={sink.name} topic={args.topic if sink.name == 'kafka' else '-'}",
          file=sys.stderr)
    print(f"[done] read={read:,}  sent={sent:,}  in {elapsed:,.1f}s "
          f"({sent / max(elapsed, 1e-6):,.0f} ev/s)", file=sys.stderr)
    if flags:
        print(f"[done] injected: held-late={injector.counts['late']:,}  "
              f"duplicated={injector.counts['dupes']:,}  "
              f"unit-shifted={injector.counts['unit_shift']:,}  "
              f"dropped={injector.counts['drop']:,}", file=sys.stderr)
    print("-" * 72, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
