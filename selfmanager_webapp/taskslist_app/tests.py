"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from taskslist_app.models import Project,Task

class SimpleTest(TestCase):
	fixtures = ['basic']

	def test_fixture_is_loaded(self):
		self.assertEqual(1,len(Project.objects.all()))
		self.assertEqual(1,len(Task.objects.all()))

