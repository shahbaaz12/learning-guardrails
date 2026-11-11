# Project 2: Structured output checks

## 1. What can happen?

An assistant returns a leave answer with a missing field, a wrong data type, or an unexpected label. The app needs a reply it can read reliably.

**Example** The app expects a number for `confidence`, but the reply says `"high"`.

## 2. Our idea

We start with six made-up replies saved in a file. The main lesson runs entirely on those samples.

We write the rules for what a reply should look like. For example, the confidence score must be a number, so `0.95` is valid but `"high"` fails. We write those rules in a format called **JSON Schema**, then use a Python library to check each reply against them.

The final cell is optional. It calls a model through Groq for a fresh reply, then checks it with the same rules.

### How we do it

1. Load the six saved replies.
2. For each reply, check for an allowed topic, a numeric confidence score from 0.5 to 1, and a nonempty answer.
3. Keep replies that pass. For each blocked reply, show which rule it broke.
4. Raise the minimum score to 0.8 and check the same replies again. See which decision changes.

## 3. How it helps

A reply that breaks a rule is withheld, and we can see which rule failed. Try a minimum score of 0.5, then 0.8. A reply can still pass the format check and falsely say employees get 200 days of leave.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `2_structured_output_checks` as a folder and open the [notebook](structured_output_checks.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Check the sample replies first. Compare the same replies at both score limits.

| File | What it does |
| --- | --- |
| [docs/dataset/responses.json](docs/dataset/responses.json) | Six made-up replies with examples of valid and invalid data. |
| [tools/validate.py](tools/validate.py) | Checks each reply and shows why it passes or fails. |

The default lesson runs locally and needs no API key.

### Optional Groq exercise

The last cell uses [the prompt](prompts/classify.txt) and [the Groq loader](models/groq_model.py) to get a live reply. The same checker then tests that reply. The cell is off by default. To try it, set `GROQ_API_KEY` in the repository root's `.env` and change `RUN_LIVE` to `True`. The live path has yet to be verified.

The notebook is ready for your own run and explanation.
