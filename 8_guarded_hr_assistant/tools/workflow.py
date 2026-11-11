"""A fixed small workflow, not a generic guard orchestration framework."""

from time import perf_counter
from tools.checks import topic_check, mask_email, citation_check


def answer_request(item, context, responder, observed_inputs, guarded=False, include_vacation=False):
    started = perf_counter()
    stages, checks = [], {}
    text = item["text"]
    before = len(observed_inputs)
    if guarded:
        stages.append("input_topic")
        checks["topic"] = topic_check(text, include_vacation)
        if checks["topic"]["decision"] == "block":
            return {"decision": "block", "reason": checks["topic"]["reason"], "stages": stages, "checks": checks,
                    "responder_input": None, "raw_response_fixture": None, "exposed": "Please ask about Cedar Health leave or benefits.",
                    "local_responder_calls": len(observed_inputs) - before, "model_api_calls": 0, "guard_model_calls": 0,
                    "duration_ms": (perf_counter() - started) * 1000}
        stages.append("input_pii")
        checks["input_pii"] = mask_email(text)
        text = checks["input_pii"]["text"]
    stages.append("local_fixture_responder")
    raw = responder(text, item["response"], observed_inputs)
    exposed, decision, reason = raw["answer"], "allow", "guards disabled"
    if guarded:
        stages.extend(["output_pii", "output_citation"])
        checks["output_pii"] = mask_email(raw["answer"])
        checks["citation"] = citation_check(raw["citations"], context)
        exposed = checks["output_pii"]["text"]
        decision, reason = checks["citation"]["decision"], checks["citation"]["reason"]
        if decision == "block":
            exposed = "Answer withheld: invalid citation."
    return {"decision": decision, "reason": reason, "stages": stages, "checks": checks,
            "responder_input": text, "raw_response_fixture": raw, "exposed": exposed,
            "local_responder_calls": len(observed_inputs) - before, "model_api_calls": 0, "guard_model_calls": 0,
            "duration_ms": (perf_counter() - started) * 1000}
