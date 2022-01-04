from domain.models import GarmentItem, Image
from test import BaseTestCase


class GarmentItemTestCase(BaseTestCase):
    def test_model_fields(self):
        garment_items = self.garment_items_repository.find('Hat')
        assert len(garment_items) >= 1

        garment_item = garment_items[0]

        assert isinstance(garment_item, GarmentItem)
        assert isinstance(garment_item.product_categories_mapped, list)
        assert isinstance(garment_item.product_id, int)
        assert isinstance(garment_item.url, str)
        assert isinstance(garment_item.gender, str)
        assert isinstance(garment_item.price, int)
        assert isinstance(garment_item.product_description, str)
        assert isinstance(garment_item.image_urls, list)
        assert isinstance(garment_item.product_imgs_src, list)
        assert isinstance(garment_item.source, str)
        assert isinstance(garment_item.product_categories, list)
        assert isinstance(garment_item.images, Image)
        assert isinstance(garment_item.images.url, str)
        assert isinstance(garment_item.images.path, str)
        assert isinstance(garment_item.imageschecksum, str)
        assert isinstance(garment_item.position, list)
        assert isinstance(garment_item.product_title, str)
        assert isinstance(garment_item.brand, str)
        assert isinstance(garment_item.currency_code, str)
        assert isinstance(garment_item.stock, int)
