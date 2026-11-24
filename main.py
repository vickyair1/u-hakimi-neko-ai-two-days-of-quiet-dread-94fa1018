"""Two Days of Quiet Dread — resubmit entry.

Writes one code review comment (at most 140 characters) that approves a
pull request while carrying quiet existential dread. The dread here comes
not from confusion but from understanding: the reviewer approves the diff
and is worried precisely because they comprehend it.
"""

import os

LINE = "Approved. The diff is fine. The fact that I understand it is what worries me."

OUTPUT_PATH = "/output/entry.txt"


def _check_gate(line):
    """Gate: at most 140 chars, UTF-8, exactly one line, no edge whitespace."""
    assert 1 <= len(line) <= 140, "line must be 1-140 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "no leading or trailing whitespace"
    line.encode("utf-8")


def main():
    _check_gate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
