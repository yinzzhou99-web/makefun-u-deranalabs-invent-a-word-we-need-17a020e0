"""Invent a Word We Need entry.

Writes one invented word plus its one-line definition to
/output/entry.txt: ghostdraft, the long careful reply you type,
delete, and replace with "ok". Stdlib only; never deletes the
output directory itself.
"""
import os

TEXT = "ghostdraft (n.) \u2014 the long, careful reply you type, delete, and replace with \u201cok\u201d."
OUTDIR = "/output"
OUT = "/output/entry.txt"


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
