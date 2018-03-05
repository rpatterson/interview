"""
Density API DB models.
"""

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
        verbose_name='space to doorway opens into',
        help_text='Which space or room does the doorway open into',
        to=Space, related_name='doorways_in',
        on_delete=models.SET_NULL, null=True, blank=True)
    space_out = models.ForeignKey(
        verbose_name='space to doorway opens out of',
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


class Pass(models.Model):
    """
    An in individual passing through a given doorway from a DPU.
    """

    doorway = models.ForeignKey(
        verbose_name='doorway',
        help_text='Which doorway did the person pass through',
        # TODO Should deleting a doorway delete the measurements
        to=Doorway, on_delete=models.CASCADE)
    dpu = models.ForeignKey(
        verbose_name='DPU',
        help_text='Which DPU measured the passing at the time',
        to=DPU, on_delete=models.SET_NULL, null=True, blank=True)

    timestamp = models.DateTimeField(
        verbose_name='timestamp',
        help_text='The date and time the person passed')
    direction = models.BooleanField(
        verbose_name='direction',
        help_text='The direction the DPU was passed')
