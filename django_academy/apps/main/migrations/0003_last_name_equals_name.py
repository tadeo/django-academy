# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
#        orm['main.Subscriber'] is equivalent to main.Subscriber
        for subscriber in orm['main.Subscriber'].objects.all():
            subscriber.last_name = subscriber.name
            subscriber.save()

    def backwards(self, orm):
        for subscriber in orm['main.Subscriber'].objects.all():
            subscriber.last_name = ''
            subscriber.save()

    models = {
        'main.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
    symmetrical = True
