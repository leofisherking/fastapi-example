from src.database import Base, uuid_pk, UUID_ID
from sqlalchemy import String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship


class EntitiesOrm(Base):
    __tablename__ = "entities"

    id: Mapped[uuid_pk]

    name: Mapped[str] = mapped_column(String(16))
    description: Mapped[str] = mapped_column(String(1024))
    price: Mapped[float] = mapped_column(Numeric(precision=9, scale=2), nullable=False)

    # tags: Mapped[list["TagsOrm"]] = relationship(back_populates='tags', secondary='entitiestags')


class TagsOrm(Base):
    __tablename__ = "tags"

    id: Mapped[uuid_pk]

    name: Mapped[str] = mapped_column(String(16))

    # entities: Mapped[list["EntitiesOrm"]] = relationship(back_populates='entities', secondary='entitiestags')


class EntitiesTagsOrm(Base):
    __tablename__ = "entitiestags"

    entity_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("entities.id", ondelete="CASCADE"),
        primary_key=True,
    )
    tag_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True
    )
