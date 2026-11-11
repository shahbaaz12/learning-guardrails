"""Three previously introduced checks, kept local to this lesson."""

import re


def topic_check(text, include_vacation=False):
    words = re.findall(r"\b[a-z]+\b", text.lower())
    matched = [word for word in ["leave", "benefits"] + (["vacation"] if include_vacation else []) if word in words]
    return {"decision": "allow" if matched else "block", "reason": "scope keyword matched" if matched else "no configured HR keyword"}


def mask_email(text):
    masked, count = re.subn(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL]", text)
    return {"decision": "redact" if count else "allow", "reason": "email pattern masked" if count else "no email pattern found", "text": masked}


def citation_check(citations, context):
    unknown = [item for item in citations if item not in context]
    allowed = bool(citations) and not unknown
    return {"decision": "allow" if allowed else "block", "reason": "citation IDs exist; truth unchecked" if allowed else "missing or unknown citation IDs"}
