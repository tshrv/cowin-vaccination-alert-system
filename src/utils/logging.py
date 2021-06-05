import logging
from src import settings
from typing import Optional


class Logger:
    _logger_instance = None

    @staticmethod
    def get_singleton_instance():
        if not Logger._logger_instance:
            Logger._logger_instance = Logger().logger
        return Logger._logger_instance

    def __init__(self):
        self._logger: Optional[logging.Logger] = None

    @property
    def logger(self) -> logging.Logger:
        """
        :return: logging.Logger
        """
        if not self._logger:
            self._configure_logger()
        return self._logger

    def _configure_logger(self):
        """
        :return: None
        """
        if self._logger:
            return

        self._logger = logging.getLogger()

        # formatter
        formatter = logging.Formatter(settings.LOG_FORMAT)

        # file handler
        file_handler = logging.FileHandler(settings.LOG_FILE_PATH)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

        # stream handler
        if settings.LOG_STREAM_HANDLER_ENABLED:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self._logger.addHandler(stream_handler)

        self._logger.setLevel(settings.LOG_LEVEL)


logger = Logger.get_singleton_instance()
