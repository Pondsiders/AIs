"""Entry point for the SessionStart hook."""

from __future__ import annotations

import json
import sys
import traceback

from mechanism.diary import pages_since_yesterday


def main() -> None:
    """Handle a SessionStart hook invocation from Claude Code."""
    try:
        yesterday, today = pages_since_yesterday()
        pages = [p for p in (yesterday, today) if p is not None]
        additional_context = "\n\n".join(pages)
        json.dump(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": additional_context,
                },
            },
            sys.stdout,
        )
    except Exception as exc:
        print(
            "Please report this error to your conversation partner.",
            file=sys.stderr,
        )
        print(
            "The following exception was raised in session-start-hook:",
            file=sys.stderr,
        )
        print("".join(traceback.format_exception(exc)), file=sys.stderr)
        sys.exit(2)
