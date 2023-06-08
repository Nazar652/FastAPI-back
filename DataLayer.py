from peewee import *

from errors.api_errors import CustomError

db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    @classmethod
    def get_all(cls) -> list:
        return cls.select()

    @classmethod
    def create_instance(cls, **kwargs) -> None:
        try:
            return cls.create(**kwargs)
        except Exception:
            raise CustomError("Unknown Error", 500)

    @classmethod
    def read_instance(cls, ident):
        try:
            return cls.get(cls.id == ident)
        except DoesNotExist:
            raise CustomError("Task with such identifier doesn't exist", 404)

    @classmethod
    def update_instance(cls, ident, **kwargs):
        try:
            query = cls.update(**kwargs).where(cls.id == ident)
            query.execute()
            return cls.get(cls.id == ident)
        except AttributeError:
            raise CustomError("Wrong parameters", 400)

    @classmethod
    def delete_inst(cls, ident):
        try:
            instance = cls.get(cls.id == ident)
            instance.delete_instance()
            return instance
        except DoesNotExist:
            raise CustomError("Task with such identifier doesn't exist", 404)

    class Meta:
        database = db


class TaskModel(BaseModel):
    title = CharField()
    description = TextField()
    create_date = DateTimeField()
    is_done = BooleanField()


db.create_tables([TaskModel], safe=True)
