from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from domain.task.task import Task
from infrastructure.database.database import Base
from usecase.task.task_model import TaskReadModel


class TaskDTO(Base):
    __tablename__ = 'task'
    id: Mapped[str] = mapped_column(String, primary_key=True, autoincrement=False)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    create_date: Mapped[datetime] = mapped_column(DateTime)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_read_model(self) -> TaskReadModel:
        return TaskReadModel(
            id=self.id,
            title=self.title,
            description=self.description,
            create_date=self.create_date,
            is_done=self.is_done
        )

    @staticmethod
    def from_entity(task: Task) -> "TaskDTO":
        now = datetime.now()
        return TaskDTO(
            id=task.id,
            title=task.title,
            description=task.description,
            create_date=now,
            is_done=task.is_done
        )
