from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from models.base import Base



class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True
    )
