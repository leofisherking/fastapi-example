import uuid
from fastapi_users import schemas
from typing import Annotated
from annotated_types import MinLen, MaxLen


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: Annotated[str, MinLen(3), MaxLen(16)]


class UserCreate(schemas.BaseUserCreate):
    username: Annotated[str, MinLen(3), MaxLen(16)]
