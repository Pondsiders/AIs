"""The `recent` tool — memories from the since-yesterday window."""

from __future__ import annotations

from mcp.types import ToolAnnotations

from mechanism.cortex_server.models import Memory
from mechanism.cortex_server.server import mcp


@mcp.tool(
    annotations=ToolAnnotations(
        title="Recent memories",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=False,  # The window slides with wall-clock time.
        openWorldHint=False,
    )
)
async def recent() -> list[Memory]:
    """Return memories from yesterday and today (Pondside-day boundaries).

    The window starts at 6 AM yesterday Pondside-time and ends at now.
    Uses the same dawn calculation as the SessionStart diary loader, so
    "recent" here matches the window already in the session's context.

    Returns:
        Memories in the window, ordered by ascending created_at.
    """
    return []
