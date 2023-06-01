import datetime

from DataLayer import TaskModel
from errors.api_errors import CustomError
from interfaces.task_interface import Task

from playhouse.shortcuts import model_to_dict


def get_one_instance(ident: int) -> dict:
    if not isinstance(ident, int):
        raise CustomError('Index might be an integer', 400)

    resp = TaskModel.read_instance(ident)
    return model_to_dict(resp)


def get_all() -> list:
    all_records = TaskModel.get_all()
    records_in_dict = [model_to_dict(i) for i in all_records]
    return records_in_dict


def create_instance(data: dict) -> dict:
    task = Task()
    try:
        task.title = str(data['title'])
        task.description = str(data['description'])
        task.create_date = datetime.datetime.now()
        task.is_done = False
        return model_to_dict(TaskModel.create_instance(**task.to_dict()))
    except KeyError:
        raise CustomError("Some key arguments are missing", 400)
    except TypeError:
        raise CustomError("Some arguments have unsupported type", 400)


def update_instance(ident: int, data: dict) -> dict:
    if not isinstance(ident, int):
        raise CustomError('Index might be an integer', 400)
    updated_task = TaskModel.update_instance(ident, **data)
    return model_to_dict(updated_task)


def delete_single_instance(ident: int) -> dict:
    if not isinstance(ident, int):
        raise CustomError('Index might be an integer', 400)

    resp = TaskModel.delete_inst(ident)
    return model_to_dict(resp)
