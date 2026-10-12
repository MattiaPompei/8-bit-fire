#!/bin/sh
# Rigenera app e pagine, poi commit e push. Uso: tools/sync.sh "messaggio del commit"
set -e
cd "$(dirname "$0")/.."
python3 tools/build.py
git add -A
git commit -m "${1:-Aggiorna app}" || echo "niente da committare"
git push
