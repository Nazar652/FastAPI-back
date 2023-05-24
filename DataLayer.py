from peewee import *

from config import USER, PASSWORD, HOST, PORT


class Task(Model):
    title = CharField()
    description = TextField()
    create_date = DateTimeField()
    is_done = BooleanField()

    @classmethod
    def create_instance(cls, title, description, create_date, is_done):
        try:
            return False, cls.create(
                title=title,
                description=description,
                create_date=create_date,
                is_done=is_done
            )
        except Exception as e:
            return True, e

    @classmethod
    def read_instance(cls, ident):
        try:
            return False, cls.get(cls.id == ident)
        except Exception as e:
            return True, e

    @classmethod
    def update_instance(cls, ident, **kwargs):
        try:
            query = cls.update(**kwargs).where(cls.id == ident)
            query.execute()
            return False, cls.get(cls.id == ident)
        except Exception as e:
            return True, e

    @classmethod
    def delete_inst(cls, ident):
        try:
            instance = cls.get(cls.id == ident)
            instance.delete_instance()
            return False, instance
        except Exception as e:
            return True, e

    class Meta:
        database = PostgresqlDatabase(
            database='database',
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
