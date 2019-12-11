from django.db import models
from django.conf import settings
from django.utils import timezone
from .managers import CompanyQuerySet


# this model represents a company that CompanyUsers are 
# apart of
class Company(models.Model):
	name = models.CharField(max_length=150)
	image = models.ImageField(blank=True, upload_to='company/')

	# admin user of the company 
	admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	# code to invite other users to the company
	invite_code = models.CharField(max_length=15)

	# time the comany was created
	timestamp = models.DateTimeField(default=timezone.now())

	# query manager
	objects = CompanyQuerySet.as_manager()

	def __str__(self):
		return self.name









