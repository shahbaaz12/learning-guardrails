# Project 12: Comparing NeMo and Guardrails AI

## 1. What can happen?

Both frameworks can mask an email address. How do we tell which differences come from the tools and which come from the rule we gave them?

**Example** Someone writes `alex at example dot test`, which a rule that looks for `@` can miss.

## 2. Our idea

We start with five saved messages, including a regular email address and one written with “at” and “dot.” Both frameworks run locally. This lesson makes no model calls.

We write one masking rule and give it to both NeMo and Guardrails AI. They check the same text and use the same replacement, so we can compare what each one catches.

### How we do it

1. Run the same saved messages through both frameworks with the original rule.
2. Use the draft labels to compare what each one masks, misses, or masks by mistake.
3. Widen the rule in both frameworks to catch the “at” and “dot” example. Run the same messages again.

## 3. How it helps

You can compare what each tool masks, misses, and masks by mistake. Both catch the simple “at” and “dot” form after the change, while a bracketed address still slips through. Local timings are only a snapshot.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `12_framework_comparison` as a folder and open the [notebook](framework_comparison.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Run both frameworks on the original rule, widen the rule, and compare the results.

| File | What it does |
| --- | --- |
| [docs/dataset/strings.json](docs/dataset/strings.json) | Made-up text with several email formats and a public example address. |
| [docs/goldends/draft_expectations.json](docs/goldends/draft_expectations.json) | Draft labels for comparing what should be masked. |
| [config/config.yml](config/config.yml) | Turns on the NeMo output rail. |
| [config/rails.co](config/rails.co) | Tells NeMo when to call the masking check. |
| [tools/compare.py](tools/compare.py) | Shares the same masking rule and shows what each framework did. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
