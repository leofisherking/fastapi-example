import uuid

from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.models import UsersOrm
from src.auth.utils import get_user_manager


fastapi_users = FastAPIUsers[UsersOrm, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

authorized_user = fastapi_users.current_user()
