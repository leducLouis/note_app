#!/bin/sh
cd "$CLAUDE_PROJECT_DIR" || exit 0
.venv/bin/python -m pytest -q -x 1>&2 || exit 2
