class Image:
    """Defines the components of a given image.

    Args:
        url (str): URL path of the image.
        path (str): Path of the image.
        checksum (str): Checksum verification code.

    """
    def __init__(self, url, path, checksum) -> None:
        self.url = url
        self.path = path
        self.checksum = checksum


class GarmentItem:
    """Defines the attributes needed for a garment item object.

    Args:
        _id (str): Unique ObjectID converted to string.
        product_categories_mapped (list): List of categories mapped.
        product_id (int): Product identification id.
        url (str): URL path for the image.
        gender (str): Gender target for the gender item.
        price (float): Price for the garment item.
        product_description (str): Description of the garment item.
        image_urls (list): List of URL paths.
        product_imgs_src (list): List of product URL paths.
        source (str): Source of the garment item.
        product_categories (list): Product categories associated.
        images (list): List of Image objects.
        position (list): Position of the garment item.
        product_title (str): Product title identifying the garment item.
        brand (str): Brand of the item.
        currency_code (str): Currency code for the price.
        stock (int): Current stock available.


    """
    def __init__(self, product_categories_mapped, product_id, url,
                 gender, price, product_description, image_urls,
                 product_imgs_src, source, product_categories,
                 images, position, product_title, brand, currency_code,
                 stock, _id=None) -> None:
        self.id = _id
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
