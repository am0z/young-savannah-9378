from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import *

urlpatterns = patterns('',
    url(r'^form/$', ContactFormView.as_view(), name='form'),
    url(r'^thanks/$', TemplateView.as_view(
        template_name='contact/thanks.html'), name='thanks'),
)
