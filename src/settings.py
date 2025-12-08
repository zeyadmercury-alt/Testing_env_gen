from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    comfy_host: str = "http://127.0.0.1:8188"
    class Config:
        env_file = ".env"

settings = Settings()