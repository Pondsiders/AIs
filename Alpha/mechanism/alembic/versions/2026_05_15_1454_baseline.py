"""baseline.

This revision exists to anchor the migration chain. It does not build the
schema; the schema lives in ``alembic/baseline-schema.sql``, captured by
pg_dump from production on 2026-05-15. ``just db-init`` restores from a
dump and ``alembic stamp head``s the database; this ``upgrade()`` is
never run in our workflow.

A real "build from scratch" recipe is a future project; the schema is
still moving and any from-zero DDL written today would age out fast.

Revision ID: 0001
Revises:
Create Date: 2026-05-15 14:54:50.998139
"""

from __future__ import annotations

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    """No-op. See the module docstring."""


def downgrade() -> None:
    """Forward-only migrations."""
    raise NotImplementedError("Forward-only migrations.")
