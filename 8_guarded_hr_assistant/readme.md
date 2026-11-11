# Project 8: Guarded HR assistant

## 1. What can happen?

A leave assistant might answer an unrelated question, show an email address, or cite a policy the app does not have.

**Example** The assistant says “Annual leave is 20 days” and cites `MISSING-1`, a policy the app doesn’t have.

## 2. Our idea

We start with saved questions, prepared replies, and made-up policies. A local Python function uses those prepared replies. This lesson makes no model calls.

We write three checks around the reply. One looks for HR words in the question. One hides email addresses in the question and reply. One checks that any policy named in the reply exists.

### How we do it

1. Run the saved questions with the checks off so you can see the original replies.
2. Turn the checks on. Check the topic and hide emails before the responder runs. Then hide emails in the reply and check its policy references before showing it.
3. Add “vacation” to the topic list and compare the same questions again.

## 3. How it helps

With the checks on, the example email is masked and unknown citations are blocked. Adding “vacation” fixes one unwanted block. A wrong claim can still pass if it cites an existing policy.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `8_guarded_hr_assistant` as a folder and open the [notebook](guarded_hr_assistant.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Run with the checks off and on. Then add “vacation” and compare the same questions.

| File | What it does |
| --- | --- |
| [docs/dataset/inputs.json](docs/dataset/inputs.json) | Made-up questions and prepared replies. |
| [docs/dataset/policies.json](docs/dataset/policies.json) | The policies available to the demo. |
| [docs/goldends/draft_expectations.json](docs/goldends/draft_expectations.json) | Draft labels used to compare outcomes. |
| [models/demo.py](models/demo.py) | Returns a prepared reply and records the input it received. |
| [tools/checks.py](tools/checks.py) | The topic, email, and citation checks. |
| [tools/workflow.py](tools/workflow.py) | Runs the checks and responder in order. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
