"""Rafeeq adapters (Layer A). Mock Tawseel backends over the JSON/JSONL
seed data in data/. Dependency-free, in-memory, mutable, with reset() and
snapshot()/restore() so TawseelBench (M3/evaluations) can set environment
state per scenario without touching a real API."""
