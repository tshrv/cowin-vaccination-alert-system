from typing import List


from .base import BaseCRUD
from src.models.notifications import Notification
from ..utils.validators import ObjectId


class NotificationCRUD(BaseCRUD):
    def __init__(self):
        self.collection_name = 'notifications'

        # configure self.db, self.collection
        super().__init__()

    @staticmethod
    def _build_notification_objects(cursor) -> List[Notification]:
        """
        loop over the cursor and build Notification objects list and return them
        :param cursor:
        :return:
        """
        notifications = []
        for doc in cursor:
            notifications.append(Notification(**doc))
        return notifications

    def create(self, notification_obj):
        """
        create new entry in collection from received object
        :param notification_obj:
        :return:
        """
        rsp = self.collection.insert(notification_obj.dict())
        return rsp

    def mark_sent(self, object_id: ObjectId):
        """
        mark the record with <id> as sent
        :return:
        """
        rsp = self.collection.update_one(
            {
                '_id': object_id,
            },
            {
                '$set': {
                    'sent': True,
                }
            }
        )
        return rsp

    def get(self, email: str) -> List[Notification]:
        """
        :param email: user email
        :return: all records available for that email
        """
        cursor = self.collection.find(
            {
                'email': {
                    '$eq': email
                }
            }
        )
        notifications = self._build_notification_objects(cursor)
        return notifications
