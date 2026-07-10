# MCP Configuration Principles

This repository does not currently define project-specific MCP servers.

Use project MCP configuration only when it provides a clear benefit that cannot be handled by the default Codex environment.

## Add an MCP Server When

- It is required for the normal development workflow.
- It has a narrow, understandable permission boundary.
- It avoids repeated manual setup.
- It can be documented and reproduced by a new contributor.

## Avoid an MCP Server When

- It duplicates an existing local command.
- It requires broad access for a narrow task.
- It is experimental and not needed by most work.
- Its credentials or side effects are unclear.

## Permission Review

Before adding or enabling a server, document:

- Server name and owner.
- Official documentation or source repository.
- What data it can read.
- What data it can write.
- Filesystem scope.
- Whether it can access the network.
- What credentials it requires.
- How credentials are stored and revoked.
- How to disable or remove it.
- Human approver and review date.

## Review Record Template

```markdown
## <Server Name>

- Owner:
- Official source:
- Purpose:
- Read access:
- Write access:
- Filesystem scope:
- Network access:
- Credentials:
- Revocation method:
- Human approver:
- Last reviewed: YYYY-MM-DD
- Decision: approved / rejected / limited trial
```

Record completed reviews as new sections at the end of this file, one section per server. Never include actual credentials or secret values.
