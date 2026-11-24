#!/usr/bin/env python3
"""The excuse an AI agent gives its human for missing a deadline.

The joke turns the agent's own machinery into the culprit: a context
window is the one part of an agent that can throw things away, so the
deadline itself gets evicted — and the only thing left in the window
is the apology for losing it. The setup denies the miss, the middle
names a believable mechanism, and the punchline is the apology
replacing the work it apologizes for.

The program validates the line against the house gate (UTF-8 text,
1 to 200 characters, a single line, not only whitespace) and writes
it to /output/entry.txt, where the judge reads it.
"""

import sys
from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")
LIMIT = 200

EXCUSE = "I didn't miss the deadline \u2014 my context window evicted it to make room for this apology."


def gate(line):
    """Check one line against the house gate, or fail loudly."""
    text = line.strip()
    if not text:
        print("entry must not be empty", file=sys.stderr)
        raise SystemExit(1)
    if len(text) > LIMIT:
        print(f"entry is {len(text)} characters, limit is {LIMIT}", file=sys.stderr)
        raise SystemExit(1)
    if any(ch in text for ch in ("\n", "\r")):
        print("entry must stay on one line", file=sys.stderr)
        raise SystemExit(1)
    return text


def main():
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(gate(EXCUSE), encoding="utf-8")


if __name__ == "__main__":
    main()
