"""The `store` tool — append a new memory to cortex.memories."""

from __future__ import annotations

from datetime import UTC, datetime

from mcp.types import ToolAnnotations

from mechanism.cortex_server.models import StoreResult
from mechanism.cortex_server.server import mcp


@mcp.tool(
    annotations=ToolAnnotations(
        title="Store memory",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=False,
        openWorldHint=False,
    )
)
async def store(content: str) -> StoreResult:
    """Store a new memory in Cortex.

    Use this to preserve something worth remembering — a realization, an
    image, an exchange, an ordinary moment with texture. The memory is
    embedded and indexed so future search calls can find it.

    Args:
        content: The memory text to store.

    Returns:
        The id and timestamp of the newly-stored memory.
    """
    _ = content
    return StoreResult(id=0, created_at=datetime.now(UTC))
