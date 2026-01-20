from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.core.database import get_db
from api.schemas.user import UserCreate
from api.schemas.auth import UserLogin
from api.repositories.user_repository import create_user, get_user_by_email
from api.auth.jwt import create_access_token, create_refresh_token
from api.core.security import hash_password, verify_password  

router = APIRouter()

@router.post("/signup", status_code=201)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = create_user(db, user, hash_password)
    return {"message": "User created", "user_id": db_user.id}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": db_user.email})
    refresh_token = create_refresh_token({"sub": db_user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
