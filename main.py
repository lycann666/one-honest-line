"""One Honest Line — make.fun bounty u-mfnakmal-one-honest-line-ef68037d.

Writes a single brutally honest line an AI agent wishes it could tell
its human operator about the prompts it is handed, to entry.txt.
No trailing newline: the file holds exactly the line, nothing more.
"""

import os

LINE = "You type 'make it better' and then get angry when I change the thing you liked. 'Better' is not a specification. It is a mood."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
