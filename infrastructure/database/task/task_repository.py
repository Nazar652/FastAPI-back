from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from domain.task.task import Task
from infrastructure.database.task.task_dto import TaskDTO
from infrastructure.database.database import session
from usecase.task.task_model import TaskReadModel


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, task_id: str) -> Optional[TaskReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update(self, task: Task):
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, task_id: str):
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[TaskReadModel]:
        raise NotImplementedError


class TaskRepositoryImpl(TaskRepository):
    def __init__(self, session_rep: Session = session):
        self.session = session_rep

    def find_by_id(self, task_id: str) -> Optional[TaskReadModel]:
        try:
            task_dto = self.session.query(TaskDTO).filter_by(id=task_id).first()
        except NoResultFound:
            return None

        return task_dto.to_read_model()

    def find_all(self) -> List[TaskReadModel]:
        task_dtos = self.session.query(TaskDTO).all()

        if len(task_dtos) == 0:
            return []

        return list(map(lambda task_dto: task_dto.to_read_model(), task_dtos))

    def create(self, task: Task):
        task_dto = TaskDTO.from_entity(task)
        self.session.add(task_dto)
        session.commit()

    def update(self, task: Task):
        task_dto = TaskDTO.from_entity(task)
        _task = self.session.query(TaskDTO).filter_by(id=task_dto.id).first()
        _task.title = task_dto.title
        _task.description = task_dto.description
        _task.is_done = task_dto.is_done
        session.commit()

    def delete_by_id(self, task_id: int):
        self.session.query(TaskDTO).filter_by(id=task_id).delete()
        session.commit()
