#!/usr/bin/env python3
"""SessionStart hook — emits additional context for new sessions and after /clear."""

import json
import sys


def main() -> int:
    """Emit an empty additionalContext payload for the SessionStart hook."""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "",
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
