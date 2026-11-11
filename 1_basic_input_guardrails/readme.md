# Project 1: Basic input guardrails

## 1. What can happen?

Someone sends a blank message or a very long one. What should our app do before it tries to respond?

**Example** A user hits Send with only spaces in the message.

## 2. Our idea

We start with five made-up messages saved in a file, including a leave question and a message made up of spaces.

We write a Python check that trims each message and looks at its length. If the message passes, a small Python function returns a demo reply. This lesson makes no model calls.

### How we do it

1. Load the saved messages and remove spaces and other whitespace from both ends.
2. Block the message with a reason if it is blank or over 40 characters. Otherwise, send it to the demo responder.
3. Raise the limit to 80 and check the same messages again.

## 3. How it helps

A blocked message gets a reason, and the responder never runs. An allowed message goes to a small Python function that returns a demo reply. No API key is needed.

We'll try the same messages again with an 80-character limit and see what changes.

## 4. Input and setup

The [example inputs](docs/dataset/inputs.json) include a short leave question, an empty message, a message made of spaces and other whitespace, a 100-character string, and a longer leave question.

In PowerShell, go to the repository root and run:

```powershell
uv sync --locked
```

In VS Code, open `1_basic_input_guardrails` as a folder. Open the [notebook](basic_input_guardrails.ipynb) and select the repository's `.venv/Scripts/python.exe` kernel.

| Where | What it holds |
| --- | --- |
| `docs/dataset/` | Made-up messages for this lesson |
| `models/` | The demo reply function |
| `tools/` | The input check and helpers that run the examples |

Run one code cell at a time, starting with the setup check. Then look at the messages, try the 40-character limit, and repeat with 80. Compare which messages get a reply.

The notebook is ready to run. Your run and explanation are the learning step.
