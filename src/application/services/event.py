from typing import List
from uuid import uuid4
from src.domain.repositories.event_repository import EventRepository
from src.domain.models.event import Event
from datetime import datetime

class EventService:
    def __init__(self, repository: EventRepository):
        self._repository = repository
    
    def create_event(self, name: str, description: str, level: int) -> None:
        now = datetime.now()
        event = Event(
            id=str(uuid4()),
            name=name,
            description=description,
            level=level,
            created_at=now,
            updated_at=now,
        )
        self._repository.save(event)
    
    def list_events(self) -> List[Event]:
        return self._repository.list()
    
    def find_event_by_id(self, id: str) -> Event:
        return self._repository.find_by_id(id)
    
