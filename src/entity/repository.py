import uuid
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.database import async_session_maker
from src.entity.models import EntitiesOrm
from src.tag.models import TagsOrm
from src.abstract_repo import AbstractRepo


class EntityRepo(AbstractRepo):
    model = EntitiesOrm

    async def create(self, data: dict):
        new_entity_tags = data.pop("tags")
        new_entity = self.model(**data)
        for tag in new_entity_tags:
            new_entity.tags.append(TagsOrm(**tag))

        async with async_session_maker() as session:
            session.add(new_entity)
            await session.commit()

            stmt = (
                select(EntitiesOrm)
                .options(selectinload(EntitiesOrm.tags))
                .where(EntitiesOrm.id == new_entity.id)
            )
            created_entity = await session.scalar(stmt)

        return created_entity

    async def get_all(self):
        pass

    async def get_by_id(self, entity_id: uuid.UUID):
        pass
