import uuid
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.database import async_session_maker
from src.tag.models import TagsOrm
from src.abstarct_repo import AbstractRepo


class TagRepo(AbstractRepo):
    async def create(self, data: dict) -> TagsOrm | None:
        new_tag = TagsOrm(**data)

        async with async_session_maker() as session:
            session.add(new_tag)
            await session.commit()

            stmt = select(TagsOrm).where(TagsOrm.id == new_tag.id)
            created_tag = await session.scalar(stmt)

        return created_tag

    async def get_all(self) -> list[TagsOrm]:
        stmt = (
            select(TagsOrm)
            .options(selectinload(TagsOrm.entities))
            .order_by(TagsOrm.created_at.desc())
        )

        async with async_session_maker() as session:
            res = await session.execute(stmt)
            tags = res.scalars().all()

        return tags

    async def get_by_id(self, tag_id: uuid.UUID) -> TagsOrm | None:
        stmt = (
            select(TagsOrm)
            .options(selectinload(TagsOrm.entities))
            .where(TagsOrm.id == tag_id)
        )

        async with async_session_maker() as session:
            tag = await session.scalar(stmt)

        return tag
