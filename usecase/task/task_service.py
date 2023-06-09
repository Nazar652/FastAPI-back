from abc import ABC, abstractmethod
from typing import Optional, List

import shortuuid

from domain.task.task import Task
from domain.task.task_exception import TaskNotFoundError
from infrastructure.database.task.task_repository import TaskRepository
from usecase.task.task_model import TaskCreateModel, TaskReadModel, TaskUpdateModel


class TaskUseCase(ABC):
    task_repository: TaskRepository

    @abstractmethod
    def fetch_task_by_id(self, task_id: str) -> Optional[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_tasks(self) -> List[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def create_task(self, data: TaskCreateModel) -> Optional[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_task(self, task_id: str, data: TaskUpdateModel) -> Optional[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_task_by_id(self, task_id: str):
        raise NotImplementedError


class TaskUseCaseImpl(TaskUseCase):
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, data: TaskCreateModel) -> Optional[TaskReadModel]:
        uuid = shortuuid.uuid()
        task = Task(
            id=uuid,
            title=data.title,
            description=data.description
        )
        self.task_repository.create(task)

        return self.task_repository.find_by_id(uuid)

    def fetch_task_by_id(self, task_id: str) -> Optional[TaskReadModel]:
        task: TaskReadModel = self.task_repository.find_by_id(task_id)
        if not task:
            raise TaskNotFoundError

        return task

    def update_task(self, task_id: str, data: TaskUpdateModel) -> Optional[TaskReadModel]:
        existing_task = self.task_repository.find_by_id(task_id)
        if not existing_task:
            raise TaskNotFoundError

        task = Task(
            id=task_id,
            title=data.title,
            description=data.description,
            is_done=data.is_done
        )

        self.task_repository.update(task)

        updated_task = self.task_repository.find_by_id(task_id)

        return updated_task

    def delete_task_by_id(self, task_id: str):
        existing_task = self.task_repository.find_by_id(task_id)
        if not existing_task:
            raise TaskNotFoundError

        self.task_repository.delete_by_id(task_id)

    def fetch_tasks(self) -> List[TaskReadModel]:
        tasks = self.task_repository.find_all()
        return tasks
