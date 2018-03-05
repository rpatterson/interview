# Generated by Django 2.0.2 on 2018-03-05 18:04

import os
import csv

from django.db import migrations
from django.utils import dateparse


def import_dpu_data(apps, schema_editor):
    """
    Create necessary initial objects and import measurements from CSV.
    """
    # Create spaces as in the diagram
    Space = apps.get_model('interview', 'Space')
    space_a = Space.objects.create(name='Space A')
    space_b = Space.objects.create(name='Space B')

    # Add the doorways
    Doorway = apps.get_model('interview', 'Doorway')
    doorway_x = Doorway.objects.create(
        name='Doorway X', space_in=space_a)
    doorway_z = Doorway.objects.create(
        name='Doorway Z', space_in=space_b, space_out=space_a)

    # Add the DPUs
    DPU = apps.get_model('interview', 'DPU')
    DPU.objects.create(
        id=283, doorway=doorway_x, space_plus=space_a)
    DPU.objects.create(
        id=423, doorway=doorway_z,
        space_plus=space_a, space_minus=space_b)

    # Load the CSV measurements
    Measurement = apps.get_model('interview', 'Measurement')
    measurements = []
    for idx, row in enumerate(csv.DictReader(open(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'dpu_data.csv')))):
        row['timestamp'] = dateparse.parse_datetime(row['timestamp'])
        row['direction'] = row['direction'] == "1"
        measurements.append(Measurement(
            id=idx + 1, doorway=DPU.objects.get(id=row['dpu_id']).doorway,
            **row))
    Measurement.objects.bulk_create(measurements)


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_dpu_data),
    ]
