import logging

logger = None


def configure_logger():
    """
    logger configuration
    :return:
    """
    global logger

    logger = logging.getLogger()
    handler = logging.FileHandler('operations.log')
    logger.addHandler(handler)


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
