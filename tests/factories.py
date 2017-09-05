import factory
from django.contrib.gis.geos import Point
from faker import Faker

from apps.juber import models


fake = Faker()

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
