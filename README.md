# Learning guardrails

## 1. What can happen?

An AI app can receive a blank question, share an email address, give a reply with missing fields, or try to run an action the user has no permission to perform.

**Example** A leave assistant replies “Annual leave is 200 days.” The policy says 20. How can the app catch that before showing the reply?

## 2. Our idea

We build small checks around an app to decide what can go through, what needs to be hidden, and what should stop. These checks are called **guardrails**.

Each lesson uses made-up questions, saved replies, or practice actions. We start with rules we write in Python. Later, we use the real NeMo Guardrails and Guardrails AI libraries to run our checks on the saved examples.

All main lessons run locally and need no API key. Projects 2 and 11 also have an optional final cell that calls a model through Groq and checks the fresh reply. That cell is off by default.

### How we do it

1. Pick one problem and look at a few saved examples.
2. Run a small check and see what passes, changes, or gets blocked.
3. Find a mistake or a missed case. Change one setting and try the same examples again.
4. Explain what improved and what the check still misses before moving to the next project.

## 3. How it helps

You can see exactly what each check does before putting it into a larger app. You also see its limits. A word filter can block a useful question, and a reply with all the right fields can still contain a wrong answer.

The notebooks keep each example small so you can run one cell, inspect the result, and explain it in your own words.

## 4. Input and setup

Use VS Code with its Python and Jupyter extensions, and have `uv` installed.

To get the project for the first time, run these commands in PowerShell.

```powershell
git clone https://github.com/shahbaaz12/learning-guardrails.git
cd learning-guardrails
uv sync --locked
```

If you already have the folder, open PowerShell at the repository root and run `uv sync --locked`. All lessons share the root environment.

In VS Code, open the numbered lesson folder and its `.ipynb` notebook. Select the repository root's `.venv/Scripts/python.exe` as the kernel. Run the cells in order, one at a time. Restart the kernel when switching lessons or editing helper files.

The sample inputs live in each lesson's `docs/dataset/` folder. Each project README explains which files that lesson uses.

### Projects

Follow the projects in this order.

| Project | What you will try |
| --- | --- |
| [1. Basic input guardrails](1_basic_input_guardrails/readme.md) | Block blank or long messages before a Python demo responder runs. Change the length limit and try again. |
| [2. Structured output checks](2_structured_output_checks/readme.md) | Check saved replies for required fields, allowed topics, and a numeric confidence score. See why a well-shaped reply can still be wrong. |
| [3. Masking personal information](3_pii_redaction/readme.md) | Hide matching emails and phone numbers before a message reaches the demo responder and before its reply is shown. |
| [4. Topic guardrails](4_topic_guardrails/readme.md) | Allow questions with HR words. See a useful vacation question get blocked and an unrelated question slip through. |
| [5. Prompt injection defenses](5_prompt_injection_defenses/readme.md) | Use a toy Python responder to show how instructions in a question or document can change a reply. Try a phrase filter and find its misses. |
| [6. Checking answers against policy](6_rag_answer_guardrails/readme.md) | Check that a saved answer cites an existing policy. Add a number check to catch the claim of 200 leave days. |
| [7. Tool execution guardrails](7_tool_execution_guardrails/readme.md) | Check a proposed leave action against the signed-in employee's details and permissions before recording a practice action. |
| [8. Guarded HR assistant](8_guarded_hr_assistant/readme.md) | Combine topic, email, and policy-reference checks around prepared replies. Compare what happens with the checks off and on. |
| [9. NeMo input and output rails](9_nemo_input_output_rails/readme.md) | Use NeMo to run our topic check before a demo reply and our email check after it. See which checks ran. |
| [10. NeMo retrieval and local actions](10_nemo_retrieval_and_actions/readme.md) | Use NeMo to hide an email in supplied policy text and check permission and confirmation before a practice leave action. |
| [11. Guardrails AI validation](11_guardrails_ai_validation/readme.md) | Use Guardrails AI to check saved replies, withhold a reply or mask its email, and try one prepared replacement after a failure. |
| [12. Comparing NeMo and Guardrails AI](12_framework_comparison/readme.md) | Give both frameworks the same email rule and messages. Compare what they mask, miss, or mask by mistake. |

### Optional model calls

For the optional Groq cell in Project 2 or 11, copy `.env.example` to `.env` at the repository root and enter your own `GROQ_API_KEY`. Enable the cell by setting `RUN_LIVE` to `True` when you reach it. Keep credentials in `.env`, which Git ignores.

The default local examples have been checked. The optional live model paths still need a learner run.

See the [roadmap](roadmap.md) for the full learning plan.
