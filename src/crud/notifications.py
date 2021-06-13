from datetime import datetime, timedelta
from typing import List

from src.models.notifications import Notification, NotificationIn
from src.utils.validators import ObjectId
from .base import BaseCRUD
from src import settings


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

    def create(self, notification_obj: NotificationIn):
        """
        create new entry in collection from received object
        :param notification_obj:
        :return:
        """
        data_dict = {
            'created_at': datetime.utcnow(),
            **notification_obj.dict()
        }
        rsp = self.collection.insert(data_dict)
        return rsp

    def mark_sent(self, object_id: ObjectId):
        """
        mark the record with <object_id> as sent
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

    def get(self, phone: str) -> List[Notification]:
        """
        :param phone: user phone
        :return: all records available for that phone
        """
        query_dict = {
            'phone': {
                '$eq': phone
            }
        }
        cursor = self.collection.find(
            query_dict
        )
        notifications = self._build_notification_objects(cursor)
        return notifications

    def previously_sent(self, phone: str, message: str,
                        timedelta_seconds: int = settings.RESEND_WINDOW) -> bool:
        """
        :param phone: user phone
        :param message: message content
        :param timedelta_seconds: created_at in range from current utc time
        :return: <bool> any notifications for those filters
        """
        query_dict = {
            'phone': {
                '$eq': phone
            },
            'message': {
                '$eq': message
            },
            'created_at': {
                '$gt': datetime.utcnow() - timedelta(seconds=timedelta_seconds)
            }
        }
        count = self.collection.count_documents(
            query_dict
        )
        return bool(count)
