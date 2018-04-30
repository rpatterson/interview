"""
A camaera logs events.
"""

import random
import datetime
import asyncio
import logging

logger = logging.getLogger(__name__)


class CameraEventLog(object):
    """
    Log camera events.
    """

    DESCRIPTIONS = [
        'detected motion at 40, 30',
        'user started viewing live video',
        'brightness adjusted +10',
        ]

    event_delay = 10

    def __init__(self, event_delay=event_delay):
        """
        Initialize the event log.
        """
        # TODO Something explicitly thread/async-await safe.
        self.events = []

        self.event_delay = event_delay

    def get_log_events(self):
        """
        Return all logged events.
        """
        # TODO return a copy?
        return self.events

    def log_event(self, description):
        """
        Log an event with a timestamp.
        """
        event = dict(
            timestamp=datetime.datetime.now().isoformat(),
            description=description)
        self.events.append(event)
        logger.info(description)
        return event

    async def run(self):
        """
        Log an event every 10 seconds.
        """
        # TODO Test coverage
        while True:  # pragma: no cover
            self.log_event(random.choice(self.DESCRIPTIONS))
            await asyncio.sleep(self.event_delay)
