from src.cowin import CowinAPI
from src.cowin.constants import Dose, Vaccine
from src.crud.notifications import NotificationCRUD
from src.crud.alerts import AlertCRUD
from src.models.notifications import Notification
from src.utils.logging import logger
import asyncio


async def slot_monitor():
    """
    :return:
    """
    logger.info('slot-monitor: Started')

    alert_task_crud = AlertCRUD()
    alert_notification_crud = NotificationCRUD()
    cowin = CowinAPI()

    alert_tasks = alert_task_crud.get_alerts_for_monitoring()

    # loop over alert tasks
    for alert_task in alert_tasks:
        # build filter
        query_filters = {
            'pin_code': alert_task.pin_code,
            'min_age_limit': alert_task.min_age_limit,
            'vaccine': Vaccine(alert_task.vaccine),
            'dose': Dose(alert_task.dose),
        }

        # query api and filter
        data = cowin.get_availability_by_pin_code(**query_filters)

        # construct alert message
        centers = data.get('centers', [])

        if not centers:
            logger.info(f'slot-monitor: {alert_task.email} - No slots available')
            continue

        logger.info(f'slot-monitor: {alert_task.email} - Slots available')
        logger.info(f'slot-monitor: {alert_task.email} - Preparing to send alert')

        message = 'Hey! Vaccination slots are available, book your appointment now.\n'
        for center in centers:
            message = f'{center.get("name"), center.get("address")}\n'
            for session in center.get('sessions', []):
                message += f'{session.get("vaccine")}: {session.get("date")}\n'
                if alert_task.dose in [Dose.FIRST.value, None]:
                    message += f'Dose 1: {session.get(Dose.FIRST.value)}\n'
                if alert_task.dose in [Dose.SECOND.value, None]:
                    message += f'Dose 2: {session.get(Dose.SECOND.value)}\n'

        # message sender
        message += '- Sent via CVAS'

        # save alert entry
        alert_notification_obj = Notification(
            email=alert_task.email,
            message=message,
        )
        alert_notification_obj = alert_notification_crud.create(alert_notification_obj)

        try:
            # send alert
            logger.info(f'slot-monitor: {alert_task.email} - Alert sent')

            # update alert entry, successfully sent
            alert_notification_obj = alert_notification_crud.mark_sent(alert_notification_obj.id)
        except Exception as e:
            logger.error(f'slot-monitor: {alert_task.email} - Failed to send alert')
            logger.exception(e)

    # sleep for 3 seconds
    await asyncio.sleep(3)

    logger.info('slot-monitor: Stopped')
