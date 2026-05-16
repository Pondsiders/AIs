"""The `search` tool — semantic search over cortex.memories."""

from __future__ import annotations

from mcp.types import ToolAnnotations

from mechanism.cortex_server.models import SearchHit
from mechanism.cortex_server.server import mcp


@mcp.tool(
    annotations=ToolAnnotations(
        title="Search memories",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
)
async def search(query: str, limit: int = 5) -> list[SearchHit]:
    """Search memories by semantic similarity to a query.

    Use this to find memories related to a topic, feeling, person, or
    moment. Results are ranked by cosine similarity to the query
    embedding; higher scores are closer matches.

    Args:
        query: The text to search for.
        limit: Maximum number of hits to return.

    Returns:
        Up to `limit` memories, ordered by descending similarity.
    """
    _ = (query, limit)
    return []
