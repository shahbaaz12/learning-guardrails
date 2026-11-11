# Project 6: Checking answers against policy

## 1. What can happen?

An answer cites the right leave policy but claims employees get 200 days off. The source itself says 20.

**Example** “Annual leave is 200 days” cites `LEAVE-1`, which says 20 days.

## 2. Our idea

We start with saved sample answers and made-up policy sections. The notebook reads both from files and makes no model calls.

We write a Python check that looks up each cited policy. Then we add a rule for one kind of claim. If the answer says “annual leave is 200 days,” compare 200 with the number in the leave policy it cites.

### How we do it

1. Load the saved answers and policies. Check that each cited policy exists and that an answer has a source when it makes a claim.
2. Turn on the annual leave number check and test the same answers again.
3. Show answers that pass. For each blocked answer, show why it was held back.

## 3. How it helps

The citation check catches missing or unknown sources on answers that make a claim. The added number check catches the 200-day mistake, but other unsupported claims can still pass.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `6_rag_answer_guardrails` as a folder and open the [notebook](rag_answer_guardrails.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Run the citation check first. Turn on the number check and compare the same answers.

| File | What it does |
| --- | --- |
| [docs/dataset/policies.json](docs/dataset/policies.json) | The made-up policy sections used as sources. |
| [docs/dataset/answers.json](docs/dataset/answers.json) | Sample answers, including one that says it cannot answer. |
| [models/fixtures.py](models/fixtures.py) | Copies the prepared answers for the lesson. |
| [tools/evidence.py](tools/evidence.py) | Checks citations and, when enabled, the annual leave number. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
