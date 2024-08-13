from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from db.base_class import Base

class Jobs(Base):
    id= Column(Integer, primary_key=True, index=True)
    title=Column(String, nullable=False)
    company=Column(String, nullable=False)
    company_url=Column(String)
    location=Column(String, nullable=False)
    description=Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())
    is_active = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"), index=True)
    owner=relationship('User',back_populates='jobs')