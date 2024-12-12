from fastapi import FastAPI, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated
from dotenv import load_dotenv
import os
from fastapi import Depends, Response, status, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated
import jwt
from jwt.exceptions import InvalidTokenError

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

security = HTTPBearer()

CLERK_PEM_PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
<YOUR JWT PUBLIC KEY>
-----END PUBLIC KEY-----
"""
router = APIRouter(prefix="/clerk", tags=["Clerk_Auth"])  # Tags for swagger


@router.get("/clerk")
async def root(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    response: Response
):
    print(f"Got token: {credentials.credentials[:10]}...")

    try:
        jwt.decode(
            credentials.credentials[:10], key=CLERK_PEM_PUBLIC_KEY, algorithms=['RS256'])
        return {"message": "Hello World"}
    except jwt.exceptions.PyJWTError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Invalid token"}
