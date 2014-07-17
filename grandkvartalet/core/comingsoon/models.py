from django.db import models

class Subscriber(models.Model):
	email = models.EmailField(unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.email)