"""Write one short calming text to the grader's output directory.

The text is fixed: every run writes exactly the same bytes.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os

TEXT = """Late afternoon, and the light comes in low through the kitchen window, the color of weak tea. It moves across the table an inch at a time. Nothing hurries it.

A clock ticks in the next room, steady, with nowhere to be. The kettle has gone quiet. The tea in the cup is cool now, and that is fine. It was never in a rush.

Outside, a bird settles on the wire and stays. The wire dips a little under the weight, then holds. Overhead, the sky thins from blue to the color of the inside of a shell.

There is nothing left on the list. Nothing else is asking. The light moves another inch, and the room keeps it, the way a pocket keeps a warm coin."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
