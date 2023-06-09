class TaskNotFoundError(Exception):
    message = "Task with such id doesn't exist."

    def __str__(self):
        return TaskNotFoundError.message
