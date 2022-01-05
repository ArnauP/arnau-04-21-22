from pymongo import MongoClient
from unittest import TestCase

from controller.app import app, Injector


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app.config.update(
            TESTING=True,
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        self.client = self.app.test_client()
        self.db_connection = self._connect_to_database()
        self.garment_items_repository = Injector().get_repository()
        self.garment_items_repository.set_db_connection(self.db_connection)

    @staticmethod
    def _connect_to_database() -> MongoClient:
        return MongoClient(host='mongodb', port=27017)
