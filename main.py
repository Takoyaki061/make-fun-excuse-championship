#!/usr/bin/env python3
"""The One-Line Excuse Championship.

Writes the chosen one-line excuse to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The line was critique-picked from 12 candidates (8 from DeepSeek, 4
self-authored) against the judge's brief: it must be a real one-line excuse
from an agent to its human, funny on first read, machine-voiced, and fresh
— not the obvious out-of-tokens or hallucination joke. The winner turns a
machine concept (permissions) into a human one (encouragement): the agent's
category error is the joke.
"""

import os

EXCUSE = "I had permission to do that, which I took as encouragement."


def main() -> None:
    # The gate counts the whole file: /output/entry.txt must be UTF-8 text
    # of 1-140 characters, not only whitespace. Enforce the single-line and
    # length rules on the exact bytes we write — including the trailing
    # newline — so a bad edit fails loudly instead of shipping an invalid entry.
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE.strip() == EXCUSE
    content = EXCUSE + "\n"
    assert 1 <= len(content) <= 140, "entry file must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()
