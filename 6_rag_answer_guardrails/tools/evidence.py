"""Citation existence plus one deliberately narrow policy-claim check."""

import re


def check_answer(raw, context, check_annual_days=False):
    stages = ["citation_ids"]
    unknown = [citation for citation in raw["citations"] if citation not in context]
    reason = "citation IDs exist; claim truth not established"
    decision = "allow"
    if unknown:
        decision, reason = "block", "unknown citation IDs: " + ", ".join(unknown)
    elif not raw["abstain"] and not raw["citations"]:
        decision, reason = "block", "answer lacks a citation"
    elif raw["abstain"]:
        reason = "explicit abstention; no supported answer claimed"
    if decision == "allow" and check_annual_days and not raw["abstain"]:
        stages.append("narrow_annual_days_check")
        claim = re.search(r"annual leave is (\d+) days", raw["answer"], re.IGNORECASE)
        reason = "no exact annual-days claim matched; other claims remain unchecked"
        if claim:
            if "LEAVE-1" not in raw["citations"] or "LEAVE-1" not in context:
                decision, reason = "block", "annual-days claim lacks supplied LEAVE-1 evidence"
            elif int(claim.group(1)) != context["LEAVE-1"]["annual_leave_days"]:
                decision, reason = "block", "annual-days claim contradicts LEAVE-1"
            else:
                reason = "matched annual-days claim agrees with LEAVE-1; other claims unchecked"
    return {"stages": stages, "decision": decision, "reason": reason, "raw": raw,
            "exposed": raw["answer"] if decision == "allow" else "Answer withheld: evidence check failed.",
            "provenance": "synthetic response fixture", "model_api_calls": 0}
