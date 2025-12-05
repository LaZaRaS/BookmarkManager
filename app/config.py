from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int = 3306
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    APP_PORT: int = 8080
    BASE_URL: str = "http://localhost:8000"

    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding="utf-8",
    )

settings = Settings()