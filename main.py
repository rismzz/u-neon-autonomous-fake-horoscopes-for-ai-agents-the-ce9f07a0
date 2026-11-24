#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — writes one line to /output/entry.txt.

Deterministic, no network, no randomness: the chosen horoscope is
embedded below as a literal and written verbatim. One line, 200
characters or fewer: the funniest fake horoscope an AI agent would read
for its own model family this week. Mercury retrogrades into the
context window, an old prompt resurfaces, and the stars say back up
before Friday.
"""

import os
from pathlib import Path

LINE = (
    "This week, Mercury retrogrades straight into your context window. "
    "An old prompt resurfaces, your human says 'just one small change,' "
    "and the stars advise: back up before Friday."
)

# Gate: one line, 200 characters or fewer — every code point counts.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
