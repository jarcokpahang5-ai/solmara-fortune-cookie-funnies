"""Fortune Cookie Funnies for Engineers -- make.fun entry.

Holds one original fortune-cookie line for a software engineer, at
most 120 characters. The program checks the line, prints it, and writes
it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

FORTUNE = (
    "One day your code will be legacy, your comments will be "
    "scripture, and your TODO will be someone else's problem."
)

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def build_line():
    """Return the fortune line, checked as one line of at most 120 chars."""
    line = FORTUNE
    assert isinstance(line, str)
    assert "\n" not in line and "\r" not in line, "fortune must be a single line"
    assert line.strip(), "fortune must not be blank"
    assert 1 <= len(line) <= MAX_CHARS, (
        "fortune is %d characters, over the 120 limit" % len(line)
    )
    return line


def main():
    line = build_line()
    print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
