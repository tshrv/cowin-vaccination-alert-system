from datetime import datetime, timedelta

from src import settings
from src.cowin import CowinAPI
from src.cowin.constants import Dose, Vaccine
from src.crud.notifications import NotificationCRUD
from src.crud.alerts import AlertCRUD
from src.models.notifications import Notification
from src.utils.logging import logger
import asyncio

from src.utils.sms import twilio_client


async def slot_monitor():
    """
    :return:
    """
    logger.info('slot-monitor: started')

    alert_crud = AlertCRUD()
    notification_crud = NotificationCRUD()
    cowin = CowinAPI()

    while True:
        alerts = alert_crud.get_alerts_for_monitoring()
        len_alerts = len(alerts)
        logger.info(f'slot-monitor: {len_alerts} alert(s) found')

        # loop over alert tasks
        for alert in alerts:
            # build filter
            query_filters = {
                'pin_code': alert.pin_code,
                'min_age_limit': alert.min_age_limit,
                'vaccine': Vaccine(alert.vaccine),
                'dose': Dose(alert.dose),
            }

            # query api and filter
            data = cowin.get_availability_by_pin_code(**query_filters)

            # construct alert message
            centers = data.get('centers', [])

            if not centers:
                logger.info(f'slot-monitor: {alert.email} - no slots available')
                continue

            logger.info(f'slot-monitor: {alert.email} - slots available')
            logger.info(f'slot-monitor: {alert.email} - preparing to send alert')

            message = '\nHey! Vaccination slots are available, book your appointment now.\n'
            for center in centers:
                message += f'{center.get("name")}, {center.get("address")}\n'
                for session in center.get('sessions', []):
                    message += f'{session.get("vaccine")}: {session.get("date")}\n'
                    if alert.dose in [Dose.FIRST.value, None]:
                        message += f'Dose 1: {session.get(Dose.FIRST.value)}\n'
                    if alert.dose in [Dose.SECOND.value, None]:
                        message += f'Dose 2: {session.get(Dose.SECOND.value)}\n'

            # message sender
            message += '- Sent via CVAS'
            
            ls = notification_crud.get(
                    phone=alert.phone,
                    message=message,
                    created_at=datetime.now(settings.TIMEZONE) - timedelta(seconds=6)
            )
            logger.info(f'here it is ################### {ls}')
            
            # send alert only if current alert message is different than the last sent alert
            if ls:
                logger.info(f'slot-monitor: {alert.email} - last sent under 6 seconds, ignoring')

            else:
                # save alert entry
                notification = Notification(
                    email=alert.email,
                    phone=alert.phone,
                    message=message,
                )
                notification_id = notification_crud.create(notification)

                try:
                    # send alert
                    message_sent = twilio_client.send_message(
                        recipient=alert.phone,
                        body=message
                    )
                    if message_sent:
                        logger.info(f'slot-monitor: {alert.email} - alert sent')
                    else:
                        logger.error(f'slot-monitor: {alert.email} - failed to send alert')

                    # update alert entry, successfully sent
                    notification_crud.mark_sent(notification_id)
                except Exception as e:
                    logger.error(f'slot-monitor: {alert.email} - something went wrong while sending the alert')
                    logger.exception(e)

            # sleep for 3 seconds
            await asyncio.sleep(3)

    logger.info('slot-monitor: stopped')
