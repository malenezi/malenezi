import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

CHUNKS = ROOT / "data/index/chunks.jsonl"


@pytest.fixture(scope="session")
def chunks():
    if not CHUNKS.exists():
        pytest.skip("run `make ingest` first")
    return [json.loads(l) for l in CHUNKS.read_text(encoding="utf-8").splitlines() if l.strip()]


@pytest.fixture(scope="session")
def backend(chunks):
    from dalil.retrieve.backends import MemoryBackend
    return MemoryBackend(chunks, dense=False)
