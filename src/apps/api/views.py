from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer, ModelSerializer, VehicleSerializer, \
                         LocationSerializer, DriverSerializer, TripSerializer
from apps.juber.models import Model, Vehicle, Location, Driver, Trip


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Returns the given user.

    list:
    Returns a list of all the existing users.

    create:
    Create a new user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ModelViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Returns the given model.

    list:
    Returns list of all models.

    create:
    Create new model instance.
    """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given vehicle.

    list:
    Returns list of all vehicles.

    create:
    Creates a new vehicle instance.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given location.

    list:
    Returns list of all locations.

    create:
    Creates a new location instance.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given driver.

    list:
    Returns list of all drivers.

    create:
    Creates a new driver instance.
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class TripViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given trip.

    list:
    Returns list of all trips.

    create:
    Creates a new trip instance.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
