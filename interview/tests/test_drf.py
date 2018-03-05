"""
Test that Django REST Framework integrations tests can be run.
"""

from django import urls
from rest_framework import test


class TestDRF(test.APITestCase):
    """
    Test that Django REST Framework integrations tests can be run.
    """

    def test_drf(self):
        """
        Test that Django REST Framework integrations tests can be run.
        """
        response = self.client.get(urls.reverse('rest_framework:login'))
        self.assertEqual(response.status_code, 200)
