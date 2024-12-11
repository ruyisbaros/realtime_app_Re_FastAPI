from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

from .song_schemas import SongOut


class AlbumBase(BaseModel):
    title: str
    artist: str
    img_url: str
    release_year: datetime


class AlbumCreate(AlbumBase):
    pass


class AlbumOut(AlbumBase):
    id: int
    title: str
    artist: str
    img_url: str
    songs: List[SongOut]
    created_at: datetime

    class Config:
        orm_mode = True
