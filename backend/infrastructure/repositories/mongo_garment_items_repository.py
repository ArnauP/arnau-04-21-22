from domain.repositories import GarmentItemsRepositoryInterface
from infrastructure.repositories import BaseRepository
from domain.models import GarmentItem, Image


class MongoGarmentItemsRepository(BaseRepository,
                                  GarmentItemsRepositoryInterface):
    def insert(self, garment_item: GarmentItem) -> None:
        images = [{
                    "url": image.url,
                    "path": image.path,
                    "checksum": image.checksum
                } for image in garment_item.images]
        item = {
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
        self.db_connection.db.garment_items.insert_one(item)

    def find(self, text: str) -> list:
        cursor = self.db_connection.db.garment_items.find(
            {"$text": {"$search": f'\"{text}\"'}})
        garment_items = []
        for document in cursor:
            images = [Image(
                    url=image.get("url"),
                    path=image.get("path"),
                    checksum=image.get("checksum")
                ) for image in document.get("images")]
            garment_items.append(GarmentItem(
                _id=document.get("_id"),
                product_categories_mapped=document.get(
                    "product_categories_mapped"),
                product_id=document.get("product_id"),
                url=document.get("url"),
                gender=document.get("gender"),
                price=document.get("price"),
                product_description=document.get("product_description"),
                image_urls=document.get("image_urls"),
                product_imgs_src=document.get("product_imgs_src"),
                source=document.get("source"),
                product_categories=document.get("product_categories"),
                images=images,
                position=document.get("position"),
                product_title=document.get("product_title"),
                brand=document.get("brand"),
                currency_code=document.get("currency_code"),
                stock=document.get("stock"),
            ))
        return garment_items
