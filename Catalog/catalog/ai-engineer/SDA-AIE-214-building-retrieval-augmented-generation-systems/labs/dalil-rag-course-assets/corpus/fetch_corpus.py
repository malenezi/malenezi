#!/usr/bin/env python3
"""
fetch_corpus.py -- resolve and download Layer A of the Dalil corpus.

SDA-AIE-214 -- Building Retrieval-Augmented Generation Systems, SDAIA Academy.

Design notes for the course team
--------------------------------
This script is deliberately defensive, because government publication pages
move. For each manifest entry it tries, in order:

    1. every URL in `url_candidates` (HEAD, then GET)
    2. link discovery on the manifest's `discovery_pages` -- matching the
       document's English and Arabic titles against anchor text and href
    3. gives up on that entry, records status=UNRESOLVED, and CONTINUES

A partially resolved Layer A is a normal, supported state: Layer B guarantees
the corpus floor, and `validate_corpus.py` reports whether the resolved subset
still meets the coverage targets the labs depend on.

Every successful fetch is recorded in corpus/LOCK.json with a SHA-256 hash, the
resolved URL, byte size, page count and fetch timestamp. Commit LOCK.json.
Cohorts that index different bytes cannot compare benchmark numbers.

Usage
-----
    python corpus/fetch_corpus.py                       # resolve + download
    python corpus/fetch_corpus.py --dry-run             # resolve only
    python corpus/fetch_corpus.py --verify              # re-check LOCK hashes
    python corpus/fetch_corpus.py --only pdpl-law,ai-ethics-principles
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, unquote

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml is required:  pip install pyyaml")

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("requests is required:  pip install requests")

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "corpus" / "manifest" / "sdaia_layer_a.yaml"
DEFAULT_OUT = ROOT / "data" / "corpus" / "layer_a"
LOCK_PATH = ROOT / "corpus" / "LOCK.json"

UA = "SDAIA-Academy-SDA-AIE-214-CourseCorpusFetcher/1.0 (training use)"
TIMEOUT = 45
RETRIES = 3
POLITE_DELAY = 1.5          # seconds between requests -- be a good citizen


@dataclass
class FetchResult:
    id: str
    status: str                      # OK | UNRESOLVED | ERROR | SKIPPED
    resolved_url: str | None = None
    path: str | None = None
    sha256: str | None = None
    bytes: int = 0
    language: str | None = None
    fetched_at: str | None = None
    detail: str = ""
    tried: list[str] = field(default_factory=list)


def load_manifest(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "*/*"})
    return s


def _get(s: requests.Session, url: str, stream: bool = False):
    last = None
    for attempt in range(RETRIES):
        try:
            r = s.get(url, timeout=TIMEOUT, stream=stream, allow_redirects=True)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
        except requests.RequestException as exc:
            last = type(exc).__name__
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(last or "unknown error")


def looks_like_pdf(resp) -> bool:
    ctype = resp.headers.get("Content-Type", "").lower()
    if "pdf" in ctype:
        return True
    head = resp.content[:5] if not resp.raw.isclosed() else b""
    return head.startswith(b"%PDF")


# --------------------------------------------------------------------------
# link discovery -- the fallback when canonical URLs have moved
# --------------------------------------------------------------------------
ANCHOR_RE = re.compile(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")


def normalise(text: str) -> str:
    text = TAG_RE.sub(" ", text)
    text = unquote(text)
    text = re.sub(r"[ـ\s_%\-]+", " ", text)       # tatweel, ws, separators
    return re.sub(r"\s+", " ", text).strip().lower()


def discover(s: requests.Session, pages: Iterable[str], titles: list[str]) -> str | None:
    """Scan index pages for an anchor whose text or href matches a title."""
    wanted = [normalise(t) for t in titles if t]
    for page in pages:
        try:
            resp = _get(s, page)
        except RuntimeError:
            continue
        html = resp.text
        for href, label in ANCHOR_RE.findall(html):
            hay = normalise(label) + " " + normalise(href)
            for w in wanted:
                # match on the distinctive head of the title (first 4 words)
                key = " ".join(w.split()[:4])
                if key and key in hay and (".pdf" in href.lower() or "document" in href.lower()):
                    return urljoin(page, href)
        time.sleep(POLITE_DELAY)
    return None


def resolve_one(s: requests.Session, doc: dict, discovery_pages: list[str]) -> tuple[str | None, list[str]]:
    tried: list[str] = []
    for url in doc.get("url_candidates", []):
        tried.append(url)
        try:
            r = _get(s, url, stream=True)
            r.close()
            return url, tried
        except RuntimeError:
            time.sleep(POLITE_DELAY)
    found = discover(s, discovery_pages, [doc.get("title_en", ""), doc.get("title_ar", "")])
    if found:
        tried.append(f"(discovered) {found}")
        return found, tried
    return None, tried


def download(s: requests.Session, url: str, dest: Path) -> tuple[str, int]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = _get(s, url, stream=True)
    h = hashlib.sha256()
    total = 0
    with dest.open("wb") as fh:
        for chunk in r.iter_content(65536):
            if not chunk:
                continue
            fh.write(chunk)
            h.update(chunk)
            total += len(chunk)
    return h.hexdigest(), total


def page_count(path: Path) -> int | None:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    try:
        with fitz.open(path) as doc:
            return doc.page_count
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--lock", type=Path, default=LOCK_PATH)
    ap.add_argument("--only", help="comma-separated document ids")
    ap.add_argument("--dry-run", action="store_true", help="resolve URLs, download nothing")
    ap.add_argument("--verify", action="store_true", help="re-hash local files against LOCK.json")
    args = ap.parse_args()

    manifest = load_manifest(args.manifest)
    docs = manifest["documents"]
    if args.only:
        keep = {x.strip() for x in args.only.split(",")}
        docs = [d for d in docs if d["id"] in keep]

    if args.verify:
        return verify(args.lock)

    s = session()
    discovery_pages = manifest.get("discovery_pages", [])
    results: list[FetchResult] = []

    for doc in docs:
        did = doc["id"]
        print(f"[..] {did}", flush=True)
        url, tried = resolve_one(s, doc, discovery_pages)
        if url is None:
            results.append(FetchResult(did, "UNRESOLVED", tried=tried,
                                       detail="no candidate resolved and discovery found nothing"))
            print(f"[!!] {did}: UNRESOLVED  (tried {len(tried)})")
            continue
        if args.dry_run:
            results.append(FetchResult(did, "SKIPPED", resolved_url=url, tried=tried,
                                       detail="dry-run"))
            print(f"[ok] {did}: resolved -> {url}")
            continue
        dest = args.out / f"{did}.pdf"
        try:
            sha, size = download(s, url, dest)
        except RuntimeError as exc:
            results.append(FetchResult(did, "ERROR", resolved_url=url, tried=tried, detail=str(exc)))
            print(f"[!!] {did}: download failed -- {exc}")
            continue
        results.append(FetchResult(
            id=did, status="OK", resolved_url=url, path=str(dest.relative_to(ROOT)),
            sha256=sha, bytes=size, language=doc.get("languages", ["en"])[0],
            fetched_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), tried=tried,
        ))
        pc = page_count(dest)
        print(f"[ok] {did}: {size/1024:.0f} KB" + (f", {pc} pages" if pc else ""))
        time.sleep(POLITE_DELAY)

    lock = {
        "manifest": str(args.manifest.relative_to(ROOT)),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "documents": [asdict(r) for r in results],
    }
    args.lock.parent.mkdir(parents=True, exist_ok=True)
    args.lock.write_text(json.dumps(lock, ensure_ascii=False, indent=2), encoding="utf-8")

    ok = sum(r.status == "OK" for r in results)
    print(f"\nresolved {ok}/{len(results)} documents -> {args.lock}")
    unresolved = [r.id for r in results if r.status != "OK"]
    if unresolved:
        print("UNRESOLVED / ERROR:", ", ".join(unresolved))
        print("This is survivable. Run corpus/validate_corpus.py to see whether the")
        print("resolved subset still meets the lab coverage targets.")
    return 0


def verify(lock_path: Path) -> int:
    if not lock_path.exists():
        print("no LOCK.json -- run the fetcher first")
        return 1
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    bad = 0
    for entry in lock["documents"]:
        if entry["status"] != "OK":
            continue
        p = ROOT / entry["path"]
        if not p.exists():
            print(f"[!!] missing: {entry['id']}")
            bad += 1
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h != entry["sha256"]:
            print(f"[!!] hash drift: {entry['id']}  (document was re-published)")
            bad += 1
    print("verify: OK" if not bad else f"verify: {bad} problem(s)")
    return 0 if not bad else 2


if __name__ == "__main__":
    raise SystemExit(main())
