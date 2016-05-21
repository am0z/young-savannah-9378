from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', cache_page(60 * 15)(
        TemplateView.as_view(template_name='base.html')), name='home'),
    url(r'^', include('youngsters.urls', namespace='youngsters')),
    url(r'^', include('contact.urls', namespace='contact')),
)
