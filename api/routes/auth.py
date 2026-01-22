from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.core.database import get_db
from api.schemas.user import UserCreate
from api.repositories.user_repository import create_user, get_user_by_email
from api.core.security import verify_password
from api.auth.jwt import create_access_token, create_refresh_token

router = APIRouter(tags=["Auth"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    db_user = create_user(db, user)
    return {"message": "User created", "user_id": db_user.id}


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    db_user = get_user_by_email(db, form_data.username)

    if not db_user or not verify_password(
        form_data.password, db_user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token({"sub": str(db_user.id)})
    refresh_token = create_refresh_token({"sub": str(db_user.id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
