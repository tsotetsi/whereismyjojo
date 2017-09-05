from django.conf.urls import url

from apps.juber.views import IndexView, TripView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'trip/', TripView.as_view(), name='trip'),
]
