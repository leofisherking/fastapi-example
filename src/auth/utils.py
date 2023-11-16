from fastapi import Depends, Request
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import UsersOrm
from src.database import get_async_session
from fastapi_users import BaseUserManager, UUIDIDMixin
from typing import Optional
import uuid
from src.global_config import config


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, UsersOrm)


class UserManager(UUIDIDMixin, BaseUserManager[UsersOrm, uuid.UUID]):
    reset_password_token_secret = config.jwt_secret.get_secret_value()
    verification_token_secret = config.jwt_secret.get_secret_value()


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)