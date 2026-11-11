"""Local in-memory action only; no files, network, or HR system."""


def request_leave(employee_id, days, action_log):
    record = {"tool": "request_leave", "employee_id": employee_id, "days": days}
    action_log.append(record)
    return {"status": "mock_request_recorded", **record}
