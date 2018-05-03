"""
API endpoints the cameras interact with.
"""

import queue
import logging

import flask
import flask_restful

logger = logging.getLogger(__name__)

# TODO multiple cameras using max_size?
open_camera_polls = queue.Queue()
user_camera_log_requests = queue.Queue()
camera_event_logs = queue.Queue()


class CameraLongPoll(flask_restful.Resource):
    """
    Hold the request open until a user requests the logs.
    """

    # TODO multiple cameras with a camera ID arg?
    def get(self):  # pragma: no cover
        """
        Hold the request open until a user requests the logs.
        """
        # TODO async test coverage
        logger.info('Long polling request from camera started')

        # Tell any waiting or future user request that this camera is
        # ready and waiting to send event logs
        # TODO memory leak?  Meaningful queue item?
        open_camera_polls.put(flask.request)

        # Wait until a user request for camera event logs has been received
        user_camera_log_requests.get()
        logger.info('Received user request for camera event logs')
        user_camera_log_requests.task_done()

        # Tell the camera to send the event logs in another request
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

        # Tell the user it can now retrieve the event logs
        camera_event_logs.put(flask.request.json)

        return True
