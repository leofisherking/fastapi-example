from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from src.auth.auth import auth_backend
from src.auth.models import UsersOrm, RolesOrm
from src.auth.schemas import UserRead, UserCreate, RoleRead
from src.entity.router import router as entity_router
from src.global_dependencies import fastapi_users
from src.tag.router import router as tag_router
from src.database import get_async_session


app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(entity_router)
app.include_router(tag_router)
