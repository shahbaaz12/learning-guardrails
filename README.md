# Learning guardrails

Small notebook projects for understanding when an AI application should allow,
block, redact, or validate information and proposed actions. We begin with
ordinary Python functions, then introduce NeMo Guardrails and Guardrails AI
through focused framework lessons.

## Setup

The repository root was initialized once using `uv init . --python 3.12`.
All numbered folders share its environment. From this folder:

```powershell
uv sync --locked
```

Open a lesson's notebook in VS Code and select `.venv/Scripts/python.exe`
from this repository. Use that numbered folder as the notebook working
directory. Restart the kernel when switching lessons or editing helpers.
Default notebook paths use labelled fixtures/local responders and need no API
keys. Projects 9–12 exercise the real installed framework APIs on those
fixtures. The shared lock includes NeMo Guardrails 0.24.1 and Guardrails AI 0.11.0.

Projects 2 and 11 include optional real Groq examples with `RUN_LIVE=False`.
To use one, copy `.env.example` to the ignored root `.env`, supply your own
`GROQ_API_KEY`, and follow that project's instructions. Live calls are separate
from the locally verified fixture paths.

## Projects

| Project | Demonstration |
| --- | --- |
| [1. Basic input guardrails](1_basic_input_guardrails/readme.md) | Allow/block before a local responder runs |
| [2. Structured output checks](2_structured_output_checks/readme.md) | Required fields, types, labels, and confidence constraints |
| [3. PII redaction](3_pii_redaction/readme.md) | Selected input/output masking and an exposed pattern limitation |
| [4. Topic guardrails](4_topic_guardrails/readme.md) | Keyword scope, accidental blocks, and missed violations |
| [5. Prompt-injection defenses](5_prompt_injection_defenses/readme.md) | Harmless direct/indirect toy fixtures, bypass, and false block |
| [6. RAG answer guardrails](6_rag_answer_guardrails/readme.md) | Citation checks versus a narrow source-evidence check |
| [7. Tool-execution guardrails](7_tool_execution_guardrails/readme.md) | Trusted application permissions before local action execution |
| [8. Guarded HR assistant](8_guarded_hr_assistant/readme.md) | Combine checks and compare guarded/unguarded fixture behavior |
| [9. NeMo input/output rails](9_nemo_input_output_rails/readme.md) | Native configured checks and registered custom actions |
| [10. NeMo retrieval/actions](10_nemo_retrieval_and_actions/readme.md) | Native retrieval masking and confirmation-gated mock actions |
| [11. Guardrails AI validation](11_guardrails_ai_validation/readme.md) | Native schema, validator history, withholding, repair, and bounded fixture re-asks |
| [12. Framework comparison](12_framework_comparison/readme.md) | Equivalent custom masking policy on identical inputs |

## Start here

- [Learning rules](rule.md)
- [Twelve-project roadmap](roadmap.md)
- [Agent roles and handoff](agent-plan.md)

All twelve projects are prepared and locally verified. Final integration on
30 October 2026 executed all 75 default code cells with zero external
connection attempts; the delivered notebooks retain empty outputs. Framework
examples use real SDK execution with labelled fixtures and custom checks.
Guardrails AI can emit its documented synchronous-validation fallback warning;
the checks still complete successfully. Optional live Groq paths remain untested.

Preparation does not mark the learner's lesson complete. Run and discuss one
project at a time. No fixed six-question rating requirement applies here.
