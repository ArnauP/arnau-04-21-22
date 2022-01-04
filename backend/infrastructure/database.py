from pymongo import MongoClient


def connect_to_database():
    return MongoClient(host='mongodb', port=27017)
