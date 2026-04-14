from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.service import get_password_hash
from app.users.repository import create_user, get_user_by_email
from app.users.schemas import UserCreate


async def register_user(db: AsyncSession, user_data: UserCreate):
    existing_user = await get_user_by_email(db, user_data.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado.",
        )

    hashed_password = get_password_hash(user_data.password)

    user = await create_user(db=db, email=user_data.email, senha_hash=hashed_password)

    return user
