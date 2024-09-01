from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    user_image: Optional[str] = None
    is_temp_password: Optional[bool] = None
    is_active: Optional[bool] = None
    created_by: Optional[str] = None
    created_on: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_on: Optional[datetime] = None

class UserCreate(UserBase):
    password: str  # Required field for user creation

class UserRead(UserBase):
    # Fields required to update an existing user
    pass

class UserUpdate(UserBase):
    # Fields required to update an existing user
    pass

class UserInDB(UserBase):
    user_id: int
    hashed_password: str  # Store hashed password for validation

    class Config:
        from_attributes = True
