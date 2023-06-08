from datetime import datetime


class Task:
    title: str
    description: str
    create_date: datetime
    is_done: bool

    def to_dict(self) -> dict:
        ret_dict = dict()
        ret_dict['title'] = self.title
        ret_dict['description'] = self.description
        ret_dict['create_date'] = self.create_date
        ret_dict['is_done'] = self.is_done
        return ret_dict
