"""Synchronous database helpers."""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING

import psycopg
from pgvector.psycopg import (  # pyright: ignore[reportMissingTypeStubs]
    register_vector,  # pyright: ignore[reportUnknownVariableType]
)

from mechanism.settings import get_settings

if TYPE_CHECKING:
    from collections.abc import Generator


@contextmanager
def open() -> Generator[psycopg.Connection, None, None]:
    """Open a connection to the database with pgvector registered."""
    conn = psycopg.connect(str(get_settings().database_url))
    try:
        _ = conn.execute("SET search_path TO public, extensions")
        register_vector(conn)
        yield conn
    finally:
        conn.close()
