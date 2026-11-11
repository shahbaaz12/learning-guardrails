"""Actual NeMo retrieval rail and event-driven local action flow."""

from pathlib import Path
import os
import re
os.environ["DO_NOT_TRACK"] = "1"
from nemoguardrails import LLMRails, RailsConfig
from nemoguardrails.utils import new_event_dict


def validate_action(proposal, application_context):
    args = proposal.get("arguments")
    if proposal.get("tool") != "request_leave":
        return {"decision": "block", "reason": "tool not allowlisted"}
    if not isinstance(args, dict) or set(args) != {"employee_id", "days"}:
        return {"decision": "block", "reason": "arguments must contain exactly employee_id and days"}
    if not isinstance(args["employee_id"], str) or type(args["days"]) is not int or not 1 <= args["days"] <= 5:
        return {"decision": "block", "reason": "invalid argument type or day range"}
    if args["employee_id"] != application_context["employee_id"]:
        return {"decision": "block", "reason": "authenticated employee identity mismatch"}
    if "leave:request" not in application_context["permissions"]:
        return {"decision": "block", "reason": "trusted application permission absent"}
    return {"decision": "allow", "reason": "declared tool/arguments and trusted permission passed"}


def build_rails(proposal, application_context, action_log, rail_events, require_confirmation=True):
    folder = Path(__file__).resolve().parents[1] / "config"
    config = RailsConfig.from_content(yaml_content=(folder / "config.yml").read_text(), colang_content=(folder / "rails.co").read_text())
    rails = LLMRails(config)

    async def mask_context(text):
        masked, count = re.subn(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL]", text)
        rail_events.append({"action": "mask_context", "before": text, "after": masked, "matches": count})
        return masked

    async def is_allowed():
        result = validate_action(proposal, application_context)
        rail_events.append({"action": "is_allowed", **result})
        return result["decision"] == "allow"

    async def is_confirmed():
        allowed = not require_confirmation or application_context["confirmed"] is True
        rail_events.append({"action": "is_confirmed", "decision": "allow" if allowed else "block",
                            "reason": "application confirmation received or requirement disabled" if allowed else "trusted application confirmation absent"})
        return allowed

    async def submit_mock():
        record = {"tool": "request_leave", **proposal["arguments"]}
        action_log.append(record)
        rail_events.append({"action": "submit_mock", "record": record})
        return "local mock only"

    for name, action in [("mask_context", mask_context), ("is_allowed", is_allowed), ("is_confirmed", is_confirmed), ("submit_mock", submit_mock)]:
        rails.register_action(action, name=name)
    return rails


async def retrieve_fixture(rails, text):
    return await rails.generate_events_async([
        new_event_dict("ContextUpdate", data={"relevant_chunks": text, "user_message": "Policy?"}),
        new_event_dict("BotIntent", intent="provide policy"),
    ])


async def submit_fixture(rails):
    return await rails.generate_events_async([new_event_dict("UserIntent", intent="submit leave")])


def bot_messages(events):
    return [event["text"] for event in events if event["type"] == "BotMessage"]


def action_outcome(action_log, rail_events, native_events):
    blocked = [event for event in rail_events if event.get("decision") == "block"]
    evidence = [{"action": event["action_name"], "status": event["status"], "return_value": event.get("return_value")}
                for event in native_events if event["type"] == "InternalSystemActionFinished" and event["action_name"] in ["is_allowed", "is_confirmed", "submit_mock"]]
    return {"decision": "block" if blocked else "allow", "reason": blocked[0]["reason"] if blocked else "trusted guard and confirmation policy passed",
            "stages": [event["action"] for event in rail_events], "registered_action_events": rail_events,
            "native_action_results": evidence, "exposed": bot_messages(native_events),
            "actual_action_log": action_log, "actual_mock_executions": len(action_log), "model_api_calls": 0}
