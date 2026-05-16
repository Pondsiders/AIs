"""Entry point for the UserPromptSubmit hook."""

from __future__ import annotations

import json
import sys
import traceback


def main() -> None:
    """Handle a UserPromptSubmit hook invocation from Claude Code."""
    try:
        json.dump(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": "",
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
            "The following exception was raised in user-prompt-submit-hook:",
            file=sys.stderr,
        )
        print("".join(traceback.format_exception(exc)), file=sys.stderr)
        sys.exit(2)
