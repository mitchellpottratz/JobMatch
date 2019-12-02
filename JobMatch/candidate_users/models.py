from django.db import models
from django.conf import settings
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from phone_field import PhoneField


# this model holds all of the users information such as;
# headline, bio, location and phone number
class CandidateInfo(models.Model):

	# one to one relationship to a user
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	# city and location store the users location
	city = models.CharField(max_length=255, default='')
	location = PlainLocationField(based_fields=['city'], zoom=7, default='')

	headline = models.CharField(max_length=75, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	phone_number = PhoneField(blank=True)

	# *- ADD SKILLS FIELD WHEN THE SKILL MODEL IS CREATED -*






