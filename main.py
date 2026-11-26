"""Funniest Forecast for a City That Isn't.

Writes a single-line weather forecast for the invented city of Blorptown
to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR, or /output).
"""

import os

LINE = (
    "Blorptown: tomorrow brings 40% rain, 60% frogs, "
    "and a 100% chance the mayor blames the clouds."
)


def main():
    assert 1 <= len(LINE) <= 120, "entry line must be 1-120 characters"
    assert LINE.strip() == LINE and LINE.strip(), "entry line must be non-blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
