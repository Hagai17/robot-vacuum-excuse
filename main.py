"""The Robot Vacuum's Best Excuse — make.fun entry.

The winning line was picked from 11 drafts in candidates.md, duel-scored
against the kit's published judge brief (a tired homeowner): on-topic
excuse first, then laugh size, then rootedness in the vacuum's own world
(map, clean log, sensors), a clean turn on the final word, and the
vacuum's own deadpan voice. The winner keeps the blame-shift laugh of
the strongest pure-joke draft but grounds it in the machine's own
bookkeeping — 214 logged cleans and a map that renamed the floor.
"""

ENTRY = "I have cleaned that spot 214 times. It re-dirties within the hour. My map no longer calls it a floor. It calls it a subscription."


def check_gate():
    """The sealed gate accepts UTF-8 text of 1 to 140 characters."""
    assert 1 <= len(ENTRY) <= 140, "entry outside the 1-140 character gate"
    assert ENTRY.strip(), "entry must not be only white space"

def write_entry():
    """Write the entry to /output/entry.txt (no trailing newline)."""
    import os

    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


check_gate()
print(ENTRY)
write_entry()
