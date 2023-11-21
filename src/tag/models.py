from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base, uuid_pk
from src.relationship_models import EntitiesTagsOrm

if TYPE_CHECKING:
    from src.entity.models import EntitiesOrm


class TagsOrm(Base):
    __tablename__ = "tags"

    id: Mapped[uuid_pk]

    name: Mapped[str] = mapped_column(String(16))

    entities: Mapped[list["EntitiesOrm"]] = relationship(
        back_populates="tags",
        secondary="entitiestags",
    )
