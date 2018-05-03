"""
Simulate a camera that records events and long polls them to an API.
"""

import asyncio
import logging

from . import eventlog
from . import longpolling

logger = logging.getLogger(__name__)


def main():  # pragma: no cover
    """
    Simulate a camera that records events and long polls them to an API.
    """
    # TODO Test coverage
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()

    event_log = eventlog.CameraEventLog()
    logger.info('Starting camera event log')
    loop.create_task(event_log.run())

    poller = longpolling.CameraLongPoller(event_log)
    logger.info('Starting camera long polling to the API')
    loop.create_task(poller.run())

    loop.run_forever()
    loop.close()

    # TODO thread cleanup, SIGINT?
