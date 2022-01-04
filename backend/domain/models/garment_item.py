class Image():
    def __init__(self, url, path, checksum) -> None:
        self.url = url
        self.path = path
        self.checksum = checksum

class GarmentItem():
    def __init__(self, product_categories_mapped, product_id, url,
                gender, price, product_description, image_urls, 
                product_imgs_src, source, product_categories,
                images, position, product_title, brand, currency_code,
                stock) -> None:
        self.product_categories_mapped = product_categories_mapped
        self.product_id = product_id
        self.url = url
        self.gender = gender
        self.price = price
        self.product_description = product_description
        self.image_urls = image_urls
        self.product_imgs_src = product_imgs_src
        self.source = source
        self.product_categories = product_categories
        self.images = images
        self.position = position
        self.product_title = product_title
        self.brand = brand
        self.currency_code = currency_code
        self.stock = stock
