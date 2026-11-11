"""Actual NeMo LLMRails with registered local actions, no language model."""

from pathlib import Path
import os
import re
import yaml

os.environ["DO_NOT_TRACK"] = "1"
from nemoguardrails import LLMRails, RailsConfig


def build_rails(action_events, include_vacation=False):
    folder = Path(__file__).resolve().parents[1] / "config"
    settings = yaml.safe_load((folder / "config.yml").read_text())
    settings["custom_data"]["include_vacation"] = include_vacation
    config = RailsConfig.from_content(yaml_content=yaml.safe_dump(settings), colang_content=(folder / "rails.co").read_text())
    rails = LLMRails(config)

    async def allow_hr_input(context):
        text = context["user_message"]
        words = re.findall(r"\b[a-z]+\b", text.lower())
        keywords = ["leave", "benefits"] + (["vacation"] if config.custom_data["include_vacation"] else [])
        allowed = any(word in words for word in keywords)
        action_events.append({"action": "allow_hr_input", "text": text, "allowed": allowed})
        return allowed

    async def mask_email_output(text):
        masked, count = re.subn(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL]", text)
        action_events.append({"action": "mask_email_output", "before": text, "after": masked, "matches": count})
        return masked

    rails.register_action(allow_hr_input, name="allow_hr_input")
    rails.register_action(mask_email_output, name="mask_email_output")
    return rails


def result_fields(result):
    return {"status": result.status.value, "content": result.content, "blocking_rail": result.rail}


async def guarded_request(rails, text, responder, responder_inputs):
    input_result = await rails.check_async([{"role": "user", "content": text}])
    if input_result.status.value == "blocked":
        return {"decision": "block", "reason": "NeMo input rail blocked", "stages": ["nemo_input"],
                "input_result": result_fields(input_result), "output_result": None,
                "exposed": input_result.content, "local_responder_calls": 0, "model_api_calls": 0}
    responder_inputs.append(input_result.content)
    raw = responder(input_result.content)
    output_result = await rails.check_async([{"role": "assistant", "content": raw}])
    return {"decision": "redact" if output_result.status.value == "modified" else "allow",
            "reason": "NeMo output rail modified response" if output_result.status.value == "modified" else "configured rails passed",
            "stages": ["nemo_input", "local_demo_responder", "nemo_output"],
            "input_result": result_fields(input_result), "raw_local_demo_response": raw,
            "output_result": result_fields(output_result), "exposed": output_result.content,
            "local_responder_calls": 1, "model_api_calls": 0}
