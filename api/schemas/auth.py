from pydantic import BaseModel, EmailStr
from typing import Optional

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenRefresh(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: str
    user_name: str
    full_name: str
    phone_number: str
    password: str
    role: str = "user"

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