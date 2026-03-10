from abc import ABC, abstractmethod
from typing import List
from src.domain.models.alert import Alert


class AlertRepository(ABC):
    @abstractmethod
    def save(self, alert: Alert) -> None:
        ...

    @abstractmethod
    def list(self) -> List[Alert]:
        ...

    @abstractmethod
    def find_by_id(self, id: str) -> Alert:
        ...