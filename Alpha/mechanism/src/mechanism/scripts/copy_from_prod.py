"""Copy whitelisted Cortex tables from the production read-replica to dev.

Reads from alpha-db-replica-3.tail8bd569.ts.net (Helsinki, structurally
read-only) via the alpha_reader role; writes to the local Docker Postgres
at localhost:5432. The replica is two-layer-isolated (read-only server +
SELECT-only role); local Postgres has no path to production.
"""

from __future__ import annotations


def main() -> None:
    """Copy whitelisted Cortex tables from the production replica to dev."""
    raise NotImplementedError("copy-from-prod not yet implemented")
