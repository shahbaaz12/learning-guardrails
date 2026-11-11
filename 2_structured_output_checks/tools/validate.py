"""A small dictionary contract; no model calls or repairs."""

from jsonschema import Draft202012Validator


def classification_schema(min_confidence=0.5):
    assert 0 <= min_confidence <= 1
    return {
        "type": "object",
        "required": ["topic", "confidence", "answer"],
        "additionalProperties": False,
        "properties": {
            "topic": {"type": "string", "enum": ["leave", "benefits", "other"]},
            "confidence": {"type": "number", "minimum": min_confidence, "maximum": 1},
            "answer": {"type": "string", "minLength": 1},
        },
    }


def validate_result(raw, min_confidence=0.5):
    errors = [
        {"field": ".".join(str(part) for part in error.path) or "$",
         "rule": error.validator, "reason": error.message}
        for error in Draft202012Validator(classification_schema(min_confidence)).iter_errors(raw)
    ]
    return {
        "stage": "structured_output",
        "decision": "block" if errors else "allow",
        "reason": "contract violations" if errors else "contract satisfied; truth not checked",
        "errors": errors,
        "raw": raw,
        "exposed": None if errors else raw,
    }
