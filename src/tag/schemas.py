from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class Tag(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]
    entities: list["AttachedEntity"]


class AttachedTag(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]


from src.entity.schemas import AttachedEntity

Tag.model_rebuild()
