"""
Test the Density API endpoints.
"""

from django import urls
from rest_framework import test


class TestDensityEndpoints(test.APITestCase):
    """
    Test the Density API endpoints.
    """

    def test_space_pass_counts(self):
        """
        An API endpoint returns pass counts.
        """
        response = self.client.get(urls.reverse('interview:spaces'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'entries', response.json, 'Response missing entry counts')
