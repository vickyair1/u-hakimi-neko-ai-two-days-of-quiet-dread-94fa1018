#!/usr/bin/env python3
"""Write the approved-with-dread review comment to /output/entry.txt.

Entry for the make.fun bounty "Two Days of Quiet Dread"
(u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018): one single-line code
review comment, at most 140 characters, that approves a pull request while
carrying quiet existential dread.
"""

import argparse

LINE = "Approved. The comment says 'do not touch', the diff touches it anyway, and the person who wrote it left in March."


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the review comment to entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path of the file to write (default: /output/entry.txt).",
    )
    args = parser.parse_args()
    # Gate: one line, 1-140 characters, not only whitespace.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
