"""
Test that Django integrations tests can be run.
"""

from django import urls
from django import test


class TestDjango(test.TestCase):
    """
    Test that Django integrations tests can be run.
    """

    def test_django(self):
        """
        Test that Django integrations tests can be run.
        """
        response = self.client.get(urls.reverse('admin:index'))
        self.assertEqual(response.status_code, 302)
        
