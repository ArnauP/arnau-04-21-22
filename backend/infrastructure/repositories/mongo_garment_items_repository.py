from domain.repositories import GarmentItemsRepositoryInterface
from infrastructure.repositories import BaseRepository


class MongoGarmentItemsRepository(BaseRepository, GarmentItemsRepositoryInterface):
    
    def insert(self, garment_item):
        pass

    def find(self, text):
        pass
