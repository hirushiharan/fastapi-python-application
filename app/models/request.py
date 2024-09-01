from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.base import Base

class Request(Base):
    __tablename__ = 'request'
    
    req_id = Column(Integer, primary_key=True, index=True)
    is_new_req = Column(Boolean, default=True)
    req_type = Column(String, nullable=True)
    rt_code = Column(String, nullable=True)
    market = Column(String, nullable=True)
    channel = Column(String, nullable=True)
    outlet_name = Column(String, nullable=True)
    drive_brand = Column(String, nullable=True)
    is_chain_outlet = Column(Boolean, default=False)
    chain_name = Column(String, nullable=True)
    is_urgent = Column(Boolean, default=False)
    status = Column(Integer, ForeignKey('lookup.lookup_id'))
    stage = Column(Integer, ForeignKey('lookup.lookup_id'))
    is_active = Column(Boolean, default=True)
    created_by = Column(String)
    created_on = Column(DateTime)
    updated_by = Column(String)
    updated_on = Column(DateTime)
    
    status_lookup = relationship('Lookup', foreign_keys=[status])
    stage_lookup = relationship('Lookup', foreign_keys=[stage])
