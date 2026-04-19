"""Provider-agnostic LLM interface.

Thin async adapter around Anthropic, OpenAI, and Google's SDKs. The public
interface (`generate_structured`) takes a JSON schema and returns a parsed
dict matching it — each provider implements the "force structured output"
pattern in its own idiomatic way:

* Anthropic — `tool_use` with forced `tool_choice`.
* OpenAI — `response_format` with a JSON schema.
* Google — `response_schema` on the `generation_config`.

Rolled our own adapter instead of pulling in `litellm` or LangChain to
keep the dependency footprint tight.
"""

from __future__ import annotations

import asyncio
import json
import os
from abc import ABC, abstractmethod
from typing import Any

DEFAULT_MAX_TOKENS = 4096
DEFAULT_TEMPERATURE = 0.0
RETRY_BACKOFF_SECONDS = (1.0, 2.0, 4.0)  # three retries, then fail


class LLMError(RuntimeError):
    """Raised when an LLM call fails unrecoverably."""


class MissingAPIKey(LLMError):
    """Raised when the required API key env var is not set."""


class Provider(ABC):
    """Abstract async provider."""

    name: str
    default_model: str

    @abstractmethod
    async def generate_structured(
        self,
        system: str,
        user: str,
        schema: dict[str, Any],
        schema_name: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> dict[str, Any]:
        """Generate a response that matches the provided JSON schema.

        The `schema` argument is a standard JSON schema object (the same
        shape you'd pass to Anthropic tool_use `input_schema` or OpenAI
        `response_format.json_schema.schema`). The `schema_name` is the
        tool/format name some providers require.
        """

    @abstractmethod
    async def generate_text(
        self,
        system: str,
        user: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> str:
        """Generate a freeform text response (no structured output constraint)."""


class AnthropicProvider(Provider):
    name = "anthropic"
    default_model = "claude-sonnet-4-20250514"

    def __init__(self, api_key: str | None = None):
        key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise MissingAPIKey("ANTHROPIC_API_KEY is not set")
        from anthropic import AsyncAnthropic

        self._client = AsyncAnthropic(api_key=key)

    async def generate_structured(
        self,
        system: str,
        user: str,
        schema: dict[str, Any],
        schema_name: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> dict[str, Any]:
        tool = {
            "name": schema_name,
            "description": f"Emit structured output matching the {schema_name} schema.",
            "input_schema": schema,
        }
        resp = await _with_retry(
            self._client.messages.create,
            model=model or self.default_model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
            tools=[tool],
            tool_choice={"type": "tool", "name": schema_name},
        )
        for block in resp.content:
            if getattr(block, "type", None) == "tool_use" and block.name == schema_name:
                payload = block.input
                if isinstance(payload, str):
                    payload = json.loads(payload)
                return payload
        raise LLMError(
            f"Anthropic response contained no {schema_name} tool_use block. "
            f"stop_reason={resp.stop_reason}"
        )

    async def generate_text(
        self,
        system: str,
        user: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> str:
        resp = await _with_retry(
            self._client.messages.create,
            model=model or self.default_model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        parts = []
        for block in resp.content:
            if getattr(block, "type", None) == "text":
                parts.append(block.text)
        return "".join(parts)


class OpenAIProvider(Provider):
    name = "openai"
    default_model = "gpt-4.1"

    def __init__(self, api_key: str | None = None):
        key = api_key or os.environ.get("OPENAI_API_KEY")
        if not key:
            raise MissingAPIKey("OPENAI_API_KEY is not set")
        from openai import AsyncOpenAI

        self._client = AsyncOpenAI(api_key=key)

    async def generate_structured(
        self,
        system: str,
        user: str,
        schema: dict[str, Any],
        schema_name: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> dict[str, Any]:
        # OpenAI requires `additionalProperties: false` on every object
        # in structured-output schemas. Walk and patch.
        patched = _openai_patch_schema(schema)
        resp = await _with_retry(
            self._client.chat.completions.create,
            model=model or self.default_model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": schema_name,
                    "strict": True,
                    "schema": patched,
                },
            },
        )
        content = resp.choices[0].message.content
        if not content:
            raise LLMError("OpenAI returned empty response")
        return json.loads(content)

    async def generate_text(
        self,
        system: str,
        user: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> str:
        resp = await _with_retry(
            self._client.chat.completions.create,
            model=model or self.default_model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp.choices[0].message.content or ""


class GoogleProvider(Provider):
    name = "google"
    default_model = "gemini-2.0-flash"

    def __init__(self, api_key: str | None = None):
        key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise MissingAPIKey("GOOGLE_API_KEY is not set")
        from google import genai

        self._client = genai.Client(api_key=key)

    async def generate_structured(
        self,
        system: str,
        user: str,
        schema: dict[str, Any],
        schema_name: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> dict[str, Any]:
        # google-genai accepts an async method via `client.aio.models.generate_content`.
        full_prompt = f"{system}\n\n{user}"
        resp = await _with_retry(
            self._client.aio.models.generate_content,
            model=model or self.default_model,
            contents=full_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": schema,
                "temperature": temperature,
                "max_output_tokens": max_tokens,
            },
        )
        text = resp.text or ""
        return json.loads(text)

    async def generate_text(
        self,
        system: str,
        user: str,
        model: str | None = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> str:
        full_prompt = f"{system}\n\n{user}"
        resp = await _with_retry(
            self._client.aio.models.generate_content,
            model=model or self.default_model,
            contents=full_prompt,
            config={"temperature": temperature, "max_output_tokens": max_tokens},
        )
        return resp.text or ""


# ── Provider registry ──


_PROVIDERS = {
    "anthropic": AnthropicProvider,
    "claude": AnthropicProvider,
    "openai": OpenAIProvider,
    "gpt": OpenAIProvider,
    "google": GoogleProvider,
    "gemini": GoogleProvider,
}

# Common model-name shortcuts. CLI `--model sonnet` → AnthropicProvider with
# claude-sonnet-4 as the model string.
_MODEL_SHORTCUTS = {
    "sonnet": ("anthropic", "claude-sonnet-4-20250514"),
    "opus": ("anthropic", "claude-opus-4-20250514"),
    "haiku": ("anthropic", "claude-haiku-4-5-20251001"),
    "gpt-4.1": ("openai", "gpt-4.1"),
    "gpt-5": ("openai", "gpt-5"),
    "gemini": ("google", "gemini-2.0-flash"),
    "gemini-pro": ("google", "gemini-2.5-pro"),
}


def resolve_provider(model: str | None) -> tuple[Provider, str | None]:
    """Map a CLI/config model string to a (Provider, model_string) pair.

    Accepted forms:
      * Shortcut name like 'sonnet', 'opus', 'gpt-4.1', 'gemini'
      * Provider name like 'anthropic' / 'openai' / 'google' (uses provider default)
      * Raw model ID like 'claude-sonnet-4-20250514' (inferred from prefix)
      * None (defaults to Anthropic sonnet if ANTHROPIC_API_KEY is set,
        otherwise falls back to whichever key is present)
    """
    if model is None:
        for env_var, key in (
            ("ANTHROPIC_API_KEY", "sonnet"),
            ("OPENAI_API_KEY", "gpt-4.1"),
            ("GOOGLE_API_KEY", "gemini"),
        ):
            if os.environ.get(env_var):
                return resolve_provider(key)
        raise MissingAPIKey(
            "No provider API key set. Set at least one of "
            "ANTHROPIC_API_KEY / OPENAI_API_KEY / GOOGLE_API_KEY."
        )

    if model in _MODEL_SHORTCUTS:
        provider_key, model_id = _MODEL_SHORTCUTS[model]
        return _PROVIDERS[provider_key](), model_id

    if model in _PROVIDERS:
        return _PROVIDERS[model](), None  # use provider default

    # Infer provider from raw model-id prefix.
    if model.startswith("claude"):
        return _PROVIDERS["anthropic"](), model
    if model.startswith(("gpt", "o1", "o3")):
        return _PROVIDERS["openai"](), model
    if model.startswith("gemini"):
        return _PROVIDERS["google"](), model

    raise ValueError(
        f"Unknown model '{model}'. "
        f"Use a shortcut ({', '.join(sorted(_MODEL_SHORTCUTS))}), "
        f"a provider name, or a full model ID."
    )


# ── Internal helpers ──


async def _with_retry(fn, **kwargs):
    """Call an async API function with exponential backoff on transient errors."""
    last_exc: Exception | None = None
    for delay in (0.0, *RETRY_BACKOFF_SECONDS):
        if delay:
            await asyncio.sleep(delay)
        try:
            return await fn(**kwargs)
        except Exception as e:  # noqa: BLE001 — SDKs raise provider-specific types
            last_exc = e
            if _is_terminal_error(e):
                raise
    raise LLMError(f"API call failed after retries: {last_exc}") from last_exc


def _is_terminal_error(exc: Exception) -> bool:
    """Return True for errors we shouldn't retry (auth, bad request, etc.)."""
    msg = str(exc).lower()
    terminal_markers = ("authentication", "unauthorized", "invalid api key", "400", "bad request")
    return any(m in msg for m in terminal_markers)


def _openai_patch_schema(schema: dict[str, Any]) -> dict[str, Any]:
    """OpenAI structured outputs require `additionalProperties: false` on every object."""
    if not isinstance(schema, dict):
        return schema
    patched = dict(schema)
    if patched.get("type") == "object":
        patched.setdefault("additionalProperties", False)
        props = patched.get("properties", {})
        patched["properties"] = {k: _openai_patch_schema(v) for k, v in props.items()}
        if "required" not in patched:
            # OpenAI strict mode requires every property to be listed as required.
            patched["required"] = list(props.keys())
    elif patched.get("type") == "array" and "items" in patched:
        patched["items"] = _openai_patch_schema(patched["items"])
    return patched
