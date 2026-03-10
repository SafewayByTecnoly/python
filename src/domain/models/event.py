from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    id: str
    name: str
    description: str
    level: int
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if self.id is None:
            raise ValueError("ID is required")
        if self.name is None:
            raise ValueError("Name is required")
        if self.description is None:
            raise ValueError("Description is required")
        if self.level is None:
            raise ValueError("Level is required")
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()