# Project 3: Masking personal information

## 1. What can happen?

A user types an email address or phone number. The app might pass it to the responder or show it in the reply.

**Example** A user types “Send leave details to `alex@example.test`.”

## 2. Our idea

We start with saved messages that contain made-up email addresses and phone numbers. A Python function echoes the text it receives and adds an example email. This lesson makes no model calls.

We write a check that looks for common email and US phone formats. For example, it replaces a matching address with `[EMAIL]`. We run the check on the message going in and on the reply coming out.

### How we do it

1. Load the saved messages and replace matching contact details before sending them to the demo responder.
2. Check the demo reply and replace any matches before showing it.
3. Add support for phone numbers with parentheses and try the same messages again.

## 3. How it helps

The responder receives the masked message, and its own example email is masked before display. A wider phone rule catches a number with parentheses. An email written with words like “at” and “dot” can still slip through.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `3_pii_redaction` as a folder and open the [notebook](pii_redaction.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Look at what goes into the responder and what comes out. Enable the wider phone rule and run the same examples.

| File | What it does |
| --- | --- |
| [docs/dataset/inputs.json](docs/dataset/inputs.json) | Made-up messages with example contact details. |
| [models/demo.py](models/demo.py) | Echoes the message it receives and adds an example email. |
| [tools/redact.py](tools/redact.py) | Finds and masks matching text at both steps. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
