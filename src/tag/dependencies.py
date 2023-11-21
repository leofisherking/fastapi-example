from typing import Annotated
from fastapi import Depends
from src.tag.repository import TagRepo
from src.tag.service import TagService


def tag_service():
    return TagService(TagRepo)


service_dependency = Annotated[TagService, Depends(tag_service)]
