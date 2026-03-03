cat > README.md << 'EOF'
# AI Eval Toolkit

Lightweight toolkit for structured evaluation of AI/LLM outputs: metrics, rubric-based scoring, and simple reporting.

## Why this exists
When you iterate on prompts or compare model outputs, you need repeatable evaluation and a way to log results consistently. This repo is a practical, evolving toolkit to support that workflow.

## What’s included (v1)
- **Rubric-based scoring** (clarity, correctness, completeness, safety)
- **Simple JSON logging** for results
- **Example evaluation run** you can execute locally

## Roadmap
- Add configurable rubrics (YAML/JSON)
- Add batch evaluation for datasets
- Add basic report generation (CSV/Markdown)
- Add unit tests and CI

## Quick start
```bash
python3 --version
# (coming next) python3 -m venv .venv && source .venv/bin/activate
