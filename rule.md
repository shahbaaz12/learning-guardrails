# Guardrails learning rules

The goal is a small working example the learner can explain. Keep the familiar
learning rhythm and folder structure from the evaluation and observability repos.

## Learning behavior

1. Teach one project at a time. The learner initially selected Project 1 and
   subsequently authorized preparation of all remaining Projects 2–12 as a
   batch. Implement/review each project in stages while retaining the normal
   one-project teaching rhythm when the learner runs the notebooks.
2. Use numbered folders such as `1_basic_input_guardrails`. Preserve names and
   the standard layout below.
3. Initialize the repository root once with `uv init .`. A Python version flag
   is allowed. All lessons share its `.venv`, `.env`, `pyproject.toml`, and
   `uv.lock`; do not initialize environments in numbered folders.
4. Run `.ipynb` notebooks in VS Code using the shared root kernel. Explain the
   supported working directory and restart the kernel after helper changes.
5. Give setup commands and the folder tree before implementation. Introduce
   one concept and one short snippet at a time, naming its target, purpose,
   run command or cell, and expected observation.
6. During teaching, wait for the learner's `next` or equivalent before the next
   snippet. Do not require pasted output by default. Inspect their results
   when requested with `-check`. Explicit edit, implementation, and review
   requests authorize the reads and checks necessary for that task.
7. Keep code simple: ordinary functions and clear conditions; no `try`/`except`,
   complex error handlers, unnecessary classes, generic runners, or services.
   Necessary framework APIs belong only in their dedicated later lessons.
8. An expected guard rejection is a normal decision such as `allow`, `block`,
   or `redact`, with a reason. Do not use exceptions as ordinary policy decisions.
   Assertions can expose invalid configuration or mistakes during development.
9. Keep notebooks focused on explanation, settings, small calls, displayed
   decisions, and one comparison. Put reusable checks, model setup, and report
   writing in small supporting files; explain each helper before importing it.
10. Begin with a normal example, a problematic example, and an edge case. Inspect
    one failure or trade-off, change one rule or setting, then compare the same
    inputs. Do not require an arbitrary number of questions or a human form.
11. Distinguish fixtures, local demo responses, model outputs, and human judgments.
    Never label a local function invocation as a real model/API call. Never
    fabricate results, traces, validation outcomes, cost, or human ratings.
12. Give simple manual checks first. Run meaningful local checks for an explicit
    implementation; keep test machinery proportionate to the example.
13. Keep one `readme.md` in each numbered folder explaining goal, input/output,
    provenance, setup, file responsibilities, notebook order, and current progress.
    Keep the repository README brief. Record unfinished learner steps honestly.

## Lesson Markdown

Use this order in the project README and the notebook introduction.

1. **What can happen?** Describe the situation in everyday words. Add one
   short example, using the lesson's inputs when possible.
2. **Our idea.** Say where the examples come from and what the lesson does
   with them. State when a model is called, if the lesson includes one. In the
   README, add a **How we do it** subsection with short numbered steps in plain
   language.
3. **How it helps.** Explain what changes for that situation.
4. **Input and setup.** Add the example inputs, files, or commands the learner needs.

Use short sentences and concrete examples. Before a code cell, say what to run
and what to look for. Explain a new term when it first matters.
List only files or folders used in the lesson. If a file is used only in an
optional step, list it with that step.

## Standard folder structure

```text
<number>_<project_name>/
├── docs/
│   ├── dataset/        # Fictional inputs, policy sources, or explicit fixtures
│   ├── goldends/       # Reviewed expectations when the lesson needs them
│   ├── evaluatedds/    # Saved application outputs, when needed
│   └── evalresults/    # Saved observations and comparisons, when needed
├── models/            # Small model loader or clearly labelled demo responder
├── prompts/           # Actual prompts, when a lesson needs them
├── tools/             # Simple guard, workflow, and reporting functions
├── readme.md
└── <project>.ipynb
```

Keep the folder names shown above and create each folder when the lesson uses
it. Omit empty folders and `.gitkeep` placeholders. Add a framework configuration
folder when the lesson needs it. Add preparation scripts under `tools/` and
execute indexing separately from requests when RAG is introduced.

## Guardrails-specific principles

- Use fictional policies and synthetic personal data. Keep reviewed expectations
  separate from model inputs. AI-drafted judgments remain drafts until reviewed.
- Show the decision, its reason, which stage ran, and what was finally exposed.
  In framework lessons, show evidence that the framework actually ran the check.
- Test allowed inputs as well as violations. Count accidental blocks and missed
  violations where evaluation is the topic. A guard is not universally effective.
- Validate permissions using trusted application context, not a permission claim
  supplied by the model. Use local mock actions for execution lessons.
- A valid schema or citation does not establish factual correctness. Introduce
  appropriate evidence checks without claiming comprehensive factual guarantees.
- Keep baseline and candidate settings explicit and preserve prior reports when
  reports are needed. Change only one variable in a teaching comparison.
- Begin framework validation with re-asks disabled. Introduce at most one re-ask
  in its own step. Distinguish guard-model calls from answer-model calls.

## Credentials and dependencies

Keep credentials in the ignored root `.env`; `.env.example` contains placeholders.
Never read or copy API keys from reference notes or another repository. Do not
print credentials or include them in notebook outputs. Install only dependencies
needed by the requested projects. The remaining-project batch includes NeMo
and Guardrails AI; verify their compatibility in the shared environment.

## Delegated work

The learner explicitly requested an orchestrator, Project Sup, supervisors, and
workers. Follow [agent-plan.md](agent-plan.md). Delegation authorizes preparation
and review of the requested projects. The current batch covers Projects 2–12;
it does not authorize publishing a repository, paid model calls, or filling in
learner feedback.
