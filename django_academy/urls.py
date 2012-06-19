from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
     url(r'^subscribe/$', 'apps.main.views.subscribe', name='subscribe'),
    # url(r'^django_academy/', include('django_academy.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
