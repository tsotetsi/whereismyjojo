import random
import string

import factory
from faker import Faker
from django.contrib.gis.geos import Point
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


from apps.juber import models

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = ''.join(random.sample(string.ascii_lowercase + string.digits, 5))
    password = make_password('user123')

    class Meta:
        model = User


class ModelFactory(factory.django.DjangoModelFactory):
    name = 'benz truck'
    description = '20 000KG, double axle.'

    class Meta:
        model = models.Model


class VehicleFactory(factory.django.DjangoModelFactory):
    model = factory.SubFactory(ModelFactory)
    registration_number = 'ABC 123 WP'
    field_number = 'CTN-021'
    liters = 30000

    class Meta:
        model = models.Vehicle


class LocationFactory(factory.django.DjangoModelFactory):
    departure = Point(60.5, 60.9)
    destination = Point(25.6, 25.3)

    class Meta:
        model = models.Location


class DriverFactory(factory.django.DjangoModelFactory):
    name = fake.name()
    contact_number = '+27831234567'
    license_number = 'WN95TP2HA9QMC99'

    class Meta:
        model = models.Driver


class TripFactory(factory.django.DjangoModelFactory):
    location = factory.SubFactory(LocationFactory)
    driver = factory.SubFactory(DriverFactory)
    vehicle = factory.SubFactory(VehicleFactory)

    class Meta:
        model = models.Model
