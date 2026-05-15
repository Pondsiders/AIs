"""Entry point for the UserPromptSubmit hook."""

from __future__ import annotations

import sys


def main() -> None:
    """Handle a UserPromptSubmit hook invocation from Claude Code.

    Not yet implemented. Exits 2 to signal "hook errored" per the
    Claude Code hook contract; blocks the prompt from reaching Claude.
    """
    sys.exit(2)
