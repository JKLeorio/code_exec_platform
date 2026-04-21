from typing import List, Text

from sqlalchemy import Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.types import SubmitStatus
from models.base import Base
from models.execute_request import ExecuteRequest


class Problem(Base):
    __tablename__ = "problems"
    description: Mapped[str] = mapped_column(
        Text
    )
    expected_answer: Mapped[str] = mapped_column(
        String
    )
    results: Mapped[List["Submit"]] = relationship(
        back_populates="submits"
    )


class Submit(Base):
    __tablename__ = "submits"
    status: Mapped[SubmitStatus] = mapped_column(
        Enum(SubmitStatus)
    )
    execute_request_id: Mapped[int] = mapped_column(
        ForeignKey(
            "execute_results.id",
            ondelete="CASCADE"
        )
    )
    execute_request: Mapped[ExecuteRequest] = relationship(
        ExecuteRequest
    )
    problem: Mapped[Problem] = relationship(
        Problem
    )
    problem_id: Mapped[int] = mapped_column(
        ForeignKey(
            "problems.id", ondelete="CASCADE"
        )
    )
    status: SubmitStatus = mapped_column(
        Enum(SubmitStatus)
    )