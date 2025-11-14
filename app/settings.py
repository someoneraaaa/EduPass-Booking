from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017"
    MONGO_DB: str = "edupass_booking"

settings = Settings()