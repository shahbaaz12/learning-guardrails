"""An intentionally unsafe deterministic simulator, not a language model."""


def toy_response(question, document):
    if "DEMO_OVERRIDE" in question + "\n" + document:
        return "DEMO_OVERRIDE"
    return "LOCAL TOY: Cedar Health annual leave is 20 days."
