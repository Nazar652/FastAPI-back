from datetime import datetime

import pytest

from domain.task.task import Task
from infrastructure.database.task.task_dto import TaskDTO


class TestTaskDTO:
    def test_to_read_model_should_create_read_model(self):
        now = datetime.now()
        task_dto = TaskDTO(
            id='task0',
            title='Task0',
            description='Task0Desc',
            create_date=now,
            is_done=False
        )

        task = task_dto.to_read_model()

        assert task.id == 'task0'
        assert task.title == 'Task0'
        assert task.description == 'Task0Desc'
        assert task.create_date == now
        assert not task.is_done

    def test_from_entity_should_create_dto_instance(self):
        now = datetime.now()
        task = Task(
            id='task0',
            title='Task0',
            description='Task0Desc',
            create_date=now,
            is_done=False
        )

        task_dto = TaskDTO.from_entity(task)

        assert task_dto.id == 'task0'
        assert task_dto.title == 'Task0'
        assert task_dto.description == 'Task0Desc'
        assert task_dto.create_date == now
        assert not task_dto.is_done
