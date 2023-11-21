from typing import Annotated
from fastapi import Depends
from src.entity.repository import EntityRepo
from src.entity.service import EntityService


def entity_service():
    return EntityService(EntityRepo)


service_dependency = Annotated[EntityService, Depends(entity_service)]
