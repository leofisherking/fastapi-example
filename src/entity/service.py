import uuid

from src.entity.models import EntitiesOrm
from src.entity.repository import AbstractRepo
from src.entity.schemas import Entity
from fastapi import HTTPException


class EntityService:
    def __init__(self, entity_repo: AbstractRepo):
        self.entity_repo = entity_repo()

    async def create_entity(self, entity: Entity) -> EntitiesOrm:
        created_entity = await self.entity_repo.create(entity.model_dump())
        return created_entity

    async def get_entities(self) -> list[EntitiesOrm]:
        entities = await self.entity_repo.get_all()
        return entities

    async def get_by_id(self, entity_id: uuid.UUID) -> EntitiesOrm:
        entitiy = await self.entity_repo.get_by_id(entity_id)
        if not entitiy:
            raise HTTPException(status_code=404, detail="entity not found")
        return entitiy
