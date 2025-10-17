from abc import ABC, abstractmethod
from interfaces.observer import Observer

class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, product_name: str):
        pass
