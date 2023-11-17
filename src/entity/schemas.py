from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, PositiveFloat


class Tag(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]


class Entity(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]
    description: Annotated[str, MaxLen(1024)] | None
    price: PositiveFloat

    # tags: list[Tag] | None
