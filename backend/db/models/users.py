from sqlalchemy import Boolean, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from db.base_class import Base

class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())
    is_active = Column(Boolean, default=True)
    is_active = Column(Boolean, default=False)
    jobs=relationship('Jobs',back_populates='owner')
