from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.lookup import Lookup
from sqlalchemy.ext.declarative import declarative_base
from app.db.base import Base

class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey('lookup.lookup_id'))
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    user_image = Column(String, nullable=True)
    hashed_password = Column(String)
    is_temp_password = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(String)
    created_on = Column(DateTime)
    updated_by = Column(String)
    updated_on = Column(DateTime)
    
    role = relationship('Lookup', foreign_keys=[role_id])
