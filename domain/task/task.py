from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str
    create_date: datetime
    is_done: bool
