from typing import Optional
from pydantic import BaseModel, EmailStr

class UserProfile :
    name: str

class Update_profile(UserProfile):
    pass

class AddUserAddress:
    pass

class UpdateAddress:
    pass

class DeleteAddress:
    pass