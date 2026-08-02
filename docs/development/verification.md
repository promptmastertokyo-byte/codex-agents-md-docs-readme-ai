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

## Reusable Hygiene Checks

The three checks that are generic across repositories (AGENTS.md length,
Markdown secret scanning, scratch/output tracking) live in
`.github/workflows/hygiene-reusable.yml` in this repository, not in
`scripts/verify.sh`. `scripts/verify.sh` only contains checks specific to
this repository's content (required files, blog draft frontmatter,
`templates/` recursive verification).

`.github/workflows/hygiene.yml` calls the reusable workflow and then the
reusable workflow runs `scripts/verify.sh` (if present) for the
repository-specific checks.

### Using it from another repository

Add a workflow that calls the reusable workflow:

```yaml
name: Repository Hygiene

on:
  pull_request:
  push:
    branches: [main]

jobs:
  hygiene:
    uses: promptmastertokyo-byte/codex-agents-md-docs-readme-ai/.github/workflows/hygiene-reusable.yml@main
    permissions:
      contents: read
```

Inputs (all optional):

- `agents-file` (default `AGENTS.md`) — path to the agents file whose line
  count is checked.
- `max-agents-lines` (default `150`) — maximum allowed line count.
- `verify-script` (default `scripts/verify.sh`) — repository-specific verify
  script to run after the generic checks. If it doesn't exist, that step is
  skipped with a notice instead of failing.
- `scratch-dirs` (default `"work outputs"`) — space-separated directories
  that must not be tracked by git.

If the calling repository is private and the workflow repository is also
private, enable access under the workflow repository's
**Settings → Actions → General → Access**, or the reusable workflow call
will fail to resolve.
