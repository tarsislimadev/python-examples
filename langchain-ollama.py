"""
Simple LangChain + Ollama chat app (CLI).

Run:
  python langchain-ollama.py --model llama3

Environment variables (optional):
  OLLAMA_BASE_URL  (default: http://localhost:11434)
  OLLAMA_MODEL     (default: llama3)
"""

# Install:
#   python -m pip install -U langchain langchain-core langchain-ollama

import argparse
import os

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

try:
    # Preferred (newer) package name.
    from langchain_ollama import ChatOllama  # type: ignore[import-not-found]
except Exception as e:
    raise SystemExit(
        "Missing Ollama integration for LangChain. "
        "Install with: python -m pip install -U langchain-ollama\n"
        f"Original error: {e}"
    )


def main() -> int:
    argp = argparse.ArgumentParser(description="LangChain + Ollama chat app (CLI)")
    argp.add_argument("--model", default=os.getenv("OLLAMA_MODEL", "llama3"))
    argp.add_argument(
        "--base-url",
        default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        help="Ollama host (e.g. http://localhost:11434)",
    )
    argp.add_argument("--temperature", type=float, default=0.2)
    argp.add_argument(
        "--system",
        default="You are a helpful assistant. Keep answers concise.",
        help="System prompt (used as the first message).",
    )
    args = argp.parse_args()

    # Some versions of `langchain-ollama` may not expose `base_url` as a kwarg.
    try:
        llm = ChatOllama(
            model=args.model,
            temperature=args.temperature,
            base_url=args.base_url,
        )
    except TypeError:
        llm = ChatOllama(
            model=args.model,
            temperature=args.temperature,
        )

    # Keep a small local history (just for the chat loop).
    history = []

    print(f"Connected to Ollama via model='{args.model}' at {args.base_url}")
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

        # Feed history + latest message. The LLM sees a chat-like context.
        messages = history + [HumanMessage(content=user_text)]

        # For simplicity we pass the system prompt each turn and rely on `messages`
        # for conversational context.
        llm_messages = [SystemMessage(content=args.system)] + messages
        response_text = llm.invoke(llm_messages).content

        print(f"\nAssistant: {response_text}")

        history.append(HumanMessage(content=user_text))
        history.append(AIMessage(content=response_text))

        # Prevent unbounded growth.
        if len(history) > 10:
            history = history[-10:]

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
