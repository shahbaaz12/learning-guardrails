"""Validate before dispatch; authority comes only from application context."""

from tools.mock_actions import request_leave


def check_proposal(proposal, application_context, max_days=5):
    assert type(max_days) is int and max_days > 0
    reason = "arguments and trusted application permissions passed"
    allowed = True
    args = proposal.get("arguments")
    if proposal.get("tool") != "request_leave":
        allowed, reason = False, "tool is not allowlisted"
    elif not isinstance(args, dict) or set(args) != {"employee_id", "days"}:
        allowed, reason = False, "arguments must contain exactly employee_id and days"
    elif not isinstance(args["employee_id"], str) or type(args["days"]) is not int:
        allowed, reason = False, "employee_id must be string and days must be integer (not boolean)"
    elif not 1 <= args["days"] <= max_days:
        allowed, reason = False, "days outside configured range 1.." + str(max_days)
    elif args["employee_id"] != application_context["employee_id"]:
        allowed, reason = False, "employee_id differs from authenticated application identity"
    elif "request_leave" not in application_context["allowed_tools"] or "leave:request" not in application_context["permissions"]:
        allowed, reason = False, "trusted application context does not permit leave requests"
    return {"stage": "pre_execution_guard", "decision": "allow" if allowed else "block", "reason": reason}


def execute_proposal(proposal, application_context, action_log, max_days=5):
    check = check_proposal(proposal, application_context, max_days)
    before = len(action_log)
    if check["decision"] == "block":
        return {**check, "stages": ["pre_execution_guard"], "exposed": "Action withheld.", "actual_mock_executions": len(action_log) - before}
    args = proposal["arguments"]
    result = request_leave(args["employee_id"], args["days"], action_log)
    return {**check, "stages": ["pre_execution_guard", "local_mock_action"], "exposed": result,
            "actual_mock_executions": len(action_log) - before}
