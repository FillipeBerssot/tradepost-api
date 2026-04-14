from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import TokenResponse
from app.auth.service import authenticate_user
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    access_token = await authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password,
    )
    return {"access_token": access_token, "token_type": "bearer"}
