# Verification Loop

The local verification command is:

```sh
./scripts/verify.sh
```

Run it before handing off meaningful changes. CI runs the same command on pull requests and on pushes to `main` or `claude/**` branches.

## What It Checks

The current docs-first verification loop checks:

- Required repository, workflow, and command files exist.
- `AGENTS.md` stays within the context budget.
- Markdown files do not contain obvious real-looking secrets. This covers `*.md` only and is a last-resort net; rely on GitHub secret scanning or a dedicated scanner as primary protection.
- Scratch and output folders are not accidentally tracked.
- Shell scripts pass `sh -n` syntax validation.
- Python scripts pass `python3 -m py_compile` syntax validation.
- Blog drafts include required frontmatter and no unresolved verification-date placeholder.
- Reusable repository templates pass their own verification scripts.

## Local and CI Parity

Keep the local command and CI entry point identical:

```sh
./scripts/verify.sh
```

Do not add a CI-only validation without documenting how to run the equivalent check locally. If a check needs an optional tool, fail with a clear setup message or document why CI is authoritative.

## When to Expand It

Add checks when the repository gains:

- Application code: add tests and linting.
- Frontend UI: add build checks and screenshot review.
- Generated assets: add freshness or reproducibility checks.
- External integrations: add configuration validation.
- More Markdown links: add a link checker.
- More shell logic: add ShellCheck in addition to `sh -n`.

## Reporting

When reporting a change, include:

- Files changed.
- Verification command run.
- Whether it passed.
- Any checks skipped and why.

## When Copying This Repository

Update the `required_files` list in `scripts/verify.sh` first. It is the most likely check to fail in a new repository.
