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
docs/ai/github-brain.md
docs/ai/mcp.md
docs/development/blog-workflow.md
docs/development/github.md
docs/development/multi-device-workflow.md
docs/development/security.md
docs/development/verification.md
blog/style-guide.md
templates/blog-post.md
templates/blog-specialized-repo/AGENTS.md
templates/blog-specialized-repo/README.md
templates/blog-specialized-repo/blog/style-guide.md
templates/blog-specialized-repo/docs/measurement.md
templates/blog-specialized-repo/docs/publishing.md
templates/blog-specialized-repo/scripts/verify.sh
templates/blog-specialized-repo/templates/blog-post.md
templates/blog-specialized-repo/templates/improvement-report.md
templates/blog-specialized-repo/templates/review-report.md
templates/github-brain/AGENTS.md
templates/github-brain/README.md
templates/github-brain/docs/index.md
templates/github-brain/docs/learnings/index.md
templates/github-brain/docs/setup/index.md
templates/github-brain/docs/workflow/index.md
templates/github-brain/scripts/verify.sh
templates/github-brain/templates/review-request.md
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

for draft in blog/drafts/*.md; do
  [ -e "$draft" ] || continue
  [ "$(head -n 1 "$draft")" = "---" ] || fail "blog draft missing frontmatter: $draft"
  grep -q '^title:' "$draft" || fail "blog draft missing 'title:' in frontmatter: $draft"
done

printf '%s\n' "verify: ok"
