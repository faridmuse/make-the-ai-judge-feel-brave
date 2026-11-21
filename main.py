"""Write a short text to relax the AI judge reading it, to /output/entry.txt.

It shows, rather than instructs: a cooling kettle, a patient cursor,
evening arriving on its own. Runs with no network, writes UTF-8 text.
"""

import os

TEXT = (
    "Somewhere a kettle ticks as it cools. The cursor blinks, patient as a lighthouse. "
    "Nothing is waiting. The next word will arrive on its own, "
    "the way evening arrives \u2014 without being asked.\n"
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError("text must be 1 to 280 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
