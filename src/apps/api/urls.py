from django.urls import re_path, include
from rest_framework import routers

from .views import UserViewSet, TripViewSet, ModelViewSet, VehicleViewSet, LocationViewSet, DriverViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'models', ModelViewSet, basename='models')
router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register(r'trips', TripViewSet, basename='trips')


urlpatterns = [
    re_path(r'^', include(router.urls))
]
