import pytest
from domain.models.alert import Alert
from datetime import datetime

def test_create_alert():
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    assert alert.id == "1"
    assert alert.name == "Test Alert"
    assert alert.description == "Test Description"

def test_create_alert_with_invalid_id():
    now = datetime.now()
    with pytest.raises(ValueError):
        Alert(
            id=None,
            name="Test Alert",
            description="Test Description",
            level=1,
            created_at=now,
            updated_at=now,
        )

def test_create_alert_with_invalid_name():
    now = datetime.now()
    with pytest.raises(ValueError):
        Alert(
            id="1",
            name=None,
            description="Test Description",
            level=1,
            created_at=now,
            updated_at=now,
        )

def test_create_alert_with_invalid_description(): 
    now = datetime.now()
    with pytest.raises(ValueError):
        Alert(
            id="1",
            name="Test Alert",
            description=None,
            level=1,
            created_at=now,
            updated_at=now,
        )

def test_create_alert_with_invalid_level():
    now = datetime.now()
    with pytest.raises(ValueError):
        Alert(
            id="1",
            name="Test Alert",
            description="Test Description",
            level=None,
            created_at=now,
            updated_at=now,
        )

def test_create_alert_with_default_created_at_and_updated_at():
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=None,
        updated_at=None,
    )

    assert alert.created_at is not None 
    assert alert.updated_at is not None
