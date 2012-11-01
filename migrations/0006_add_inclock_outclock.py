# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Shift.in_clock'
        db.add_column('labgeeks_chronos_shift', 'in_clock', self.gf('django.db.models.fields.related.ForeignKey')(related_name='in_punchclock', blank=True, null=True, to=orm['labgeeks_chronos.Punchclock']), keep_default=False)

        # Adding field 'Shift.out_clock'
        db.add_column('labgeeks_chronos_shift', 'out_clock', self.gf('django.db.models.fields.related.ForeignKey')(related_name='out_punchclock', blank=True, null=True, to=orm['labgeeks_chronos.Punchclock']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Shift.in_clock'
        db.delete_column('labgeeks_chronos_shift', 'in_clock_id')

        # Deleting field 'Shift.out_clock'
        db.delete_column('labgeeks_chronos_shift', 'out_clock_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'labgeeks_chronos.location': {
            'Meta': {'object_name': 'Location'},
            'active_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'labgeeks_chronos.punchclock': {
            'Meta': {'object_name': 'Punchclock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'labgeeks_chronos.shift': {
            'Meta': {'object_name': 'Shift'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_clock': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_punchclock'", 'to': "orm['labgeeks_chronos.Punchclock']"}),
            'intime': ('django.db.models.fields.DateTimeField', [], {}),
            'out_clock': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'out_punchclock'", 'blank': 'True', 'null': 'True', 'to': "orm['labgeeks_chronos.Punchclock']"}),
            'outtime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'punchclock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Punchclock']"}),
            'shiftnote': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['labgeeks_chronos']
