from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, SecretStr


class Settings(BaseSettings):
    pg_host: str
    pg_port: str
    pg_name: str
    pg_user: str
    pg_pass: SecretStr

    jwt_secret: SecretStr

    @property
    def pg_dsn(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.pg_user}:{self.pg_pass.get_secret_value()}@{self.pg_host}:{self.pg_port}/{self.pg_name}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Settings()
