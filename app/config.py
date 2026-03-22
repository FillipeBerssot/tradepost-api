from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # APP
    app_name: str = "TradePost API"
    app_version: str = "0.1.0"
    debug: bool = True

    # Banco de Dados
    database_url: str = (
        "postgresql+asyncpg://tradepost:tradepost123@localhost:5432/tradepost"
    )

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # JWT
    secret_key: str = "sua-chave-secreta"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # Celery
    celery_broker_url: str = "redis://localhost:6379/1"

    model_config = {"env_file": ".env"}


settings = Settings()
