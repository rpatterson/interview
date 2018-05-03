"""
API endpoints the cameras interact with.
"""

import time
import random
import logging

import flask_restful

logger = logging.getLogger(__name__)


class CameraLongPoll(flask_restful.Resource):
    """
    Hold the request open until a user requests the logs.
    """

    def get(self):  # pragma: no cover
        """
        Hold the request open until a user requests the logs.
        """
        # TODO async test coverage
        logger.info('Long polling request from camera started')
        time.sleep(random.choice((30, 60)))
        logger.info('Received user request for camera event logs')
        return True




class CameraLogsResponse(flask_restful.Resource):
    """
    The camera sends the event logs to the API.
    """

    def post(self):  # pragma: no cover
        """
        Receive the event logs from a camera.
        """
        # TODO async test coverage
        logger.info('Received event log from a camera')
        return True
