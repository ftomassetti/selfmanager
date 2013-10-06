from django.db import models
from abc import ABCMeta, abstractmethod

class TaskContainer(models.Model):

	class Meta:
		abstract = True

class Descripted(models.Model):
	title       = models.CharField(max_length=200)
	description = models.CharField(max_length=2000,null=True)  

	class Meta:
		abstract = True

class Project(Descripted, TaskContainer):
    pass    

class Task(Descripted, TaskContainer):
    parent_task  = models.ForeignKey('Task',null=True)
    project_task = models.ForeignKey(Project,null=True)  

    def check_parent_valid(self):
		if parent_task==None and project_task==None:
			raise ValidationError("Neither parent nor project task are set")

		if parent_task!=None and project_task!=None:
			raise ValidationError("Both parent and project task are set")
