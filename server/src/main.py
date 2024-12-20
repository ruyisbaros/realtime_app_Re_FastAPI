from fastapi import FastAPI
from .utils.oauth import verify_access_token

from .utils.database import get_db, engine
from fastapi.middleware.cors import CORSMiddleware
from .utils import models
from .routes import auth_routes, clerkauth_routes
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
get_db()  # run DB connection

models.Base.metadata.create_all(bind=engine)

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# SET ROUTES
app.include_router(auth_routes.router)
app.include_router(clerkauth_routes.router)
# app.include_router(song_routes.router)
# app.include_router(album_routes.router)
# app.include_router(stats_routes.router)
