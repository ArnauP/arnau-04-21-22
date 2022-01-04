from domain.repositories import GarmentItemsRepositoryInterface
from infrastructure.repositories import BaseRepository
from domain.models import GarmentItem, Image


class MongoGarmentItemsRepository(BaseRepository,
                                  GarmentItemsRepositoryInterface):
    def insert(self, garment_item):
        images = [{
                    "url": image.url,
                    "path": image.path,
                    "checksum": image.checksum
                } for image in garment_item.images]
        json_data = {
            "product_categories_mapped":
                garment_item.product_categories_mapped,
            "product_id": garment_item.product_id,
            "url": garment_item.url,
            "gender": garment_item.gender,
            "price": garment_item.price,
            "product_description": garment_item.product_description,
            "image_urls": garment_item.image_urls,
            "product_imgs_src": garment_item.product_imgs_src,
            "source": garment_item.source,
            "product_categories": garment_item.product_categories,
            "images": images,
            "position": garment_item.position,
            "product_title": garment_item.product_title,
            "brand": garment_item.brand,
            "currency_code": garment_item.currency_code,
            "stock": garment_item.stock
        }
        self.db_connection.db.garment_items.insert_one(json_data)

    def find(self, text):
        cursor = self.db_connection.db.garment_items.find(
            {"$text": {"$search": f'\"{text}\"'}})
        garment_items = []
        for document in cursor:
            images = [Image(
                    url=image["url"],
                    path=image["path"],
                    checksum=image["checksum"]
                ) for image in document["images"]]
            garment_items.append(GarmentItem(
                product_categories_mapped=document[
                    "product_categories_mapped"],
                product_id=document["product_id"],
                url=document["url"],
                gender=document["gender"],
                price=document["price"],
                product_description=document["product_description"],
                image_urls=document["image_urls"],
                product_imgs_src=document["product_imgs_src"],
                source=document["source"],
                product_categories=document["product_categories"],
                images=images,
                position=document["position"],
                product_title=document["product_title"],
                brand=document["brand"],
                currency_code=document["currency_code"],
                stock=document["stock"],
            ))
        return garment_items
