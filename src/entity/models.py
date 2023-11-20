from src.database import Base, uuid_pk
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.tag.models import TagsOrm


class EntitiesOrm(Base):
    __tablename__ = "entities"

    id: Mapped[uuid_pk]

    name: Mapped[str] = mapped_column(String(16))
    description: Mapped[str] = mapped_column(String(1024))
    price: Mapped[float] = mapped_column(Numeric(precision=9, scale=2), nullable=False)

    tags: Mapped[list["TagsOrm"]] = relationship(
        back_populates="entities",
        secondary="entitiestags",
    )
