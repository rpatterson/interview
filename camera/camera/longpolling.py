"""
Wait for a request for camera event logs and send them.
"""

import os
import time
import asyncio
import logging

import requests

logger = logging.getLogger(__name__)


class CameraLongPoller(object):
    """
    Wait for a request for camera event logs and send them.
    """

    API_URL = os.environ.get(
        'VERKADA_CAMERA_API_URL', 'http://localhost:5000')

    POLL_PATH = '/camera/poll/'
    POLL_TIMEOUT = 60

    LOGS_POST_PATH = '/camera/logs/'

    def __init__(self, event_log):
        """
        Capture an event log for this camera.
        """
        self.event_log = event_log

    def _open_long_poll(self, poll_url):  # pragma: no cover
        """
        Open the long poll request with a timeout.
        """
        # TODO async test coverage
        logger.info('Opening long polling connection to %s', poll_url)
        return requests.get(poll_url, timeout=self.POLL_TIMEOUT)

    async def run(self):  # pragma: no cover
        """
        Wait for a request for camera event logs and send them.
        """
        # TODO async test coverage
        loop = asyncio.get_event_loop()

        poll_url = self.API_URL + self.POLL_PATH
        post_url = self.API_URL + self.LOGS_POST_PATH
        while True:
            try:
                # TODO Maybe instead of the default thread-based async
                # here, use something more efficient for I/O waiting
                # such as something based on `select()`
                poll_response = await asyncio.wait_for(
                    loop.run_in_executor(
                        None, self._open_long_poll, poll_url),
                    timeout=self.POLL_TIMEOUT)
                # Only proceed if the server gives a 2xx response status
                poll_response.raise_for_status()
            except (requests.exceptions.Timeout, asyncio.TimeoutError):
                logger.info(
                    'Refreshing long polling connection to %s', poll_url)
                continue
            except Exception:
                logger.exception(
                    'Unexpected long polling error for %s', poll_url)
                # Avoid spamming the server or logs for unknown errors
                # TODO backoff timing, max retries, etc.
                time.sleep(1)
                continue
            else:
                logger.info(
                    'Long polling connection response from %s:\n%s',
                    poll_url, poll_response.text)
                logger.info(
                    'POSTing camera event log to the API')
                try:
                    post_response = requests.post(
                        post_url, json=self.event_log.get_log_events())
                except Exception:
                    logger.exception(
                        'Unexpected event log POST exception for %s', post_url)
                    continue
                try:
                    post_response.raise_for_status()
                except Exception:
                    logger.exception(
                        'Unexpected event log POST response status for %s',
                        post_url)
                    continue
