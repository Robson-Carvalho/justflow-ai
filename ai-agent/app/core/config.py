from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    TAVILY_API_KEY: str
    HUB_URL: str = "http://realtime-hub:4000/api/alerts"
    
    AGENT_INTERVAL: int = 120
    MAX_RETRIES: int = 3
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()