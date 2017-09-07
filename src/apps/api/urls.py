from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, TripViewSet, ModelViewSet, VehicleViewSet, LocationViewSet, DriverViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'models', ModelViewSet, base_name='models')
router.register(r'vehicles', VehicleViewSet, base_name='vehicles')
router.register(r'locations', LocationViewSet, base_name='locations')
router.register(r'drivers', DriverViewSet, base_name='drivers')
router.register(r'trips', TripViewSet, base_name='trips')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_docs.urls'))
]
