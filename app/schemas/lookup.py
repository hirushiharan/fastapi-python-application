from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class LookupBase(BaseModel):
    category: Optional[str] = None
    display_value: Optional[str] = None
    sort: Optional[int] = None
    is_active: Optional[bool] = None
    created_by: Optional[str] = None
    created_on: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_on: Optional[datetime] = None

class LookupCreate(LookupBase):
    # Fields required to create a new lookup
    pass

class LookupRead(LookupBase):
    # Fields required to read an existing lookup
    pass

class LookupUpdate(LookupBase):
    # Fields required to update an existing lookup
    pass

class LookupInDB(LookupBase):
    lookup_id: int
    # Fields from LookupBase plus unique fields (e.g., ID)

    class Config:
        from_attributes = True
