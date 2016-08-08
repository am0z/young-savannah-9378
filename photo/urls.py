from django.conf.urls import patterns, url
from .views import PhotoListView

urlpatterns = patterns('',
    url(r'^$', PhotoListView.as_view(), name='list'),
)
