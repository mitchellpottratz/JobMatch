from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# User model
# costumizes django's default User model
class User(AbstractUser):

	# removes the usernae field
	username = None

	# profile picture
	image = models.ImageField(blank=True)

	# if the user is apart of a company, a user that creates 
	# job postings for a company
	company_user = models.BooleanField(default=False)

	# if the use is just a candidate user, a user that is just
	# looking for job.
	candidate_user = models.BooleanField(default=False)

	# makes the first_name, last_name and email field all required
	first_name = models.CharField(max_length=150, blank=False)
	last_name = models.CharField(max_length=150, blank=False)
	email = models.EmailField(unique=True, blank=False)

	# if the user has confirmed their email address
	email_confirmed = models.BooleanField(default=False)

	# changes the username field to the email field
	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []
