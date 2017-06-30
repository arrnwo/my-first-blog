from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(blank=True, null=True)
<<<<<<< HEAD
	published_date = models.DateTimeField(
            blank=True, null=True)

||||||| merged common ancestors
	
=======
	published_date = models.DateTimeField(
            blank=True, null=True)
			
>>>>>>> 09b80ce20830067fdb4726b87b74cbd0376ab813
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
