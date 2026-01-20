from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from api.core.config import Settings
from api.core.database import get_db
from api.schemas.user import UserCreate
from api.schemas.auth import UserLogin, TokenRefresh
from api.repositories.user_repository import (
    create_user,
    get_user_by_email,
    authenticate_user,
)
from api.auth.jwt import create_access_token, create_refresh_token


settings = Settings()
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    db_user = create_user(db, user)
    return {
        "message": "User created successfully",
        "user_id": db_user.id,
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token({"sub": db_user.email})
    refresh_token = create_refresh_token({"sub": db_user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

@router.post("/refresh")
def refresh_token(data: TokenRefresh):
    try:
        payload = jwt.decode(
            data.refresh_token,
            settings.REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        email = payload.get("sub")
        access_token = create_access_token({"sub": email})

        return {"access_token": access_token}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
