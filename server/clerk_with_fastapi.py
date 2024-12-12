from fastapi import FastAPI, Depends  # <- (1)
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer  # <- (2)
from typing import Annotated  # <- (3)
import requests  # <- (1)
from fastapi import FastAPI, Depends, Response, status  # <- (2)
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated
app = FastAPI()
security = HTTPBearer()  # <- (4)


@app.get("/")
async def root(
    credentials: Annotated[HTTPAuthorizationCredentials,
                           Depends(security)]  # <- (5)
):
    print(f"Got token: {credentials.credentials[:10]}...")  # <- (6)
    return {"message": "Hello World"}


CLERK_PEM_PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
<YOUR JWT PUBLIC KEY>
-----END PUBLIC KEY-----
"""  # <- (3)

app = FastAPI()
security = HTTPBearer()


@app.get("/")
async def root(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    response: Response  # <- (4)
):
    print(f"Got token: {credentials.credentials[:10]}...")

    # (5) add all this section below
    try:
        jwt.decode(token, key=CLERK_PEM_PUBLIC_KEY, algorithms=['RS256'])
        return {"message": "Hello World"}
    except jwt.exceptions.PyJWTError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Invalid token"}
