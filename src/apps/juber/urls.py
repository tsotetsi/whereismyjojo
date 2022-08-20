from django.urls import re_path

from apps.juber.views import IndexView, TripView


urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'trip/', TripView.as_view(), name='trip'),
]
