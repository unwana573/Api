from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.core.database import get_db
from api.schemas.user import UserCreate, UserResponse
from api.schemas.auth import Token
from api.repositories.user_repository import (
    create_user,
    get_user_by_email
)
from api.auth.jwt import create_access_token
from api.repositories.user_repository import create_user, get_user_by_email
from api.core.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", status_code=201)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = create_user(db, user, hash_password)
    return {"message": "User created", "user_id": db_user.id}

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_email(db, form_data.username)

    if not user or not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"sub": user.id})
    return {"access_token": token}
