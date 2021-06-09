from src.utils.logging import logger
from src import settings
from typing import Optional
from pymongo import MongoClient


class DBClient:
    _client_instance = None

    def __init__(self):
        self._client: Optional[MongoClient] = None

    @staticmethod
    def get_singleton_instance():
        logger.info('database: Requesting client')
        if not DBClient._client_instance:
            DBClient._client_instance = DBClient().client
        return DBClient._client_instance

    @property
    def client(self):
        """
        :return: MongoClient
        """
        if not self._client:
            self._configure_client()
        return self._client

    def _configure_client(self):
        """
        :return: None
        """
        logger.info('database: establishing connection')
        self._client = MongoClient(settings.DB_CONNECTION_STRING).get_database(settings.DB_NAME)
        logger.info('database: connection established')


db_client = DBClient.get_singleton_instance()
