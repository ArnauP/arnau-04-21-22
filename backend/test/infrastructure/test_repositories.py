from unittest.mock import patch 
from infrastructure.database import create_indexes
from domain.models import GarmentItem, Image
from test import BaseTestCase


class MongoGarmentItemsRepositoryTestCase(BaseTestCase):


    def test_db_text_search(self):
        garment_items = self.garment_items_repository.find('pool shoes')
        assert len(garment_items) == 1
        
        assert isinstance(garment_items[0], GarmentItem)
