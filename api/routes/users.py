from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.core.database import get_db
from api.repositories.auth import get_all_users
from api.schemas.auth import UserOut
from api.auth.dependencies import require_admin

router = APIRouter(tags=["Users"])

@router.get("/", response_model=List[UserOut])
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),  
):
    return get_all_users(db)

@router.post("/")
def user_profile():
    return

# @router.put("/")
# def user_profile():
#     return

@router.post("/")
def user_address():
    return

@router.put("/")
def user_address():
    return

@router.delete("/")
def user_address():
    return