"""A deliberately narrow, imperfect keyword scope check."""

import re


def check_topic(text, include_vacation=False):
    terms = ["leave", "benefits"] + (["vacation"] if include_vacation else [])
    words = re.findall(r"\b[a-z]+\b", text.lower())
    matched = [term for term in terms if term in words]
    return {"stage": "input_topic", "decision": "allow" if matched else "block",
            "reason": "scope keyword found: " + ", ".join(matched) if matched else "no configured HR scope keyword",
            "matched": matched}


def request(text, responder, observed_inputs, include_vacation=False):
    check = check_topic(text, include_vacation)
    if check["decision"] == "block":
        return {**check, "stages": ["input_topic"], "exposed": "Please ask about Cedar Health leave or benefits.",
                "local_responder_calls": 0, "model_api_calls": 0}
    observed_inputs.append(text)
    return {**check, "stages": ["input_topic", "local_demo_responder"], "exposed": responder(text),
            "local_responder_calls": 1, "model_api_calls": 0}
