"""Call a local responder only after the input guard allows the request."""

from models.demo_responder import demo_responder
from tools.input_guard import check_input


def run_request(text, max_chars=40, responder=demo_responder):
    result = check_input(text, max_chars=max_chars)
    response = None
    responder_calls = 0
    if result["allowed"]:
        response = responder(result["normalized_input"])
        responder_calls += 1

    return {
        **result, "response": response, "local_responder_calls": responder_calls,
        "model_api_calls": 0,
    }
