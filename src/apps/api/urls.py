from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_docs.urls'))
]
