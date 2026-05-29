from typing import Literal

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DatabaseProvider = Literal["mongodb", "mysql"]


class Settings(BaseSettings):
    DATABASE_PROVIDER: DatabaseProvider = "mongodb"

    MONGODB_URI: str | None = None
    MONGODB_DATABASE: str | None = None

    MYSQL_HOST: str = "127.0.0.1"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = ""
    MYSQL_DATABASE: str = "naboo_project"

    model_config = SettingsConfigDict(env_file=".env")

    @model_validator(mode="after")
    def validate_database_settings(self) -> "Settings":
        if self.DATABASE_PROVIDER == "mongodb":
            if not self.MONGODB_URI or not self.MONGODB_DATABASE:
                raise ValueError(
                    "MONGODB_URI and MONGODB_DATABASE are required when "
                    "DATABASE_PROVIDER is mongodb"
                )
        return self


settings = Settings()
