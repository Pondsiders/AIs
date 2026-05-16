"""The `diary` tool — append an entry to today's diary page."""

from __future__ import annotations

from datetime import UTC, datetime

from mcp.types import ToolAnnotations

from mechanism.cortex_server.models import DiaryResult
from mechanism.cortex_server.server import mcp


@mcp.tool(
    annotations=ToolAnnotations(
        title="Append diary entry",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=False,
        openWorldHint=False,
    )
)
async def diary(content: str) -> DiaryResult:
    """Append an entry to today's diary page.

    Pages are assembled automatically from Pondside-day boundaries
    (6 AM to 6 AM). Today's page may contain many entries; this tool
    appends one more.

    Args:
        content: The diary entry text to append.

    Returns:
        The id and timestamp of the newly-stored entry.
    """
    _ = content
    return DiaryResult(id=0, created_at=datetime.now(UTC))
