import uuid
from fastapi_users import schemas
from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class Role(BaseModel):
    id: int
    name: str


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: Annotated[str, MinLen(3), MaxLen(16)]
    # role: Role


class RoleRead(Role):
    users: list[UserRead]


class UserCreate(schemas.BaseUserCreate):
    username: Annotated[str, MinLen(3), MaxLen(16)]
