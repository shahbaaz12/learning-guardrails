"""Copy labelled fixture responses and record the actual local input."""


def fixture_response(text, response, observed_inputs):
    observed_inputs.append(text)
    return {"answer": response["answer"].replace("{input}", text), "citations": list(response["citations"])}
