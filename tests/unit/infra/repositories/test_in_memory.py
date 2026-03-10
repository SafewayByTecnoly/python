from infra.repositories.in_memory import InMemoryAlertRepository
from infra.repositories.in_memory import InMemoryEventRepository
from domain.models.event import Event
from domain.models.alert import Alert

from datetime import datetime
import pytest


def test_save_alert_to_repository():
    repository = InMemoryAlertRepository()
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    repository.save(alert)
    assert len(repository.alerts) == 1
    assert repository.alerts[0].id == "1"
    assert repository.alerts[0].name == "Test Alert"
    assert repository.alerts[0].description == "Test Description"
    assert repository.alerts[0].level == 1
    assert repository.alerts[0].created_at == now
    assert repository.alerts[0].updated_at == now

def test_list_alerts_from_repository():
    repository = InMemoryAlertRepository()
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    repository.save(alert)
    alerts = repository.list()
    assert len(alerts) == 1
    assert alerts[0].id == "1"
    assert alerts[0].name == "Test Alert"
    assert alerts[0].description == "Test Description"
    assert alerts[0].level == 1
    assert alerts[0].created_at == now
    assert alerts[0].updated_at == now

def test_find_alert_by_id_from_repository():
    repository = InMemoryAlertRepository()
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    repository.save(alert)

    alert_found = repository.find_by_id(alert.id)
    assert alert_found.id == alert.id
    assert alert_found.name == alert.name
    assert alert_found.description == alert.description
    assert alert_found.level == alert.level
    assert alert_found.created_at == alert.created_at
    assert alert_found.updated_at == alert.updated_at
    
def test_find_alert_by_id_from_repository_not_found():
    repository = InMemoryAlertRepository()
    with pytest.raises(ValueError):
        repository.find_by_id("1")

def test_save_event_to_repository():
    repository = InMemoryEventRepository()
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    repository.save(event)
    assert len(repository.events) == 1
    assert repository.events[0].id == "1"
    assert repository.events[0].name == "Test Event"
    assert repository.events[0].description == "Test Description"
    assert repository.events[0].level == 1
    assert repository.events[0].created_at == now
    assert repository.events[0].updated_at == now

def test_list_events_from_repository():
    repository = InMemoryEventRepository()
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    repository.save(event)
    events = repository.list()
    assert len(events) == 1
    assert events[0].id == "1"
    assert events[0].name == "Test Event"
    assert events[0].description == "Test Description"
    assert events[0].level == 1
    assert events[0].created_at == now
    assert events[0].updated_at == now

def test_find_event_by_id_from_repository():
    repository = InMemoryEventRepository()
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    repository.save(event)

    event_found = repository.find_by_id(event.id)
    assert event_found.id == event.id
    assert event_found.name == event.name
    assert event_found.description == event.description
    assert event_found.level == event.level
    assert event_found.created_at == event.created_at
    assert event_found.updated_at == event.updated_at

def test_find_event_by_id_from_repository_not_found():
    repository = InMemoryEventRepository()
    with pytest.raises(ValueError):
        repository.find_by_id("1")
