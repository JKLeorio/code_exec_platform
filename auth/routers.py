from fastapi_users import FastAPIUsers

from auth.depends import get_user_manager
from auth.backend import auth_backend
from models.user import User
from schemas.user import UserBase, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

register_router = fastapi_users.get_register_router(
    UserBase, UserCreate
)
login_router = fastapi_users.get_auth_router(
    auth_backend
)
password_reset_router = fastapi_users.get_reset_password_router()