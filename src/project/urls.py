from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.juber.urls'), name='index'),
    url(r'api/', include('apps.api.urls'), name='api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
]
