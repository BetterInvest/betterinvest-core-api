"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration. All secrets come from the environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""
    mistral_api_key: str = ""
    marketstack_api_key: str = ""
    coingecko_api_key: str = ""


def get_settings() -> Settings:
    """Return a Settings instance (fresh read of the environment)."""
    return Settings()
