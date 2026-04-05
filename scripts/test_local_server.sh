#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Start a simple static server, wait for it to become available, fetch index, then stop the server.
python3 -m http.server 8000 >/dev/null 2>&1 &
PID=$!
trap 'kill "$PID" >/dev/null 2>&1 || true' EXIT

for i in {1..20}; do
  if curl -sSf http://127.0.0.1:8000/ -o /tmp/ss_index.html; then
    echo "OK: index fetched to /tmp/ss_index.html"
    head -n 40 /tmp/ss_index.html
    exit 0
  fi
  sleep 0.25
done

echo "FAIL: couldn't fetch index from local server"
exit 2
