from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..utils import models
from ..utils.database import get_db
from ..schemas.users_schemas import UserCreate, UserOut, Token, UserLogin
from ..utils.pswds import hash_paswords, verify_password
from ..utils.oauth import create_access_token, get_current_user

router = APIRouter(prefix="/songs", tags=["Songs"])  # Tags for swagger
