# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subscriber.email'
        db.add_column('main_subscriber', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)


        # Changing field 'Subscriber.name'
        db.alter_column('main_subscriber', 'name', self.gf('django.db.models.fields.CharField')(default='NA', max_length=400))

    def backwards(self, orm):
        # Deleting field 'Subscriber.email'
        db.delete_column('main_subscriber', 'email')


        # Changing field 'Subscriber.name'
        db.alter_column('main_subscriber', 'name', self.gf('django.db.models.fields.CharField')(max_length=400, null=True))

    models = {
        'main.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['main']