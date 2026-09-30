#!/usr/bin/env bash
# Builds demo repos (idempotent) and starts the RAMAV backend, which also
# serves the frontend dashboard from the same origin.
set -e
cd "$(dirname "$0")/.."

echo "== RAMAV: setting up demo repositories =="
python3 scripts/setup_demo_repos.py

echo "== RAMAV: installing backend dependencies =="
pip install -r backend/requirements.txt --quiet || pip install -r backend/requirements.txt --break-system-packages --quiet

echo "== RAMAV: starting backend (serves API + dashboard on http://localhost:8000) =="
cd backend
export RAMAV_PORT="${RAMAV_PORT:-8000}"
python3 -m app.main
