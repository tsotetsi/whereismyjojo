# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string
import random

from django.contrib.gis.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from model_utils.models import TimeStampedModel


class Model(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Vehicle(TimeStampedModel):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=25)
    field_number = models.CharField(max_length=25)
    liters = models.FloatField(validators=[MinLengthValidator(0), MaxLengthValidator(50000)])
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return '{} with reg number {} having {:.2d} liter(s).'.format(self.model, self.registration_number, self.liters)

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
        return super(Vehicle, self).save(*args, **kwargs)


class Location(models.Model):
    departure = models.PointField()
    destination = models.PointField()

    def __str__(self):
        return '{} : {}.'.format(self.departure, self.destination)


class Driver(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=16)
    license_number = models.CharField(max_length=100)
    has_pdp = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Trip(models.Model):
    location = models.ManyToManyField(Location)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return '{} going to {}.'.format(self.driver.name, self.location)
