from domain.models.event import Event
from datetime import datetime
import pytest

def test_create_event_successfully():
    now = datetime.now()
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    assert event.id == "1"
    assert event.name == "Test Event"
    assert event.description == "Test Description"

def test_create_event_with_invalid_id():
    now = datetime.now()
    with pytest.raises(ValueError):
        Event(
            id=None,
            name="Test Event",
            description="Test Description",
            level=1,
            created_at=now,
            updated_at=now,
        )

def test_create_event_with_invalid_name():
    now = datetime.now()
    with pytest.raises(ValueError):
        Event(
            id="1",
            name=None,
            description="Test Description",
            level=1,
            created_at=now,
            updated_at=now,
        )

def test_create_event_with_invalid_description():
    now = datetime.now()
    with pytest.raises(ValueError):
        Event(
            id="1",
            name="Test Event",
            description=None,
            level=1,
            created_at=now,
            updated_at=now,
        )

def test_create_event_with_invalid_level():
    now = datetime.now()
    with pytest.raises(ValueError):
        Event(
            id="1",
            name="Test Event",
            description="Test Description",
            level=None,
            created_at=now,
            updated_at=now,
        )

def test_create_event_with_default_created_at_and_updated_at():
    event = Event(
        id="1",
        name="Test Event",
        description="Test Description",
        level=1,
        created_at=None,
        updated_at=None,
    )
    assert event.created_at is not None
    assert event.updated_at is not None