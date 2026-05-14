#!/usr/bin/env python3
"""UserPromptSubmit hook — emits additional context appended to each user prompt."""
import json
import sys


def main() -> int:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": "",
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
