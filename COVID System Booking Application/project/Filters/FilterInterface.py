from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def filter(self, json):
        pass