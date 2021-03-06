from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.contrib import admin
from django.views.generic.list import ListView
from apps.main.models import Subscriber, Course
from apps.main.views import SubscriberDetailView, CourseDetailView
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
     url(r'^subscribe/$', 'apps.main.views.subscribe', name='subscribe'),
     url(r'^subscribers/$', ListView.as_view(model=Subscriber, paginate_by=3), name='subscribers'),
     url(r'^subscribers/(?P<pk>\d+)$', SubscriberDetailView.as_view(model=Subscriber), name='subscriber_detail'),
     url(r'^courses/$', ListView.as_view(model=Course, paginate_by=3), name='courses'),
     url(r'^courses/(?P<pk>\d+)$', CourseDetailView.as_view(model=Course), name='course_detail'),
    # url(r'^django_academy/', include('django_academy.foo.urls')),
     url(r'^courses/$', 'apps.main.views.list_courses', name='list_courses'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
