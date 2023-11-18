import datetime
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy import UUID, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Annotated, AsyncGenerator
import uuid
from src.global_config import config


engine = create_async_engine(config.pg_dsn)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# Custom column types

UUID_ID = uuid.UUID
uuid_pk = Annotated[
    UUID_ID,
    mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()")),
]

created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]


class Base(DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


# Триггер updated_at на стороне бд. Импрортируется в алембик ревизию
create_refresh_updated_at_func = """
    CREATE FUNCTION public.refresh_updated_at()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $func$
    BEGIN
       NEW.updated_at := TIMEZONE('utc', now());
       RETURN NEW;
    END
    $func$;
"""

create_trigger = """
    CREATE TRIGGER trig_{table}_updated BEFORE UPDATE ON public.{table}
    FOR EACH ROW EXECUTE PROCEDURE public.refresh_updated_at();
"""

create_default_roles = """
    INSERT INTO public.roles (name) VALUES ('admin'), ('member');
"""
