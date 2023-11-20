from typing import Annotated
from fastapi import APIRouter, Depends
import uuid
from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload

from src.entity.repository import EntityRepo
from src.entity.schemas import Entity
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.entity.models import EntitiesOrm, TagsOrm
from src.entity.service import EntityService
from src.entity.dependencies import entity_service

entity_router = APIRouter(prefix="/entities", tags=["entities"])


@entity_router.get("/")
async def get_entity_list():
    return "entities"


@entity_router.get("/{id}/")
async def get_entity(e_id: uuid.UUID):
    return {"id": e_id}


@entity_router.post("/")
async def create_entity(
    entity: Entity,
    service: Annotated[EntityService, Depends(entity_service)],
) -> Entity:
    created_entity = await service.create_entity(entity)
    return created_entity
