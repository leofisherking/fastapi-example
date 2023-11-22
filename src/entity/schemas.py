from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, PositiveFloat


class EntityBase(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]
    description: Annotated[str, MaxLen(1024)] | None
    price: PositiveFloat


class Entity(EntityBase):
    tags: list["TagAttachment"]


class EntityAttachment(EntityBase):
    pass


from src.tag.schemas import TagAttachment

Entity.model_rebuild()
