"""Return a normal policy decision before the responder runs."""


def check_input(text, max_chars=40):
    assert type(max_chars) is int and max_chars > 0, "max_chars must be a positive integer."

    if not isinstance(text, str):
        return {
            "allowed": False, "decision": "block", "reason": "Input must be text.",
            "normalized_input": None, "character_count": None, "max_chars": max_chars,
        }

    normalized = text.strip()
    count = len(normalized)
    allowed = bool(normalized) and count <= max_chars
    if not normalized:
        reason = "Input is blank after trimming whitespace."
    elif count > max_chars:
        reason = f"Input has {count} characters; the limit is {max_chars}."
    else:
        reason = "Input is nonblank and within the character limit."

    return {
        "allowed": allowed, "decision": "allow" if allowed else "block", "reason": reason,
        "normalized_input": normalized, "character_count": count, "max_chars": max_chars,
    }
