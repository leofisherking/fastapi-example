from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.auth.auth import auth_backend
from src.auth.models import UsersOrm, RolesOrm
from src.auth.schemas import UserRead, UserCreate, RoleRead
import uuid
from src.auth.utils import get_user_manager
from src.entity.router import router as entity_router
from src.tag.router import router as tag_router
from src.database import get_async_session

app = FastAPI()


fastapi_users = FastAPIUsers[UsersOrm, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

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


# один ко многим со стороны многих
@app.get("/users")
async def get_users(
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> list[UserRead]:
    stmt = select(UsersOrm).options(joinedload(UsersOrm.role))
    res = await session.execute(stmt)
    users = res.scalars().all()
    return users


# один ко монгим со стороны одного
@app.get("/roles")
async def get_roles(
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> list[RoleRead]:
    stmt = select(RolesOrm).options(selectinload(RolesOrm.users))
    res = await session.execute(stmt)
    roles = res.scalars().all()
    return roles

