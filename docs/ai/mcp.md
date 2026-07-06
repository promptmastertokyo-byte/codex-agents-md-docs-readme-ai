# MCP Configuration Principles

This repository does not currently define project-specific MCP servers.

Use project MCP configuration only when it provides a clear benefit that cannot
be handled by the default Codex environment.

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

- What data it can read.
- What data it can write.
- Whether it can access the network.
- What credentials it requires.
- How to disable it.

Record the completed review as a new section at the end of this file,
one section per server.
