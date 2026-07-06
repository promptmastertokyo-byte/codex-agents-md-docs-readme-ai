# Security and Permission Boundaries

This repository should not store secrets or machine-specific credentials.

## Do Not Commit

- API keys
- Tokens
- Private keys
- Passwords
- `.env` files with real values
- Local cache directories
- Personal browser or app data

## Permission Model

Keep automation narrow:

- Prefer read-only access unless write access is required.
- Prefer repository-local commands over global machine changes.
- Document third-party tools before making them part of the workflow.

## Third-Party Skills and Tools

Before relying on a third-party skill, plugin, or MCP server:

- Confirm what it can read and write.
- Prefer official or locally audited tools.
- Avoid broad filesystem or network permissions for convenience.
- Record required setup in `docs/development/` or `docs/ai/`.

## Secret Handling

Use example files such as `.env.example` for names and shape only.
Use the hosting provider or local secret manager for real values.

