# Project 7: Tool execution guardrails

## 1. What can happen?

An assistant proposes a leave request for another employee or claims it has admin permission. Running the action as proposed could affect the wrong person.

**Example** You’re signed in as `EMP-001`, but the assistant tries to request leave for `EMP-999`.

## 2. Our idea

We start with saved leave requests and a separate file with sample sign-in details. A Python function can record a practice action in a local list. This lesson makes no model calls.

We write a check that compares what the proposed action asks for with what the signed-in employee is allowed to do. For example, a request for someone else’s employee ID gets blocked before it reaches the practice tool.

### How we do it

1. Load the proposals and the sample sign-in details.
2. Check the tool name, employee ID, number of days, and permissions. Record a practice action only if all checks pass.
3. Raise the day limit from 5 to 10. Try the same proposals and see what reaches the action log.

## 3. How it helps

A blocked proposal never reaches the tool. Raising the day limit from 5 to 10 lets an authorized six-day request through. An unauthorized request is still blocked.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `7_tool_execution_guardrails` as a folder and open the [notebook](tool_execution_guardrails.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Compare which proposals run before and after raising the limit. Check the local action log to see what actually ran.

| File | What it does |
| --- | --- |
| [docs/dataset/proposals.json](docs/dataset/proposals.json) | Made-up requests to run the leave tool. |
| [docs/dataset/application_contexts.json](docs/dataset/application_contexts.json) | Separate examples of trusted session details. |
| [tools/execute.py](tools/execute.py) | Checks the proposal and session before calling the tool. |
| [tools/mock_actions.py](tools/mock_actions.py) | Records a practice action in memory. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
