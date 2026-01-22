from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.core.database import get_db
from api.repositories.user_repository import get_all_users
from api.schemas.user import UserOut
from api.auth.dependencies import get_current_user, require_admin

router = APIRouter(tags=["Users"])

@router.get("/", response_model=List[UserOut])
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),  
):
    return get_all_users(db)
