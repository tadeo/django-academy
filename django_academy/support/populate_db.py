#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################
# Python Standard Library #
###########################
import os, sys

#################
# Project setup #
#################
SITE_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.insert(0, SITE_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_academy.settings'

from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from apps.main.utils import get_form_by_class, camelcase_to_underscore
from support.utils import get_lines_objects_from_csv, hash_password
from apps.main.models import UserProfile, Course, Teacher, Student

file_path = os.path.dirname(os.path.realpath(__file__))


def import_model_csv(model_class, create_profile=False, file_name=None):
    file_name = file_name or camelcase_to_underscore(model_class.__name__)
    data_lines = get_lines_objects_from_csv('%s/%s.csv' % (file_path, file_name))
    model_form = get_form_by_class(model_class)
    instances = []
    for line_data in data_lines:
        data_dict = line_data.data
        if create_profile:
            username = '%s%s' % (data_dict['first_name'], line_data.line_number)
            password = hash_password(data_dict['first_name'])
            user, created = User.objects.get_or_create(
                username = username,
                password = password,
                first_name = data_dict['first_name'],
                last_name = data_dict['last_name'],
                email = data_dict['email'],
            )
#            user = User(
#                username = username,
#                password = password,
#                first_name = data_dict['first_name'],
#                last_name = data_dict['last_name'],
#                email = data_dict['email'],
#            )
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            data_dict['user_profile'] = str(user_profile.id)

        instance_form = model_form(data_dict)
        if instance_form.is_valid():
            instance = instance_form.save()
            instances.append(instance)
        else:
            print 'Error importing line %s' % line_data.line_number
    print '%s of %s instances created successful' % (len(instances), model_class.__name__)

import_model_csv(Course)
import_model_csv(Teacher, create_profile=True)
import_model_csv(Student, create_profile=True)
