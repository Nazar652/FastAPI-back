from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status

from domain.task.task_exception import TaskNotFoundError
from infrastructure.database.database import create_tables
from infrastructure.database.task.task_repository import TaskRepository, TaskRepositoryImpl
from presentation.task.task_error_message import ErrorMessageTaskNotFound
from usecase.task.task_model import TaskReadModel, TaskCreateModel, TaskUpdateModel
from usecase.task.task_service import TaskUseCase, TaskUseCaseImpl

app = FastAPI()

create_tables()


def task_usecase() -> TaskUseCase:
    task_repository: TaskRepository = TaskRepositoryImpl()
    return TaskUseCaseImpl(task_repository)


@app.get(
    '/api/tasks',
    response_model=List[TaskReadModel],
    status_code=status.HTTP_200_OK
)
def get_tasks(
        task_usecase_local: TaskUseCase = Depends(task_usecase)
):
    try:
        tasks = task_usecase_local.fetch_tasks()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    return tasks


@app.get(
    '/api/tasks/{task_id}',
    response_model=TaskReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTaskNotFound
        }
    }
)
def get_book(
    task_id: str,
    task_usecase_local: TaskUseCase = Depends(task_usecase)
):
    try:
        task = task_usecase_local.fetch_task_by_id(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    return task


@app.post(
    '/api/tasks',
    response_model=TaskReadModel,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    data: TaskCreateModel,
    task_usecase_local: TaskUseCase = Depends(task_usecase)
):
    try:
        task = task_usecase_local.create_task(data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    return task


@app.put(
    '/api/tasks/{task_id}',
    response_model=TaskReadModel,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTaskNotFound
        }
    }
)
def update_task(
    task_id: str,
    data: TaskUpdateModel,
    task_usecase_local: TaskUseCase = Depends(task_usecase),
):
    try:
        updated_task = task_usecase_local.update_task(task_id, data)
    except TaskNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    return updated_task


@app.delete(
    '/api/tasks/{task_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTaskNotFound
        }
    }
)
def delete_task(
    task_id: str,
    task_usecase_local: TaskUseCase = Depends(task_usecase)
):
    try:
        task_usecase_local.delete_task_by_id(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
