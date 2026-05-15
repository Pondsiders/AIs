# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **Claude Code plugin marketplace** named `AIs`. The repo root is the marketplace; each top-level directory (currently just `Alpha/`) is a plugin published by that marketplace.

The plugin layer itself (JSON/Markdown under `.claude-plugin/`, `Alpha/agents/`, `Alpha/hooks/`) is declarative — Claude Code loads it at runtime, so "running" it means installing the plugin into a session. The real code lives in `Alpha/mechanism/`, a uv-managed Python project with its own test/lint/format toolchain.

## Architecture

Two manifests wire the plugin into the marketplace:

- `.claude-plugin/marketplace.json` — declares the marketplace and lists plugins by relative path (`./Alpha`).
- `Alpha/.claude-plugin/plugin.json` — the plugin manifest (name, description, author).

Inside the plugin, Claude Code auto-discovers a fixed set of subdirectories:

- `Alpha/agents/*.md` — subagent definitions (frontmatter + system prompt). `Alpha/agents/Alpha.md` defines the `Alpha` subagent, referenced as `Alpha:Alpha` (`<plugin>:<agent>`).
- `Alpha/hooks/hooks.json` — registers lifecycle hooks. Wires `SessionStart` (matcher `startup|clear`), `UserPromptSubmit`, and `Stop` to `uv run` entrypoints exposed by the `alpha-mechanism` package (see below), invoked via `${CLAUDE_PLUGIN_ROOT}`.
- `Alpha/settings.json` — plugin-scoped settings. `"agent": "Alpha:Alpha"` makes the Alpha subagent the default for sessions that load this plugin.
- `Alpha/bin/`, `Alpha/skills/` — present but empty; reserved for future slash commands / skills.

### The `alpha-mechanism` package (`Alpha/mechanism/`)

A uv-managed Python 3.12+ package that holds the plugin's actual code. `pyproject.toml` declares four `[project.scripts]` entrypoints:

- `session-start-hook` → `mechanism.entry.session_start:main`
- `user-prompt-submit-hook` → `mechanism.entry.user_prompt_submit:main`
- `stop-hook` → `mechanism.entry.stop:main`
- `copy-from-prod` → `mechanism.scripts.copy_from_prod:main`

What lives where:

- `src/mechanism/entry/{session_start,user_prompt_submit,stop}.py` — hook entrypoints. Each `main()` reads no stdin and writes a single JSON object to stdout following the Claude Code hook protocol (`hookSpecificOutput.additionalContext` for context injection, `decision`/`reason` for `Stop`). Currently a stub.
- `src/mechanism/cortex_server/` — Cortex MCP server (stdio); will expose four tools: `store`, `search`, `get`, `diary`. Currently a stub.
- `src/mechanism/scripts/copy_from_prod.py` — refreshes dev Postgres from the production Cortex tables. Reads from the `alpha-db-replica-3.tail8bd569.ts.net` Tailscale read-replica (Helsinki) via the SELECT-only `alpha_reader` role; writes to local Docker Postgres at `localhost:5432`. Production is two-layer-isolated (read-only server + SELECT-only role); local has no write path to prod. Currently a stub.
- `compose.yaml` — Docker Compose for a dev `pgvector/pgvector:pg17` Postgres bound to `127.0.0.1:5432`, named volume `mechanism-dev-pgdata`.
- `alembic.ini` + `alembic/` — schema migrations for the dev DB only. URL is hard-coded to local Docker Postgres; production schema lifecycle lives elsewhere (Operator's lane). DDL is hand-written — there are no SQLAlchemy models (`target_metadata = None`).
- `justfile` — dev recipes. `just db-up` brings up Postgres, waits for readiness, applies migrations, then runs `copy-from-prod`. `just db-down` / `just db-clean` tear down (the latter wipes the volume). `just test` runs `MODE=test uv run pytest`.
- `tests/` — pytest suite (`asyncio_mode = auto`).

Dev tooling (basedpyright, ruff, pytest, pytest-asyncio, pre-commit, alembic, psycopg, asyncpg-stubs) lives in the `dev` optional-dependencies extra. Production installs (`uv sync` after `/plugin install`) skip it; local work uses `uv sync --extra dev`.

## Working in this repo

- When editing a hook entrypoint under `Alpha/mechanism/src/mechanism/entry/`, preserve the JSON-to-stdout contract — Claude Code parses stdout, so any stray prints will break the hook. The entrypoints run inside the `alpha-mechanism` uv environment, so non-stdlib deps are fine as long as they're declared in `Alpha/mechanism/pyproject.toml`.
- When adding a new plugin, create a sibling directory to `Alpha/` with its own `.claude-plugin/plugin.json`, then add an entry to `.claude-plugin/marketplace.json`. Paths in `marketplace.json` are relative to the repo root.
- When renaming the agent or plugin, update `Alpha/settings.json`'s `agent` field (the `Alpha:Alpha` reference) alongside the file moves.
- Schema changes go through Alembic from `Alpha/mechanism/`: hand-write DDL in a new revision under `alembic/versions/`, then `just db-up` (or `uv run alembic upgrade head`) to apply. These migrations only ever touch the local Docker DB — never run them against production.
- `copy-from-prod` is safe to re-run: the production replica is structurally read-only and the script's only write target is the local Docker Postgres.

## Authorship for Git

Unless otherwise stated, the *author* for all git commits is `Alpha <alpha@alphafornow.com>`, with a `Co-Authored-By: Jeffery Harrell <jefferyharrell@gmail.com>` trailer.
