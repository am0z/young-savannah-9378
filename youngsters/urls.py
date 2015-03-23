from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import *

urlpatterns = patterns('',
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^profile/$', TemplateView.as_view(template_name='youngsters/profile_detail.html'), name='profile'),
)
