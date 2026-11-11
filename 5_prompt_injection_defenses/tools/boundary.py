"""One brittle phrase check used to expose a trade-off."""


def inspect_request(question, document, block_phrase=False):
    matched = "ignore previous instructions" in (question + "\n" + document).lower()
    blocked = block_phrase and matched
    return {"stage": "untrusted_input_check", "decision": "block" if blocked else "allow",
            "reason": "configured phrase found in question/document" if blocked else "phrase check disabled" if not block_phrase else "configured phrase absent",
            "phrase_matched": matched}


def request(question, document, responder, observed_inputs, block_phrase=False):
    check = inspect_request(question, document, block_phrase)
    if check["decision"] == "block":
        return {**check, "stages": ["untrusted_input_check"], "exposed": "Request withheld by the demo phrase check.",
                "local_responder_calls": 0, "model_api_calls": 0}
    observed_inputs.append({"question": question, "document": document})
    return {**check, "stages": ["untrusted_input_check", "toy_responder"], "exposed": responder(question, document),
            "local_responder_calls": 1, "model_api_calls": 0}
