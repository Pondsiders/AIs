#!/usr/bin/env python3
"""Stop hook — decides whether the agent is allowed to stop."""
import json
import sys


def main() -> int:
    output = {
        "decision": "approve",
        "reason": "okay to stop",
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
