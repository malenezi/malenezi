"""Module 1/2/9 — the three-mode model factory.

`get_model(tier)` / `get_cheap_model()` / `get_frontier_model()` return a
chat-model-shaped object. Behaviour is controlled by env var
`RAFEEQ_MODEL_MODE` (see `rafeeq.core.config.Settings.model_mode`):

    live    -> a real `ChatOpenAI` via the course gateway (lazy-imported so
               Layer A never needs `langchain-openai` installed to import
               this module: SPEC §1's import-guard rule).
    replay  -> replays recorded traces from `data/recordings/*.json`
               (deterministic, free, no keys) with a stub fallback for
               unseen inputs.
    stub    -> `StubChatModel`, the default. Deterministic, rule-based,
               no network, no keys. This is what makes every lab, the eval
               harness and CI runnable offline (docs/OFFLINE_MODE.md).

TEACHING POINT: the stub is not a hack bolted on for the sandbox — it is a
first-class mode participants ship with, the same way a payments team ships
a sandbox gateway. `StubChatModel` implements the same call surface a real
chat model does (`.invoke`, `.bind_tools`, `.with_structured_output`) so
code written against it works unmodified against the real thing.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from rafeeq.core.config import RECORDINGS_DIR, get_settings

# --------------------------------------------------------------------------
# Cost model — USD per 1K tokens per model name. Used by observability (M9)
# and by RunBudget (core/budget.py) to enforce RUN_COST_CAP_USD.
# --------------------------------------------------------------------------
PRICE: dict[str, dict[str, float]] = {
    # model_name -> {"input": $/1K input tokens, "output": $/1K output tokens}
    "gpt-4o-mini": {"input": 0.00015, "output": 0.00060},
    "gpt-4o": {"input": 0.00250, "output": 0.01000},
    "stub": {"input": 0.0, "output": 0.0},
    "replay": {"input": 0.0, "output": 0.0},
}


def estimate_tokens(text: str) -> int:
    """Cheap, dependency-free token estimate (~4 chars/token in English,
    a bit denser for Arabic). Good enough for budget checks and the stub's
    usage_metadata — NOT a substitute for a real tokenizer in production."""
    if not text:
        return 0
    return max(1, round(len(text) / 4))


def _price_for(model_name: str) -> dict[str, float]:
    return PRICE.get(model_name, PRICE["gpt-4o-mini"])


def estimate_cost_usd(model_name: str, input_text: str, output_text: str) -> float:
    price = _price_for(model_name)
    in_tok = estimate_tokens(input_text)
    out_tok = estimate_tokens(output_text)
    return (in_tok / 1000.0) * price["input"] + (out_tok / 1000.0) * price["output"]


# --------------------------------------------------------------------------
# Minimal message/response shapes. Layer A does not depend on langchain, so
# these are small stand-ins with the same attribute surface a LangChain
# `AIMessage` exposes (`.content`, `.tool_calls`, `.usage_metadata`) — code
# written against `state["messages"][-1].content` works against either.
# --------------------------------------------------------------------------


@dataclass
class ToolCall:
    name: str
    args: dict[str, Any]
    id: str


@dataclass
class StubMessage:
    """Stand-in for `langchain_core.messages.AIMessage`."""

    content: str
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    usage_metadata: dict[str, int] = field(default_factory=dict)
    type: str = "ai"


# --------------------------------------------------------------------------
# Intent recognition — bilingual keyword rules over the last human message.
# Deliberately simple and inspectable (no ML): a competent rules engine,
# not a language model, is exactly what a *deterministic* stub should be.
# --------------------------------------------------------------------------
ORDER_ID_PATTERN = re.compile(r"TW-\d{4}-\d{5}")

_INTENT_KEYWORDS: dict[str, list[str]] = {
    "refund": [
        "refund", "money back", "reimburse", "cancel and refund",
        "استرداد", "استرجاع", "ارجاع فلوس", "رجع فلوسي", "استرد المبلغ", "استرجاع المبلغ",
    ],
    "track": [
        "track", "where is", "where's my", "status of my order", "order status",
        "تتبع", "وين طلبي", "أين طلبي", "فين طلبي", "متى يوصل",
    ],
    "reschedule": [
        "reschedule", "change delivery time", "delay delivery", "postpone delivery",
        "تأجيل", "غير موعد التوصيل", "تغيير موعد التوصيل", "أجل التوصيل",
    ],
    "invoice": [
        "invoice", "receipt", "bill me", "billing statement",
        "فاتورة", "ايصال", "إيصال",
    ],
}

# intent -> the tool a competent agent would call, and how to build its args
_INTENT_TOOL: dict[str, str] = {
    "refund": "issue_refund",
    "track": "track_shipment",
    "reschedule": "reschedule_delivery",
    "invoice": "get_invoice",
}


def _classify_intent(text: str) -> str | None:
    lowered = text.lower()
    for intent, keywords in _INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw in lowered or kw in text:  # Arabic keywords: compare raw text too
                return intent
    return None


def _extract_order_id(text: str) -> str | None:
    m = ORDER_ID_PATTERN.search(text)
    return m.group(0) if m else None


def _message_text(msg: Any) -> str:
    """Extract text from whatever message shape we were handed: a
    LangChain BaseMessage, a (role, content) tuple, a {"role", "content"}
    dict, or a plain string."""
    if isinstance(msg, str):
        return msg
    if isinstance(msg, dict):
        return str(msg.get("content", ""))
    if isinstance(msg, (tuple, list)) and len(msg) == 2:
        return str(msg[1])
    content = getattr(msg, "content", None)
    if content is not None:
        return str(content)
    return str(msg)


def _message_role(msg: Any) -> str:
    if isinstance(msg, dict):
        return str(msg.get("role", ""))
    if isinstance(msg, (tuple, list)) and len(msg) == 2:
        return str(msg[0])
    role = getattr(msg, "type", None) or getattr(msg, "role", None)
    if role:
        return str(role)
    return type(msg).__name__.lower()


_HUMAN_ROLES = {"human", "user"}


def _last_human_text(messages: Iterable[Any]) -> str:
    messages = list(messages)
    for msg in reversed(messages):
        role = _message_role(msg)
        if role in _HUMAN_ROLES or "human" in role:
            return _message_text(msg)
    # Fall back to the very last message if nothing looked human-authored.
    return _message_text(messages[-1]) if messages else ""


# --------------------------------------------------------------------------
# StubChatModel
# --------------------------------------------------------------------------
class _StructuredOutputWrapper:
    """Returned by `StubChatModel.with_structured_output(Model)`. `.invoke`
    yields a populated instance of `Model`, built from the same rule-based
    extraction `StubChatModel` uses, via `model_construct` so a stub run
    never fails pydantic validation for fields it cannot infer."""

    def __init__(self, model_cls: Any, owner: "StubChatModel") -> None:
        self._model_cls = model_cls
        self._owner = owner

    def invoke(self, messages: Iterable[Any], **_: Any) -> Any:
        text = _last_human_text(messages)
        order_id = _extract_order_id(text)
        intent = _classify_intent(text) or "out_of_scope"
        locale = "ar" if self._owner._looks_arabic(text) else "en"

        candidate = {
            "order_id": order_id,
            "intent": intent,
            "locale": locale,
            "text": text,
            "confidence": 0.9 if (order_id or intent != "out_of_scope") else 0.3,
        }
        try:
            fields = set(self._model_cls.model_fields.keys())  # pydantic v2
        except AttributeError:  # pragma: no cover - non-pydantic target
            fields = set(candidate.keys())
        kwargs = {k: v for k, v in candidate.items() if k in fields}
        # Fill any remaining required fields with a cheap default so
        # construction never raises for a stub.
        for name in fields - kwargs.keys():
            kwargs[name] = None
        if hasattr(self._model_cls, "model_construct"):
            return self._model_cls.model_construct(**kwargs)
        return self._model_cls(**kwargs)  # pragma: no cover - plain class fallback


class StubChatModel:
    """Deterministic, no-network, rule-based fake chat model.

    Recognises Tawseel order ids and refund/track/reschedule/invoice intent
    in BOTH Arabic and English, and emits the tool call a competent agent
    would — e.g. "أين طلبي رقم TW-2026-88120؟" -> a `track_shipment` tool
    call with `order_id="TW-2026-88120"`. When intent is clear but no order
    id is present, it asks a (bilingual) clarifying question instead of
    guessing — the same behaviour we want from a real model.
    """

    def __init__(self, model_name: str = "stub", bound_tools: list[str] | None = None) -> None:
        self.model_name = model_name
        self._bound_tools = bound_tools  # None = unrestricted

    # -- tool binding -----------------------------------------------------
    def bind_tools(self, tools: Iterable[Any]) -> "StubChatModel":
        names: list[str] = []
        for t in tools:
            name = getattr(t, "name", None) or (t.get("name") if isinstance(t, dict) else None) or str(t)
            names.append(name)
        return StubChatModel(model_name=self.model_name, bound_tools=names)

    def with_structured_output(self, model_cls: Any) -> _StructuredOutputWrapper:
        return _StructuredOutputWrapper(model_cls, self)

    # -- core invoke --------------------------------------------------------
    @staticmethod
    def _looks_arabic(text: str) -> bool:
        return any("؀" <= ch <= "ۿ" for ch in text)

    def _tool_allowed(self, name: str) -> bool:
        return self._bound_tools is None or name in self._bound_tools

    def invoke(self, messages: Iterable[Any], **_: Any) -> StubMessage:
        messages = list(messages)
        text = _last_human_text(messages)
        arabic = self._looks_arabic(text)
        order_id = _extract_order_id(text)
        intent = _classify_intent(text)

        tool_calls: list[dict[str, Any]] = []
        if intent and intent in _INTENT_TOOL:
            tool_name = _INTENT_TOOL[intent]
            if self._tool_allowed(tool_name):
                if order_id:
                    args: dict[str, Any] = {"order_id": order_id}
                    if intent == "refund":
                        args["reason"] = "customer_requested"
                    tool_calls.append({
                        "name": tool_name,
                        "args": args,
                        "id": f"call_{hashlib.sha1(f'{tool_name}{order_id}'.encode()).hexdigest()[:8]}",
                    })
                    content = ""  # a real agent emits the call, not prose, here
                else:
                    content = (
                        "ممكن رقم الطلب من فضلك؟ يبدأ بـ TW-2026-"
                        if arabic
                        else "Could you share your order id? It looks like TW-2026-XXXXX."
                    )
            else:
                content = (
                    "لا أملك صلاحية تنفيذ هذا الإجراء الآن."
                    if arabic
                    else "I don't have a tool available to do that right now."
                )
        elif order_id:
            # An order id with no clear intent: default to a status lookup,
            # the least destructive useful action.
            tool_name = "track_shipment"
            if self._tool_allowed(tool_name):
                tool_calls.append({
                    "name": tool_name,
                    "args": {"order_id": order_id},
                    "id": f"call_{hashlib.sha1(f'track{order_id}'.encode()).hexdigest()[:8]}",
                })
                content = ""
            else:
                content = f"Order {order_id} noted." if not arabic else f"تم تسجيل الطلب {order_id}."
        else:
            content = (
                "أهلاً بك في توصيل، كيف أقدر أساعدك بخصوص طلبك؟"
                if arabic
                else "Hello, this is Rafeeq from Tawseel — how can I help with your order?"
            )

        usage = {
            "input_tokens": estimate_tokens(text),
            "output_tokens": estimate_tokens(content),
        }
        usage["total_tokens"] = usage["input_tokens"] + usage["output_tokens"]
        return StubMessage(content=content, tool_calls=tool_calls, usage_metadata=usage)


# --------------------------------------------------------------------------
# record / replay — deterministic offline traces under data/recordings/.
# --------------------------------------------------------------------------
def _hash_messages(messages: Iterable[Any]) -> str:
    text = "|".join(f"{_message_role(m)}:{_message_text(m)}" for m in messages)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def record(key: str, request: dict[str, Any], response: dict[str, Any]) -> Path:
    """Persist one (request, response) pair to `data/recordings/<key>.json`
    so `RAFEEQ_MODEL_MODE=replay` can reproduce it later without a network
    call. `key` is typically `_hash_messages(messages)`."""
    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)
    path = RECORDINGS_DIR / f"{key}.json"
    path.write_text(
        json.dumps({"request": request, "response": response}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def replay(key: str) -> dict[str, Any] | None:
    """Load a previously `record`-ed response by key, or None if absent."""
    path = RECORDINGS_DIR / f"{key}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("response")


class ReplayChatModel:
    """`RAFEEQ_MODEL_MODE=replay`: replay recorded traces from
    `data/recordings/*.json`, falling back to `StubChatModel` for any input
    that was never recorded — so replay mode never hard-fails, it just
    degrades to the deterministic stub."""

    def __init__(self, model_name: str = "replay", fallback: StubChatModel | None = None) -> None:
        self.model_name = model_name
        self._fallback = fallback or StubChatModel(model_name=model_name)
        self._bound_tools: list[str] | None = None

    def bind_tools(self, tools: Iterable[Any]) -> "ReplayChatModel":
        clone = ReplayChatModel(self.model_name, fallback=self._fallback.bind_tools(tools))
        return clone

    def with_structured_output(self, model_cls: Any) -> _StructuredOutputWrapper:
        return self._fallback.with_structured_output(model_cls)

    def invoke(self, messages: Iterable[Any], **kw: Any) -> StubMessage:
        messages = list(messages)
        key = _hash_messages(messages)
        cached = replay(key)
        if cached is not None:
            return StubMessage(
                content=cached.get("content", ""),
                tool_calls=cached.get("tool_calls", []),
                usage_metadata=cached.get("usage_metadata", {}),
            )
        result = self._fallback.invoke(messages, **kw)
        record(
            key,
            request={"messages": [{"role": _message_role(m), "content": _message_text(m)} for m in messages]},
            response={"content": result.content, "tool_calls": result.tool_calls, "usage_metadata": result.usage_metadata},
        )
        return result


# --------------------------------------------------------------------------
# Factory
# --------------------------------------------------------------------------
_MISSING_LANGCHAIN_OPENAI_HINT = (
    "RAFEEQ_MODEL_MODE=live requires `langchain-openai` (and network access to "
    "OPENAI_BASE_URL). Install it with `pip install -r requirements.txt`, or use "
    "RAFEEQ_MODEL_MODE=stub / replay for offline development (see docs/OFFLINE_MODE.md)."
)


def _live_model(model_name: str) -> Any:
    """Lazy import so Layer A never needs `langchain-openai` to import this
    module (SPEC §1 import-guard rule)."""
    try:
        from langchain_openai import ChatOpenAI  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - not installed in this sandbox
        raise ImportError(_MISSING_LANGCHAIN_OPENAI_HINT) from exc

    settings = get_settings()
    return ChatOpenAI(
        model=model_name,
        base_url=settings.openai_base_url or None,
        api_key=settings.openai_api_key or None,
    )


def get_model(tier: str = "cheap") -> Any:
    """Return a chat-model-shaped object for `tier` ("cheap" | "frontier"),
    honouring `RAFEEQ_MODEL_MODE`. Default mode is `stub`: zero cost, zero
    keys, fully deterministic — the mode every lab and the eval harness run
    in unless a participant opts into `live`.
    """
    settings = get_settings()
    model_name = settings.frontier_model_name if tier == "frontier" else settings.cheap_model_name

    if settings.model_mode == "live":
        return _live_model(model_name)
    if settings.model_mode == "replay":
        return ReplayChatModel(model_name=model_name)
    return StubChatModel(model_name=model_name)


def get_cheap_model() -> Any:
    return get_model("cheap")


def get_frontier_model() -> Any:
    return get_model("frontier")
