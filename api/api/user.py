"""
API endpoints the users interact with.
"""
# Better module name, less clashy

import logging

import flask
import flask_restful

from . import camera

logger = logging.getLogger(__name__)


class UserCameraLogs(flask_restful.Resource):
    """
    Return camera logs to the user.
    """

    def get(self):  # pragma: no cover
        """
        Return camera logs to the user.
        """
        # TODO async test coverage
        logger.info('Received user request for camera revent logs')

        # Check if a camera is ready or wait for one to be ready
        camera.open_camera_polls.get()

        # Tell the waiting cameras to proceed to send their logs
        # TODO memory leak?  Meaningful queue item?
        camera.user_camera_log_requests.put(flask.request)

        # Wait for the cameras to send their event logs
        args = camera.camera_event_logs.get()

        camera.open_camera_polls.task_done()
        camera.camera_event_logs.task_done()

        # Return the event logs to the user
        return args
