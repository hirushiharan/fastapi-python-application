from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RequestBase(BaseModel):
    is_new_req: Optional[bool] = None
    req_type: Optional[str] = None
    rt_code: Optional[str] = None
    market: Optional[str] = None
    channel: Optional[str] = None
    outlet_name: Optional[str] = None
    drive_brand: Optional[str] = None
    is_chain_outlet: Optional[bool] = None
    chain_name: Optional[str] = None
    is_urgent: Optional[bool] = None
    address_id: Optional[int] = None
    status: Optional[int] = None
    stage: Optional[int] = None
    is_active: Optional[bool] = None
    created_by: Optional[str] = None
    created_on: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_on: Optional[datetime] = None

class RequestCreate(RequestBase):
    # Fields required to create a new request
    pass

class RequestRead(RequestBase):
    # Fields required to read an existing request
    pass

class RequestUpdate(RequestBase):
    # Fields required to update an existing request
    pass

class RequestInDB(RequestBase):
    req_id: int
    # Fields from RequestBase plus unique fields (e.g., ID)

    class Config:
        from_attributes = True
