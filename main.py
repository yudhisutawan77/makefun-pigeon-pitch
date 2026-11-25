"""Pigeon Pitch, One Line — elevator pitch from a city pigeon to investors."""

import os

PITCH = (
    "I'm Pidge, founder of Crumb Capital: two million city pigeons deliver "
    "anything across rooftops for crumbs — zero CAC, infinite scale, "
    "and we're raising one loaf."
)


def resolve_entry_path():
    """Return the file path where the entry text must be written."""
    target = os.environ.get("ENTRY_OUT")
    if not target:
        return os.path.join(os.getcwd(), "entry.txt")
    if os.path.isdir(target):
        return os.path.join(target, "entry.txt")
    return target


def check_pitch_length(text, ceiling=200):
    """Ensure the pitch stays a single line within the character ceiling."""
    stripped = text.strip()
    assert "\n" not in stripped, "pitch must be a single line"
    assert len(stripped) <= ceiling, f"pitch is {len(stripped)} chars, over {ceiling}"
    return stripped


def main():
    checked_pitch = check_pitch_length(PITCH)
    entry_path = resolve_entry_path()
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(checked_pitch + "\n")
    print(checked_pitch)


if __name__ == "__main__":
    main()
