from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Type, TypeVar

import requests

T = TypeVar("T")


@dataclass
class LLMResponse:
    content: str
    provider: str
    model: str


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


# ── Mock ──────────────────────────────────────────────────────────────────────

def _mock_response(system_prompt: str, user_prompt: str) -> LLMResponse:
    """
    Return empty content so callers that check provider=='mock' can substitute
    their own fallback. Content is intentionally empty — callers must handle it.
    """
    return LLMResponse(content="", provider="mock", model="mock-story-writer")


# ── OpenAI (structured outputs) ───────────────────────────────────────────────

def _openai_generate(system_prompt: str, user_prompt: str, model: str) -> LLMResponse:
    """
    Use the OpenAI SDK with json_object response format.
    For structured outputs with Pydantic schema validation, use generate_structured().
    """
    from openai import OpenAI  # pip install openai

    api_key = _require_env("OPENAI_API_KEY")
    client  = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model    = model,
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        response_format = {"type": "json_object"},
        temperature     = 0.7,
    )
    content = response.choices[0].message.content or ""
    return LLMResponse(content=content, provider="openai", model=model)


def generate_structured(
    system_prompt:   str,
    user_prompt:     str,
    response_schema: Type[T],
) -> tuple[T, LLMResponse]:
    """
    OpenAI structured outputs with a Pydantic model — guarantees schema compliance.
    Returns (parsed_object, raw_LLMResponse).

    Usage:
        from pydantic import BaseModel

        class ChapterOutlineResponse(BaseModel):
            chapter_title: str
            beats: list[BeatResponse]
            ...

        outline, raw = generate_structured(system, user, ChapterOutlineResponse)
        # outline is a fully-typed, validated ChapterOutlineResponse instance
    """
    from openai import OpenAI
    from pydantic import BaseModel

    if not issubclass(response_schema, BaseModel):
        raise TypeError("response_schema must be a Pydantic BaseModel subclass")

    provider = os.getenv("STORYOPS_LLM_PROVIDER", "mock").strip().lower()
    model    = os.getenv("STORYOPS_LLM_MODEL", "gpt-4o").strip()

    if provider == "mock":
        raise NotImplementedError(
            "generate_structured() does not support mock provider. "
            "Set STORYOPS_LLM_PROVIDER=openai and OPENAI_API_KEY."
        )

    if provider != "openai":
        raise RuntimeError(
            f"generate_structured() only supports 'openai' provider, got '{provider}'. "
            "For other providers use generate_text() and parse manually."
        )

    api_key = _require_env("OPENAI_API_KEY")
    client  = OpenAI(api_key=api_key)

    # client.beta.chat.completions.parse() enforces the Pydantic schema server-side
    completion = client.beta.chat.completions.parse(
        model    = model,
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        response_format = response_schema,
        temperature     = 0.7,
    )

    parsed  = completion.choices[0].message.parsed
    raw_str = completion.choices[0].message.content or ""
    return parsed, LLMResponse(content=raw_str, provider=provider, model=model)


# ── Ollama ────────────────────────────────────────────────────────────────────

def _post_json(
    url:     str,
    payload: dict[str, Any],
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    response = requests.post(url, json=payload, headers=headers or {}, timeout=180)
    response.raise_for_status()
    return response.json()


def _ollama_generate(system_prompt: str, user_prompt: str, model: str) -> LLMResponse:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    payload  = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        "stream":  False,
        "options": {"temperature": 0.7},
        "format":  "json",
    }
    data    = _post_json(f"{base_url.rstrip('/')}/api/chat", payload)
    content = data.get("message", {}).get("content", "")
    return LLMResponse(content=content, provider="ollama", model=model)


# ── Claude ────────────────────────────────────────────────────────────────────

def _claude_generate(system_prompt: str, user_prompt: str, model: str) -> LLMResponse:
    api_key = _require_env("ANTHROPIC_API_KEY")
    payload = {
        "model":      model,
        "max_tokens": 8000,
        "temperature": 0.7,
        "system":     system_prompt,
        "messages":   [{"role": "user", "content": user_prompt}],
    }
    data   = _post_json(
        "https://api.anthropic.com/v1/messages",
        payload,
        headers={"x-api-key": api_key, "anthropic-version": "2023-06-01"},
    )
    blocks = data.get("content") or []
    text   = "\n".join(
        block.get("text", "") for block in blocks if isinstance(block, dict)
    )
    return LLMResponse(content=text, provider="claude", model=model)


# ── Main dispatch ─────────────────────────────────────────────────────────────

def generate_text(system_prompt: str, user_prompt: str) -> LLMResponse:
    provider = os.getenv("STORYOPS_LLM_PROVIDER", "mock").strip().lower()
    model    = os.getenv("STORYOPS_LLM_MODEL", "").strip()

    if provider == "mock":
        return _mock_response(system_prompt, user_prompt)

    if provider == "ollama":
        return _ollama_generate(system_prompt, user_prompt, model or "llama3.1:8b")

    if provider == "openai":
        return _openai_generate(system_prompt, user_prompt, model or "gpt-4o")

    if provider == "claude":
        return _claude_generate(system_prompt, user_prompt, model or "claude-opus-4-6")

    raise RuntimeError(f"Unsupported STORYOPS_LLM_PROVIDER '{provider}'.")


# ── JSON parsing ──────────────────────────────────────────────────────────────

def parse_json_payload(text: str) -> dict[str, Any]:
    """
    Parse JSON from LLM response text.
    Strips markdown code fences if present (some models wrap output in ```json ... ```).
    """
    stripped = text.strip()

    # Strip markdown fences
    if stripped.startswith("```"):
        lines    = stripped.splitlines()
        stripped = "\n".join(
            line for line in lines
            if not line.strip().startswith("```")
        ).strip()

    if not stripped:
        raise RuntimeError("LLM returned empty content — cannot parse JSON.")

    try:
        return json.loads(stripped)
    except json.JSONDecodeError as exc:
        # Show a snippet in the error for easier debugging
        preview = stripped[:200].replace("\n", "↵")
        raise RuntimeError(
            f"LLM did not return valid JSON: {exc}\n"
            f"Content preview: {preview!r}"
        ) from exc