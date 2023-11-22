from fastapi import APIRouter, Depends
import uuid
from src.entity.schemas import Entity
from src.entity.dependencies import service_dependency
from src.global_dependencies import authorized_user
from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/entities",
    tags=["Entities"],
    dependencies=[Depends(authorized_user)],
)


@router.get("/")
@cache(expire=60)
async def get_entities(
    service: service_dependency,
) -> list[Entity]:
    entities = await service.get_entities()
    return entities


@router.get("/{id}/")
async def get_entity_by_id(
    entity_id: uuid.UUID,
    service: service_dependency,
) -> Entity:
    entity = await service.get_by_id(entity_id)
    return entity


@router.post("/")
async def create_entity(
    entity: Entity,
    service: service_dependency,
) -> Entity:
    created_entity = await service.create_entity(entity)
    return created_entity
