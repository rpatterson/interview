"""
Test that the local Python development environment is working.
"""

import unittest

from camera import eventlog


class TestCameraEventLog(unittest.TestCase):
    """
    Test that simulated camera logs events.
    """

    def test_retrieve_log_events(self):
        """
        Test that the simulated camera returns logged events.
        """
        camera = eventlog.CameraEventLog()
        events = camera.get_log_events()
        self.assertFalse(events, 'Empty event log evaluates true.')
        self.assertIsInstance(
            events, list, 'Event log is not a list.')

    def test_log_events(self):
        """
        Test that the simulated camera logs new events.
        """
        camera = eventlog.CameraEventLog()

        first_description = camera.DESCRIPTIONS[0]
        camera.log_event(first_description)
        events = camera.get_log_events()
        self.assertTrue(
            events, 'Event log with events evaluates false.')
        self.assertEqual(
            len(events), 1, 'Wrong number of logged events')
        self.assertEqual(
            events[0]['description'], first_description,
            'Wrong logged event content')

        second_description = camera.DESCRIPTIONS[1]
        camera.log_event(second_description)
        events = camera.get_log_events()
        self.assertEqual(
            len(events), 2, 'Wrong number of logged events')
        self.assertEqual(
            events[1]['description'], second_description,
            'Wrong logged event content')
