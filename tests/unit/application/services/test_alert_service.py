from typing import List

import pytest
from src.domain.models.alert import Alert
from src.domain.repositories.alert_repository import AlertRepository
from src.application.services.alert import AlertService
from datetime import datetime

class FakeAlertRepository(AlertRepository):
    def __init__(self):
        self.alerts = []
    
    def save(self, alert: Alert) -> None:
        self.alerts.append(alert)
    
    def list(self) -> List[Alert]:
        return self.alerts
    
    def find_by_id(self, id: str) -> Alert:
        for alert in self.alerts:
            if alert.id == id:
                return alert
        raise ValueError(f"Alert with id {id} not found")

def test_create_alert_and_save_to_repository():
    repository = FakeAlertRepository()
    service = AlertService(repository)
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    service.create_alert(alert)
    assert service.find_alert_by_id(alert.id) == alert

def test_list_alerts_from_repository():
    repository = FakeAlertRepository()
    service = AlertService(repository)
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    service.create_alert(alert)

    alerts = service.list_alerts()
    assert len(alerts) == 1
    assert alerts[0].id == alert.id
    assert alerts[0].name == alert.name
    assert alerts[0].description == alert.description
    assert alerts[0].level == alert.level
    assert alerts[0].created_at == alert.created_at
    assert alerts[0].updated_at == alert.updated_at
    
def test_find_alert_by_id_from_repository():
    repository = FakeAlertRepository()
    service = AlertService(repository)
    now = datetime.now()
    alert = Alert(
        id="1",
        name="Test Alert",
        description="Test Description",
        level=1,
        created_at=now,
        updated_at=now,
    )
    service.create_alert(alert)

    alert_found = service.find_alert_by_id(alert.id)
    assert alert_found.id == alert.id
    assert alert_found.name == alert.name
    assert alert_found.description == alert.description
    assert alert_found.level == alert.level
    assert alert_found.created_at == alert.created_at
    assert alert_found.updated_at == alert.updated_at

def test_find_alert_by_id_from_repository_not_found():
    repository = FakeAlertRepository()
    service = AlertService(repository)
    with pytest.raises(ValueError):
        service.find_alert_by_id("1")