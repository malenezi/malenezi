"""Rafeeq (رفيق) — Tawseel's agentic operations assistant.

Top-level package. See docs/ and SPEC.md (course build contract) for the
overall architecture. This package is split into Layer A ("core" — pure
Python/stdlib, dependency-free, importable under plain python3) and Layer B
("graph" — LangGraph/MCP, requires third-party deps not available in the
build/CI sandbox but import-guarded so it still loads).
"""
