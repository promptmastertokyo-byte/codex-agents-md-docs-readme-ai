#!/usr/bin/env python3
"""Push a Markdown draft to a self-hosted WordPress site as a draft post.

Reads WP_SITE_URL, WP_USERNAME, and WP_APP_PASSWORD from the environment.
Always creates the post with status "draft" -- publishing is a manual
step the operator takes in wp-admin.

The Markdown body is converted to HTML before sending (the WordPress REST
API expects HTML in `content`). Requires the `markdown` package:

    pip install markdown
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

try:
    import markdown as md
except ImportError:
    md = None


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("draft is missing the opening '---' frontmatter delimiter")
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("draft is missing the closing '---' frontmatter delimiter")

    meta = {}
    for line in lines[1:end]:
        m = re.match(r"^(title|description|slug):\s*(.+)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    if "title" not in meta:
        raise ValueError("frontmatter is missing a 'title:' field")

    body = "\n".join(lines[end + 1:]).strip() + "\n"
    body = re.sub(r"^#\s+" + re.escape(meta["title"]) + r"\s*\n+", "", body)
    return meta, body


def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} <blog/drafts/*.md>")
    draft_path = sys.argv[1]

    site_url = os.environ.get("WP_SITE_URL")
    username = os.environ.get("WP_USERNAME")
    app_password = os.environ.get("WP_APP_PASSWORD")
    if not (site_url and username and app_password):
        sys.exit(
            "WP_SITE_URL, WP_USERNAME, and WP_APP_PASSWORD environment "
            "variables are required. See .env.example."
        )

    with open(draft_path, encoding="utf-8") as f:
        meta, body = parse_frontmatter(f.read())

    if md is None:
        sys.exit(
            "The 'markdown' package is required to convert the draft to HTML "
            "(WordPress expects HTML content). Install it with: pip install markdown"
        )
    html = md.markdown(body, extensions=["tables", "fenced_code"])

    post = {"title": meta["title"], "content": html, "status": "draft"}
    if "slug" in meta:
        post["slug"] = meta["slug"]
    if "description" in meta:
        post["excerpt"] = meta["description"]

    payload = json.dumps(post).encode()
    endpoint = site_url.rstrip("/") + "/wp-json/wp/v2/posts"
    auth = base64.b64encode(f"{username}:{app_password}".encode()).decode()

    request = urllib.request.Request(
        endpoint,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
    except urllib.error.HTTPError as e:
        sys.exit(f"WordPress API error {e.code}: {e.read().decode(errors='replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"Could not reach WordPress: {e.reason}")

    print(f"Created WordPress draft: {result.get('link', '(no link returned)')}")
    print("Status is 'draft' -- log into wp-admin and click Publish when ready.")


if __name__ == "__main__":
    main()
