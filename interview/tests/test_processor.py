"""
Test that the sensor processor removes low signal sensors.
"""

import unittest

from processor import main


class TestSensorProcessor(unittest.TestCase):
    """
    Test that the sensor processor removes low signal sensors.
    """

    def test_sample_files(self):
        """
        Test the sample files end-to-end.
        """
        # cd to some sort of tmp dir with cleanup
        main()
        with open('...1.json') as first_output:
            self.assert
