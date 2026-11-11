"""Small batch and display helpers for the same fixed teaching examples."""

from tools.guarded_request import run_request


def run_examples(examples, max_chars):
    return [
        {"case_id": example["case_id"], **run_request(example["input"], max_chars=max_chars)}
        for example in examples
    ]


def show_results(results):
    print("Case | Characters | Decision | Local responder calls | Model/API calls")
    for result in results:
        print(
            f"{result['case_id']} | {result['character_count']} | {result['decision']} | "
            f"{result['local_responder_calls']} | {result['model_api_calls']}"
        )
        print("  Reason:", result["reason"])


def show_comparison(baseline, candidate):
    assert [row["case_id"] for row in baseline] == [row["case_id"] for row in candidate]
    print("Case | Baseline decision | Candidate decision")
    for before, after in zip(baseline, candidate):
        assert before["normalized_input"] == after["normalized_input"], "Keep inputs unchanged."
        print(f"{before['case_id']} | {before['decision']} | {after['decision']}")
