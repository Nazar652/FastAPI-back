from pydantic import BaseModel, Field

from domain.task.task_exception import TaskNotFoundError


class ErrorMessageTaskNotFound(BaseModel):
    detail: str = Field(example=TaskNotFoundError.message)
