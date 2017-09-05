# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models as gismodel
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from model_utils.models import TimeStampedModel


class TruckBrand(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Truck(TimeStampedModel):
    brand = models.ForeignKey(TruckBrand, on_delete=models.CASCADE)
    reg_num = models.CharField(max_length=10)
    field_num = models.CharField(max_length=10)
    liters = models.FloatField(validators=[MinLengthValidator(0), MaxLengthValidator(50000)])

    def __str__(self):
        return '{} with reg number {} having {} liter(s)'.format(self.model, self.reg_num, self.liters)

    @staticmethod
    def generate_field_num():
        return


class Location(models.Model):
    departure = gismodel.PointField()
    destination = gismodel.PointField()

    def __str__(self):
        return '{} : {}'.format(self.departure, self.destination)


class JojoTrip(models.Model):
    pass


class Trip(models.Model):
    pass
