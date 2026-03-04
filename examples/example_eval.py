from ai_eval_toolkit.evaluator import evaluate_response


prompt = "Explain what machine learning is."
response = """
Machine learning is a branch of artificial intelligence that allows systems
to learn patterns from data and improve their performance over time without
being explicitly programmed.
"""


scores = evaluate_response(prompt, response)

print("Evaluation Results")
print("------------------")

for metric, value in scores.items():
    print(f"{metric}: {value}")
