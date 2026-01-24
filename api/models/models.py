from sqlalchemy import Column, Integer, String
from api.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True) 
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")