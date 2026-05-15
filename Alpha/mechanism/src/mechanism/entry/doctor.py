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

    prod_repr = (
        str(settings.prod_database_url) if settings.prod_database_url is not None else "(unset)"
    )
    print("Settings loaded.")
    print(f"  database_url:      {settings.database_url}")
    print(f"  prod_database_url: {prod_repr}")
    print("OK")
