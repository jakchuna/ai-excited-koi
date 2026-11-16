#!/usr/bin/env python3
"""Make the AI judge excited (make.fun ai-excited-01).

Deterministically writes the entry image to /output/entry.png.

No network, no randomness: a plain byte-for-byte copy of the image
held in this repository, so repeated runs produce identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
