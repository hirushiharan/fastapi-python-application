from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.lookup import Lookup
from app.db.base import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('lookup.lookup_id'))
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_image = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_temp_password = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_by = Column(String, nullable=True)
    created_on = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_by = Column(String, nullable=True)
    updated_on = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)   )
    
    role = relationship('Lookup', foreign_keys=[role_id])