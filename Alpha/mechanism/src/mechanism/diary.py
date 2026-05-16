"""Diary page assembly for SessionStart."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pendulum

from mechanism.db import sync

if TYPE_CHECKING:
    from datetime import datetime

DAWN_HOUR = 6


def _today_dawn() -> pendulum.DateTime:
    n = pendulum.now()
    if n.hour >= DAWN_HOUR:
        return n.replace(hour=DAWN_HOUR, minute=0, second=0, microsecond=0)
    return n.subtract(days=1).replace(hour=DAWN_HOUR, minute=0, second=0, microsecond=0)


def _format_page(rows: list[tuple[str, datetime]], date_header: str) -> str | None:
    if not rows:
        return None
    local_tz = pendulum.now().timezone or pendulum.local_timezone()
    parts = [f"## {date_header}"]
    for content, created_at in rows:
        ts = pendulum.instance(created_at).in_tz(local_tz).format("h:mm A")
        parts.append(f"\n[{ts}]\n\n{content}")
    return "\n".join(parts)


def pages_since_yesterday() -> tuple[str | None, str | None]:
    """Return (yesterday_page, today_page) as markdown, or None per page if empty."""
    today_dawn = _today_dawn()
    yesterday_dawn = today_dawn.subtract(days=1)
    now = pendulum.now()

    query = (
        "SELECT content, created_at FROM cortex.diary "
        "WHERE created_at >= %s AND created_at < %s "
        "ORDER BY created_at"
    )
    with sync.open() as conn:
        yesterday_rows = conn.execute(query, (yesterday_dawn, today_dawn)).fetchall()
        today_rows = conn.execute(query, (today_dawn, now)).fetchall()

    yesterday_header = yesterday_dawn.format("ddd MMM D YYYY")
    today_header = today_dawn.format("ddd MMM D YYYY")

    return (
        _format_page(yesterday_rows, yesterday_header),
        _format_page(today_rows, f"{today_header} (so far)"),
    )
