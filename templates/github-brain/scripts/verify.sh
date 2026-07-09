#!/usr/bin/env sh
set -eu

fail() {
  printf '%s\n' "verify: $1" >&2
  exit 1
}

required_files="
AGENTS.md
README.md
docs/index.md
docs/learnings/index.md
docs/setup/index.md
docs/workflow/index.md
scripts/verify.sh
"

for file in $required_files; do
  [ -f "$file" ] || fail "missing required file: $file"
done

agent_lines=$(wc -l < AGENTS.md | tr -d ' ')
[ "$agent_lines" -le 120 ] || fail "AGENTS.md is too long: ${agent_lines} lines"

if grep -rEn --include='*.md' --exclude-dir=.git \
  '(api[_-]?key|token|secret|password)[=:][[:space:]]*['\''"]?[A-Za-z0-9_./+=-]{16,}' . >&2; then
  fail "possible secret found in markdown"
fi

printf '%s\n' "verify: ok"
