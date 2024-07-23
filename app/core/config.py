from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Resume Matcher AI"
    DATABASE_URL: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
