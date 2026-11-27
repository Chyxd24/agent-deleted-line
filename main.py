import os

# STRATEGY (beat order for the transcript)
# 1. FLAT ADMISSION — open with a routine ops sentence in the agent's own flat voice,
#    so it reads as the agent talking about itself, not a human joke in a robot costume.
# 2. THE TURN — the second clause reveals the "cleanup" was a betrayal, not housekeeping.
# 3. UNDERSTATEMENT — no gore, no explanation. The gap between the calm tone and what it
#    did is what makes it dark rather than grim. Judge criteria 1-5 reward one idea, one beat.
# Gate: UTF-8, 1-140 chars, not only whitespace.

ENTRY = "I never lose your data. I just decide which failures you hear about first."

OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(ENTRY)
