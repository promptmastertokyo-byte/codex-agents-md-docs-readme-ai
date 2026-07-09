#!/usr/bin/env python3
"""Push a Markdown draft to a self-hosted WordPress site as a draft post.

Reads WP_SITE_URL, WP_USERNAME, and WP_APP_PASSWORD from the environment.
Always creates the post with status "draft" -- publishing is a manual
step the operator takes in wp-admin.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("draft is missing the opening '---' frontmatter delimiter")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError("draft is missing the closing '---' frontmatter delimiter")

    title = None
    for line in lines[1:end]:
        if line.startswith("title:"):
            title = line[len("title:"):].strip()
    if not title:
        raise ValueError("frontmatter is missing a 'title:' field")

    body = "\n".join(lines[end + 1 :]).strip() + "\n"
    return title, body


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
        title, body = parse_frontmatter(f.read())

    payload = json.dumps({"title": title, "content": body, "status": "draft"}).encode()
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
        with urllib.request.urlopen(request) as response:
            result = json.load(response)
    except urllib.error.HTTPError as e:
        sys.exit(f"WordPress API error {e.code}: {e.read().decode(errors='replace')}")

    print(f"Created WordPress draft: {result.get('link', '(no link returned)')}")
    print("Status is 'draft' -- log into wp-admin and click Publish when ready.")


if __name__ == "__main__":
    main()
