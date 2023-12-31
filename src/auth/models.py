from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, ForeignKey, text, Boolean, sql
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base, uuid_pk, UUID_ID


class UsersOrm(SQLAlchemyBaseUserTable[UUID_ID], Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    email: Mapped[str]
    username: Mapped[str] = mapped_column(String(16))
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)

    # При создании таблицы ролей в нее по умолчанию добавляются 2 роли: admin с индексом 1 и member с индексом 2
    # Каждому новому юзеру присваевается роль member
    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id"), server_default=text("2"), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, server_default=sql.true(), nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, server_default=sql.false(), nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, server_default=sql.false(), nullable=False
    )

    role: Mapped["RolesOrm"] = relationship(back_populates="users")


class RolesOrm(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(16))

    users: Mapped[list["UsersOrm"]] = relationship(back_populates="role")
