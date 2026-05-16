"""Pydantic models for Cortex MCP tool inputs and outputs.

These are the wire shapes the MCP server returns to clients. FastMCP
auto-generates JSON Schema from these so the LLM sees properly-shaped
tool descriptions and the inspector renders structured output.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Memory(BaseModel):
    """A single memory row from cortex.memories."""

    id: int = Field(description="Memory id.")
    content: str = Field(description="The memory text.")
    created_at: datetime = Field(description="When the memory was stored.")


class SearchHit(BaseModel):
    """A memory returned by a semantic search, with its similarity score."""

    id: int = Field(description="Memory id.")
    content: str = Field(description="The memory text.")
    created_at: datetime = Field(description="When the memory was stored.")
    score: float = Field(description="Cosine similarity to the query (0.0 to 1.0).")


class StoreResult(BaseModel):
    """The result of storing a new memory."""

    id: int = Field(description="The id of the newly-stored memory.")
    created_at: datetime = Field(description="When the memory was stored.")


class DiaryResult(BaseModel):
    """The result of appending a diary entry."""

    id: int = Field(description="The id of the newly-stored diary entry.")
    created_at: datetime = Field(description="When the entry was stored.")
