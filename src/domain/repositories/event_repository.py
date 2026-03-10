from abc import ABC, abstractmethod
from typing import List
from src.domain.models.event import Event


class EventRepository(ABC):
    @abstractmethod
    def save(self, event: Event) -> None:
        ...
    
    @abstractmethod
    def list(self) -> List[Event]:
        ...
    
    @abstractmethod
    def find_by_id(self, id: str) -> Event:
        ...