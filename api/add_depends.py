from fastapi import Depends
from sqlalchemy.orm import Session
from api.core.database import get_db

def db_dependency() -> Session:
    return Depends(get_db)
