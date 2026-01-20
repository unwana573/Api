from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.database import get_db

router = APIRouter()

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return {"message": "List of users"}
