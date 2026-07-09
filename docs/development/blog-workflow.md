# Blog Workflow (Design -> Review -> Verify -> Fix -> Publish)

This repository manages Markdown drafts for a self-hosted WordPress blog.
Drafts are written and reviewed here like code; publishing to WordPress is
a deliberate manual step, not automated.

## Directory Layout

- `blog/drafts/` - one Markdown file per post
- `blog/style-guide.md` - writing, review, publishing, and improvement guide
- `templates/blog-post.md` - full article template for a new draft
- `templates/blog-specialized-repo/` - copyable template for a blog-only repository
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

1. **Design** - use `blog/style-guide.md` to choose the reader, search
   phrase, proof source, and article angle.
2. **Draft** - copy `templates/blog-post.md` to `blog/drafts/<slug>.md`,
   write the post, and keep concrete numbers, tables, FAQ, and evidence.
3. **Review** - open a pull request. Reviewers check SEO title, readability,
   practical examples, evidence, and missing edge cases.
4. **Verify** - CI runs `./scripts/verify.sh`, which checks every file
   under `blog/drafts/` has valid frontmatter with a `title:` field.
5. **Fix** - address review or CI feedback with more commits on the same
   pull request.
6. **Publish (manual, by design)** - after merge, run:

   ```sh
   WP_SITE_URL=https://example.com \
   WP_USERNAME=your-wp-username \
   WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx' \
   python3 scripts/publish-wordpress.py blog/drafts/<slug>.md
   ```

   This creates a WordPress post with status `draft` via the REST API --
   it never publishes automatically. Log into wp-admin, review the draft,
   and click Publish yourself.
7. **Measure and improve** - after 2-4 weeks, review Search Console and
   analytics data. Improve title, intro, headings, examples, FAQ, or internal
   links based on actual queries and reader behavior.

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
