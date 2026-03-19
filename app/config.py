from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    debug: bool = False
    admin_email: str

    class Config:
        env_file = ".env"

settings = Settings()