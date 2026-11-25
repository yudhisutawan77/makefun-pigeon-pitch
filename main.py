"""Pigeon Pitch, One Line — a city pigeon's elevator pitch to investors."""

import os

PITCH = (
    "I'm Pidge, founder of Crumb Capital: two million city pigeons deliver "
    "anything across rooftops for crumbs — zero CAC, infinite scale, "
    "and we're raising one loaf."
)


def resolve_entry_targets():
    """Resolve output targets in priority order.

    ENTRY_OUT wins, then MAKEFUN_OUTPUT_DIR, then /output/entry.txt,
    with the working directory as the last resort. A value naming a
    directory means entry.txt inside it; a value naming a file is used
    as-is.
    """
    resolved = []
    for name in ("ENTRY_OUT", "MAKEFUN_OUTPUT_DIR"):
        raw = os.environ.get(name)
        if not raw:
            continue
        if os.path.isdir(raw):
            resolved.append(os.path.join(raw, "entry.txt"))
        else:
            resolved.append(raw)
    resolved.append("/output/entry.txt")
    resolved.append(os.path.join(os.getcwd(), "entry.txt"))
    return resolved


def validate_pitch_line(text, ceiling=200):
    """Ensure the pitch stays a single line within the character ceiling."""
    cleaned = text.strip()
    assert "\n" not in cleaned, "pitch must be a single line"
    assert len(cleaned) <= ceiling, f"pitch is {len(cleaned)} chars, over {ceiling}"
    return cleaned


def write_entry_file(target_path, pitch_text):
    """Write the pitch to one target; return the OSError, or None."""
    parent = os.path.dirname(target_path)
    try:
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as handle:
            handle.write(pitch_text + "\n")
    except OSError as exc:
        return exc
    return None


def main():
    pitch_text = validate_pitch_line(PITCH)
    last_error = None
    for target_path in resolve_entry_targets():
        last_error = write_entry_file(target_path, pitch_text)
        if last_error is None:
            print(pitch_text)
            return
    raise last_error


if __name__ == "__main__":
    main()
