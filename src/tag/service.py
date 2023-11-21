import uuid
from src.entity.repository import AbstractRepo
from fastapi import HTTPException
from src.tag.models import TagsOrm
from src.tag.schemas import Tag


class TagService:
    def __init__(self, tag_repo: AbstractRepo):
        self.tag_repo = tag_repo()

    async def create_tag(self, tag: Tag) -> TagsOrm:
        created_tag = await self.tag_repo.create(tag.model_dump())
        return created_tag

    async def get_tags(self) -> list[TagsOrm]:
        tags = await self.tag_repo.get_all()
        return tags

    async def get_by_id(self, tag_id: uuid.UUID) -> TagsOrm:
        tag = await self.tag_repo.get_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail="tag not found")
        return tag
