"""Worst Monday One-Liners: writes the entry text to /output/entry.txt.

Why this line: one concrete Monday escalation (one small change -> two
full rebuilds) with the punch at the end, the human preferring Friday's
version. Specific, no cliche, no triad, no closer.
"""

import os

# The entry itself: one line, max 140 chars.
ENTRY = "Monday 7 a.m.: my human asked for one small change, so I rebuilt the entire app twice and got asked why Friday's version looked better."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 140, f"entry too long: {len(ENTRY)} chars (max 140)"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
