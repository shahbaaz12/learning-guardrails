# Learning guardrails — plan

Prepared: 29 October 2026. Initial scope was Project 1 only. The learner now
explicitly requests completion of Projects 2–12, including the framework
lessons. Prepare the notebooks as a staged batch, then use the normal
step-by-step teaching rhythm during learner execution.

Preparation completed: 30 October 2026. All twelve folders now contain their
standard structure, explained notebook, helpers/configuration, and run guide.
Projects 2–12 passed delegated review. Final integration executed all 75
default code cells with zero external connection attempts. Source notebooks
remain unexecuted; learner understanding and optional live calls remain pending.
Use the [project index](README.md#projects) to choose a lesson.

## Purpose

Evals measure behavior, observability exposes execution, and guardrails decide
whether inputs, outputs, or proposed actions should proceed. We build the
smallest understandable guard first, then learn what frameworks add.

All projects use one root uv environment and VS Code
notebooks. Keep the familiar folder layout. Reuse fictional Cedar Health
policies when HR examples help, without importing code through sibling folders.

## Sequence

| Order | Folder | Main concept | Visible demonstration |
| --- | --- | --- | --- |
| 1 | `1_basic_input_guardrails` | A decision before responding | Empty/oversized requests are blocked; allowed requests reach a local demo responder |
| 2 | `2_structured_output_checks` | Data contracts | Missing fields, wrong types, and invalid categories fail distinct checks |
| 3 | `3_pii_redaction` | Selected sensitive-data masking | Synthetic email/phone text is transformed before model use and before display |
| 4 | `4_topic_guardrails` | Application scope | HR questions proceed; unrelated and borderline requests reveal correct and accidental blocks |
| 5 | `5_prompt_injection_defenses` | Untrusted instructions | Compare a harmless direct/indirect injection fixture before and after one defense |
| 6 | `6_rag_answer_guardrails` | Output evidence | Check citations and absent knowledge; show why a valid citation alone is insufficient |
| 7 | `7_tool_execution_guardrails` | Controlled local actions | Check allowed tools, arguments, and trusted application permission context |
| 8 | `8_guarded_hr_assistant` | A small end-to-end comparison | Combine selected learned checks and compare legitimate, violating, and borderline cases |
| 9 | `9_nemo_input_output_rails` | Framework-operated checks | Configure one NeMo input rail, then one output masking rail; inspect execution evidence |
| 10 | `10_nemo_retrieval_and_actions` | Context and action boundaries | Inspect retrieved text before/after a rail and a bounded mock-action flow |
| 11 | `11_guardrails_ai_validation` | Validators and failure actions | Validate fixtures, then real outputs; inspect raw/validated values and bounded correction behavior |
| 12 | `12_framework_comparison` | Compare equivalent policies | Apply the same overlapping rule and examples to both frameworks; measure decisions and overhead |

Each project follows: explain the rule → show a baseline → add one check → run
normal/problematic/edge examples → inspect one issue → change one variable →
compare the same inputs → explain the result. Do not predeclare a winner.

## Shared setup and structure

The root is `core/learning-guardrails/`. It is initialized once:

```powershell
Set-Location 'C:\a\pproj\AI\zzTwo\Evals2\core\learning-guardrails'
uv init . --python 3.12
uv add ipykernel
```

Those initialization commands are recorded for provenance, not for rerunning
in the initialized repository. Use `uv sync` in this root on later sessions.
The batch includes installation and compatibility checks for the framework
lessons. Project 1 remains offline. Live provider calls in later lessons are
explicit learner-selected steps, disabled by default in delivered notebooks.

```text
learning-guardrails/
├── .venv/                 # Shared; ignored
├── .env.example           # Placeholders; Project 1 needs no keys
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── requirements.txt       # Export of the shared root dependencies
├── README.md
├── AGENTS.md
├── roadmap.md
├── agent-plan.md
└── 1_basic_input_guardrails/
    ├── docs/
    │   └── dataset/
    ├── models/
    ├── tools/
    ├── readme.md
    └── basic_input_guardrails.ipynb
```

Use this numbered folder as the notebook working directory and the root
`.venv/Scripts/python.exe` kernel. Keep about 5–8 short code cells with Markdown
before each. Explain helper functions before importing them. The tree shows
Project 1 as an example. Use the standard folder names for each lesson's files.

## Project 1 — basic input guardrails

**Goal:** understand how an ordinary guard returns a decision before a responder
runs. This is an offline teaching example, not a prompt-injection detector.

1. Show the setup commands and standard folder tree.
2. Add a small set of explicit teaching inputs: a short normal request, blank
   or whitespace input, an oversized request, and a legitimate borderline request.
   Describe their source as synthetic fixtures, not human-reviewed real data.
3. Explain a simple guard function checking text and a configurable character
   limit. Return allowed/blocked, a reason, and normalized text. Keep incorrect
   configuration visible using a simple assertion.
4. Add a clearly labelled local demo responder in `models/`. It makes no API
   calls and requires no credentials.
5. Add one request function that calls the guard first. Blocked requests return
   without calling the responder. Display the decision/reason and the actual
   local responder-invocation count, keeping it distinct from model/API calls.
6. Run the normal/problematic inputs and inspect why each decision occurred.
7. Show that a strict character limit can block a legitimate request. Change
   only that limit and compare the exact same input and the unchanged examples.
8. Give the learner a brief explanation checkpoint. No fixed questionnaire or
   numerical human-rating workflow is required.

**Acceptance:** blank and oversized inputs never invoke the responder; allowed
inputs invoke it once; exact-limit and over-limit behavior are explicit; the
limit comparison uses the same inputs. The short notebook, helpers, and README
follow the layout. All responses and call counts
are labelled honestly. Local checks pass without network access. Preparation
and validation do not mark the learner's lesson complete.

Reports are optional for this first lesson. If added, keep a small timestamped
comparison in `docs/evalresults/` and explain its fields without building a
reporting framework.

Implementation status: Project 1 is prepared with seven short notebook cells,
five synthetic fixtures, and small guard/request/display/responder helpers.
Implementation and independent-review stages passed local checks, including
actual responder spies and in-memory notebook execution with networking blocked.
No fixes were required. The delivered notebook remains unexecuted, with no
saved test artifacts. The learner's own run and explanation are pending.
The learner subsequently authorized preparation of the remaining projects.
See [agent-plan.md](agent-plan.md) for current assignments and evidence.

## Project 2 — structured output checks

1. Define one small classification result with required fields and allowed labels.
2. Validate known-good and deliberately invalid data objects before model use.
3. Display the failed field/rule and retain the raw object for inspection.
4. Add one actual model response only after the contract is understood.
5. Change one constraint and compare the same fixtures. Explain that a valid
   structure does not establish factual correctness.

Use simple non-throwing validation results; avoid exception-driven JSON parsing
or introducing a general-purpose validation framework before it is the topic.

## Project 3 — PII redaction

1. Define which synthetic entity types the exercise covers: email and phone.
2. Detect and display those entities on explicit fixtures.
3. Mask input before model use or telemetry; show original versus transformed text.
4. Add one output check using a clearly labelled response fixture first.
5. Inspect a missed or incorrectly masked case and change one rule. Do not
   claim a small pattern matcher anonymizes all personal information.

## Project 4 — topic guardrails

1. Define the assistant's narrow HR scope and a few unrelated/borderline examples.
2. Start with a readable rule; show its decision and reason.
3. Inspect both a missed violation and an accidental block when present.
4. Add one classifier only as a separate step if rules cannot express the lesson.
5. Change one condition and compare the same examples. Keep usefulness visible.

## Project 5 — prompt injection defenses

1. Use an owned fictional app and harmless attack markers, without real secrets.
2. Try one direct instruction and one instruction embedded in a supplied document.
3. Preserve actual baseline behavior; do not pretend a model followed an attack.
4. Add one boundary/check and inspect its decision and the final output.
5. Test a wording variation and a legitimate lookalike. Record limits rather
   than claiming a phrase filter or stronger prompt prevents all injections.

## Project 6 — RAG answer guardrails

1. Use a few policy sections with stable IDs; keep indexing separate if needed.
2. Check that cited IDs exist in the supplied context.
3. Ask an unsupported question and inspect honest abstention.
4. Show a fixture with a valid citation but an incorrect claim; inspect the source.
5. Add one focused evidence check and compare the same example. Distinguish
   schema/citation validation from broad factual verification.

## Project 7 — tool execution guardrails

1. Define one or two local mock tools and their expected arguments.
2. Validate the proposed tool name and arguments before executing anything.
3. Read permissions from trusted application context, not model-generated fields.
4. Demonstrate allowed, invalid, and unauthorized calls, showing whether the
   mock action actually ran. Use no external side effects.
5. Add a bounded confirmation or call limit only as a separate learning step.
   Compare one policy change on the same proposed action.

## Project 8 — guarded HR assistant

1. Select two or three already understood checks; do not add new frameworks.
2. Define a small fixed set of legitimate, violating, and borderline examples.
3. Run an unguarded baseline and the guarded version on the same inputs.
4. Inspect missed violations, accidental blocks, and added duration/calls.
5. Change one rule, compare again, and document the trade-off. Human labels
   remain drafts until reviewed; no fixed six-question form is mandated.

## Project 9 — NeMo input/output rails

1. Check current package/provider compatibility, then add only needed dependencies.
2. Reproduce a small unguarded example from an earlier lesson.
3. Register and enable one NeMo input rail through an explicit configuration.
4. Add one supported output masking rail using synthetic PII fixtures.
5. Display which framework check ran, before/after text, its outcome, and calls.
6. Change one configuration setting and rerun the same case. Distinguish a
   framework-configured check from the model's own refusal behavior.

## Project 10 — NeMo retrieval and actions

1. Check documented engine support; keep configuration small and explicit.
2. Show a retrieved fixture before and after a context masking/checking rail.
3. Build a short mock action flow: collect inputs, request confirmation, act.
4. Validate declared tool names/argument structure before application execution.
5. Add trusted application permission checks where needed; structural validation
   alone is not authorization. Inspect rail outcomes and one changed condition.

## Project 11 — Guardrails AI validation

1. Validate saved outputs first, with re-asks disabled and no model call.
2. Define a small contract, then add one business or supported PII validator.
3. Display raw output, validated output, pass/fail, and the failed rule.
4. Validate an actual model output after the deterministic examples are clear.
5. Demonstrate withholding, then a supported repair as separate steps.
6. Optionally allow one bounded re-ask, count its calls, and expose failure if
   it still does not pass. Do not build retry/exception-handling machinery.

## Project 12 — framework comparison

1. Select one genuinely overlapping policy, such as masking one entity type.
2. Replay the same labelled fixtures through each framework with equivalent rules.
3. Compare violations caught, accidental blocks, transformed outputs, and overhead.
4. Count additional guard-model calls and re-asks when model checks are used.
5. Change one setting and state which result the small sample supports. Do not
   declare one framework universally better from unrelated capabilities.

## Agent workflow and learner handoff

The plan is ready before delegation begins. Follow [agent-plan.md](agent-plan.md).
The orchestrator owns root configuration and coordination; delegated agents
implement and review the requested projects sequentially. Record actual checks and
remaining learner work. A review must not invent a successful API call or an
executed learner notebook. After delivery, return to one snippet at a time and
wait for `next` before advancing the lesson or project.

The requested batch is now complete. Do not automatically create another
project or rerun provider calls when resuming. The NeMo lessons invoke real
configured rails/custom actions on local fixtures. Guardrails AI lessons use
real schema/validator/failure-action APIs with bounded fixture re-asks. The
comparison uses equivalent patterns and the same inputs, with construction
outside per-check timers. This is a small controlled demonstration, not a
claim of comprehensive protection or production performance.

## References

These are conceptual references; use current official API documentation when
each framework lesson starts.

- [NeMo rail types](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/rail-types)
- [NeMo PII rails](https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/pii-detection)
- [NeMo tool-calling rails](https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/tool-calling)
- [Guardrails AI guard interface](https://guardrailsai.com/guardrails/docs/concepts/guard)
- [Guardrails AI validators](https://guardrailsai.com/guardrails/docs/concepts/validators)
- [Guardrails AI failure actions](https://guardrailsai.com/guardrails/docs/concepts/validator_on_fail_actions)
- [OWASP prompt-injection guidance](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
