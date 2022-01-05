from abc import ABCMeta, abstractmethod
from domain.model import GarmentItem


class GarmentItemsRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, data: GarmentItem) -> None:
        pass

    @abstractmethod
    def find(self, query: str) -> list:
        pass
