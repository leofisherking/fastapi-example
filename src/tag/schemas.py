from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class Tag(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(16)]
