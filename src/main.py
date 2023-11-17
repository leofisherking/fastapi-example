from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from src.auth.auth import auth_backend
from src.auth.models import UsersOrm
from src.auth.schemas import UserRead, UserCreate
import uuid
from src.auth.utils import get_user_manager
from src.entity.router import entity_router


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
