from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.users.schemas import UserCreate, UserResponse
from app.users.service import register_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(db=db, user_data=user_data)
