"""Runtime configuration for alpha-mechanism."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import ClassVar

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


def _config_path() -> Path:
    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg) if xdg else Path.home() / ".config"
    return base / "alpha" / "env"


class Settings(BaseSettings):
    """Configuration loaded from the alpha env file at process startup."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=_config_path(),
        env_file_encoding="utf-8",
        extra="forbid",
    )

    database_url: PostgresDsn


@lru_cache
def get_settings() -> Settings:
    """Return the process-singleton Settings instance."""
    return Settings()  # pyright: ignore[reportCallIssue]
