from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dashboard(models.Model):
	username = models.CharField(max_length = 100)
	about = models.TextField(default = 'default about text')
	location = models.CharField(default="location default text",max_length = 200,blank=True)
	worktitle = models.CharField(max_length=100,null=True,blank=True)
	def __unicode__(self):  #used to display username on admin pages. 
		return self.username

