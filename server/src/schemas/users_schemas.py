from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    clerk_id: str
    img_url: str
    password: str
    role: Optional[str] = None

    def __getitem__(self, key):
        return self.__dict__[key]


class UserOut(BaseModel):
    id: int
    email: EmailStr
    clerk_id: str
    img_url: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str
    email: str
