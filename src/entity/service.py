from src.entity.repository import EntityRepo, AbstractRepo
from src.entity.schemas import Entity


class EntityService:
    def __init__(self, entity_repo: AbstractRepo):
        self.entity_repo = entity_repo()

    async def create_entity(self, entity: Entity):
        created_entity = await self.entity_repo.create(entity.model_dump())
        return created_entity
