from twilio.rest import Client

from src import settings
from src.utils.logging import logger


class TwilioClient:
    def __init__(self):
        self.sender_number = settings.TWILIO_SENDER
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_message(self, recipient, body):
        """
        :param recipient: country code format +911234567890
        :param body: message content
        :return: bool
        """
        message_sent = False
        try:
            resp = self.client.messages.create(
                body=body,
                from_=self.sender_number,
                to=recipient
            )
            if resp.error_code or resp.error_message:
                logger.error(f'twilio - failed to send sms to {recipient}, {resp.error_message}:{resp.error_code}')
            else:
                message_sent = True
        except Exception as e:
            logger.exception(e)
        return message_sent


twilio_client = TwilioClient()
