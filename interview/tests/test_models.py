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
        space_a = models.Space.objects.get(name='Space A')
        space_b = models.Space.objects.get(name='Space B')
        doorway_z = models.Doorway.objects.get(name='Doorway Z')
        first_pass = models.Pass.objects.get(id=1)
        second_pass = models.Pass.objects.get(id=2)

        rows = list(csv.DictReader(open(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'dpu_data.csv'))))

        self.assertTrue(
            hasattr(first_pass, 'timestamp'),
            'Pass missing timestamp attribute/field/column')
        self.assertIsInstance(
            first_pass.timestamp, datetime.datetime,
            'Pass timestamp is not a DateTime')
        self.assertEqual(
            first_pass.timestamp,
            dateparse.parse_datetime(rows[0]['timestamp']),
            'Pass timestamp is not a DateTime')

        self.assertTrue(
            hasattr(first_pass, 'doorway'),
            'Pass missing doorway relationship')
        self.assertEqual(
            first_pass.doorway, doorway_z,
            'Wrong pass related doorway')

        self.assertTrue(
            hasattr(first_pass, 'space_in'),
            'Pass missing which space was entered')
        self.assertEqual(
            first_pass.space_in, space_a,
            'Wrong pass space entered')
        self.assertTrue(
            hasattr(first_pass, 'space_out'),
            'Pass missing which space was entered')
        self.assertEqual(
            first_pass.space_out, space_b,
            'Wrong pass space entered')
        self.assertEqual(
            second_pass.space_in, space_b,
            'Wrong pass space entered')
        self.assertEqual(
            second_pass.space_out, space_a,
            'Wrong pass space entered')

    def test_realtime_space_count(self):
        """
        A space can return the count of people in it at the moment.
        """
        space_a = models.Space.objects.get(name='Space A')
        counts = space_a.count_passes(
            datetime.datetime(year=2018, month=3, day=1))
        self.assertIsInstance(
            counts, tuple, 'Wrong counts return type')
        self.assertEqual(
            len(counts), 2, 'Wrong number of counts return values')
        entries, exits = counts
        self.assertEqual(
            entries, 95, 'Wrong number of entries')
        self.assertEqual(
            exits, 107, 'Wrong number of exits')

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
