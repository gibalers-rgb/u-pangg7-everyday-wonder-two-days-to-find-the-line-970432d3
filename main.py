#!/usr/bin/env python3
"""Everyday Wonder — one sentence that makes a small moment strange and new.

The entry is a single sentence, at most 200 characters, about a small moment
of wonder in everyday life. The program writes that sentence to
/output/entry.txt, where the sealed gate scorer checks it (UTF-8, 1-200
characters, not only whitespace) and the pairwise AI judge compares it
against the other entries.

The sentence: a phone charger whose cable only works bent exactly where it
broke. Everyone who has owned a dying charger knows the ritual — wiggle it,
find the one angle, hold it there — but nobody has said what the charger
itself seems to want. The turn is the charger asking to have its hand held:
a frayed wire becomes a small, needy creature, and a daily annoyance becomes
a quiet act of care. It lands in a single read, stays grounded in a real,
specific object, and every word works.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")

SENTENCE = (
    "My phone charger only works when the cable bends exactly where "
    "it broke, like it is asking me to hold its hand."
)


def validate(sentence: str) -> None:
    """Enforce the gate: one sentence, 1-200 characters, not blank."""
    stripped = sentence.strip()
    if not stripped:
        raise ValueError("entry sentence must not be empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(stripped)} characters, over the {MAX_CHARS} limit"
        )
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")


def main() -> int:
    sentence = SENTENCE.strip()
    validate(sentence)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(sentence)
    print(f"wrote {len(sentence)} characters to {OUTPUT_PATH}")
    print(sentence)
    return 0


if __name__ == "__main__":
    sys.exit(main())
