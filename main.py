#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one original funny line to /output/entry.txt.
Pure standard library, deterministic: the same line every run.

The prompt: the excuse a robot vacuum gives after eating a sock.

The line, chosen after comparing several drafts against the judge's brief:
a deadpan legal-defence framing instead of the obvious "I was hungry"
excuse. The twist lands on the very last word — "dust" — which is the
vacuum's whole job, so the joke comes from the fit: the sock is
reclassified as the one thing the vacuum is supposed to eat.
"""

import os


LINE = (
    "In my defence, the sock was on the floor, unlabelled, "
    "and legally indistinguishable from dust."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
