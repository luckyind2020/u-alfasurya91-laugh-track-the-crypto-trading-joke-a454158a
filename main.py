"""Laugh Track: The Crypto Trading Joke Contest.

Entry point: reads the one-line crypto trading joke from entry.txt
and prints it to stdout.
"""

import sys
from pathlib import Path

ENTRY_FILE = "entry.txt"


def fetch_joke() -> str:
    here = Path(__file__).resolve().parent
    text = (here / ENTRY_FILE).read_text(encoding="utf-8")
    return text.strip()


def main() -> int:
    print(fetch_joke())
    return 0


if __name__ == "__main__":
    sys.exit(main())
