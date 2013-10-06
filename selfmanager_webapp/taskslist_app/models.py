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
