from abc import ABC, abstractmethod
from typing import List, Optional, Type

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.task.task import Task
from infrastructure.database.Task.task_dto import TaskDTO
from infrastructure.database.database import session


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def update(self, task: Task) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, task_id: int):
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        raise NotImplementedError


class TaskRepositoryImpl(TaskRepository):
    session: Session = session

    def find_by_id(self, task_id: int) -> Optional[Task]:
        try:
            task_dto: TaskDTO = self.session.query(TaskDTO()).filter_by(id=task_id).first()
        except NoResultFound:
            return None

        return task_dto.to_entity()

    def find_all(self) -> List[]:
