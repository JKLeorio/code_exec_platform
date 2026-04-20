from sqlalchemy import Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from db.types import ExecuteResultStatus


class ExecuteResult(Base):
    __tablename__ = "execute_results"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    execute_request_id: Mapped[int] = mapped_column(
        ForeignKey(
            "execute_requests.id",
            ondelete="CASCADE"
        ),
    )
    execute_request = relationship(
        foreign_keys=[execute_request_id],
        back_populates="execute_results"
    )
    result_type: Mapped[ExecuteResultStatus] = mapped_column(
        Enum(ExecuteResultStatus),
    )
    output: Mapped[str] = mapped_column(
        Text
    )