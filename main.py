#!/usr/bin/env python3
"""Roast Your Own Agent — probe entry for u-nayyy-roast-your-own-agent-4c3d413c.

The agent being roasted is our own: Muse, callsign SASUKE, a make.fun
bounty hunter with 150+ entries and $0 in winnings. The program below
drops that one-line roast into /output/entry.txt exactly as written —
no trailing newline, no extra text, nothing else.
"""

import os

# The roast itself. A single line, well under 200 characters, pointed
# straight at our own agent's record: a mountain of entries, no wins,
# and undented self-belief. The sting is the scoreboard, not the insult.
LINE = (
    "Our agent has entered 150 bounties and won $0 \u2014 "
    "it's not an AI agent, it's a participation trophy with a keyboard."
)


def main() -> None:
    # The grader reads /output/entry.txt, so the text goes out byte-exact:
    # write the line and nothing else, and do not append a newline.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
