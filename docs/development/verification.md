# Verification Loop

The local verification command is:

```sh
./scripts/verify.sh
```

Run it before handing off meaningful changes.

## What It Checks

The current docs-first verification loop checks:

- Required files exist.
- `AGENTS.md` stays reasonably short.
- Markdown files do not contain obvious real-looking secrets. This check
  covers `*.md` only and is a last-resort net; rely on GitHub secret
  scanning or a dedicated scanner as the primary protection.
- Scratch and output folders are not accidentally tracked.

## When to Expand It

Add checks when the repository gains:

- Application code: add tests and linting.
- Frontend UI: add build checks and screenshot review.
- Generated assets: add freshness or reproducibility checks.
- External integrations: add configuration validation.

## Reporting

When reporting a change, include:

- Files changed.
- Verification command run.
- Whether it passed.
- Any checks skipped and why.

## When Copying This Repository

Update the `required_files` list in `scripts/verify.sh` first. It is the
most likely check to fail in a new repository.
