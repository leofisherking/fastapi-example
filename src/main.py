from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.auth.auth import auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.entity.router import router as entity_router
from src.global_dependencies import fastapi_users
from src.tag.router import router as tag_router
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from src.global_config import config


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        f"redis://{config.redis_host}:{config.redis_port}",
        encoding="utf8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(entity_router)
app.include_router(tag_router)
