# Multi-Device Workflow (Phone + PC)

This repository is meant to be worked on from more than one device, for
example Claude Code on the web from a phone and a local clone on a PC.
The goal is to let both continue the same work without silently
overwriting each other.

## Core Rule

Never edit the same branch from two devices at the same time without
syncing first. Pick one pattern:

1. **One branch at a time** - finish a session and push (or merge) from
   one device before starting on the other.
2. **One branch per session** - each device/session works on its own
   short-lived branch and merges via pull request.

## Starting a Session (any device)

```sh
git fetch origin <branch>
git pull origin <branch>
```

Do this before making changes, even if you just pushed from another
device minutes ago.

## Ending a Session (any device)

- Commit logical units of work.
- Push before switching devices: `git push -u origin <branch>`.
- Do not leave uncommitted changes if you plan to continue elsewhere;
  commit or stash them first.

## PC Setup

- Clone the repository normally (`git clone <url>`).
- Follow the branch naming and pull request conventions in
  `docs/development/github.md`.

## Phone / Claude Code on the Web

- Sessions run on a dedicated branch (for example `claude/<slug>`).
  Treat it like any other feature branch: pull before continuing it,
  push when done.
- Merge it into the branch you use on your PC (or vice versa) through a
  pull request rather than copying files by hand.

## Conflict Avoidance

- Keep changes small and push often, per the Backup Reliability section
  of `docs/development/github.md`.
- If both devices touched the same file, resolve it locally with
  `git pull --rebase`, then re-push.
- Use pull requests as the single merge point; avoid fast-forwarding
  `main` by hand from two places at once.

## See Also

- `docs/development/github.md` - branch, pull request, and CI conventions
- `docs/development/verification.md` - run `./scripts/verify.sh` after
  pulling changes made on another device
