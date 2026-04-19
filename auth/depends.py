from fastapi import Depends

from auth.user_manager import UserManager
from models.user import User

from db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase

async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
):
    yield SQLAlchemyUserDatabase(
        session=session,
        user_table=User
    )

async def get_user_manager(
    user_db = Depends(get_user_db)
):
    yield UserManager(user_db=user_db)

