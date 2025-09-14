import json
import requests
from pprint import pprint

BASE_URL = "http://localhost:3001"

def post_json(path: str, payload: dict):
    url = f"{BASE_URL}{path}"
    r = requests.post(url, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()

def ask_openai(message: str):
    """Non-streaming call to /openai/invoke."""
    return post_json("/openai/invoke", {"input": message})

def ask_essay(topic: str):
    """Non-streaming call to /essay/invoke."""
    return post_json("/essay/invoke", {"input": {"topic": topic}})

def stream(path: str, payload: dict):
    """Generic streaming helper for any LangServe /<route>/stream endpoint."""
    url = f"{BASE_URL}{path}"
    with requests.post(url, json=payload, stream=True, timeout=300) as r:
        r.raise_for_status()
        for raw in r.iter_lines(decode_unicode=True):
            if not raw:
                continue
            # LangServe emits SSE-style lines: "data: {json}\n"
            if raw.startswith("data:"):
                raw = raw[len("data:"):].strip()
            try:
                evt = json.loads(raw)
            except json.JSONDecodeError:
                continue

            kind = evt.get("event")
            data = evt.get("data", {})

            if kind == "data":
                # token chunk is usually under .chunk (sometimes .content)
                chunk = data.get("chunk") or data.get("content") or ""
                print(chunk, end="", flush=True)
            elif kind == "end":
                print()  # newline at end
                break
            elif kind == "error":
                raise RuntimeError(data)

if __name__ == "__main__":
    print("Calling /openai (invoke)…")
    pprint(ask_openai("What is LangChain in one paragraph?"))

    print("\nCalling /essay (invoke)…")
    pprint(ask_essay("Artificial Intelligence"))

    print("\nStreaming /openai (stream)…")
    stream("/openai/stream", {"input": "Stream a single concise sentence about embeddings."})

    print("\nStreaming /essay (stream)…")
    stream("/essay/stream", {"input": {"topic": "AI governance"}})

