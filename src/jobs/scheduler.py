import aiojobs

from src.jobs.slot_monitor import slot_monitor
from src.utils.logging import logger


async def bootstrap_schedulers():
    """
    Spawn jobs to run in the background.
    :return:
    """
    logger.info('scheduler: spawning jobs started')

    scheduler = await aiojobs.create_scheduler()
    await scheduler.spawn(slot_monitor())

    logger.info('scheduler: spawning jobs completed')
