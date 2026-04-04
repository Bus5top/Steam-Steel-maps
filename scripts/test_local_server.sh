#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Start a simple static server, fetch index, then stop the server.
python3 -m http.server 8000 &
PID=$!
sleep 0.5
if curl -sSf http://127.0.0.1:8000/ -o /tmp/ss_index.html; then
  echo "OK: index fetched to /tmp/ss_index.html"
  head -n 40 /tmp/ss_index.html
  kill $PID || true
  exit 0
else
  echo "FAIL: couldn't fetch index from local server"
  kill $PID || true
  exit 2
fi
