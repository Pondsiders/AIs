"""Cortex MCP server — stdio, five tools: store, get, search, recent, diary.

The `mcp` instance lives in `server`; tool modules are imported here
for their side effects (each module's `@mcp.tool` decorator registers
its tool against the shared instance). `fastmcp run` on this package
picks up the full tool surface.
"""

from mechanism.cortex_server import diary, get, recent, search, store
from mechanism.cortex_server.server import mcp

# Side-effect imports — silence the unused-import warnings.
_ = (store, get, search, recent, diary)

__all__ = ["mcp"]
