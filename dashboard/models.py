from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dashboard(models.Model):
	username = models.CharField(max_length=100)
	about = models.TextField(default = 'default about text')
	def __unicode__(self):
		return self.name

