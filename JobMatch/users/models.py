from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# User model
# costumizes django's default User model
class User(AbstractUser):
	username = models.CharField(max_length=155, unique=True, blank=True)

	# profile picture
	image = models.ImageField(blank=True)

	# if the user is apart of a company, a user that creates 
	# job postings for a company
	company_user = models.BooleanField(default=False)

	# if the use is just a candidate user, a user that is just
	# looking for job.
	candidate_user = models.BooleanField(default=False)

	# makes the email field all required
	email = models.EmailField(unique=True)

	# if the user has confirmed their email address
	email_confirmed = models.BooleanField(default=False)








