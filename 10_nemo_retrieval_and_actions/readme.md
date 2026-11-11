# Project 10: NeMo retrieval and local actions

## 1. What can happen?

A supplied policy could expose an email in a reply. A proposed leave action could also run before the employee confirms it.

**Example** The assistant proposes two days of leave before the employee clicks Confirm.

## 2. Our idea

We start with a saved policy excerpt and made-up leave proposals. We also supply sample app records that say who signed in and whether they confirmed the action. This lesson makes no model calls.

We configure NeMo to run two sets of checks we write. One masks emails in the policy before it appears in a reply. The other checks a proposed leave action before a Python function records it in a local list.

### How we do it

1. Give NeMo the saved policy. Let it hide the email address before using the policy text in a reply.
2. For each leave proposal, check the request details, permission, and confirmation. Record the action only if it passes.
3. Turn off the confirmation requirement and try the same proposals. Compare what reaches the local log.

## 3. How it helps

You can see the masked policy in the reply and check the local action log. Turning off confirmation lets the authorized, unconfirmed proposal run. Unauthorized and invalid proposals still stop.

## 4. Input and setup

Run `uv sync --locked` from the repository root. In VS Code, open `10_nemo_retrieval_and_actions` as a folder and open the [notebook](nemo_retrieval_and_actions.ipynb). Select the repository's `.venv/Scripts/python.exe` kernel.

Run one code cell at a time. Run the policy example first. Then try the action examples with confirmation on and off. The notebook supplies the events directly.

| File | What it does |
| --- | --- |
| [docs/dataset/policy.txt](docs/dataset/policy.txt) | A made-up policy excerpt supplied as retrieved text. |
| [docs/dataset/actions.json](docs/dataset/actions.json) | Example proposals and separate app-owned session details. |
| [config/config.yml](config/config.yml) | Sets up the NeMo flows. |
| [config/rails.co](config/rails.co) | Defines the policy masking and action steps. |
| [tools/native_flows.py](tools/native_flows.py) | Runs NeMo on the supplied examples and records practice actions. |

The default lesson runs locally and needs no API key.

The notebook is ready for your own run and explanation.
