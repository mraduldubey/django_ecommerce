from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.
class dashboard(models.Model):
	username = models.CharField(max_length = 100)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,blank=True) #Note.imp.
	about = models.TextField(default = 'default about text')
	location = models.CharField(default="location default text",max_length = 200,blank=True)
	worktitle = models.CharField(max_length=100,null=True,blank=True)

	def __unicode__(self):  #used to display username on admin pages. 
		return self.username

class stripeUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username