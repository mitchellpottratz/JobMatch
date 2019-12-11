from django.db import models
from django.utils import timezone


# this model is used by the JobPost and CandidateUserInfo
# models for a many-to-many relationship
class Skill(models.Model):
	name = models.CharField(max_length=75)
	timestamp = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.name


