from src.entity.repository import EntityRepo
from src.entity.service import EntityService


def entity_service():
    return EntityService(EntityRepo)
