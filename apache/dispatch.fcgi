#!/usr/bin/python
import os, sys

sys.path.insert(0, '/home/tadeo/projects/django-academy/env/lib/python2.6/site-packages')
sys.path.insert(0, '/home/tadeo/projects/django-academy/apache')
sys.path.insert(0, '/home/tadeo/projects/django-academy')
os.chdir('/home/tadeo/projects/django-academy')

from fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_academy.settings'
WSGIServer(WSGIHandler()).run()
