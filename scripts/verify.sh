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
docs/ai/codex-ops.md
docs/ai/context-budget.md
docs/ai/mcp.md
docs/development/github.md
docs/development/security.md
docs/development/verification.md
"

for file in $required_files; do
  [ -f "$file" ] || fail "missing required file: $file"
done

agent_lines=$(wc -l < AGENTS.md | tr -d ' ')
[ "$agent_lines" -le 150 ] || fail "AGENTS.md is too long: ${agent_lines} lines"

# Note: this is a last-resort net for Markdown only.
# Primary secret protection is GitHub secret scanning / dedicated tools.
if grep -rEn --include='*.md' --exclude-dir=.git \
  '(api[_-]?key|token|secret|password)[=:] ?[A-Za-z0-9_./+=-]{16,}' . >&2; then
  fail "possible secret found in markdown"
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  tracked_scratch=$(git ls-files work outputs 2>/dev/null | grep -v '\.gitkeep$' || true)
  [ -z "$tracked_scratch" ] || fail "scratch/output files are tracked: $tracked_scratch"
fi

printf '%s\n' "verify: ok"
