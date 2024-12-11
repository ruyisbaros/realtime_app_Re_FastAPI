from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

from .album_schemas import Albums


class SongBase(BaseModel):
    title: str
    artist: str
    img_url: str
    audio_url: str
    duration: float


class SongCreate(SongBase):
    album_id: Optional[int]


class SongOut(SongBase):
    id: int
    title: str
    artist: str
    img_url: str
    audio_url: str
    album_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True
