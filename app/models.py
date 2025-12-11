from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, UTC
from .database import Base

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    url = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))