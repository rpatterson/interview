"""
Test that the Flask app is working.
"""

import unittest

import api


class FlaskTestCase(unittest.TestCase):
    """
    Test that the Flask app is working.
    """

    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_root(self):
        """
        Test that the Flask app responds at the root path.
        """
        response = self.app.get('/')
        self.assertEqual(
            response.get_json(), api.ROOT_RESPONSE,
            'Wrong root response content')
