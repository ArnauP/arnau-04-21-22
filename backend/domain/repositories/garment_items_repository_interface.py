from abc import ABCMeta, abstractmethod


class GarmentItemsRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def find(self, name):
        pass
