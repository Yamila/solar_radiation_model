# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
import pytz

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SensorCalibration.sensor'
        db.add_column('stations_sensorcalibration', 'sensor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['stations.Sensor']),
                      keep_default=False)

        # Adding field 'Configuration.begin'
        db.add_column('stations_configuration', 'begin',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 14, 0, 0).replace(tzinfo=pytz.UTC)),
                      keep_default=False)

        # Adding field 'Configuration.end'
        db.add_column('stations_configuration', 'end',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SensorCalibration.sensor'
        db.delete_column('stations_sensorcalibration', 'sensor_id')

        # Deleting field 'Configuration.begin'
        db.delete_column('stations_configuration', 'begin')

        # Deleting field 'Configuration.end'
        db.delete_column('stations_configuration', 'end')


    models = {
        'stations.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        },
        'stations.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'begin': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'calibration': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.SensorCalibration']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'devices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'configurations'", 'symmetrical': 'False', 'to': "orm['stations.Device']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Position']"})
        },
        'stations.datalogger': {
            'Meta': {'object_name': 'Datalogger', '_ormbases': ['stations.Device']},
            'device_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stations.Device']", 'unique': 'True', 'primary_key': 'True'})
        },
        'stations.device': {
            'Meta': {'object_name': 'Device'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Product']"}),
            'serial_number': ('django.db.models.fields.TextField', [], {'default': "''", 'db_index': 'True'})
        },
        'stations.inclinedsupport': {
            'Meta': {'object_name': 'InclinedSupport', '_ormbases': ['stations.Device']},
            'angle': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '7', 'decimal_places': '4'}),
            'device_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stations.Device']", 'unique': 'True', 'primary_key': 'True'})
        },
        'stations.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'between': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'configuration': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Configuration']"}),
            'finish': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mean': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'refresh_presision': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'stations.opticfilter': {
            'Meta': {'object_name': 'OpticFilter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        },
        'stations.position': {
            'Meta': {'object_name': 'Position'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '10', 'decimal_places': '7'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '10', 'decimal_places': '7'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['stations.Station']", 'null': 'True'})
        },
        'stations.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Brand']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'specifications': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        },
        'stations.sensor': {
            'Meta': {'object_name': 'Sensor', '_ormbases': ['stations.Device']},
            'device_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stations.Device']", 'unique': 'True', 'primary_key': 'True'}),
            'optic_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.OpticFilter']", 'null': 'True'})
        },
        'stations.sensorcalibration': {
            'Meta': {'object_name': 'SensorCalibration'},
            'coefficient': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '10', 'decimal_places': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stations.Sensor']"}),
            'shift': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '10', 'decimal_places': '7'})
        },
        'stations.shadowball': {
            'Meta': {'object_name': 'ShadowBall', '_ormbases': ['stations.Device']},
            'device_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stations.Device']", 'unique': 'True', 'primary_key': 'True'})
        },
        'stations.station': {
            'Meta': {'object_name': 'Station'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        },
        'stations.tracker': {
            'Meta': {'object_name': 'Tracker', '_ormbases': ['stations.Device']},
            'device_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stations.Device']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['stations']