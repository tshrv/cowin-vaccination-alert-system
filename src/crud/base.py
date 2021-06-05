from src.utils.db import db_client


class BaseCRUD:
    def __init__(self):
        self.db_client = db_client
        assert hasattr(self, 'collection_name'), 'collection_name is required'
        self.collection = self.db_client.get_collection(self.collection_name)
