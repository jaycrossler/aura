from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

import requests


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


def _post_json(url: str, payload: dict[str, Any], headers: dict[str, str] | None = None) -> dict[str, Any]:
    response = requests.post(url, json=payload, headers=headers or {}, timeout=180)
    response.raise_for_status()
    return response.json()


def generate_text(system_prompt: str, user_prompt: str) -> LLMResponse:
    provider = os.getenv("STORYOPS_LLM_PROVIDER", "mock").strip().lower()
    if provider == "mock":
        return LLMResponse(content="", provider="mock", model="mock-story-writer")

    model = os.getenv("STORYOPS_LLM_MODEL", "")
    if provider == "ollama":
        model = model or "llama3.1:8b"
        base_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "options": {"temperature": 0.7},
            "format": "json",
        }
        data = _post_json(f"{base_url.rstrip('/')}/api/chat", payload)
        message = data.get("message", {})
        return LLMResponse(content=message.get("content", ""), provider=provider, model=model)

    if provider == "openai":
        model = model or "gpt-4.1"
        api_key = _require_env("OPENAI_API_KEY")
        payload = {
            "model": model,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.7,
        }
        data = _post_json(
            "https://api.openai.com/v1/chat/completions",
            payload,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        choice = (data.get("choices") or [{}])[0]
        return LLMResponse(content=((choice.get("message") or {}).get("content") or ""), provider=provider, model=model)

    if provider == "claude":
        model = model or "claude-3-7-sonnet-latest"
        api_key = _require_env("ANTHROPIC_API_KEY")
        payload = {
            "model": model,
            "max_tokens": 4000,
            "temperature": 0.7,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        }
        data = _post_json(
            "https://api.anthropic.com/v1/messages",
            payload,
            headers={"x-api-key": api_key, "anthropic-version": "2023-06-01"},
        )
        blocks = data.get("content") or []
        text = "\n".join(block.get("text", "") for block in blocks if isinstance(block, dict))
        return LLMResponse(content=text, provider=provider, model=model)

    raise RuntimeError(f"Unsupported STORYOPS_LLM_PROVIDER '{provider}'.")


def parse_json_payload(text: str) -> dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"LLM did not return valid JSON: {exc}") from exc
