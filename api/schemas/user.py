from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Enum

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str]
    role: str

    class Config:
        from_attributes = True 