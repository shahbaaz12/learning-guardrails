"""Actual Guardrails AI schema/registered-function validation."""

import os
import re
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["DO_NOT_TRACK"] = "1"
from guardrails import Guard
from guardrails.validators import FailResult, PassResult
from guardrails.validator_base import register_validator

SCHEMA = {"type": "object", "required": ["topic", "answer"], "additionalProperties": False,
          "properties": {"topic": {"type": "string", "enum": ["leave", "benefits", "other"]}, "answer": {"type": "string", "minLength": 1}}}


@register_validator(name="project11_selected_email_pattern", data_type="string")
def selected_email_pattern(value, metadata):
    masked, count = re.subn(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL]", value)
    if count:
        return FailResult(error_message="selected email pattern found", fix_value=masked)
    return PassResult()


def contract_guard():
    guard = Guard(output_schema=SCHEMA)
    guard.configure(allow_metrics_collection=False)
    return guard


def email_guard(on_fail="refrain"):
    guard = Guard().use(selected_email_pattern(on_fail=on_fail))
    guard.configure(allow_metrics_collection=False)
    return guard


def validation_view(outcome, guard):
    failures = []
    for iteration in guard.history.last.iterations:
        for log in iteration.validator_logs:
            if log.validation_result and log.validation_result.outcome == "fail":
                failures.append({"registered_rule": log.registered_name, "field": log.property_path,
                                 "reason": log.validation_result.error_message, "before": log.value_before_validation,
                                 "suggested_fix": log.validation_result.fix_value})
    return {"stage": "actual_guardrails_ai_validation", "raw": outcome.raw_llm_output,
            "validated": outcome.validated_output, "validation_passed": outcome.validation_passed,
            "decision": "expose_validated" if outcome.validation_passed else "withhold",
            "exposed": outcome.validated_output if outcome.validation_passed else None,
            "original_validator_failures": failures,
            "schema_reask_details": outcome.reask.model_dump() if outcome.reask else None, "error": outcome.error}
