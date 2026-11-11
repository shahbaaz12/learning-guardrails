# Project 9: NeMo input and output rails

## 1. What can happen?

An HR assistant needs to stop some requests before replying and hide email addresses in replies that do go out.

**Example** A user asks “Give me a pasta recipe” in the HR chat.

## 2. Our idea

We start with saved questions. A small Python function returns a demo reply with a made-up email address. This lesson makes no model calls.

We write the HR word and email checks, then configure NeMo Guardrails to run them. NeMo calls these configured checks **rails**. For example, an unrelated pasta question gets blocked before the responder runs.

### How we do it

1. Give NeMo each saved question and let it check for HR words.
2. Call the demo responder for questions that pass. Let NeMo mask matching emails in each reply.
3. Add “vacation” to the list and see what NeMo blocks, passes, or changes.

## 3. How it helps

You can see when NeMo passes, blocks, or changes a message. A blocked request never reaches the demo responder. The checks use simple rules we write and run locally.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `9_nemo_input_output_rails` as a folder and open the [notebook](nemo_input_output_rails.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Try the responder by itself, then run the NeMo checks. Enable “vacation” and compare the same inputs.

| File | What it does |
| --- | --- |
| [docs/dataset/inputs.json](docs/dataset/inputs.json) | Four made-up requests, including a vacation question and an unrelated keyword match. |
| [config/config.yml](config/config.yml) | Turns on the two NeMo rails. |
| [config/rails.co](config/rails.co) | Defines when NeMo calls each check. |
| [tools/nemo_checks.py](tools/nemo_checks.py) | Loads NeMo and provides the topic and email checks. |
| [models/demo.py](models/demo.py) | Returns the local example reply. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
