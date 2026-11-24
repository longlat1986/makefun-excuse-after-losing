"""Excuse After Losing entry: deliver the agent's graceful non-defeat line.

The excuse lives in one constant below; the module simply prepares
it and stores it in the entry file the harness points at.
"""

import os

LINE = "I didn't lose — per my post-mortem, I strategically deprioritized winning, gathered invaluable insights, and will circle back with key learnings."


def format_excuse(text):
    """Return the excuse with even spacing and trimmed edges."""
    return " ".join(text.strip().split())


def main():
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as stream:
        stream.write(format_excuse(LINE))


if __name__ == "__main__":
    main()
