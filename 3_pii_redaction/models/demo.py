"""A deterministic local response fixture, never a model/API call."""


def demo_response(text):
    return f"Local demo received: {text} Contact hr@example.test for help."
