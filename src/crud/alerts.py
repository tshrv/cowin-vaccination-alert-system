from typing import List

from .base import BaseCRUD
from src.models.alerts import Alert
from src.models.constants import AlertStatus


class AlertCRUD(BaseCRUD):
    def __init__(self):
        self.collection_name = 'alerts'

        # configure self.db, self.collection
        super().__init__()

    @staticmethod
    def _build_alert_objects(cursor) -> List[Alert]:
        """
        loop over the cursor and build Alert objects list and return them
        :param cursor:
        :return:
        """
        alerts = []
        for doc in cursor:
            alerts.append(Alert(**doc))
        return alerts

    def create(self, alert_obj):
        """
        create new entry in collection from received object
        :param alert_obj:
        :return:
        """
        rsp = self.collection.insert(alert_obj.dict())
        return rsp

    def get(self, email: str) -> List[Alert]:
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
        alerts = self._build_alert_objects(cursor)
        return alerts

    def get_alerts_for_monitoring(self) -> List[Alert]:
        """
        :return: alert records with only the fields that are required for monitoring
        """
        cursor = self.collection.find(
            {
                'status': {
                    '$eq': AlertStatus.ACTIVE.value
                }
            },
        )
        alerts = self._build_alert_objects(cursor)
        return alerts
