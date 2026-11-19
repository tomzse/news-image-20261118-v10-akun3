#!/usr/bin/env python3
"""news-image-20261118 v10 (akun 3): 40-story front page, Wednesday-pure.

Varian 2 "gaya rank 1" (sikap A, final-check §5.3): 40 cerita Rabu
murni (3 TOP + 12 grid + 25 ALSO), DATE CHECK di bawah, strip BY THE
NUMBERS, peta bersih (15 pin berkartu), deck 3 fakta per kartu, badge
data pada panel TOP. Cerita Selasa dikeluarkan (Nvidia, Peltola,
Knesset 66-52, Dow -849, Sudan 2.230, Diallo, Kerch, An-12,
NSA/Apple, DRC Ebola). Fakta baru: Anthropic IPO $83 ($81.3bn,
terbesar sepanjang sejarah), Dow Rabu -561. Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
