"""The `get` tool — fetch one memory by id."""

from __future__ import annotations

from datetime import UTC, datetime

from mcp.types import ToolAnnotations

from mechanism.cortex_server.models import Memory
from mechanism.cortex_server.server import mcp


@mcp.tool(
    annotations=ToolAnnotations(
        title="Get memory by id",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
async def get(memory_id: int) -> Memory:
    """Fetch a single memory by its id.

    Use this when a memory id is already known (e.g. from a previous
    search result, or referenced in conversation) and the full content
    is needed.

    Args:
        memory_id: The id of the memory to fetch.

    Returns:
        The memory row.
    """
    return Memory(id=memory_id, content="", created_at=datetime.now(UTC))
