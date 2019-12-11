from django.db import models
from django.conf import settings
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from phone_field import PhoneField
from skills.models import Skill


# this model holds all of the users information such as;
# headline, bio, location and phone number
class CandidateInfo(models.Model):

	# one to one relationship to a user
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='candidate_info')
	
	# where the users lives
	location = models.CharField(max_length=250, blank=True, null=True)

	resume = models.FileField(blank=True, upload_to='resumes/')

	headline = models.CharField(max_length=75, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	phone_number = models.CharField(max_length=20, blank=True)

	# the users skills
	skills = models.ManyToManyField(Skill)

	last_updated = models.DateTimeField(default=timezone.now())
	timestamp = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.user.get_full_name()






