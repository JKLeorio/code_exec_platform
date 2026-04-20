from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.user import User


class ExecuteRequest(Base):
    __tablename__ = "execute_requests"

    id: Mapped[int]
    owner_id: Mapped[int] = mapped_column(
        ForeignKey(
            ""
        )
    )
    description: Mapped[str] = mapped_column(
        Text
    )
    code: Mapped[Text] = mapped_column(
        Text
    )
    owner: Mapped[User] = relationship()