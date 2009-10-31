#coding: utf-8

from south.db import db
from django.db import models
from yandex_maps.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'MapAndAddress'
        db.create_table('yandex_maps_mapandaddress', (
            ('id', orm['yandex_maps.MapAndAddress:id']),
            ('address', orm['yandex_maps.MapAndAddress:address']),
            ('longtitude', orm['yandex_maps.MapAndAddress:longtitude']),
            ('latitude', orm['yandex_maps.MapAndAddress:latitude']),
        ))
        db.send_create_signal('yandex_maps', ['MapAndAddress'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'MapAndAddress'
        db.delete_table('yandex_maps_mapandaddress')
        
    
    
    models = {
        'yandex_maps.mapandaddress': {
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['yandex_maps']
