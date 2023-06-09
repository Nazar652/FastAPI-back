from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    id: str
    title: str
    description: str
    create_date: Optional[datetime] = None
    is_done: bool = False
