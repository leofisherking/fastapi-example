from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class TagBase(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]


class Tag(TagBase):
    entities: list["EntityAttachment"]


class TagAttachment(TagBase):
    pass


from src.entity.schemas import EntityAttachment

Tag.model_rebuild()
