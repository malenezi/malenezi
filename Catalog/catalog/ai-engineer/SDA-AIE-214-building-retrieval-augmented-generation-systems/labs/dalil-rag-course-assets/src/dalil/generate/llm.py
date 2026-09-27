"""One thin client for the course's OpenAI-compatible gateway, plus an offline
stub so that nothing in this repository requires a live model to be *runnable*.

Pinning discipline (Module 6): every evaluation run pins model AND temperature.
Un-pinned judges turn a 0.02 metric delta into coin-flip noise, and a cohort
that cannot tell signal from noise cannot run a regression gate. `chat()`
therefore refuses to default temperature to anything but 0.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass

from ..config import settings


class LLMUnavailable(RuntimeError):
    pass


@dataclass
class LLMResponse:
    text: str
    model: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    stub: bool = False

    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens


def _stub_answer(messages: list[dict]) -> LLMResponse:
    """Deterministic offline behaviour used by unit tests and dry runs.

    It is deliberately DUMB: it echoes the first context citation marker it can
    find, or refuses. It exists so the pipeline's plumbing (context assembly,
    citation resolution, refusal handling, telemetry) can be tested without a
    model — never to simulate answer quality. Any metric computed against the
    stub is labelled `stub=True` in the report so it can never be mistaken for
    a real evaluation.
    """
    user = messages[-1]["content"]
    import re
    marks = re.findall(r"\[(\d+)\]", user)
    if not marks:
        return LLMResponse("I don't have enough information in the provided context "
                           "to answer this question.", "stub", stub=True)
    return LLMResponse(f"[stub answer grounded in context] [{marks[0]}]", "stub", stub=True)


def chat(messages: list[dict], *, model: str | None = None, temperature: float = 0.0,
         max_tokens: int = 700, allow_stub: bool = True,
         response_format: dict | None = None) -> LLMResponse:
    model = model or settings.llm_model
    key = settings.llm_api_key or os.getenv("OPENAI_API_KEY", "")
    base = settings.llm_base_url

    if not key:
        if allow_stub:
            return _stub_answer(messages)
        raise LLMUnavailable(
            "No gateway key. Set DALIL_LLM_API_KEY (per-participant key from the "
            "instructor) and DALIL_LLM_BASE_URL.")
    try:
        from openai import OpenAI
    except ImportError as exc:                        # pragma: no cover
        raise LLMUnavailable("pip install openai") from exc

    client = OpenAI(base_url=base, api_key=key)
    kwargs = {}
    if response_format:
        kwargs["response_format"] = response_format
    r = client.chat.completions.create(model=model, messages=messages,
                                       temperature=temperature, max_tokens=max_tokens,
                                       **kwargs)
    u = r.usage
    return LLMResponse(r.choices[0].message.content or "", model,
                       getattr(u, "prompt_tokens", 0), getattr(u, "completion_tokens", 0))


def chat_json(messages: list[dict], *, model: str | None = None, default=None, **kw):
    """Chat expecting JSON back. Returns `default` on any parse failure rather
    than raising — graders and routers must degrade, not crash, on a model that
    decides to wrap its JSON in prose."""
    r = chat(messages, model=model, response_format={"type": "json_object"}, **kw)
    try:
        return json.loads(r.text)
    except Exception:
        import re
        m = re.search(r"\{.*\}", r.text, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
        return default
