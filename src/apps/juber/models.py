# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string
import random

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
    def generate_field_number():
        return '{}-{}'.format(random.sample(
            string.ascii_uppercase + string.digits, 3),
            random.sample(string.digits, 2))

    @staticmethod
    def generate_registration_number():
        return '{prefix} {word} {postfix}'.format(prefix=random.sample(string.ascii_uppercase + string.digits, 3),
                                                  word=random.sample(string.ascii_uppercase + string.digits, 3),
                                                  postfix=random.choice(['GP', 'MP', 'FS', 'WP'])
                                                  )

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.field_num = self.generate_field_number()
            self.ref_num = self.generate_registration_number()
        return super(Truck, self).save(*args, **kwargs)


class Location(models.Model):
    departure = gismodel.PointField()
    destination = gismodel.PointField()

    def __str__(self):
        return '{} : {}'.format(self.departure, self.destination)


class JojoTrip(models.Model):
    pass


class Trip(models.Model):
    pass
