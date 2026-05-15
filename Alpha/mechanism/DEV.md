# Development

## Dev database lifecycle

The dev database runs in Docker locally and is managed via the justfile.

```sh
just db-up      # start it
just db-down    # stop it (preserves data)
just db-init <dump>   # wipe, fresh-start, restore, stamp Alembic
```

`db-init` refuses to run while the container is up — `just db-down` first.

## Preparing a dump

`db-init` restores from a full `pg_dump`-format file (schema + data) of the
production database. Take a fresh dump from a production replica using the
read-only `alpha_reader` role. The pg_dump binary must match the server
major version, so run it inside the `pgvector/pgvector:pg17` image:

```sh
docker run --rm --network host \
    pgvector/pgvector:pg17 \
    pg_dump \
        --no-owner \
        --no-acl \
        --format=custom \
        "postgresql://alpha_reader:PASSWORD@alpha-db-replica-3.tail8bd569.ts.net:5432/alpha" \
    > $HOME/alpha.dump
```

Then:

```sh
just db-init ~/alpha.dump
```

The dump lives in your home directory and stays on the VM.

## Alembic

The dev database is brought under Alembic management by `db-init`'s final
two steps: after the restore lands, `db-init` drops the legacy
`public.alembic_version` table that comes along with the dump, then runs
`alembic stamp head` to mark the database as at the latest revision. From
that point on, `uv run alembic upgrade head` applies any new migrations.

The baseline migration (`alembic/versions/...`) describes the schema as it
exists in production at the moment we adopted Alembic. It is a faithful
mirror, not a clean-up. Future migrations clean things up incrementally.
