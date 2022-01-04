from pymongo import MongoClient


def create_indexes(db_connection):
    db_connection.db.garment_items.create_index([
        ("product_title", "text"), 
        ("brand", "text"), 
        ("product_description", "text")])


def connect_to_database():
    mongo = MongoClient(host='mongodb', port=27017)
    create_indexes(mongo)
    return mongo
