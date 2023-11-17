from typing import Annotated
from fastapi import APIRouter, Depends
import uuid

from sqlalchemy import insert

from src.entity.schemas import Entity
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.entity.models import EntitiesOrm

entity_router = APIRouter(prefix="/entities", tags=["entities"])


@entity_router.get("/")
async def get_entity_list():
    return "entities"


@entity_router.get("/{id}/")
async def get_entity(e_id: uuid.UUID):
    return {"id": e_id}


@entity_router.post("/")
async def create_entity(
    entity: Entity, session: Annotated[AsyncSession, Depends(get_async_session)]
):
    e_dict = entity.model_dump()
    stmt = insert(EntitiesOrm).values(**e_dict).returning(EntitiesOrm.id)
    res = await session.execute(stmt)
    await session.commit()

    return {"e_id": res.scalar_one()}
