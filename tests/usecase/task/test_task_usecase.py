from datetime import datetime
from unittest.mock import MagicMock, Mock

import pytest

from infrastructure.database.task.task_repository import TaskRepositoryImpl
from usecase.task.task_model import TaskReadModel
from usecase.task.task_service import TaskUseCaseImpl


class TestTaskUseCase:
    def test_fetch_task_by_id_should_return_task(self):
        session = MagicMock()
        task_repository = TaskRepositoryImpl(session)
        now = datetime.now()
        task_repository.find_by_id = Mock(
            return_value=TaskReadModel(
                id='task0',
                title='Task0',
                description='Task0Desc',
                create_date=now,
                is_done=False
            )
        )

        task_usecase = TaskUseCaseImpl(task_repository)

        task = task_usecase.fetch_task_by_id('task0')

        if task is not None:
            assert task.id == 'task0'

    def test_fetch_tasks_should_return_tasks(self):
        session = MagicMock()
        task_repository = TaskRepositoryImpl(session)
        now = datetime.now()
        task_repository.find_all = Mock(
            return_value=[
                TaskReadModel(
                    id='task0',
                    title='Task0',
                    description='Task0Desc',
                    create_date=now,
                    is_done=False
                )
            ]
        )

        task_usecase = TaskUseCaseImpl(task_repository)

        tasks = task_usecase.fetch_tasks()

        assert len(tasks) == 1
        assert tasks[0].create_date == now
