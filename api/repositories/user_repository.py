from sqlalchemy.orm import Session
from api.models.models import User  # your SQLAlchemy User model

def create_user(db: Session, user, hash_func):
    """
    Create a new user in the database.
    hash_func: function to hash the password (e.g., hash_password from security.py)
    """
    hashed = hash_func(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed,
        full_name=user.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
