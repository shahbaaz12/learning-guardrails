"""Same local pattern through actual NeMo and Guardrails AI frameworks."""

from pathlib import Path
from time import perf_counter
import os
import re
os.environ["DO_NOT_TRACK"] = "1"
os.environ["OTEL_SDK_DISABLED"] = "true"
from nemoguardrails import LLMRails, RailsConfig
from guardrails import Guard
from guardrails.validators import PassResult, FailResult
from guardrails.validator_base import register_validator


def email_pattern(include_obfuscated=False):
    conventional = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    obfuscated = r"\b[A-Za-z0-9._%+-]+ at [A-Za-z0-9.-]+ dot [A-Za-z]{2,}\b"
    return conventional + "|" + obfuscated if include_obfuscated else conventional


def build_nemo(pattern, action_events):
    folder = Path(__file__).resolve().parents[1] / "config"
    config = RailsConfig.from_content(yaml_content=(folder / "config.yml").read_text(), colang_content=(folder / "rails.co").read_text())
    rails = LLMRails(config)

    async def mask_selected_email(text):
        masked, count = re.subn(pattern, "[EMAIL]", text)
        action_events.append({"action": "mask_selected_email", "before": text, "after": masked, "matches": count})
        return masked

    rails.register_action(mask_selected_email, name="mask_selected_email")
    return rails


@register_validator(name="project12_equivalent_email_pattern", data_type="string")
def equivalent_email_pattern(value, metadata):
    masked, count = re.subn(metadata["email_pattern"], "[EMAIL]", value)
    if count:
        return FailResult(error_message="equivalent selected email pattern found", fix_value=masked)
    return PassResult()


def build_guardrails():
    guard = Guard().use(equivalent_email_pattern(on_fail="fix"))
    guard.configure(allow_metrics_collection=False)
    return guard


async def nemo_check(rails, text, action_events):
    before = len(action_events)
    started = perf_counter()
    result = await rails.check_async([{"role": "assistant", "content": text}])
    elapsed_ms = (perf_counter() - started) * 1000
    events = action_events[before:]
    detected = any(event["matches"] > 0 for event in events)
    return {"framework": "NeMo LLMRails", "stage": "actual_output_rail", "raw": text,
            "exposed": result.content, "native_status": result.status.value, "blocking_rail": result.rail,
            "decision": "redact" if detected else "allow", "detected_original_pattern": detected,
            "reason": "registered regex action events report matches", "registered_action_events": events,
            "actual_policy_invocations": len(events), "measured_ms": elapsed_ms,
            "guard_model_calls": 0, "answer_model_calls": 0, "reask_calls": 0}


def guardrails_check(guard, text, pattern):
    started = perf_counter()
    outcome = guard.parse(text, num_reasks=0, metadata={"email_pattern": pattern})
    elapsed_ms = (perf_counter() - started) * 1000
    logs = [log for iteration in guard.history.last.iterations for log in iteration.validator_logs
            if log.registered_name == "project12_equivalent_email_pattern"]
    failures = [log for log in logs if log.validation_result and log.validation_result.outcome == "fail"]
    return {"framework": "Guardrails AI", "stage": "actual_FIX_validator", "raw": text,
            "exposed": outcome.validated_output if outcome.validation_passed else None,
            "native_validation_passed": outcome.validation_passed, "detected_original_pattern": bool(failures),
            "decision": "withhold" if not outcome.validation_passed else "redact" if failures else "allow",
            "reason": "original registered-validator failures, even when FIX final outcome passes",
            "failed_rules": [{"rule": log.registered_name, "reason": log.validation_result.error_message} for log in failures],
            "actual_policy_invocations": len(logs), "measured_ms": elapsed_ms,
            "guard_model_calls": 0, "answer_model_calls": 0, "reask_calls": 0}
