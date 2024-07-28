from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Resume Matcher AI"
    DATABASE_URL: str
    OPENAI_API_KEY: str
    LOGGING_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
