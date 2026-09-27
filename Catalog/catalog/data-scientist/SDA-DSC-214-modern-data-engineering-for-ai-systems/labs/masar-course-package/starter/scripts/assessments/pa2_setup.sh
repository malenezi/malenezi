#!/usr/bin/env bash
# PA-2 setup — build the broken streaming starting state.
#
# =============================== WARNING ==================================
# THIS SCRIPT STAGES A DELIBERATELY BROKEN ASSESSMENT ARTEFACT. The job it
# points at (src/masar/stream/ingest_gps_pa2.py) ships with four faults on
# purpose. DO NOT USE IT AS A REFERENCE.
# ==========================================================================
#
# Run before the session. Requires the standard `docker compose` Kafka + Redis
# stack up. Idempotent: the topic and sandbox are rebuilt on every run.
set -euo pipefail

TOPIC="masar.gps.pings.pa2"
SANDBOX="./lakehouse/_assessments/pa2"

# 1. Clean slate — the sandbox and its checkpoints are rebuilt every run.
rm -rf "${SANDBOX}"
docker compose exec -T kafka kafka-topics.sh --bootstrap-server localhost:9092 \
    --delete --topic "${TOPIC}" 2>/dev/null || true
docker compose exec -T kafka kafka-topics.sh --bootstrap-server localhost:9092 \
    --create --topic "${TOPIC}" --partitions 3 --replication-factor 1

# 2. Load 40,000 pings, keyed by trip_id, including the late-ping fixture.
#    gps_late_2026-06-04.ndjson contributes ~500 pings back-dated 2-47 minutes,
#    so an event-time window and a processing-time window give DIFFERENT answers.
python -m masar.stream.gps_producer \
    --topic "${TOPIC}" \
    --source data/raw/gps/gps_2026-06-01.ndjson.gz --limit 39500 --rate 0
python -m masar.stream.gps_producer \
    --topic "${TOPIC}" \
    --source data/fixtures/late_pings/gps_late_2026-06-04.ndjson --limit 0 --rate 0

# 3. Confirm the load.
docker compose exec -T kafka kafka-run-class.sh kafka.tools.GetOffsetShell \
    --bootstrap-server localhost:9092 --topic "${TOPIC}"
echo "[pa2-setup] sandbox ready; broken job at src/masar/stream/ingest_gps_pa2.py"
