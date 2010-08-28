# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MapAndAddress'
        db.create_table('yandex_maps_mapandaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
            ('longtitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('yandex_maps', ['MapAndAddress'])


    def backwards(self, orm):
        
        # Deleting model 'MapAndAddress'
        db.delete_table('yandex_maps_mapandaddress')


    models = {
        'yandex_maps.mapandaddress': {
            'Meta': {'object_name': 'MapAndAddress'},
            'address': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yandex_maps']
