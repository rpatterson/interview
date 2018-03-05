"""
Density API DB models.
"""

import datetime

from django.db import models


class Space(models.Model):
    """
    A space or room.
    """

    name = models.CharField(
        verbose_name='space name',
        help_text='The name of the space or room',
        # TODO More sensible max length
        max_length=255)

    def count_passes(self, start, end=None):
        """
        Return the number of entries and exits for the time period.
        """
        if end is None:
            # TODO TZ?
            end = datetime.datetime.now()
        return (
            self.entries.filter(timestamp__range=(start, end)).count(),
            self.exits.filter(timestamp__range=(start, end)).count())


class Doorway(models.Model):
    """
    A doorway into or out of a space.
    """

    name = models.CharField(
        verbose_name='doorway name',
        help_text='The name of the doorway',
        # TODO More sensible max length
        max_length=255)

    space_in = models.ForeignKey(
        verbose_name='space the doorway opens into',
        help_text='Which space or room does the doorway open into',
        to=Space, related_name='doorways_in',
        on_delete=models.SET_NULL, null=True, blank=True)
    space_out = models.ForeignKey(
        verbose_name='space the doorway opens out of',
        help_text='Which space or room does the doorway open out of',
        to=Space, related_name='doorways_out',
        on_delete=models.SET_NULL, null=True, blank=True)


class DPU(models.Model):
    """
    A depth processing unit (DPU) installed on a doorway.
    """

    doorway = models.ForeignKey(
        verbose_name='installed on doorway',
        help_text='Which doorway is this DPU installed on currently',
        to=Doorway, on_delete=models.SET_NULL, null=True, blank=True)

    space_plus = models.ForeignKey(
        verbose_name='plus measures into space',
        help_text='Which space or room does a +1 measurement '
        'mean passing into',
        to=Space, related_name='dpus_plus',
        on_delete=models.SET_NULL, null=True, blank=True)
    space_minus = models.ForeignKey(
        verbose_name='minus measures into space',
        help_text='Which space or room does a -1 measurement '
        'mean passing into',
        to=Space, related_name='dpus_minus',
        on_delete=models.SET_NULL, null=True, blank=True)


class PassManager(models.Manager):
    """
    Database manager for DPU passes.
    """

    def create(self, timestamp, direction, dpu_id, id=None):
        """
        Interpret directionality when creating passes.
        """
        # TODO I'm not sure this is the most appropriate place for this logic

        dpu = DPU.objects.get(id=dpu_id)

        direction = int(direction)
        if direction == 1:
            space_in = dpu.space_plus
            space_out = dpu.space_minus
        else:
            space_in = dpu.space_minus
            space_out = dpu.space_plus

        return super(PassManager, self).create(
            id=id, timestamp=timestamp, doorway=dpu.doorway,
            space_in=space_in, space_out=space_out)


class Pass(models.Model):
    """
    An in individual passing through a given doorway from a DPU.
    """

    objects = PassManager()

    doorway = models.ForeignKey(
        verbose_name='doorway',
        help_text='Which doorway did the person pass through',
        # TODO Should deleting a doorway delete the measurements
        to=Doorway, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(
        verbose_name='measurement timestamp',
        help_text='The date and time this measurement was taken')

    space_in = models.ForeignKey(
        verbose_name='space passed into',
        help_text='Which space or room did the person pass into',
        to=Space, related_name='entries',
        on_delete=models.SET_NULL, null=True, blank=True)
    space_out = models.ForeignKey(
        verbose_name='space passed out of',
        help_text='Which space or room did the person pass out of',
        to=Space, related_name='exits',
        on_delete=models.SET_NULL, null=True, blank=True)
