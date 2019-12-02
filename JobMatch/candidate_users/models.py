from django.db import models
from django.conf import settings
from django.utils import timezone
from location_field.models.plain import PlainLocationField


# this model holds all of the users information such as;
# headline, bio, location and phone number
class CandidateInfo(models.Model):

	# # one to one relationship to a user
	# user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASECADE)
	
	# # city and location store the users location
	# city = models.CharField(max_length=255)
 #    location = PlainLocationField(based_fields=['city'], zoom=7)

 #    headline = models.CharField(max_length=75, blank=True, null=True)
 #    bio = models.TextField(max_length=500, blank=True, null=True)
	pass





