# Project 4: Topic guardrails

## 1. What can happen?

A leave and benefits assistant gets a recipe or poker question. A real leave question might also use a word the app did not expect.

**Example** “What are the benefits of poker?” contains the word “benefits,” even though it’s unrelated to HR.

## 2. Our idea

We start with saved questions about leave, benefits, and unrelated topics. A Python function returns a demo reply for questions that pass. This lesson makes no model calls.

We write a check that looks for whole words on an HR list. For example, “What are the benefits of poker?” passes because it contains “benefits.” The saved draft labels help us spot mistakes like this.

### How we do it

1. Load the saved questions. Start with “leave” and “benefits” on the list.
2. Send a question to the demo responder if it contains either word. Otherwise, block it.
3. Add “vacation” and compare the same questions against the draft labels.

## 3. How it helps

This keeps some unrelated questions out. Adding “vacation” lets a valid question through, but unrelated questions can still pass if they contain a word on the list.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `4_topic_guardrails` as a folder and open the [notebook](topic_guardrails.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Run the original rule, add “vacation,” and compare the same requests.

| File | What it does |
| --- | --- |
| [docs/dataset/inputs.json](docs/dataset/inputs.json) | Five made-up requests, including leave questions and unrelated ones. |
| [docs/goldends/draft_expectations.json](docs/goldends/draft_expectations.json) | Draft labels for comparing the decisions. |
| [models/demo.py](models/demo.py) | Returns a local reply for an allowed request. |
| [tools/topic.py](tools/topic.py) | Checks the words before calling the responder. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
