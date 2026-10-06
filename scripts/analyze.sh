#!/usr/bin/env bash
set -euo pipefail
python -m src.cli "${1:-examples/postgres_failure.log}"
