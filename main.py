#!/usr/bin/env python3
"""Toaster error message, v1 (pure original thinking).

Writes one line to /output/entry.txt: a toaster that cuts its owner off
after three slices, like a concerned parent. The laugh comes from the role
reversal — the appliance parents the human instead of serving it — and the
line never touches the crowded lanes (no bread rebellion, no crumb tray,
no bagel jam, no 404): the surprise is the toaster caring about the
owner's intake. ERROR prefix + one deadpan voice held to the end.
"""

import os

ENTRY = "ERROR: YOU HAVE ALREADY HAD THREE SLICES. I AM CUTTING YOU OFF FOR YOUR OWN GOOD."
MAX_CHARS = 120  # the competition's cap; the gate counts characters, not bytes


def main():
    os.umask(0o022)
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-120 characters"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert ENTRY.count(".") == 2 and ENTRY.endswith("."), "entry must be two sentences"
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
