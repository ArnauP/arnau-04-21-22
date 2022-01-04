from domain.models import GarmentItem
from test import BaseTestCase


class MongoGarmentItemsRepositoryTestCase(BaseTestCase):
    def test_db_text_search(self):
        garment_items = self.garment_items_repository.find('pool shoes')
        assert len(garment_items) == 1

        assert isinstance(garment_items[0], GarmentItem)
