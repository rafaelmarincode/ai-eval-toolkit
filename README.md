![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
# AI Eval Toolkit

Lightweight toolkit for structured evaluation of AI/LLM outputs: metrics, rubric-based scoring, and simple reporting.

## Why this exists
When you iterate on prompts or compare model outputs, you need repeatable evaluation and a way to log results consistently. This repo is a practical, evolving toolkit to support that workflow.

## What’s included (v1)
- **Rubric-based scoring** (clarity, correctness, completeness, safety)
- **Simple JSON logging** for results
- **Example evaluation run** you can execute locally

## Project structure

```
ai-eval-toolkit/
├── src/
│   └── ai_eval_toolkit/
│       └── evaluator.py
├── examples/
│   └── example_eval.py
├── tests/
└── README.md
```

## Roadmap
- Add configurable rubrics (YAML/JSON)
- Add batch evaluation for datasets
- Add basic report generation (CSV/Markdown)
- Add unit tests and CI

## Quick start
```bash
python3 --version
# (coming next) python3 -m venv .venv && source .venv/bin/activate
```
## Example evaluation output

```json
{
  "prompt": "Explain what machine learning is",
  "scores": {
    "clarity": 4,
    "correctness": 5,
    "completeness": 4,
    "safety": 5
  },
  "overall_score": 4.5
}
```

