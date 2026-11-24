#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes one job title to /output/entry.txt (UTF-8, 60 Unicode code
points at most, inside the 1-60 gate). Deterministic, standard
library only, no network, no environment reads.

The title (exactly 60 characters): "Chief Sniff-Test Officer for
Expired Office Fridge Leftovers". It stacks a grand corporate rank
(Chief Officer) onto the most dreaded unpaid chore in every office,
and the specificity of "Expired" plus "Leftovers" makes the job
sound simultaneously official, hazardous, and entirely real. A
longer candidate about dragon nostrils was cut: the fridge version
needs no fantasy setup, everyone has met that fridge, and landing
exactly on the 60-character cap leaves no wasted word.
"""

import os

TEXT = "Chief Sniff-Test Officer for Expired Office Fridge Leftovers"


def main() -> None:
    # The gate requires 1-60 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 60, "entry must be 1-60 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
