from django.db import models

class Subscriber(models.Model):
	email = models.EmailField(unique=True)

	def __unicode__(self):
		return unicode(self.email)