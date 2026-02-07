from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DATABASE: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
