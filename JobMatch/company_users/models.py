from django.db import models
from users.models import User
from django.utils import timezone


# this model represents a company that CompanyUsers are 
# apart of
class Company(models.Model):
	name = models.CharField(max_length=150)
	image = models.ImageField(blank=True)

	# admin user of the company 
	admin = models.OneToOneField(User, on_delete=models.CASCADE)

	# code to invite other users to the company
	invite_code = models.CharField(max_length=15)

	# time the comany was created
	timestamp = models.DateTimeField(default=timezone.now())









