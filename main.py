# Writes the one error line to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "Your upload didn't fail — our storage did. The file is safe on your device; we're rebooting the bucket it was supposed to land in. Try again in five minutes."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
