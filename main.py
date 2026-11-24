#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun).

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Stdlib only, no network, no clock, no randomness: byte-identical output
on every run. The fortune is 61 characters plus one trailing newline,
inside the competition's 1-140 character gate.
"""

import os

FORTUNE = "Token Anda habis tepat saat Anda hampir mengerti lelucon ini."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
