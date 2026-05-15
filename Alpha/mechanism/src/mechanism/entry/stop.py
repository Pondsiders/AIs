"""Entry point for the Stop hook."""

from __future__ import annotations

import sys


def main() -> None:
    """Handle a Stop hook invocation from Claude Code.

    Not yet implemented. Exits 2 to signal "hook errored" per the
    Claude Code hook contract.
    """
    sys.exit(2)
