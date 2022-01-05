from pymongo import MongoClient


def create_indexes(db_connection) -> None:
    db_connection.db.garment_items.create_index([
        ("product_title", "text"),
        ("brand", "text"),
        ("product_description", "text")])


def connect_to_database() -> MongoClient:
    mongo = MongoClient(host='mongodb', port=27017)
    create_indexes(mongo)
    return mongo
