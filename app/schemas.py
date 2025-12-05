from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    model_config = {"from_attributes": True}


class BookmarkBase(BaseModel):
    url: HttpUrl
    title: str
    description: Optional[str] = None

class BookmarkCreate(BookmarkBase):
    tags: List[str] = []

class BookmarkUpdate(BaseModel):
    url: Optional[HttpUrl] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_archived: Optional[bool] = None
    tags: Optional[List[str]] = None

class Bookmark(BookmarkBase):
    id: int
    is_archived: bool
    tags: List[Tag] = []

    model_config = {"from_attributes": True}
