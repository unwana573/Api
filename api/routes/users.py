from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.user import UserCreate, UserResponse
from api.repositories.user_repository import (
    create_user,
    get_all_users
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
    return get_all_users(db)
