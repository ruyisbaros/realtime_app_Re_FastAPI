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
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
