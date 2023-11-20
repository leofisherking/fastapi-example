from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, uuid_pk, UUID_ID


class EntitiesTagsOrm(Base):
    __tablename__ = "entitiestags"

    id: Mapped[uuid_pk]

    entity_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("entities.id", ondelete="CASCADE"),
        nullable=False,
    )
    tag_id: Mapped[UUID_ID] = mapped_column(
        ForeignKey("tags.id", ondelete="CASCADE"),
        nullable=False,
    )

    UniqueConstraint("entity_id", "tag_id", name="idx_unq_entity_tag")
