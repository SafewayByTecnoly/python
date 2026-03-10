from src.domain.repositories.alert_repository import AlertRepository
from src.domain.models.alert import Alert
from typing import List

class AlertService:
    def __init__(self, repository: AlertRepository):
        self._repository = repository
    
    def create_alert(self, alert: Alert) -> None:
        self._repository.save(alert)
    
    def list_alerts(self) -> List[Alert]:
        return self._repository.list()
    
    def find_alert_by_id(self, id: str) -> Alert:
        return self._repository.find_by_id(id)
    