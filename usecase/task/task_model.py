from datetime import datetime

from pydantic import BaseModel, Field, validator

from domain.task.task import Task


class TaskCreateModel(BaseModel):
    title: str = Field(example="Title example")
    description: str = Field(example="Description example")


class TaskUpdateModel(BaseModel):
    title: str = Field(example="Title example")
    description: str = Field(example="Description example")
    is_done: bool = Field(example=False)


class TaskReadModel(BaseModel):
    id: int = Field()
    title: str = Field()
    description: str = Field()
    create_date: datetime = Field()
    is_done: bool = Field()

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(task: Task) -> "TaskReadModel":
        return TaskReadModel(
            id=task.id,
            title=task.title,
            description=task.description,
            create_date=task.create_date,
            is_done=task.is_done
        )