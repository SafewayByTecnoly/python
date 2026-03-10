from ast import List
from datetime import datetime
from domain.models.event import Event
from domain.repositories.event_repository import EventRepository
from application.services.event import EventService
import pytest

class FakeEventRepository(EventRepository):
    def __init__(self):
        self.events = []
    
    def save(self, event: Event) -> None:
        self.events.append(event)
    
    def list(self) -> List[Event]:
        return self.events
    
    def find_by_id(self, id: str) -> Event:
        for event in self.events:
            if event.id == id:
                return event
        raise ValueError(f"Event with id {id} not found")


def test_create_event_and_save_to_repository():
    repository = FakeEventRepository()
    service = EventService(repository)
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    service.create_event(event)
    assert service.find_event_by_id(event.id) == event

def test_list_events_from_repository():
    repository = FakeEventRepository()
    service = EventService(repository)
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    service.create_event(event)
    events = service.list_events()
    assert len(events) == 1
    assert events[0].id == event.id
    assert events[0].name == event.name
    assert events[0].description == event.description
    assert events[0].level == event.level
    assert events[0].created_at == event.created_at
    assert events[0].updated_at == event.updated_at

def test_find_event_by_id_from_repository():
    repository = FakeEventRepository()
    service = EventService(repository)
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    service.create_event(event)
    event_found = service.find_event_by_id(event.id)
    assert event_found.id == event.id
    assert event_found.name == event.name
    assert event_found.description == event.description
    assert event_found.level == event.level
    assert event_found.created_at == event.created_at
    assert event_found.updated_at == event.updated_at

def test_find_event_by_id_from_repository_not_found():
    repository = FakeEventRepository()
    service = EventService(repository)
    with pytest.raises(ValueError):
        service.find_event_by_id("1")
        