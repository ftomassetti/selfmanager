# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'taskslist_app_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
        ))
        db.send_create_signal(u'taskslist_app', ['Project'])

        # Adding model 'Task'
        db.create_table(u'taskslist_app_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('parent_task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskslist_app.Task'], null=True)),
            ('project_task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskslist_app.Project'], null=True)),
        ))
        db.send_create_signal(u'taskslist_app', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'taskslist_app_project')

        # Deleting model 'Task'
        db.delete_table(u'taskslist_app_task')


    models = {
        u'taskslist_app.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'taskslist_app.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['taskslist_app.Task']", 'null': 'True'}),
            'project_task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['taskslist_app.Project']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['taskslist_app']