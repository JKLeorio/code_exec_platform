from sqlalchemy import Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.types import SubmitStatus
from models.base import Base
from models.execute_request import ExecuteRequest


class Problem(Base):
    __tablename__ = "problems"

    pass


class Submit(Base):
    __tablename__ = "submits"
    status: Mapped[SubmitStatus] = mapped_column(
        Enum(SubmitStatus)
    )