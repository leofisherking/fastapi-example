import uuid
from abc import ABC, abstractmethod


class AbstractRepo(ABC):
    @abstractmethod
    async def create(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, entity_id: uuid.UUID):
        raise NotImplementedError
