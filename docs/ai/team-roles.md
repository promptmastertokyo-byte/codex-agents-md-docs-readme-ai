# AI Team Roles and Approval Gates

Use this file for editorial and multi-agent work. Routine repository maintenance does not need to load it.

## Roles

| AI | Primary role | Scope |
|---|---|---|
| Claude (chat) | Editorial lead | Planning, titles, structure review, final pre-publication review, metrics analysis, and playbook recommendations |
| Claude Code | Draft production | Create drafts, rewrite content, run verification, prepare pull requests, and create WordPress draft posts |
| Codex | Repository infrastructure | Maintain scripts and CI, expand verification, and investigate technical risk |
| GPT | Independent reviewer | Provide alternative titles and third-party review; do not directly edit editorial files unless assigned |
| Gemini | Research support | Verify official sources and statistics; a human transfers validated findings into the repository |
| Grok | Trend discovery | Find reader concerns and X trends; every claim and quotation requires manual verification |

## Workflow Boundary

- Claude (chat) owns planning through briefs.
- Claude Code owns drafting through WordPress draft creation.
- Codex owns repository infrastructure and verification changes.
- Gemini and Grok do not receive direct repository access. Their findings move through human verification before being recorded.

## Approval Gates

- Human approval is required before public publication.
- WordPress automation may create a draft post only; it must never publish automatically.
- An AI may recommend promoting a lesson to `playbook`, but a human approves the promotion.
- Repository changes should use a branch and pull request when practical.
- No AI may approve and merge its own pull request.
- Destructive commands, credential changes, permission expansion, and external writes require explicit human authorization.

## Escalation

Stop and ask for human review when:

- instructions conflict;
- evidence is missing or sources disagree;
- a change expands access, network, filesystem, or publishing permissions;
- verification cannot run or fails for an unrelated reason;
- the proposed action is irreversible or affects public content.
