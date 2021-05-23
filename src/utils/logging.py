import logging
from src import settings

logger = None


def configure_logger():
    """
    logger configuration
    :return:
    """
    global logger

    logger = logging.getLogger()

    # formatter
    formatter = logging.Formatter(settings.LOG_FORMAT)

    # file handler
    file_handler = logging.FileHandler(settings.LOG_FILE_PATH)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # stream handler
    if settings.LOG_STREAM_HANDLER_ENABLED:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    logger.setLevel(settings.LOG_LEVEL)


def get_logger():
    """
    singleton instance of logger
    :return:
    """
    global logger

    # configure logger if not already
    if not logger:
        configure_logger()

    return logger
