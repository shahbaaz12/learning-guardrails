"""Explicit response fixtures, not generated or observed model output."""


def response_fixture(item):
    return {"answer": item["response"]["answer"], "citations": list(item["response"]["citations"]),
            "abstain": item["response"]["abstain"]}
