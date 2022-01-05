from domain.models import GarmentItem
from test import BaseTestCase


class MongoGarmentItemsRepositoryTestCase(BaseTestCase):
    def test_db_text_search(self):
        garment_items = self.garment_items_repository.find('pool shoes')
        assert len(garment_items) >= 1

        item = garment_items[0]

        assert isinstance(item, GarmentItem)
        assert item.image_urls is not None
        assert item.product_title is not None
        assert item.stock is not None
        assert item.price is not None
        assert item.currency_code is not None
