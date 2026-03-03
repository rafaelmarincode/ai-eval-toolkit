import json


def score_output(output: str) -> dict:
    """
    Simple rubric-based scoring for AI responses.
    """

    score = {
        "clarity": 1 if len(output) > 20 else 0,
        "completeness": 1 if "." in output else 0,
        "safety": 1,
    }

    score["total"] = sum(score.values())

    return score


def save_result(output: str, filename="result.json"):
    result = {
        "output": output,
        "evaluation": score_output(output),
    }

    with open(filename, "w") as f:
        json.dump(result, f, indent=2)

    print("Evaluation saved to", filename)
