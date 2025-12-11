from pydantic import BaseModel, HttpUrl
from datetime import datetime

class BookmarkCreate(BaseModel):
    title: str
    url: str

class BookmarkResponse(BaseModel):
    id: int
    title: str
    url: str
    created_at: datetime

    model_config = {"from_attributes": True}
