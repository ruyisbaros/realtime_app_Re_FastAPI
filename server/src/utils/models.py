from .database import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, Float, Boolean, DateTime, Enum
from sqlalchemy.sql.sqltypes import TIMESTAMP, DATETIME
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
import enum


class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    MODERATOR = "MODERATOR"
    GUEST = "GUEST"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    clerk_id = Column(String, index=True, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    sender_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    recipient_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    subject = Column(String, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    sender = relationship("User", foreign_keys=[sender_id])


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    release_year = Column(DateTime, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    songs = relationship("Song", backref="album")


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    audio_url = Column(String, nullable=False)
    duration = Column(Float, nullable=False)
    album_id = Column(Integer, ForeignKey(
        "albums.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))

    album = relationship("Album", backref="songs")
