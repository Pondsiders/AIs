"""Entry point for the Stop hook."""

from __future__ import annotations

import sys
import traceback


def main() -> None:
    """Handle a Stop hook invocation from Claude Code."""
    try:
        # Stop's canonical "approve the stop" is exit 0 with no output.
        # To block the stop instead, print to stdout:
        #     {"decision": "block", "reason": "..."}
        return
    except Exception as exc:
        print(
            "Please report this error to your conversation partner.",
            file=sys.stderr,
        )
        print(
            "The following exception was raised in stop-hook:",
            file=sys.stderr,
        )
        print("".join(traceback.format_exception(exc)), file=sys.stderr)
        sys.exit(2)
