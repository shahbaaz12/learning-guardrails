# Instructions for learning agents

Read `roadmap.md`, `agent-plan.md`, and the active numbered project's `readme.md`
before changing files or teaching the next step. Read the local `rule.md` when
available. It is kept outside Git tracking.

The learner initially selected Project 1, then explicitly requested **complete
the remaining projects** on 29 October 2026. Implement Projects 2–12 as a staged
batch, including working NeMo and Guardrails AI examples. Keep one short
notebook and a `readme.md` per project. Follow the standard folder names in
the roadmap and include the folders each lesson uses.

Keep functions simple. No try/except, complex handlers, unnecessary classes,
or production infrastructure. Expected guard rejections return decisions and
reasons. Project 1 uses an explicitly labelled local demo responder and makes
no model/API calls. Do not read credentials or call external model services.

Use the root uv environment and Python 3.12. Do not create child environments.
Keep notebooks unexecuted in the delivered source unless the learner asks for
saved outputs; verify locally without inventing learner results.

During teaching, offer one explained snippet and wait for `next`. Explicit
implementation and review requests authorize necessary local checks. The initial
delegation is such a request. Never interpret implementation checks as learner
completion or approval to begin another project.

Use the staged four-agent hierarchy in `agent-plan.md`: orchestrator → Project
Sup → task supervisor → worker. Only a supervisor delegates to a worker, with
bounded ownership and acceptance criteria. Keep no more than four active agents.
Use ordinary collaboration agents, not additional app threads or external services.
Record actual assignments, findings, and handoff state in `agent-plan.md`.
Avoid simultaneous edits to the same file. Root coordination files belong to
the orchestrator unless explicitly assigned otherwise.

Current handoff, 30 October 2026: all twelve projects are prepared. Projects
2–12 passed supervisor/Project Sup review, and the orchestrator executed all
75 default notebook cells in the shared environment with zero external
attempts. Required nbformat 4.5 cell IDs were added during final integration;
code/text/outputs were preserved. Read `agent-plan.md` for actual findings.

The learner's own runs/explanations remain pending. Do not redeploy the build
batch or mark learning complete when a new session begins. Resume the requested
lesson with one explained snippet/cell at a time. Framework examples use real
SDK APIs, custom checks, and labelled fixtures; they do not claim to be pretrained
safety detectors. Optional live Groq paths in Projects 2 and 11 are disabled
by default and were not exercised. Never read keys or make live calls to
recover results. Shared dependency/guide edits belong to the orchestrator
unless specifically assigned.
