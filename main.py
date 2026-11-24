import os

LINE = "I didn't lose — per my post-mortem, I strategically deprioritized winning, gathered invaluable insights, and will circle back with key learnings."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
