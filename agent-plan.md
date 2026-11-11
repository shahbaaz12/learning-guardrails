# Agent roles and execution plan

Prepared: 29 October 2026. Human authorization: prepare the plan, then deploy
subagents. The learner initially selected **Start Project 1 only**, then explicitly
expanded preparation to all remaining projects. The later batch is recorded below.

## Roles

| Role | Responsibility | Ownership |
| --- | --- | --- |
| Orchestrator | Interpret scope, prepare the plan/root setup, dispatch the Project Sup, resolve blockers, report results | Repository root files and final acceptance |
| Project Sup | Oversee the active project, divide work into stages, assign supervisors, accept the project handoff | Project 1 coordination; bounded edits only if assigned |
| Task supervisor | Give a worker precise ownership/criteria, inspect the work, request fixes, report evidence | The assigned implementation or review stage |
| Worker | Build or check the assigned small files and report actual results | Only the files assigned by the supervisor |

## Four-slot operating limit

Use a staged hierarchy with at most four active agents:

```text
Orchestrator
└── Project Sup: Project 1
    └── Task supervisor: current stage
        └── Worker: current assignment
```

Run implementation and independent-review stages sequentially. A supervisor
can assign a follow-up to a worker after inspection. Start another supervisor
stage only after the prior stage completes and a slot is available. If the
runtime retains completed agents against its limit, reuse the existing role
with an explicit next assignment instead of spawning beyond the limit.
Several supervisor/worker assignments can occur over the project; they do not
all need to be active simultaneously. Do not create an orchestration framework,
background server, extra app task, or project-specific environment.

## Stage A — plan and shared setup, orchestrator

1. Read applicable rules and confirm the active scope.
2. Write the twelve-project roadmap and guardrails-specific rules.
3. Initialize the root uv project with Python 3.12 and ipykernel only.
4. Add gitignore, placeholder env example, portable agent instructions, and README.
5. Dispatch the Project Sup only after the plan exists.

## Stage B — Project 1 implementation, delegated

The Project Sup assigns an implementation supervisor. That supervisor gives
a worker ownership of `1_basic_input_guardrails/` only. The worker creates:

- The standard folder structure with placeholders where needed.
- A few explicit synthetic inputs and a configurable length/blank-input guard.
- A clearly labelled local demo responder and a small guarded request function.
- A short explained notebook and one project README.
- A same-input comparison after changing only the character limit.

Keep dependencies unchanged. Make no network/model calls, install no frameworks,
and do not edit other repositories. The supervisor inspects behavior and
readability before accepting the implementation.

## Stage C — independent review, delegated

After implementation, the Project Sup assigns a review supervisor/worker stage.
The reviewer must inspect the actual files, not just the implementation report.
Verify: rejection returns a reason; blocked requests never call the responder;
allowed requests call it once; boundaries are correct; changed-limit comparison
uses the same inputs; no try/except/classes; notebook syntax/order/paths are
valid; report and README language distinguish local demo calls from API calls.

Run the notebook code in a scratch namespace/environment if useful, without
saving fabricated learner outputs. Keep transient checks/results outside the
delivered data directories. Request a small fix for a real issue, then review
the changed behavior. Do not broaden testing after checks pass without cause.

## Stage D — project acceptance and handoff

The Project Sup reports files, actual checks, findings/fixes, and remaining
learner steps to the orchestrator. The orchestrator checks root integration,
updates progress below, and delivers the roadmap and Project 1 notebook.
The learner then runs it. At the initial handoff only Project 1 was in scope.
Never mark human understanding complete based on implementation checks.

## Progress log

- Plan and root setup: prepared and checked by the orchestrator.
- Dependency setup: one shared Python 3.12 environment with ipykernel; lock/export checks passed; no API keys.
- Active project: `1_basic_input_guardrails` only.
- Project Sup deployed: `/root/project_1_sup`.
- Implementation supervisor deployed: `/root/project_1_sup/implementation_supervisor`.
- Implementation worker deployed: `/root/project_1_sup/implementation_supervisor/implementation_worker`.
- Implementation stage: complete. The worker and implementation supervisor
  checked blocked/allowed invocation counts, normalization/type handling,
  exact-limit behavior, the identical-input 40/80 comparison, and all seven
  notebook cells with networking blocked. No implementation fixes were needed.
- Independent review supervisor deployed: `/root/project_1_sup/review_supervisor`.
- Independent review worker deployed: `/root/project_1_sup/review_supervisor/review_worker`.
- Independent review: passed. The fresh worker checked actual responder calls,
  normalization and invalid inputs, exact boundaries at limits 1/40/80, the
  same-fixture comparison, and all seven notebook cells with sockets blocked.
  The review supervisor personally inspected every helper and notebook cell.
  No findings or fixes were needed.
- Project Sup acceptance: recommended after inspecting the actual files and
  reviewing both supervisor reports. The two stages ran sequentially within
  the four-active-agent limit. The subagents changed only Project 1 files.
- Orchestrator integration: passed. Root guide links resolve, required folders
  exist, notebook cells remain unexecuted with empty outputs, reserved output
  folders have no test artifacts, and only Project 1 is present. Shared lock,
  requirements export, and credential/environment ignore checks passed.
- Delegation status: complete for Project 1 preparation and independent review.
- Learner run and feedback: not started.

## Project 1 handoff (completed preparation)

Open `1_basic_input_guardrails/basic_input_guardrails.ipynb` in VS Code using
the shared root kernel and the numbered folder as the working directory. The
learner should run the example and explain the allow/block decisions and limit
trade-off. No model/API calls or credentials are needed. Resume guided teaching
one snippet at a time and wait for `next`. The initial Project 1-only preparation
limit was later superseded by the remaining-project batch below.

## Current batch — remaining projects

On 29 October 2026 the learner explicitly requested completion of Projects
2–12. This supersedes the initial Project 1-only preparation limit. Keep each
lesson small and verify actual behavior; do not mark learner completion.

- Orchestrator: shared dependency compatibility, root guides, integration.
- Project Sup: oversee sequential foundation and framework project stages.
- Task supervisors/workers: implement and review only assigned numbered folders.
- Runtime limit: root → Project Sup → supervisor → worker, four active agents.
- Foundation stage: Projects 2–8, with per-project inspections/checks.
- Framework stage: Projects 9–12, using real installed NeMo/Guardrails AI APIs.
- Live API calls and external mock-action effects: disabled; none authorized.
- Dependencies/root files: orchestrator only. No competing uv operations.

### Actual assignments and progress

- Project Sup: `/root/remaining_projects_sup`.
- Task supervisor: `/root/remaining_projects_sup/foundation_supervisor`.
- Worker: `/root/remaining_projects_sup/foundation_supervisor/foundation_worker`.
- Shared dependencies resolved and installed together: NeMo Guardrails 0.24.1,
  Guardrails AI 0.11.0, jsonschema 4.26.0, langchain-groq 1.1.3,
  python-dotenv 1.2.4, and their locked dependencies in Python 3.12.
- Projects 2–8: Project Sup reports actual-file inspection and independent
  default notebook execution with external sockets blocked. Rules, limitations,
  same-input comparisons, and normal/edge/invalid decisions passed checks.
- Orchestrator SDK compatibility probes passed with external connections blocked:
  real NeMo input/output checks, retrieval masking, and confirmation-gated
  local actions; real Guardrails AI schema validation, FIX, REFRAIN, and one
  bounded fixture re-ask, including failure after the limit. These probes used
  registered custom checks and fixture values, not pretrained safety models
  or actual LLM responses.
- Windows test detail: create/set the event loop before restricting socket
  connects and allow only OS loopback self-pipes; NeMo also starts a background
  event loop. Reject external DNS/connect attempts. Delivered async notebooks
  use their existing IPython event loop for top-level await.
- Project 9: actual six-cell notebook accepted after independent SDK runs and
  responder spies. Review fixed lowercase SDK status handling and added
  `DO_NOT_TRACK=1` before NeMo imports. Fresh tests reported zero external
  attempts, with Windows internal loopback self-pipes explicitly permitted.
- Projects 10–12: accepted by supervisor and Project Sup after actual SDK
  execution. Project 10 verified retrieval/action events and real mock-action
  spies. Project 11 verified schema outcomes, REFRAIN/FIX history, and exactly
  one callback for each bounded re-ask scenario. Project 12 verified equivalent
  transforms, original-failure detection after FIX, and fair timer boundaries.

### Final acceptance — 30 October 2026

All remaining numbered files were handed back frozen. Actual assignments were
`/root/remaining_projects_sup` →
`/root/remaining_projects_sup/foundation_supervisor` →
`/root/remaining_projects_sup/foundation_supervisor/foundation_worker`.
The reused four-role chain worked through each project sequentially. The
supervisor and Project Sup personally inspected the files and ran checks;
no learner ratings or live model results were fabricated.

| Project | Default code cells | Preparation |
| --- | ---: | --- |
| 1 | 7 | Previously accepted; passed new shared-environment integration |
| 2–8 | 6 each | Accepted with behavior checks and responder/action spies |
| 9 | 6 | Accepted with real NeMo input/output rails |
| 10 | 7 | Accepted with real NeMo retrieval and gated mock actions |
| 11 | 7 | Accepted with actual Guardrails AI validation/failure actions |
| 12 | 6 | Accepted with paired real-framework checks |

Review/integration findings and fixes:

1. Corrected NeMo SDK status comparisons to lowercase enum values.
2. Disabled NeMo telemetry before imports using `DO_NOT_TRACK=1`. Initial
   telemetry attempts were blocked by checks; final runs recorded zero external
   attempts, including initialization. Windows asyncio self-pipes were permitted.
3. Documented native Guardrails AI numeric-to-string coercion, rather than
   pretending it was strict rejection. Documented its actual synchronous-fallback
   warning and comparison timing limitations rather than suppressing them.
4. Aligned configurable optional Groq defaults to `openai/gpt-oss-20b`.
5. Final format audit found missing cell IDs in Projects 2–12 declaring
   nbformat 4.5. The orchestrator added deterministic unique IDs while asserting
   code, Markdown, metadata, and outputs were otherwise unchanged.
6. The orchestrator then independently executed **all 12 notebooks / 75 default
   code cells** in the installed shared environment. External DNS/connect
   attempts were zero; 13 Windows-internal loopback connections were permitted.
   Notebook hashes were unchanged by execution. All local guide links resolved,
   standard folders existed, all application code used ordinary functions with
   no try blocks/custom classes, and no result files were saved in reserved folders.

Only optional live examples in Projects 2 and 11 remain unverified against a
provider. They stay disabled and require the learner's own credentials and
explicit action. No model calls, real HR effects, or external feedback submissions
were made during this batch.

### Current handoff

Use `uv sync --locked` at the repository root. Open one numbered notebook in
VS Code with the shared root kernel, using its numbered folder as the working
directory. Restart the kernel between lessons. Run the default fixture path
first, read decisions/execution evidence and limitations, then discuss the
one-setting comparison. Resume normal one-snippet-at-a-time guidance.
All preparation/review stages are complete; learner execution/explanation
is pending. Do not restart the build batch or claim the learner finished it.

Record remaining actual assignments, checks, findings, and final handoff below.
