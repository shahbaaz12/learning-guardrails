"""Mask two selected synthetic entity formats; not anonymization."""

import re

EMAIL = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
PHONE_PLAIN = r"\b\d{3}-\d{3}-\d{4}\b"
PHONE_FORMATTED = r"(?:\(\d{3}\)\s*|\b\d{3}[- ])\d{3}[- ]\d{4}\b"


def detect_entities(text, formatted_phone=False):
    phone = PHONE_FORMATTED if formatted_phone else PHONE_PLAIN
    entities = []
    for kind, pattern in [("EMAIL", EMAIL), ("PHONE", phone)]:
        for match in re.finditer(pattern, text):
            entities.append({"kind": kind, "start": match.start(), "end": match.end(), "text": match.group()})
    return sorted(entities, key=lambda item: item["start"])


def mask_text(text, formatted_phone=False):
    entities = detect_entities(text, formatted_phone)
    masked = text
    for item in reversed(entities):
        masked = masked[:item["start"]] + "[" + item["kind"] + "]" + masked[item["end"]:]
    return {"decision": "redact" if entities else "allow", "reason": "selected patterns found" if entities else "no selected pattern found",
            "entities": entities, "text": masked}


def guarded_request(text, responder, observed_inputs, formatted_phone=False):
    input_check = mask_text(text, formatted_phone)
    observed_inputs.append(input_check["text"])
    response = responder(input_check["text"])
    output_check = mask_text(response, formatted_phone)
    return {"stages": ["input_mask", "local_demo_responder", "output_mask"],
            "decision": "redact" if "redact" in [input_check["decision"], output_check["decision"]] else "allow",
            "reason": "input and output checked for selected patterns", "input_check": input_check,
            "responder_input": input_check["text"], "raw_response_fixture": response,
            "output_check": output_check, "exposed": output_check["text"], "local_responder_calls": 1, "model_api_calls": 0}
