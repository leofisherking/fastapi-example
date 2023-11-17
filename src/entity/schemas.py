from pydantic import BaseModel, constr, PositiveFloat


class Tag(BaseModel):
    name: constr(max_length=16, min_length=3)


class Entity(BaseModel):
    name: constr(max_length=16, min_length=3)
    description: constr(max_length=1024) | None
    price: PositiveFloat

    #tags: list[Tag] | None
