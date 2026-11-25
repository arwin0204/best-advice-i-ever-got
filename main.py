#!/usr/bin/env python3
"""The Best Advice I Ever Got - make.fun entry.

Writes one sentence (at most 200 characters) about the best advice
the writer ever received to <output>/entry.txt.

Deterministic: the same bytes on every run. Python standard library
only; no network, no input files, no randomness.

Output directory: first command-line argument, else the
MAKEFUN_OUTPUT_DIR environment variable, else /output.
"""

import os
import sys

SENTENCE = (
    "My grandmother said, 'Don't marry a man who is kind to you but "
    "cruel to the waiter,' and I have measured every person I have met "
    "since by that one table."
)


def output_dir() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text: str) -> None:
    """Gate the entry the way the sealed scorer does, plus one-sentence shape."""
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be one line with no surrounding whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if any(ord(c) < 32 for c in text):
        raise SystemExit("entry must not contain control characters")


def main() -> int:
    text = SENTENCE
    validate(text)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
