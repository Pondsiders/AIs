"""Entry point for the `doctor` diagnostic command."""

from __future__ import annotations

import sys

from pydantic import ValidationError

from mechanism.settings import get_settings


def main() -> None:
    """Verify configuration loads cleanly and report status to stdout."""
    try:
        settings = get_settings()
    except ValidationError as exc:
        print("doctor: configuration error", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        sys.exit(1)

    print("Settings loaded.")
    print(f"  database_url: {settings.database_url}")
    print("OK")
