import pytest

from domain.task.task import Task


class TestTask:
    def test_creating_task(self):
        task = Task(
            id='task0',
            title='Task0',
            description='Task0Desc'
        )

        assert task.id == 'task0'
        assert task.title == 'Task0'
        assert task.description == 'Task0Desc'

    def test_task_should_be_identified(self):
        task0 = Task(
            id='task0',
            title='Task0',
            description='Task0Desc'
        )

        task1 = Task(
            id='task0',
            title='Task0',
            description='Task0Desc'
        )

        task2 = Task(
            id='task1',
            title='Task1',
            description='Task1Desc'
        )

        assert task0 == task1
        assert task0 != task2

    @pytest.mark.parametrize(
        "is_done",
        [
            (True, ),
            (False, ),
        ]
    )
    def test_is_done_setter_should_update_value(self, is_done):
        task = Task(
            id='task0',
            title='Task0',
            description='Task0Desc'
        )

        task.is_done = is_done

        assert task.is_done == is_done