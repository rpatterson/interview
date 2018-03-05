"""
Test the Density DB models.
"""

import os
import datetime
import csv

from django.utils import dateparse
from django import test

from interview import models


class TestDensityModels(test.TestCase):
    """
    Test the Density DB models.
    """

    def test_models(self):
        """
        Test all the Density objects and their relationships.
        """
        doorway_z = models.Doorway.objects.get(name='Doorway Z')
        dpu_423 = models.DPU.objects.get(id=423)
        # TODO relies on DB insertion order
        first_measurement = models.Measurement.objects.get(id=1)
        second_measurement = models.Measurement.objects.get(id=2)

        rows = list(csv.DictReader(open(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'dpu_data.csv'))))

        self.assertTrue(
            hasattr(first_measurement, 'timestamp'),
            'Measurement missing timestamp attribute/field/column')
        self.assertIsInstance(
            first_measurement.timestamp, datetime.datetime,
            'Measurement timestamp is not a DateTime')
        self.assertEqual(
            first_measurement.timestamp,
            dateparse.parse_datetime(rows[0]['timestamp']),
            'Measurement timestamp is not a DateTime')
        self.assertTrue(
            hasattr(first_measurement, 'direction'),
            'Measurement missing direction attribute/field/column')
        self.assertIsInstance(
            first_measurement.direction, bool,
            'Measurement direction is not a boolean')
        self.assertTrue(
            first_measurement.direction,
            'Wrong measurement direction')
        self.assertFalse(
            second_measurement.direction,
            'Wrong measurement direction')
        self.assertTrue(
            hasattr(first_measurement, 'dpu'),
            'Measurement missing DPU relationship')
        self.assertEqual(
            first_measurement.dpu, dpu_423,
            'Wrong measurement related DPU')
        self.assertTrue(
            hasattr(first_measurement, 'doorway'),
            'Measurement missing doorway relationship')
        self.assertEqual(
            first_measurement.doorway, doorway_z,
            'Wrong measurement related doorway')

    def test_dpu_empty_spaces_constraint(self):
        """
        A DPU's plus and minus spaces may not both be empty.
        """
        self.skipTest('TODO ' + __doc__)
        # space_a = models.Space.objects.create(name='Space A')
        # doorway_x = models.Doorway.objects.create(
        #     name='Doorway X', space_in=space_a)
        # with self.assertRaises(TODO) as exc:
        #     models.DPU.objects.create(
        #         name='DPU 666', doorway=doorway_x)
        # self.assertEqual(exc.TODO, TODO, 'Wrong DPU empty spaces error')

    def test_doorway_space_deletion(self):
        """
        It is an error to delete a space that leaves any doorways orphaned.
        """
        self.skipTest('TODO ' + __doc__)
