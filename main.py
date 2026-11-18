"""news-image-20261118 — sum up 18 November 2026 world news in one image.

The entry image (entry.png, a 1024x1024 PNG newspaper front page for
Wednesday 18 November 2026) is held in this repository. This program
copies it byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png.

Standard library only, no network, no clock, no randomness: two runs
write identical bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Byte-for-byte copy, so the output is identical on every run.
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    print("wrote entry.png")


if __name__ == "__main__":
    main()
