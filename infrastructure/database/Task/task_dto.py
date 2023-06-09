from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from domain.task.task import Task
from infrastructure.database.database import Base
from usecase.task.task_model import TaskReadModel


class TaskDTO(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    create_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_entity(self) -> Task:
        return Task(
            id=self.id,
            title=self.title,
            description=self.description,
            create_date=self.create_date,
            is_done=self.is_done
        )

    def to_read_model(self) -> TaskReadModel:
        return TaskReadModel(
            id=self.id,
            title=self.title,
            description=self.description,
            create_date=self.create_date,
            is_done=self.is_done
        )
