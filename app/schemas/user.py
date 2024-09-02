from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None

class UserCreate(UserBase):
    role_id: int

class UserUpdate(UserBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class PasswordReset(BaseModel):
    current_password: str
    new_password: str

class UserRead(UserBase):
    user_id: int
    created_on: datetime
    updated_on: datetime

    class Config:
        from_attributes = True
