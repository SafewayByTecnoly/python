from typing import List
from src.domain.models.alert import Alert
from src.domain.models.event import Event
from src.domain.repositories.alert_repository import AlertRepository
from src.domain.repositories.event_repository import EventRepository


class InMemoryAlertRepository(AlertRepository):
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

class InMemoryEventRepository(EventRepository):
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