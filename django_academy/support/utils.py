# -*- coding: utf-8 -*-

###########################
# Python Standard Library #
###########################
import csv
from django.contrib.auth.hashers import make_password

class LineObject(object):
    def __init__(self, line_data, line_number, labels):
        self.line_data = line_data
        self.line_number = line_number
        self.labels = labels
        self.data  = self.get_data_dict()

    def get_data_dict(self):
        return dict(zip(self.labels, self.line_data))


def hash_password(raw_password):
    return make_password(raw_password, None, 'sha1')


def get_lines_objects_from_csv(file_path):
    csvio = open(file_path)
    csv_reader = csv.reader(csvio)
    first_line = csv_reader.next()
    line_objects = []
    n = 1
    for row in csv_reader:
        n += 1
        line_data = map(str.strip, row)
        if ''.join(line_data):
            line_object = LineObject(line_data, n, first_line)
            line_objects.append(line_object)
    return line_objects


def add_image_to_object_image_set(object=None, image_class=None, field_name='image_set', image_filename='', img_prefix='uploads', attributes_dictionary={}):
    if not image_filename: return

    image = image_class(**attributes_dictionary)
    image.save()

    getattr(object, field_name).add(image)

    from django.db import connection, transaction
    dbcursor = connection.cursor()

    sql_statement = "update main_%s set image = '%s/%s' where id=%d" % (image_class.__name__.lower(), img_prefix, image_filename, image.id)
    dbcursor.execute(sql_statement)
    transaction.commit_unless_managed()


def set_image_to_object(object=None, image_filename='', img_prefix='uploads', image_field_name='image', id_column_name='id', ):
    if not image_filename: return

    from django.db import connection, transaction
    dbcursor = connection.cursor()

    sql_statement = "update main_" + object.__class__.__name__.lower() + " set %s = '%s/%s' where %s=%d" % (image_field_name, img_prefix, image_filename, id_column_name, object.id)
    dbcursor.execute(sql_statement)
    transaction.commit_unless_managed()