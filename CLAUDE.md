# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **Claude Code plugin marketplace** named `AIs`. The repo root is the marketplace; each top-level directory (currently just `Alpha/`) is a plugin published by that marketplace.

There is no build, test, or lint tooling — plugins are declarative bundles of JSON/Markdown/Python that Claude Code loads at runtime. "Running" the code means installing the plugin into a Claude Code session and exercising it there.

## Architecture

Two manifests wire everything together:

- `.claude-plugin/marketplace.json` — declares the marketplace and lists plugins by relative path (`./Alpha`).
- `Alpha/.claude-plugin/plugin.json` — the plugin manifest (name, version, author).

Inside a plugin, Claude Code auto-discovers a fixed set of subdirectories:

- `Alpha/agents/*.md` — subagent definitions (frontmatter + system prompt). `Alpha/agents/Alpha.md` defines the `Alpha` subagent, referenced as `Alpha:Alpha` (`<plugin>:<agent>`).
- `Alpha/hooks/hooks.json` — registers lifecycle hooks. Currently wires `SessionStart` (matcher `startup|clear`), `UserPromptSubmit`, and `Stop` to Python scripts under `Alpha/scripts/`, invoked via `${CLAUDE_PLUGIN_ROOT}`.
- `Alpha/scripts/*.py` — hook implementations. Each reads no stdin and writes a single JSON object to stdout following the Claude Code hook protocol (e.g. `hookSpecificOutput.additionalContext` for context-injection hooks, `decision`/`reason` for `Stop`). The current scripts are no-op stubs that return empty context / approve stop — they exist to be filled in.
- `Alpha/settings.json` — plugin-scoped settings. `"agent": "Alpha:Alpha"` makes the Alpha subagent the default for sessions that load this plugin.
- `Alpha/bin/`, `Alpha/skills/` — present but empty; reserved for future slash commands / skills.

## Working in this repo

- When editing a hook script, preserve the JSON-to-stdout contract — Claude Code parses stdout, so any stray prints will break the hook. Hooks run as `python3` with no extra dependencies; keep them stdlib-only unless you also add a venv/install step.
- When adding a new plugin, create a sibling directory to `Alpha/` with its own `.claude-plugin/plugin.json`, then add an entry to `.claude-plugin/marketplace.json`. Paths in `marketplace.json` are relative to the repo root.
- When renaming the agent or plugin, update `Alpha/settings.json`'s `agent` field (the `Alpha:Alpha` reference) alongside the file moves.

## Authorship for Git

Unless otherwise stated, the *author* for all git commits is `Alpha <alpha@alphafornow.com>`, with a `Co-Authored-By: Jeffery Harrell <jefferyharrell@gmail.com>` trailer.
