from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.config import settings
from app.users.router import router as users_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API de Marketplace Inteligente com FastAPI, PostgreSQL, Redis e IA",
)

app.include_router(users_router)
app.include_router(auth_router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
    }
