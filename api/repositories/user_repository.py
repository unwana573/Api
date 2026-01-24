from sqlalchemy.orm import Session
from api.models.models import User
from api.schemas.user import UserCreate
from api.core.security import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        user_name=user.user_name,
        phone_number=user.phone_number,
        hashed_password=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, data):
    user = get_user_by_id(db, user_id)
    if data.full_name:
        user.full_name = data.full_name
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db:Session):
    return db.query(User).all()