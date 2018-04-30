"""
Test that the Flask app is working.
"""

import unittest

import interview


class FlaskTestCase(unittest.TestCase):
    """
    Test that the Flask app is working.
    """

    def setUp(self):
        interview.app.testing = True
        self.app = interview.app.test_client()

    def test_root(self):
        """
        Test that the Flask app responds at the root path.
        """
        response = self.app.get('/')
        self.assertEqual(
            response.get_json(), interview.ROOT_RESPONSE,
            'Wrong root response content')
