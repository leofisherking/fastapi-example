from typing import Annotated
from fastapi import APIRouter, Depends
import uuid
from src.entity.schemas import Entity
from src.entity.service import EntityService
from src.entity.dependencies import entity_service


router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


@router.get("/")
async def get_entities():
    return "get_all"


@router.get("/{id}/")
async def get_entity_by_id(e_id: uuid.UUID):
    return "get_by_id"


@router.post("/")
async def create_entity(
    entity: Entity,
    service: Annotated[EntityService, Depends(entity_service)],
) -> Entity:
    created_entity = await service.create_entity(entity)
    return created_entity
