"""
Simulate a camera that records events and long polls them to an API.
"""

import asyncio
import logging

from . import eventlog

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

    loop.run_forever()
    loop.close()

    # TODO thread cleanup, SIGINT?
