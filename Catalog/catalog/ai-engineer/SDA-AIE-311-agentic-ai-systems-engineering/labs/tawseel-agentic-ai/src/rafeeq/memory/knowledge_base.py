"""Module 4 — the Tawseel policy knowledge base as versioned long-term memory.

Policies are retrievable long-term memory, not a frozen prompt block: a
policy edit propagates the moment `seed_kb()` re-ingests it, with no model
retraining and no prompt redeploy. `policy_context()` retrieves the
CURRENT version only (`rafeeq.core.config.CURRENT_POLICY_VERSION`) — a
superseded policy is worse than no policy at all (Module 4's stale-memory
failure mode, made concrete): confidently quoting last year's 300 SAR
refund limit is a silent-wrongness bug, not a crash, so nothing here ever
retrieves `SUPERSEDED_POLICY_VERSION` content without the caller asking
for it explicitly (`policy_context_including_superseded`, used ONLY by
the stale-policy demo/tests, never by a normal answer path).

Built on `rafeeq.memory.vector_store.get_store()` — dependency-free by
default (SPEC §1), same as `long_term.py`, but a SEPARATE collection: KB
content is not personal data, and separating it from `long_term.py`'s
PII-bearing customer-memory collection is exactly the governance split
Module 4's production notes call for.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from rafeeq.core.config import CURRENT_POLICY_VERSION, POLICIES_DIR, SUPERSEDED_POLICY_VERSION
from rafeeq.memory.vector_store import Document, get_store

POLICY_KB_COLLECTION = "tawseel_policies"

_store_cache: dict[str, Any] = {}

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
_FIELD_RE = re.compile(r'^([A-Za-z_]+):\s*(.*)$')


def _kb_store() -> Any:
    store = _store_cache.get(POLICY_KB_COLLECTION)
    if store is None:
        store = get_store(POLICY_KB_COLLECTION)
        _store_cache[POLICY_KB_COLLECTION] = store
    return store


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse the small YAML-ish frontmatter block every `data/policies/**`
    file carries (`policy_version`, `locale`, `effective_from`,
    `supersedes`). Deliberately NOT a real YAML parser (no dependency
    beyond stdlib `re`) — the frontmatter shape is simple and fixed, one
    `key: value` pair per line, values optionally quoted or `null`."""
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    raw_fields, body = match.group(1), match.group(2)
    fields: dict[str, str] = {}
    for line in raw_fields.splitlines():
        line = line.strip()
        if not line:
            continue
        field_match = _FIELD_RE.match(line)
        if not field_match:
            continue
        key, value = field_match.group(1), field_match.group(2).strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value == "null":
            value = ""
        fields[key] = value
    return fields, body.strip()


def _chunk(body: str, max_chars: int = 1200) -> list[str]:
    """Split a policy document into retrieval-sized chunks on markdown
    `##` section boundaries, falling back to a single chunk for a short
    document. Simple and dependency-free — a real production KB would use
    a smarter splitter, but chunk boundaries are not this module's
    teaching point (versioning and version-filtered retrieval are)."""
    sections = re.split(r"\n(?=## )", body)
    chunks: list[str] = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        if len(section) <= max_chars:
            chunks.append(section)
        else:
            for i in range(0, len(section), max_chars):
                chunks.append(section[i:i + max_chars])
    return chunks or ([body.strip()] if body.strip() else [])


def seed_kb(policies_dir: Path = POLICIES_DIR) -> dict[str, int]:
    """Ingest every `data/policies/**/*.md` file into the KB vector store,
    tagging each chunk with `policy_version`/`locale` metadata read from
    its own frontmatter — INCLUDING the superseded 2026.1 set
    (`data/policies/superseded/{en,ar}/*.md`), so the stale-policy demo
    (retrieve without a version filter -> get the wrong threshold; filter
    on `CURRENT_POLICY_VERSION` -> get the right one) is reproducible
    against real ingested documents, not a hand-built fixture.

    Idempotent-ish for a lab/demo: re-running clears the collection first
    (`reset()`) rather than accumulating duplicate chunks on every re-seed.
    Returns a small summary (`{"documents": N, "chunks": M, "current": C,
    "superseded": S}`) for a quick sanity check after seeding.
    """
    store = _kb_store()
    store.reset()

    documents = 0
    chunks_total = 0
    current_count = 0
    superseded_count = 0

    for path in sorted(policies_dir.rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fields, body = _parse_frontmatter(raw)
        policy_version = fields.get("policy_version", "")
        locale = fields.get("locale", "")
        if not policy_version or not locale:
            continue  # not a versioned policy doc (e.g. a README) - skip, don't guess
        documents += 1
        docs_for_file = []
        for idx, chunk in enumerate(_chunk(body)):
            docs_for_file.append(Document(page_content=chunk, metadata={
                "policy_version": policy_version,
                "locale": locale,
                "effective_from": fields.get("effective_from", ""),
                "supersedes": fields.get("supersedes", ""),
                "source_path": str(path.relative_to(policies_dir)),
                "chunk_index": idx,
            }))
        if docs_for_file:
            store.add_documents(docs_for_file)
            chunks_total += len(docs_for_file)
            if policy_version == CURRENT_POLICY_VERSION:
                current_count += len(docs_for_file)
            elif policy_version == SUPERSEDED_POLICY_VERSION:
                superseded_count += len(docs_for_file)

    return {
        "documents": documents, "chunks": chunks_total,
        "current_version_chunks": current_count,
        "superseded_version_chunks": superseded_count,
    }


def policy_context(question: str, locale: str, k: int = 3) -> str:
    """Retrieve the CURRENT policy version ONLY, filtered by
    `policy_version` and `locale` BEFORE ranking (Module 4's metadata-
    filter-first rule) — refuses to surface `SUPERSEDED_POLICY_VERSION`
    content under any circumstance. Returns `"NO_POLICY_FOUND"` (a
    sentinel, not an exception — SPEC §7's "errors are return values"
    idea applied to retrieval) when nothing matches, so a caller can
    detect an empty KB rather than silently grounding on nothing."""
    hits = _kb_store().similarity_search(question, k=k, filter={
        "policy_version": CURRENT_POLICY_VERSION, "locale": locale,
    })
    return "\n\n".join(h.page_content for h in hits) or "NO_POLICY_FOUND"


def policy_context_including_superseded(question: str, locale: str, k: int = 3) -> list[dict[str, Any]]:
    """DEMO/TEST ONLY — deliberately skips the version filter so the
    stale-memory failure mode is reproducible: without a `policy_version`
    filter, a semantically similar SUPERSEDED chunk can rank above the
    current one. Never call this from a normal answer path; it exists so
    `tests/unit` and the classroom demo can show the failure `policy_context`
    is built to prevent."""
    hits = _kb_store().similarity_search_with_score(question, k=k, filter={"locale": locale})
    return [{"content": doc.page_content, "metadata": doc.metadata, "score": score} for doc, score in hits]
