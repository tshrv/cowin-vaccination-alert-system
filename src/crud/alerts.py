from typing import List

from .base import BaseCRUD
from src.models.alerts import AlertTask


class AlertTaskCRUD(BaseCRUD):
    def __init__(self):
        self.collection_name = 'alerts'

        # configure self.db, self.collection
        super().__init__()

    def create(self, alert_task_obj):
        rsp = self.collection.insert(alert_task_obj.dict())
        return rsp

    def get(self, email: str) -> List[AlertTask]:
        cursor = self.collection.find(
            {
                'email': {
                    '$eq': email
                }
            }
        )
        alert_tasks = []
        for doc in cursor:
            alert_tasks.append(AlertTask(**doc))
        return alert_tasks
