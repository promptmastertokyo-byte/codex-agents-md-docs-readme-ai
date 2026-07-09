# Blog Workflow (Design -> Review -> Verify -> Fix -> Publish)

This repository manages Markdown drafts for a self-hosted WordPress blog.
Drafts are written and reviewed here like code; publishing to WordPress is
a deliberate manual step, not automated.

## Directory Layout

- `blog/drafts/` - one Markdown file per post
- `blog/style-guide.md` - tone and structure reference distilled from past articles
- `templates/blog-post.md` - starting frontmatter for a new draft
- `scripts/publish-wordpress.py` - pushes a draft to WordPress as a draft post

## Draft Format

Every draft needs a `title:` frontmatter field:

```markdown
---
title: My Post Title
---

Post body goes here.
```

## Cycle

1. **Design** - copy `templates/blog-post.md` to `blog/drafts/<slug>.md`,
   write the post, commit on a feature branch, and push.
2. **Review** - open a pull request. Reviewers read the diff and comment,
   the same as a code review.
3. **Verify** - CI runs `./scripts/verify.sh`, which checks every file
   under `blog/drafts/` has valid frontmatter with a `title:` field.
4. **Fix** - address review or CI feedback with more commits on the same
   pull request.
5. **Publish (manual, by design)** - after merge, run:

   ```sh
   WP_SITE_URL=https://example.com \
   WP_USERNAME=your-wp-username \
   WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx' \
   python3 scripts/publish-wordpress.py blog/drafts/<slug>.md
   ```

   This creates a WordPress post with status `draft` via the REST API --
   it never publishes automatically. Log into wp-admin, review the draft,
   and click Publish yourself.

## Credentials

- `WP_SITE_URL`, `WP_USERNAME`, `WP_APP_PASSWORD` are read from the
  environment and must never be committed.
- Generate an Application Password in WordPress under
  Users -> Profile -> Application Passwords.
- Copy `.env.example` to `.env` (already git-ignored) and load it before
  running the script, e.g. `set -a; . ./.env; set +a`.

## See Also

- `docs/development/github.md` - branch, pull request, and CI conventions
- `docs/development/security.md` - secret handling rules
- `docs/development/verification.md` - local and CI verification loop
