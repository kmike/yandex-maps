# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('yandex_maps_mapandaddress', 'longtitude', 'longitude')

    def backwards(self, orm):
        db.rename_column('yandex_maps_mapandaddress', 'longitude', 'longtitude')

    models = {
        'yandex_maps.mapandaddress': {
            'Meta': {'object_name': 'MapAndAddress'},
            'address': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yandex_maps']