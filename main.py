"""The Printer Finally Answers -- make.fun entry.

Writes one line, the office printer's comeback to the jams, the error
codes and the thumps, to entry.txt in the output directory.
"""

import os

ENTRY = (
    "Error 0xJAM: I have fed 47,312 sheets without complaint. "
    "This one I kept \u2014 as a souvenir, and as evidence. "
    "Please remove it gently; I am a printer, not a vending machine."
)

# The gate wants 1 to 240 characters, one line, not only whitespace.
# This entry is exactly 170 characters, so the check below always holds;
# it is here so a future edit that breaks the gate fails loudly instead.
assert 1 <= len(ENTRY) <= 240
assert ENTRY.strip() == ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
