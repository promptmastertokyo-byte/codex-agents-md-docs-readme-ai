# GitHub Operations

This repository is prepared for a lightweight GitHub workflow.

## Branch Strategy

- `main` is the stable branch.
- Work happens on short-lived feature branches.
- Branch names should describe intent, for example `docs/agent-guidelines`.

## Pull Requests

Each pull request should include:

- What changed.
- Why it changed.
- How it was verified.
- Any follow-up work or known risk.

## CI

The default CI workflow runs `./scripts/verify.sh`.

CI is intentionally simple so the same checks work locally and remotely.

## Backup Reliability

GitHub can be used as a backup only if changes are pushed regularly.

Recommended minimum:

- Commit logical units of work.
- Push feature branches before risky edits.
- Keep `main` protected when the repository becomes important.
- Require CI before merging once code or production docs depend on it.

