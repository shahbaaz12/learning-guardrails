# Project 11: Guardrails AI validation

## 1. What can happen?

An assistant reply might have missing JSON fields or contain an email address the app should hide.

**Example** The reply is `{"answer": "Ask HR."}`. The required `topic` field is missing.

## 2. Our idea

We start with six made-up replies saved in a file. The main lesson runs locally on those samples. The retry also uses a prepared reply.

We give Guardrails AI rules for the fields a reply must contain and write a separate email check. For example, if a reply contains a matching email, we can tell Guardrails AI to hold back the reply or to hide the address and show the rest.

The optional final cell calls a model through Groq for a fresh reply, then checks its required fields. That cell is off by default.

### How we do it

1. Load the saved replies and check which ones have the required fields.
2. Run the email check twice. First hold back replies with matches, then mask the addresses instead.
3. Try one prepared replacement for an invalid reply. Show it only if it passes.

## 3. How it helps

The lesson shows what failed, what the user sees, and what the check fixed. It also shows one retry using a prepared reply. If that reply still fails, the result stays hidden.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `11_guardrails_ai_validation` as a folder and open the [notebook](guardrails_ai_validation.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Start with the sample replies. Compare withholding and masking on the same text, then try the single local retry.

| File | What it does |
| --- | --- |
| [docs/dataset/outputs.json](docs/dataset/outputs.json) | Made-up replies with valid and invalid examples. |
| [tools/validation.py](tools/validation.py) | Builds the checks and shows the original and checked results. |

The default lesson runs locally and needs no API key.

### Optional Groq exercise

The last cell uses [the prompt](prompts/answer.txt) and [the Groq loader](models/groq_model.py) to check a live reply. It is off by default. To try it, set `GROQ_API_KEY` in the repository root's `.env` and change `RUN_LIVE` to `True`. The live path has yet to be verified.

The notebook is ready for your own run and explanation.
