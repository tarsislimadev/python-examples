# Usage: python langchain-dmr-restapi.py --model docker.io/llama3.2:1B-Q4_0

"""
LangChain + Docker Model Runner REST API (OpenAI-compatible) chat app (CLI).

This uses Docker Model Runner's OpenAI-compatible API:
  POST /engines/v1/chat/completions

Run:
  python langchain-dmr-restapi.py --model ai/smollm2

Common environment variables:
  DMR_BASE_URL  (default: http://localhost:12434/engines/v1)
  DMR_MODEL     (default: ai/smollm2)
  DMR_API_KEY   (optional; DMR ignores it, default: not-needed)
"""

# Install:
#   python -m pip install -U langchain langchain-openai langchain-core

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

try:
    # Preferred (newer) integration package name.
    from langchain_openai import ChatOpenAI  # type: ignore[import-not-found]
except Exception as e:
    raise SystemExit(
        "Missing LangChain OpenAI integration for DMR.\n"
        "Install with:\n"
        "  python -m pip install -U langchain-openai\n"
        f"Original error: {e}"
    )


def _http_get_json(url: str, timeout_s: float = 30.0) -> Any:
    req = Request(url, headers={"Accept": "application/json"})
    with urlopen(req, timeout=timeout_s) as resp:  # nosec - example code
        raw = resp.read().decode("utf-8")
        return json.loads(raw)


def list_models(base_url: str, timeout_s: float = 30.0) -> None:
    """
    Calls GET {base_url}/models
    where base_url should be like: http://localhost:12434/engines/v1
    """

    url = f"{base_url.rstrip('/')}/models"
    try:
        data = _http_get_json(url, timeout_s=timeout_s)
    except HTTPError as e:
        raise SystemExit(f"HTTP error calling {url}: {e.code} {e.reason}") from e
    except URLError as e:
        raise SystemExit(f"Error calling {url}: {e}") from e

    # OpenAI list models returns: { "data": [ {"id": "..."} , ... ] }
    model_ids: list[str] = []
    if isinstance(data, dict):
        if isinstance(data.get("data"), list):
            for m in data["data"]:
                if isinstance(m, dict) and "id" in m:
                    model_ids.append(str(m["id"]))
        # Some servers might use a different shape; fall back to raw printing.
    if model_ids:
        for mid in model_ids:
            print(mid)
        return

    print(json.dumps(data, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="LangChain + Docker Model Runner (OpenAI-compatible) chat app"
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("DMR_BASE_URL", "http://localhost:12434/engines/v1"),
        help="DMR OpenAI-compatible base URL ending in /engines/v1",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("DMR_MODEL", "ai/smollm2"),
        help="Model identifier including namespace (e.g. ai/smollm2)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=float(os.getenv("DMR_TEMPERATURE", "0.2")),
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=int(os.getenv("DMR_MAX_TOKENS", "512")),
        help="Max tokens for each completion",
    )
    parser.add_argument(
        "--system",
        default=os.getenv("DMR_SYSTEM", "You are a helpful assistant. Keep answers concise."),
        help="System prompt",
    )
    parser.add_argument(
        "--max-history",
        type=int,
        default=int(os.getenv("DMR_MAX_HISTORY", "10")),
        help="Max number of messages to keep in local chat history",
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List models available at GET {base_url}/models and exit",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=float(os.getenv("DMR_HTTP_TIMEOUT", "30")),
        help="HTTP timeout (seconds) for non-chat endpoints",
    )
    args = parser.parse_args()

    if args.list_models:
        list_models(args.base_url, timeout_s=args.timeout)
        return 0

    api_key = os.getenv("DMR_API_KEY", "not-needed")

    # DMR doesn't require an API key; it ignores Authorization.
    try:
        llm = ChatOpenAI(
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            base_url=args.base_url,
            api_key=api_key,
        )
    except TypeError:
        # Older langchain-openai versions may not support `max_tokens` on init.
        llm = ChatOpenAI(
            model=args.model,
            temperature=args.temperature,
            base_url=args.base_url,
            api_key=api_key,
        )

    history: list[Any] = []  # stores HumanMessage/AIMessage alternating
    print(f"Connected to Docker Model Runner at {args.base_url}")
    print(f"Using model: {args.model}")
    print("Type your message. Use 'exit' or 'quit' to leave.")

    while True:
        try:
            user_text = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            return 0

        if not user_text:
            continue
        if user_text.lower() in {"exit", "quit"}:
            return 0

        # Each turn: (system) + (previous chat history) + (latest user message)
        messages = [SystemMessage(content=args.system), *history, HumanMessage(content=user_text)]
        response = llm.invoke(messages)
        response_text = response.content

        print(f"\nAssistant: {response_text}")

        history.append(HumanMessage(content=user_text))
        history.append(AIMessage(content=response_text))

        # Cap growth (history contains both Human and AI messages).
        if args.max_history > 0 and len(history) > args.max_history * 2:
            history = history[-args.max_history * 2 :]

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
