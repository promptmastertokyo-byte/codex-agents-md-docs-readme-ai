#!/usr/bin/env sh
set -eu

fail() {
  printf '%s\n' "verify: $1" >&2
  exit 1
}

required_files="
AGENTS.md
README.md
blog/style-guide.md
docs/publishing.md
docs/measurement.md
templates/blog-post.md
templates/review-report.md
templates/improvement-report.md
"

for file in $required_files; do
  [ -f "$file" ] || fail "missing required file: $file"
done

for draft in blog/drafts/*.md; do
  [ -e "$draft" ] || continue
  [ "$(head -n 1 "$draft")" = "---" ] || fail "blog draft missing frontmatter: $draft"
  grep -q '^title:' "$draft" || fail "blog draft missing title: $draft"
  grep -q '^description:' "$draft" || fail "blog draft missing description: $draft"
  grep -q '^slug:' "$draft" || fail "blog draft missing slug: $draft"
done

printf '%s\n' "verify: ok"
