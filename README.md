# ai-engineering-lab

Personal lab for AI engineering experiments: prompts, agents, RAG, evals, and small end-to-end builds.

## Structure

```
experiments/   one folder per experiment
notebooks/     exploratory notebooks
src/           reusable code
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt       # runtime only
pip install -r requirements-dev.txt   # runtime + tests
```

Copy `.env.example` to `.env` and fill in your keys.
