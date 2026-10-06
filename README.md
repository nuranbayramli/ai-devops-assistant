# AI DevOps Assistant

CLI developer tool that turns noisy failed CI/CD logs into a concise diagnosis: **problem, likely cause, suggested fix, confidence**.

## Stack
Python 3.11+, pytest, Docker, Bash, GitHub Actions, Git; optional OpenAI-compatible LLM API.

## Run
```bash
python -m src.cli examples/postgres_failure.log
```

## Optional LLM mode
```bash
export LLM_API_KEY="..."
export LLM_BASE_URL="https://api.openai.com/v1"
export LLM_MODEL="gpt-5-mini"
python -m src.cli examples/postgres_failure.log --llm
```

## Tests
```bash
pip install -r requirements-dev.txt
pytest -q
```

## Docker
```bash
docker build -t ai-devops-assistant .
docker run --rm ai-devops-assistant examples/postgres_failure.log
```

## How it works
1. CLI reads a CI log.
2. Extractor keeps error/failure lines plus context.
3. Local analyzer classifies common failures; optional LLM mode provides richer triage.
4. Tool prints a compact diagnosis for a developer.

## Next steps
GitHub API ingestion, workflow summaries/PR comments, JSON output, more failure categories.
