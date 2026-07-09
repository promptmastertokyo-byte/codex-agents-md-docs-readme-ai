#!/usr/bin/env sh
set -eu

fail() {
  printf '%s\n' "new-post: $1" >&2
  exit 1
}

[ "$#" -eq 1 ] || fail "usage: sh scripts/new-post.sh <slug>"

slug=$1
case "$slug" in
  *[!A-Za-z0-9._-]* | "" )
    fail "slug must contain only letters, numbers, dots, underscores, or hyphens"
    ;;
esac

template=templates/blog-post.md
draft=blog/drafts/$slug.md

[ -f "$template" ] || fail "missing template: $template"
[ ! -e "$draft" ] || fail "draft already exists: $draft"

year=$(date '+%Y')
month=$(date '+%m')
day=$(date '+%d')
month=${month#0}
day=${day#0}
verify_date="${year}年${month}月${day}日"

sed \
  -e "s/{{VERIFY_DATE}}/$verify_date/g" \
  -e "s/^slug: .*/slug: $slug/" \
  "$template" > "$draft"

printf '%s\n' "created: $draft"
