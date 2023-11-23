import uuid
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from src.global_dependencies import authorized_user
from src.tag.dependencies import service_dependency
from src.tag.schemas import Tag


router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


@router.get("/")
@cache(expire=60)
async def get_tags(
    service: service_dependency,
) -> list[Tag]:
    tags = await service.get_tags()
    return tags


@router.get("/{id}")
async def get_tag_by_id(
    tag_id: uuid.UUID,
    service: service_dependency,
) -> Tag:
    tag = await service.get_by_id(tag_id)
    return tag


@router.post(
    "/",
    dependencies=[Depends(authorized_user)],
)
async def create_tag(
    tag: Tag,
    service: service_dependency,
) -> Tag:
    created_tag = await service.create_tag(tag)
    return created_tag
